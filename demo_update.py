#!/usr/bin/env python3
"""
Demo version of the Solana Repo Tracker - works without GitHub token
Uses cached/mock data to demonstrate the functionality
"""

import yaml
import json
import re
from datetime import datetime, timedelta
import os

# Mock data for demo purposes
MOCK_REPO_DATA = {
    "coral-xyz/anchor": {
        "stars": 3729,
        "contributors": 187,
        "last_activity": "v0.30.1 (Dec 15, 2024)",
        "archived": False,
        "language": "Rust"
    },
    "solana-labs/solana": {
        "stars": 13847,
        "contributors": 488,
        "last_activity": "Archived; v1.18.26 (Oct 2024)",
        "archived": True,
        "language": "Rust"
    },
    "anza-xyz/agave": {
        "stars": 426,
        "contributors": 89,
        "last_activity": "v2.0.17 (Dec 20, 2024)",
        "archived": False,
        "language": "Rust"
    },
    "solana-foundation/solana-web3.js": {
        "stars": 2156,
        "contributors": 136,
        "last_activity": "v1.98.2 (Apr 24, 2025)",
        "archived": False,
        "language": "TypeScript"
    }
}

MOCK_NEW_PROJECTS = [
    {
        "name": "solana-program-test",
        "repo": "solana-labs/solana-program-test",
        "description": "Framework for testing Solana programs",
        "category": "SDKs & Tooling",
        "stars": 127,
        "is_new": True
    },
    {
        "name": "pyth-sdk-solana",
        "repo": "pyth-network/pyth-sdk-solana",
        "description": "Pyth SDK for Solana price feeds",
        "category": "Oracles",
        "stars": 89,
        "is_new": True
    }
]

class SolanaRepoDemoTracker:
    def __init__(self):
        self.demo_mode = True
    
    def format_number(self, num):
        """Format large numbers (e.g., 1500 -> 1.5k)"""
        if num >= 1000:
            return f"{num/1000:.1f}k"
        return str(num)
    
    def get_mock_stats(self, repo_name):
        """Get mock stats for demo"""
        if repo_name in MOCK_REPO_DATA:
            return MOCK_REPO_DATA[repo_name]
        
        # Generate some reasonable mock data
        import random
        stars = random.randint(10, 1000)
        contributors = random.randint(5, 50)
        
        return {
            "stars": stars,
            "contributors": contributors,
            "last_activity": "Active (mock data)",
            "archived": False,
            "language": "Unknown"
        }
    
    def update_readme(self, repos_data):
        """Update the README with fresh data"""
        print("📝 Updating README.md (DEMO MODE)...")
        
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
            print("❌ README.md not found!")
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
                    name = f"🆕 {name}"
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
            f'Last updated: {today} (DEMO MODE)',
            new_readme
        )
        
        # Write back to file
        try:
            with open('README_DEMO.md', 'w', encoding='utf-8') as f:
                f.write(new_readme)
            
            print(f"✅ README_DEMO.md created successfully!")
            print(f"📊 Demo includes {len(repos_data)} total repositories")
            if new_projects_count > 0:
                print(f"🆕 Simulated {new_projects_count} new projects!")
                
        except Exception as e:
            print(f"❌ Error writing README: {e}")

def main():
    print("🚀 Solana Projects Demo Tracker")
    print("🎭 Running in DEMO MODE (no GitHub token required)")
    print("=" * 60)
    
    # Load config
    try:
        with open('repos.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        print(f"📋 Loaded {len(config['repositories'])} existing repositories")
    except FileNotFoundError:
        print("❌ repos.yaml not found! Please create it first.")
        return
    except Exception as e:
        print(f"❌ Error loading repos.yaml: {e}")
        return
    
    tracker = SolanaRepoDemoTracker()
    
    # Update existing repos with mock data
    repos_data = config['repositories'].copy()
    
    print(f"\n📊 Simulating updates for {len(repos_data)} repositories...")
    print("-" * 50)
    
    for i, repo in enumerate(repos_data, 1):
        print(f"[{i}/{len(repos_data)}] 📈 Mock update: {repo['repo']}")
        stats = tracker.get_mock_stats(repo['repo'])
        repo['stats'] = stats
        print(f"    ✅ {stats['stars']} stars, {stats['contributors']} contributors")
    
    # Add some mock new projects
    print(f"\n🔍 Simulating discovery of new projects...")
    print("-" * 50)
    
    for new_repo in MOCK_NEW_PROJECTS:
        print(f"🆕 Found: {new_repo['repo']} ({new_repo['stars']} stars)")
        stats = tracker.get_mock_stats(new_repo['repo'])
        new_repo['stats'] = stats
        repos_data.append(new_repo)
    
    # Update README
    print(f"\n📝 Generating demo README...")
    print("-" * 50)
    tracker.update_readme(repos_data)
    
    print(f"\n🎉 Demo completed!")
    print(f"📄 Check README_DEMO.md to see the results")
    print(f"📊 Total projects in demo: {len(repos_data)}")
    print(f"🆕 New projects simulated: {len(MOCK_NEW_PROJECTS)}")
    print("\n💡 To run with real data:")
    print("   1. Get GitHub token from: https://github.com/settings/tokens")
    print("   2. export GITHUB_TOKEN='your_token_here'")
    print("   3. python3 update_repos.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
