# Open-source Solana Projects — Live Sheet Reference 

A curated list of actively maintained open-source projects in the Solana ecosystem. Each entry includes a short description, repository link, and key maintenance signals (stars, contributors, last activity), organized by category.

Notes
- Counts change frequently; treat numbers as snapshots. For auto-updates, consider adding a GitHub Actions workflow to refresh this table daily or weekly.
- Focus areas: core infrastructure, SDKs, tooling, wallets, payments, NFTs, DeFi, and oracles.

Last updated: 2025-08-19

## Directory

- Infrastructure
- SDKs & Tooling
- Wallets & Mobile
- Programs (SPL/Metaplex) & NFTs
- Payments
- DeFi & Oracles

## Projects (Snapshot)

| Project | Description | Repo | Stars | Contributors | Last Activity | Category |
|---|---|---|---|---|---|---|
| Solana (archived; moved to Agave) | Web-scale blockchain reference implementation; now archived with development transitioned to Agave | https://github.com/solana-labs/solana | 14.3k | 488 | Archived; last release v1.18.26 (Oct 2024) | Infrastructure |
| Agave (validator) | Current Solana validator implementation maintained by Anza | https://github.com/anza-xyz/agave | — | — | Active | Infrastructure |
| Solana SDK (Rust) | Rust SDK used by on-chain program developers and the Agave validator | https://github.com/anza-xyz/solana-sdk | — | — | Active | SDKs & Tooling |
| Anchor | Framework for building Solana programs (Rust eDSL, IDL, TS client, CLI) | https://github.com/coral-xyz/anchor | 4.5k | — | Active | SDKs & Tooling |
| Solana Web3.js (v1.x) | Official JavaScript SDK (maintenance branch; successor work referenced as @solana/kit) | https://github.com/solana-foundation/solana-web3.js | 2.5k | 136 | v1.98.2 (Apr 24, 2025) | SDKs & Tooling |
| Wallet Adapter | Modular TypeScript wallet adapters and UI components | https://github.com/anza-xyz/wallet-adapter | 1.9k | 122 | Releases (Jun 10, 2025) | Wallets & Mobile |
| Solana Program Library (legacy) | Historic collection of core on-chain programs; archived and migrated to new org | https://github.com/solana-labs/solana-program-library | 4k | 239 | Archived (Mar 11, 2025) | Programs (SPL) |
| SPL Libraries (new org) | Helper libraries/building blocks for on-chain programs | https://github.com/solana-program/libraries | 6 | 21 | Release (Apr 14, 2025) | Programs (SPL) |
| Metaplex Token Metadata | Core NFT/fungible token metadata program & SDKs | https://github.com/metaplex-foundation/mpl-token-metadata | — | — | Active | NFTs & Programs |
| Candy Machine (Core) | Metaplex Core Candy Machine (Core assets) | https://github.com/metaplex-foundation/mpl-core-candy-machine | — | — | Active | NFTs & Minting |
| Candy Machine (Token Metadata V3) | Candy Machine for Token Metadata NFTs | https://developers.metaplex.com/candy-machine | — | — | Docs current | NFTs & Minting |
| Jupiter org (SDKs/APIs) | DEX aggregator org with SDKs, APIs, examples | https://github.com/jup-ag | — | — | Active | DeFi |
| Jupiter Swap API | Jupiter V6 Swap API binaries and releases | https://github.com/jup-ag/jupiter-swap-api | 198 | 2 | v6.0.53 (Jul 17, 2025) | DeFi |
| Switchboard org | Oracle protocol; Solana SDKs and templates | https://github.com/switchboard-xyz | — | — | Active | Oracles |
| Solana Pay (standard) | Open payment standard and tooling for Solana | https://github.com/anza-xyz/solana-pay | — | — | Active | Payments |
| Solana Payments App | Reference Solana Pay integration app | https://github.com/solana-labs/solana-payments-app | — | — | Active | Payments |
| Solana Mobile Stack SDK | Android SDKs: Mobile Wallet Adapter, Seed Vault | https://github.com/solana-mobile/solana-mobile-stack-sdk | — | — | Active | Wallets & Mobile |
| Mobile Wallet Adapter | Protocol for connecting apps to mobile wallets | https://github.com/solana-mobile/mobile-wallet-adapter | — | — | Active | Wallets & Mobile |
| Seed Vault SDK | Secure key custody API/service for Android | https://github.com/solana-mobile/seed-vault-sdk | — | — | Active | Wallets & Mobile |
| Solders (Python) | High-performance Python toolkit for Solana (Rust-backed) | https://github.com/kevinheavey/solders | — | — | Active | SDKs & Tooling |
| Solana Python (solana) | Python client library (PyPI package name: “solana”) | https://github.com/michaelhly/solana-py (or successor org) | — | — | Active | SDKs & Tooling |

- Stars/Contributors: Snapshot values; “—” indicates to-be-filled or varies (especially for org-level entries or during repo migrations).
- Last Activity: Typically last release or last commit; “Docs current” for documentation sources.

## How will i keep README “Live”

Option A — Manual refresh
- Periodically check each repo and update stars, contributors, and last activity.

Option B — Automated updates( will implement) 
- Add a scheduled GitHub Actions workflow that:
  - Reads a JSON/YAML list of repos.
  - Queries the GitHub API for stars, contributors, last commit/release.
  - Rebuilds this table and commits changes daily/weekly.





## Contributions

- PRs welcome for additions, category tweaks, and fixes.
- Preference for:
  - Active repos with recent commits/releases.
  - NEW projects
  - Widely used infrastructure, SDKs, standards, and tooling.
  - Clear OSS licensing and good documentation.
 
Stars ⭐ appreciated — helps others discover this repo.  
More projects & automation (GitHub Actions for live updates) coming soon.  


## Security note 

