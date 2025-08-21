#!/usr/bin/env python3
"""
Demo script to showcase the Solana Projects Tracker functionality
without requiring a GitHub token (read-only operations).
"""

import yaml
import json
from update_repos import SolanaRepoTracker

def demo_without_token():
    """Demonstrate the tracker functionality without GitHub API calls"""
    print("🎮 Solana Projects Tracker - Demo Mode")
    print("=" * 50)
    
    # Load existing configuration
    try:
        with open('repos.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        print(f"✅ Loaded configuration with {len(config['repositories'])} repositories")
    except FileNotFoundError:
        print("❌ repos.yaml not found!")
        return
    
    # Create tracker instance (no API calls in demo mode)
    tracker = SolanaRepoTracker("demo_token")
    
    # Demonstrate categorization logic
    print("\n🏷️  Category Classification Examples:")
    print("-" * 30)
    
    test_cases = [
        ("Solana wallet for mobile devices", ["wallet", "mobile"]),
        ("DEX aggregator for Solana", ["defi", "trading"]),
        ("NFT marketplace on Solana", ["nft", "marketplace"]),
        ("Anchor framework for smart contracts", ["framework", "sdk"]),
        ("Solana validator node software", ["infrastructure"]),
        ("Oracle price feeds for DeFi", ["oracle", "price"]),
    ]
    
    for description, topics in test_cases:
        category = tracker.categorize_repo(description, topics)
        print(f"📋 '{description[:40]}...' → {category}")
    
    # Demonstrate number formatting
    print("\n📊 Number Formatting Examples:")
    print("-" * 30)
    
    numbers = [42, 156, 1500, 12500, 125000]
    for num in numbers:
        formatted = tracker.format_number(num)
        print(f"💫 {num:>6} → {formatted}")
    
    # Show repository statistics
    print("\n📈 Repository Categories Breakdown:")
    print("-" * 35)
    
    category_counts = {}
    for repo in config['repositories']:
        category = repo.get('category', 'Unknown')
        category_counts[category] = category_counts.get(category, 0) + 1
    
    # Sort by count
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    
    for category, count in sorted_categories:
        bar = "█" * min(20, count // 2)  # Visual bar chart
        print(f"🔹 {category:<20} {count:>3} {bar}")
    
    # Show search queries
    print(f"\n🔍 Configured Search Queries ({len(config['search_queries'])}):")
    print("-" * 35)
    
    for i, query in enumerate(config['search_queries'], 1):
        print(f"{i:>2}. {query}")
    
    print("\n✨ Demo completed! To run with live data:")
    print("   1. Get a GitHub token: https://github.com/settings/tokens")
    print("   2. export GITHUB_TOKEN='your_token_here'")
    print("   3. python update_repos.py")
    print("=" * 50)

if __name__ == "__main__":
    demo_without_token()