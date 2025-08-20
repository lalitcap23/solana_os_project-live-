#!/usr/bin/env python3
"""
Interactive setup script for Solana Projects Auto-Updater
"""

import os
import sys
import getpass
import requests
import subprocess

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import yaml
        import requests
        print("✅ Python dependencies satisfied")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("💡 Install with: pip install -r requirements.txt")
        return False

def setup_github_token():
    """Interactive GitHub token setup"""
    print("\n🔑 GitHub Token Setup")
    print("=" * 30)
    
    # Check if token already exists
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            content = f.read()
            if 'GITHUB_TOKEN=' in content and 'your_github_token_here' not in content:
                print("✅ GitHub token already configured in .env file")
                return True
    
    print("📋 You need a GitHub Personal Access Token to run the automation.")
    print("   This allows the script to read public repository data.")
    print("")
    print("🌐 Steps to create a token:")
    print("   1. Go to: https://github.com/settings/tokens")
    print("   2. Click 'Generate new token (classic)'")
    print("   3. Give it a name like 'Solana Projects Tracker'")
    print("   4. Select scope: 'public_repo'")
    print("   5. Click 'Generate token'")
    print("   6. Copy the generated token")
    print("")
    
    # Ask if user wants to proceed
    proceed = input("📝 Do you have a GitHub token ready? (y/n): ").lower().strip()
    
    if proceed != 'y':
        print("⏸️  Setup paused. Come back when you have your token!")
        return False
    
    # Get token from user
    token = getpass.getpass("🔐 Paste your GitHub token (hidden input): ").strip()
    
    if not token:
        print("❌ No token provided. Setup cancelled.")
        return False
    
    # Test the token
    print("🧪 Testing token...")
    try:
        headers = {'Authorization': f'token {token}'}
        response = requests.get('https://api.github.com/rate_limit', headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            remaining = data['rate']['remaining']
            print(f"✅ Token works! API calls remaining: {remaining}/5000")
        else:
            print(f"❌ Token test failed: {response.status_code}")
            print("💡 Please check your token and try again.")
            return False
            
    except Exception as e:
        print(f"❌ Error testing token: {e}")
        return False
    
    # Save to .env file
    env_content = f"# Solana Projects Auto-Updater Environment\nGITHUB_TOKEN={token}\n"
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("💾 Token saved to .env file")
        return True
    except Exception as e:
        print(f"❌ Error saving token: {e}")
        return False

def test_setup():
    """Run the test script"""
    print("\n🧪 Testing Setup")
    print("=" * 20)
    
    # Load environment variables
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    
    try:
        result = subprocess.run([sys.executable, 'test_setup.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Setup test passed!")
            return True
        else:
            print("❌ Setup test failed:")
            print(result.stdout)
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error running test: {e}")
        return False

def main():
    print("🚀 Solana Projects Auto-Updater - Interactive Setup")
    print("=" * 55)
    print("")
    
    # Step 1: Check dependencies
    print("1️⃣ Checking dependencies...")
    if not check_dependencies():
        return
    
    # Step 2: Setup GitHub token
    print("\n2️⃣ Setting up GitHub token...")
    if not setup_github_token():
        return
    
    # Step 3: Test setup
    print("\n3️⃣ Testing setup...")
    if not test_setup():
        return
    
    print("\n🎉 Setup Complete!")
    print("=" * 20)
    print("")
    print("📋 What's next:")
    print("   🎮 python3 demo_update.py      # Try the demo")
    print("   🚀 python3 update_repos.py     # Run full update")
    print("   📖 Read AUTOMATION_GUIDE.md    # Complete guide")
    print("")
    print("⚡ GitHub Actions will run automatically every 3 days")
    print("   (after you push to GitHub and add GITHUB_TOKEN secret)")

if __name__ == "__main__":
    main()
