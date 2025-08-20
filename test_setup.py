#!/usr/bin/env python3
"""
Quick test script to verify our Solana repo tracker setup
"""

import os
import sys
import requests
import yaml

def test_setup():
    """Test if everything is set up correctly"""
    print("🧪 Testing Solana Repo Tracker Setup")
    print("=" * 40)
    
    # Test 1: Check if required files exist
    required_files = ['repos.yaml', 'update_repos.py', 'README.md']
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} found")
        else:
            print(f"❌ {file} missing")
            return False
    
    # Test 2: Check if repos.yaml is valid
    try:
        with open('repos.yaml', 'r') as f:
            config = yaml.safe_load(f)
        print(f"✅ repos.yaml valid - {len(config['repositories'])} repos loaded")
    except Exception as e:
        print(f"❌ repos.yaml error: {e}")
        return False
    
    # Test 3: Check GitHub token
    github_token = os.getenv('GITHUB_TOKEN')
    if github_token:
        print("✅ GITHUB_TOKEN environment variable set")
        
        # Test API access
        try:
            headers = {'Authorization': f'token {github_token}'}
            response = requests.get('https://api.github.com/rate_limit', headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ GitHub API access working - {data['rate']['remaining']}/5000 requests remaining")
            else:
                print(f"❌ GitHub API error: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ GitHub API test failed: {e}")
            return False
    else:
        print("⚠️  GITHUB_TOKEN not set - you'll need this for the full script")
        print("   Create one at: https://github.com/settings/tokens")
        print("   Then run: export GITHUB_TOKEN='your_token_here'")
    
    # Test 4: Quick API call to a known Solana repo
    if github_token:
        try:
            test_repo = "coral-xyz/anchor"
            url = f"https://api.github.com/repos/{test_repo}"
            headers = {'Authorization': f'token {github_token}'}
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Test API call successful - {test_repo} has {data['stargazers_count']} stars")
            else:
                print(f"❌ Test API call failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Test API call error: {e}")
            return False
    
    print("\n🎉 Setup test completed successfully!")
    print("\nNext steps:")
    print("1. Set GITHUB_TOKEN if not already set")
    print("2. Run: python update_repos.py")
    print("3. Check the updated README.md")
    
    return True

if __name__ == "__main__":
    success = test_setup()
    sys.exit(0 if success else 1)
