import requests
import yaml
import json
import re
from datetime import datetime, timedelta
import os
import base64
import time

class SolanaRepoTracker:
    def __init__(self, github_token):
        self.token = github_token
        self.headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.rate_limit_remaining = 5000
    
    def check_rate_limit(self):
        """Check GitHub API rate limits"""
        try:
            response = requests.get('https://api.github.com/rate_limit', headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                self.rate_limit_remaining = data['rate']['remaining']
                reset_time = datetime.fromtimestamp(data['rate']['reset'])
                print(f"Rate limit remaining: {self.rate_limit_remaining}/5000")
                print(f"Resets at: {reset_time.strftime('%H:%M:%S')}")
                
                if self.rate_limit_remaining < 100:
                    print("Low rate limit! Sleeping for 60 seconds...")
                    time.sleep(60)
        except Exception as e:
            print(f"Error checking rate limit: {e}")
    
    def get_repo_stats(self, repo_name):
        """Get comprehensive repo statistics"""
        try:
            print(f"  Fetching stats for {repo_name}...")
            
            # Basic repo info
            repo_url = f"https://api.github.com/repos/{repo_name}"
            response = requests.get(repo_url, headers=self.headers)
            
            if response.status_code == 404:
                print(f"  Repository {repo_name} not found (404)")
                return None
            elif response.status_code != 200:
                print(f"  Error fetching {repo_name}: {response.status_code}")
                return None
            
            repo_data = response.json()
            
            # Get contributors count (optimized approach)
            contributors_count = 0
            try:
                contributors_url = f"https://api.github.com/repos/{repo_name}/contributors?per_page=1"
                contributors_response = requests.get(contributors_url, headers=self.headers)
                
                if contributors_response.status_code == 200:
                    # Check if there's pagination info in headers
                    link_header = contributors_response.headers.get('Link', '')
                    if 'rel="last"' in link_header:
                        # Extract the last page number
                        import re
                        last_page_match = re.search(r'page=(\d+)>; rel="last"', link_header)
                        if last_page_match:
                            contributors_count = int(last_page_match.group(1))
                    else:
                        # If no pagination, count the returned contributors
                        contributors_data = contributors_response.json()
                        contributors_count = len(contributors_data) if contributors_data else 0
            except Exception as e:
                print(f"    Could not get contributors count: {e}")
                contributors_count = 0
            
            # Get latest release or latest commit
            last_activity = "No releases"
            try:
                releases_url = f"https://api.github.com/repos/{repo_name}/releases/latest"
                releases_response = requests.get(releases_url, headers=self.headers)
                
                if releases_response.status_code == 200:
                    release_data = releases_response.json()
                    release_date = datetime.strptime(release_data['published_at'], '%Y-%m-%dT%H:%M:%SZ')
                    last_activity = f"{release_data['tag_name']} ({release_date.strftime('%b %d, %Y')})"
                else:
                    # Fallback to last commit
                    commits_url = f"https://api.github.com/repos/{repo_name}/commits?per_page=1"
                    commits_response = requests.get(commits_url, headers=self.headers)
                    if commits_response.status_code == 200:
                        commits_data = commits_response.json()
                        if commits_data:
                            commit_date = datetime.strptime(commits_data[0]['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')
                            last_activity = f"Last commit ({commit_date.strftime('%b %d, %Y')})"
            except Exception as e:
                print(f"    Could not get activity info: {e}")
                last_activity = "Active"
            
            stats = {
                'stars': repo_data['stargazers_count'],
                'contributors': contributors_count,
                'last_activity': last_activity,
                'archived': repo_data['archived'],
                'updated_at': repo_data['updated_at'],
                'language': repo_data.get('language', 'Unknown')
            }
            
            print(f"    {repo_data['stargazers_count']} stars, {contributors_count} contributors")
            return stats
            
        except Exception as e:
            print(f"  Error processing {repo_name}: {str(e)}")
            return None
    
    def search_new_solana_projects(self, query, existing_repos):
        """Search for new Solana projects"""
        print(f"Searching: {query}")
        
        search_url = f"https://api.github.com/search/repositories"
        params = {
            'q': query,
            'sort': 'stars',
            'order': 'desc',
            'per_page': 15  # Reduced to save API calls
        }
        
        try:
            response = requests.get(search_url, headers=self.headers, params=params)
            
            if response.status_code != 200:
                print(f"  Search failed: {response.status_code}")
                return []
            
            search_data = response.json()
            new_repos = []
            
            for repo in search_data['items']:
                repo_name = repo['full_name']
                
                # Skip if already in our list
                if repo_name in existing_repos:
                    continue
                
                # Skip forks and very small repos
                if repo['fork'] or repo['stargazers_count'] < 3:
                    continue
                
                # Check if it's actually Solana-related
                description = (repo['description'] or '').lower()
                is_solana_related = (
                    'solana' in description or 
                    'anchor' in description or
                    'spl' in description or
                    'metaplex' in description
                )
                
                if is_solana_related:
                    category = self.categorize_repo(repo['description'], repo.get('topics', []))
                    
                    new_repos.append({
                        'name': repo['name'],
                        'repo': repo_name,
                        'description': repo['description'] or 'No description available',
                        'category': category,
                        'stars': repo['stargazers_count'],
                        'is_new': True
                    })
                    print(f"  Found: {repo_name} ({repo['stargazers_count']} stars)")
            
            return new_repos
            
        except Exception as e:
            print(f"  Search error: {e}")
            return []
    
    def categorize_repo(self, description, topics):
        """Auto-categorize based on description and topics"""
        desc = (description or '').lower()
        topics = [t.lower() for t in (topics or [])]
        
        # Check topics first (more reliable)
        if 'wallet' in topics or 'mobile' in topics:
            return 'Wallets & Mobile'
        elif 'nft' in topics or 'metaplex' in topics:
            return 'NFTs & Programs'
        elif 'defi' in topics or 'dex' in topics:
            return 'DeFi'
        elif 'oracle' in topics:
            return 'Oracles'
        elif 'sdk' in topics or 'api' in topics:
            return 'SDKs & Tooling'
        
        # Check description
        if any(word in desc for word in ['wallet', 'mobile']):
            return 'Wallets & Mobile'
        elif any(word in desc for word in ['nft', 'metaplex', 'candy', 'token metadata']):
            return 'NFTs & Programs'
        elif any(word in desc for word in ['defi', 'dex', 'swap', 'amm', 'jupiter']):
            return 'DeFi'
        elif any(word in desc for word in ['oracle', 'price', 'feed', 'switchboard']):
            return 'Oracles'
        elif any(word in desc for word in ['payment', 'pay']):
            return 'Payments'
        elif any(word in desc for word in ['validator', 'node', 'rpc', 'infrastructure', 'agave']):
            return 'Infrastructure'
        elif any(word in desc for word in ['sdk', 'client', 'api', 'library', 'framework']):
            return 'SDKs & Tooling'
        else:
            return 'SDKs & Tooling'  # Default
    
    def format_number(self, num):
        """Format large numbers (e.g., 1500 -> 1.5k)"""
        if num >= 1000:
            return f"{num/1000:.1f}k"
        return str(num)
    
    def update_readme(self, repos_data):
        """Update the README with fresh data"""
        print("Updating README.md...")
        
        # Group by category
        categories = {
            'Infrastructure': [],
            'SDKs & Tooling': [],
            'Wallets & Mobile': [],
            'Programs (SPL)': [],
            'NFTs & Programs': [],
            'NFTs & Minting': [],
            'Payments': [],
            'DeFi': [],
            'Oracles': []
        }
        
        for repo in repos_data:
            category = repo.get('category', 'SDKs & Tooling')
            # Handle legacy category names
            if category == 'Programs (SPL/Metaplex) & NFTs':
                category = 'NFTs & Programs'
            categories[category].append(repo)
        
        # Read current README
        try:
            with open('README.md', 'r', encoding='utf-8') as f:
                readme_content = f.read()
        except FileNotFoundError:
            print("README.md not found!")
            return
        
        # Generate new table
        table_lines = [
            "| Project | Description | Repo | Stars | Contributors | Last Activity | Category |",
            "|---|---|---|---|---|---|---|"
        ]
        
        new_projects_count = 0
        
        for category, repos in categories.items():
            if not repos:  # Skip empty categories
                continue
                
            for repo in repos:
                stats = repo.get('stats', {})
                
                # Format stats
                if stats:
                    stars = self.format_number(stats.get('stars', 0))
                    contributors = stats.get('contributors', 0)
                    contributors_str = str(contributors) if contributors > 0 else '—'
                    last_activity = stats.get('last_activity', 'Active')
                    
                    # Handle archived repos
                    if stats.get('archived'):
                        last_activity = f"Archived; {last_activity}"
                else:
                    stars = '—'
                    contributors_str = '—'
                    last_activity = 'Active'
                
                # Mark new repos
                name = repo['name']
                if repo.get('is_new'):
                    name = f"NEW {name}"
                    new_projects_count += 1
                
                repo_url = f"https://github.com/{repo['repo']}"
                
                table_lines.append(
                    f"| {name} | {repo['description']} | {repo_url} | {stars} | {contributors_str} | {last_activity} | {category} |"
                )
        
        # Replace table in README
        table_content = '\n'.join(table_lines)
        
        # Find and replace the table section
        pattern = r'(\| Project \| Description.*?\n\|.*?\n)(.*?)(\n\n- Stars/Contributors:)'
        
        new_readme = re.sub(
            pattern,
            f'\\1{table_content}\\3',
            readme_content,
            flags=re.DOTALL
        )
        
        # Update the "Last updated" line
        today = datetime.now().strftime('%Y-%m-%d')
        new_readme = re.sub(
            r'Last updated: \d{4}-\d{2}-\d{2}',
            f'Last updated: {today}',
            new_readme
        )
        
        # Write back to file
        try:
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_readme)
            
            print(f"README.md updated successfully!")
            if new_projects_count > 0:
                print(f"Added {new_projects_count} new projects!")
                
        except Exception as e:
            print(f"Error writing README: {e}")


def main():
    print("Starting Solana Projects Auto-Updater...")
    print("=" * 50)
    
    # Load config
    try:
        with open('repos.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        print(f"Loaded {len(config['repositories'])} existing repositories")
    except FileNotFoundError:
        print("repos.yaml not found! Please create it first.")
        return
    except Exception as e:
        print(f"Error loading repos.yaml: {e}")
        return
    
    # Get GitHub token from environment
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        print("Please set GITHUB_TOKEN environment variable")
        print("   Get one from: https://github.com/settings/tokens")
        return
    
    tracker = SolanaRepoTracker(github_token)
    tracker.check_rate_limit()
    
    # Update existing repos
    repos_data = config['repositories'].copy()
    existing_repo_names = {repo['repo'] for repo in repos_data}
    
    print(f"\nUpdating {len(repos_data)} existing repositories...")
    print("-" * 40)
    
    for i, repo in enumerate(repos_data, 1):
        print(f"[{i}/{len(repos_data)}] {repo['repo']}")
        stats = tracker.get_repo_stats(repo['repo'])
        repo['stats'] = stats
        
        # Check rate limit every 10 requests
        if i % 10 == 0:
            tracker.check_rate_limit()
    
    # Search for new projects
    print(f"\nSearching for new Solana projects...")
    print("-" * 40)
    
    for query in config['search_queries']:
        new_repos = tracker.search_new_solana_projects(query, existing_repo_names)
        
        for new_repo in new_repos:
            # Get stats for new repos too
            stats = tracker.get_repo_stats(new_repo['repo'])
            new_repo['stats'] = stats
            
            repos_data.append(new_repo)
            existing_repo_names.add(new_repo['repo'])
        
        # Brief pause between searches to be nice to the API
        time.sleep(1)
    
    # Update README
    print(f"\nGenerating new README...")
    print("-" * 40)
    tracker.update_readme(repos_data)
    
    # Update repos.yaml with new discoveries (remove 'is_new' flag for persistence)
    for repo in repos_data:
        if 'is_new' in repo:
            del repo['is_new']
    
    config['repositories'] = repos_data
    
    try:
        with open('repos.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print("Updated repos.yaml with new projects")
    except Exception as e:
        print(f"Error updating repos.yaml: {e}")
    
    print(f"\nUpdate complete!")
    print(f"Total projects: {len(repos_data)}")
    print("=" * 50)

if __name__ == "__main__":
    main()
