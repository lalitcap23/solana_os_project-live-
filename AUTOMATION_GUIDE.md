# Solana Projects Auto-Updater

🤖 Automated tracking and discovery of Solana open-source projects with GitHub Actions.

## 🚀 Features

- **Auto-discovery** of new Solana projects via GitHub API search
- **Live stats updates** - stars, contributors, last activity every 3 days
- **Smart categorization** - automatically categorizes projects by type
- **GitHub Actions automation** - runs on schedule without manual intervention
- **Rate limit handling** - respects GitHub API limits
- **New project alerts** - marks discoveries with 🆕 emoji

## 📁 Project Structure

```
├── README.md              # Main project documentation (auto-updated)
├── repos.yaml            # Repository configuration and data
├── update_repos.py       # Main automation script
├── demo_update.py        # Demo version (no token required)
├── test_setup.py         # Setup verification script
├── requirements.txt      # Python dependencies
└── .github/workflows/
    └── update-repos.yml  # GitHub Actions workflow
```

## 🛠️ Setup Instructions

### 1. GitHub Personal Access Token

Create a GitHub Personal Access Token:

1. Go to [GitHub Settings → Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select scopes:
   - ✅ `public_repo` (for reading public repositories)
   - ✅ `repo` (if you want to update private repos)
4. Copy the token

### 2. Local Setup

```bash
# Clone and navigate to your repo
cd your-solana-projects-repo

# Install dependencies
pip install -r requirements.txt

# Set your GitHub token
export GITHUB_TOKEN="your_token_here"

# Test the setup
python3 test_setup.py

# Run a demo (no token needed)
python3 demo_update.py

# Run the real updater
python3 update_repos.py
```

### 3. GitHub Actions Setup

1. **Add Repository Secret:**
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `GITHUB_TOKEN`
   - Value: Your personal access token

2. **Enable Actions:**
   - Go to Actions tab in your repo
   - Enable GitHub Actions if not already enabled
   - The workflow will run automatically every 3 days

3. **Manual Trigger:**
   - Go to Actions → "Auto-Update Solana Projects"
   - Click "Run workflow" to trigger manually

## 📋 Configuration

### repos.yaml Structure

```yaml
repositories:
  - name: "Project Name"
    repo: "owner/repo-name"
    description: "Project description"
    category: "Category Name"

search_queries:
  - "solana framework language:rust stars:>50"
  - "anchor solana stars:>10"
  # Add more search queries...
```

### Categories

- **Infrastructure** - Validators, nodes, core systems
- **SDKs & Tooling** - Development libraries, frameworks
- **Wallets & Mobile** - Wallet software, mobile apps
- **Programs (SPL)** - Smart contracts, on-chain programs
- **NFTs & Programs** - NFT-related projects
- **Payments** - Payment systems, Solana Pay
- **DeFi** - Decentralized finance protocols
- **Oracles** - Price feeds, data oracles

## 🤖 How It Works

### Discovery Process

1. **Search GitHub** using configured queries
2. **Filter results** by stars, activity, and Solana relevance
3. **Auto-categorize** based on description and topics
4. **Fetch stats** for all repositories
5. **Update README** with formatted table
6. **Commit changes** automatically

### Rate Limiting

- GitHub API: 5,000 requests/hour
- Script includes rate limit checks
- Pauses when limits are low
- Optimized API calls

### Scheduling

```yaml
# Runs every 3 days at 6 AM UTC
- cron: '0 6 */3 * *'
```

## 📊 Output

The automation generates:

1. **Updated README.md** with fresh stats
2. **Updated repos.yaml** with new discoveries
3. **Commit messages** with change summaries
4. **Action summaries** with run details

Example commit message:
```
🤖 Auto-update: Solana projects refresh (2025-08-20)

📊 Repository statistics updated
🔍 New project discovery completed
📝 README.md regenerated with latest data

⚡ Automated by GitHub Actions
```

## 🔧 Customization

### Add New Search Queries

Edit `repos.yaml`:

```yaml
search_queries:
  - "solana defi language:rust stars:>20"
  - "metaplex nft solana stars:>5"
  - "your custom query here"
```

### Modify Categories

Update the `categorize_repo()` function in `update_repos.py`:

```python
def categorize_repo(self, description, topics):
    # Add your custom categorization logic
    if 'your_keyword' in description:
        return 'Your Custom Category'
```

### Change Schedule

Edit `.github/workflows/update-repos.yml`:

```yaml
schedule:
  # Run daily at midnight
  - cron: '0 0 * * *'
  # Run every Monday at 9 AM
  - cron: '0 9 * * 1'
```

## 🐛 Troubleshooting

### Common Issues

1. **Rate limit exceeded**
   - Wait for reset (shown in logs)
   - Reduce search queries temporarily

2. **Token permissions**
   - Ensure token has `public_repo` scope
   - Check token hasn't expired

3. **Workflow not running**
   - Check Actions are enabled
   - Verify workflow file syntax
   - Check repository secrets

### Debug Mode

Add debug logging:

```bash
export DEBUG=1
python3 update_repos.py
```

## 📈 Monitoring

### GitHub Actions Logs

- Go to Actions tab → Latest run
- Check job logs for errors
- Review step summaries

### API Usage

```bash
# Check current rate limit
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/rate_limit
```

## 🤝 Contributing

1. Fork the repository
2. Make your changes
3. Test with `python3 test_setup.py`
4. Submit a pull request

### Adding New Features

- New search strategies
- Better categorization logic
- Additional statistics
- UI improvements

## 📄 License

MIT License - feel free to adapt for your own projects!

## 🔗 Related Projects

- [Solana Foundation](https://solana.org/)
- [Awesome Solana](https://github.com/paul-schaaf/awesome-solana)
- [Solana Cookbook](https://solanacookbook.com/)

---

⭐ Star this repo if it helps you discover amazing Solana projects!
