# Open-source Solana Projects — Live Sheet Reference

## 🤖 Automation Status: IMPLEMENTED!

✅ **Fully Automated Updates** - This repository now automatically:
- 🔍 **Discovers new Solana projects** via GitHub API search
- 📊 **Updates repository statistics** (stars, contributors, activity) 
- 📝 **Regenerates this README** with fresh data
- 💾 **Commits changes** every 30 minute via GitHub Actions
- 🆕 **Highlights new discoveries** with emoji markers

📋 **Setup Guide:** See [AUTOMATION_GUIDE.md](./AUTOMATION_GUIDE.md) for full details

🎮 **Try the Demo:** Run `python3 demo_update.py` (no GitHub token needed)


A curated list of actively maintained open-source projects in the Solana ecosystem. Each entry includes a short description, repository link, and key maintenance signals (stars, contributors, last activity), organized by category.

Notes
- Counts change frequently; treat numbers as snapshots. For auto-updates, consider adding a GitHub Actions workflow to refresh this table daily or weekly.
- Focus areas: core infrastructure, SDKs, tooling, wallets, payments, NFTs, DeFi, and oracles.

Last updated: 2025-08-28

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
| Project | Description | Repo | Stars | Contributors | Last Activity | Category |
|---|---|---|---|---|---|---|
| Solana (archived; moved to Agave) | Web-scale blockchain reference implementation; now archived with development transitioned to Agave | https://github.com/solana-labs/solana | 14.3k | 352 | Archived; v1.18.26 (Oct 12, 2024) | Infrastructure |
| Agave (validator) | Current Solana validator implementation maintained by Anza | https://github.com/anza-xyz/agave | 1.3k | 362 | v2.3.7 (Aug 08, 2025) | Infrastructure |
| Solana SDK (Rust) | Rust SDK used by on-chain program developers and the Agave validator | https://github.com/anza-xyz/solana-sdk | 113 | 149 | sanitize@v3.0.1 (Aug 27, 2025) | SDKs & Tooling |
| Anchor | Framework for building Solana programs (Rust eDSL, IDL, TS client, CLI) | https://github.com/coral-xyz/anchor | 4.6k | 303 | v0.31.1 (Apr 19, 2025) | SDKs & Tooling |
| Solana Web3.js (v1.x) | Official JavaScript SDK (maintenance branch; successor work referenced as @solana/kit) | https://github.com/solana-foundation/solana-web3.js | 2.6k | 127 | v1.98.4 (Jul 31, 2025) | SDKs & Tooling |
| Solders (Python) | High-performance Python toolkit for Solana (Rust-backed) | https://github.com/kevinheavey/solders | 406 | 8 | 0.26.0 (Feb 18, 2025) | SDKs & Tooling |
| anchor | ⚓ Solana Sealevel Framework | https://github.com/solana-foundation/anchor | 4.6k | 303 | v0.31.1 (Apr 19, 2025) | SDKs & Tooling |
| trident | Rust-based framework to Fuzz Solana programs, designed to help you ship secure code. | https://github.com/Ackee-Blockchain/trident | 307 | 19 | 0.11.0 (Aug 14, 2025) | SDKs & Tooling |
| solana-poc-framework | A framework for creating PoC's for Solana Smart Contracts in a painless and intuitive way | https://github.com/neodyme-labs/solana-poc-framework | 234 | 12 | Last commit (May 20, 2025) | SDKs & Tooling |
| steel | Solana smart contract framework. | https://github.com/regolith-labs/steel | 233 | 7 | 2.1.0 (Oct 23, 2024) | SDKs & Tooling |
| nautilus | SQL-native Solana program framework | https://github.com/nautilus-project/nautilus | 93 | 6 | Last commit (Nov 08, 2024) | SDKs & Tooling |
| znap | Performance-first Rust Framework to build APIs compatible with the Solana Actions Spec. | https://github.com/heavy-duty/znap | 69 | 4 | 0.1.36 (Aug 29, 2024) | SDKs & Tooling |
| sol-ctf-framework | Framework for Solana CTF challenges | https://github.com/otter-sec/sol-ctf-framework | 67 | 6 | Last commit (May 24, 2025) | SDKs & Tooling |
| ethereum-boilerplate | The ultimate NextJS Ethereum Dapp Boilerplate which gives you maximum flexibility and speed. Feel free to fork and contribute. Although this repo is called "Ethereum Boilerplate" it works with any EVM system and since it uses Moralis SDK You can even use it on Solana!  Happy BUIDL!👷‍♂️ | https://github.com/ethereum-boilerplate/ethereum-boilerplate | 4.1k | 11 | Last commit (Apr 26, 2023) | SDKs & Tooling |
| kit | Solana JavaScript SDK | https://github.com/anza-xyz/kit | 515 | 141 | v3.0.0 (Aug 27, 2025) | SDKs & Tooling |
| js-wallet-sdk | Multi-chain typescript signature sdk, supports bitcoin, ethereum, solana, cosmos, etc. | https://github.com/okx/js-wallet-sdk | 329 | 13 | Last commit (Aug 25, 2025) | SDKs & Tooling |
| program-examples | A repository of Solana program examples | https://github.com/solana-developers/program-examples | 1.3k | 45 | Last commit (Jul 23, 2025) | SDKs & Tooling |
| Solana_Dice_SmartContract | This project is a simple on-chain Dice Game smart contract built for the Solana blockchain using Rust and the Anchor framework. It demonstrates the fundamentals of Solana program development, including instruction handling, randomness simulation, state management, and token transfers. | https://github.com/kinexbt/Solana_Dice_SmartContract | 680 | 1 | Last commit (May 08, 2025) | SDKs & Tooling |
| Solana_Bita_Coinflip_SmartContract | A lightweight on-chain Coin Flip betting game built on the Solana blockchain using Rust and the Anchor framework. This contract allows users to wager SOL (or tokens) on a 50/50 coin flip outcome — win or lose instantly, with no intermediaries. | https://github.com/kinexbt/Solana_Bita_Coinflip_SmartContract | 674 | 1 | Last commit (May 07, 2025) | SDKs & Tooling |
| complete-guide-to-full-stack-solana-development | Code examples for the blog post titled The Complete Guide to Full Stack Solana Development with React, Anchor, Rust, and Phantom | https://github.com/dabit3/complete-guide-to-full-stack-solana-development | 485 | 2 | Last commit (Sep 18, 2021) | SDKs & Tooling |
| seahorse-lang | Write Anchor-compatible Solana programs in Python | https://github.com/ameliatastic/seahorse-lang | 343 | 4 | Last commit (Feb 24, 2023) | SDKs & Tooling |
| Solana-Prediction-Market | Solana Prediction Market where users can create market, add liquidity, and bet | https://github.com/HyperBuildX/Solana-Prediction-Market | 303 | 1 | Last commit (Aug 26, 2025) | SDKs & Tooling |
| awesome-solana-security | A collection of resources to help you build better and more secure Solana programs. Kept up to date. | https://github.com/0xMacro/awesome-solana-security | 307 | 2 | Last commit (Jun 18, 2025) | SDKs & Tooling |
| Pumpfun-solana-smart-contract | pump.fun clone: pumpfun smart contract fork (pump.fun fork), solana pump fun smart contract source code | https://github.com/cutupdev/Pumpfun-solana-smart-contract | 290 | 1 | Last commit (Jun 30, 2025) | SDKs & Tooling |
| anchor-go | Generate Go clients from anchor IDLs for Solana blockchain programs | https://github.com/gagliardetto/anchor-go | 267 | 4 | v1.0.0 (Jul 02, 2025) | SDKs & Tooling |
| solana-copy-bot | Copy any transaction at any address in Solana | https://github.com/Abraham-007/solana-copy-bot | 550 | 1 | Last commit (Aug 19, 2025) | SDKs & Tooling |
| solana-trading-bot | Solana Trading Bot - RC: For Solana token sniping and trading, the latest version has completed all optimizations | https://github.com/warp-abbott/solana-trading-bot | 536 | 1 | Last commit (Aug 19, 2025) | SDKs & Tooling |
| spl-token-ui | Interface for creating and managing SPL Tokens | https://github.com/paul-schaaf/spl-token-ui | 202 | 1 | Archived; Last commit (Jul 08, 2021) | SDKs & Tooling |
| solana-spl-token-sniper | Solana SPL-Token sniper for new Raydium liquidity pools | https://github.com/danbayk/solana-spl-token-sniper | 193 | 1 | Last commit (Mar 19, 2024) | SDKs & Tooling |
| solana-sniper-bot | AxisBot - Solana Sniper Bot. Snipe and sell SPL tokens at lightning speed.  Our sniping bot helps you maintain a higher level of security while also giving you the fastest sniping speed possible. Built by Traders for Traders. | https://github.com/AxisBotV2/solana-sniper-bot | 81 | 1 | Last commit (Jul 07, 2024) | SDKs & Tooling |
| solana-spl-tutorial | This repository contains full tutorial on Solana SPL token | https://github.com/YosephKS/solana-spl-tutorial | 75 | 1 | Last commit (Feb 12, 2022) | SDKs & Tooling |
| solana-playground | Quickly develop, deploy and test Solana programs from browsers | https://github.com/solana-playground/solana-playground | 818 | 28 | Last commit (Aug 27, 2025) | SDKs & Tooling |
| anchor-escrow | Escrow program implemented in Anchor | https://github.com/ironaddicteddog/anchor-escrow | 193 | 3 | Last commit (Aug 29, 2024) | SDKs & Tooling |
| pumpfun-rs | A comprehensive Rust SDK for seamless interaction with the PumpFun Solana program. | https://github.com/nhuxhr/pumpfun-rs | 140 | 5 | Last commit (Aug 15, 2025) | SDKs & Tooling |
| Solana-Auditors-Bootcamp | Learn to audit Solana programs and help secure the ecosystem. Take your security practices to the next level and get certified by Ackee Blockchain Security. It's free, too. | https://github.com/Ackee-Blockchain/Solana-Auditors-Bootcamp | 138 | 2 | Last commit (Sep 23, 2024) | SDKs & Tooling |
| radar | A static analysis tool for anchor rust programs. | https://github.com/Auditware/radar | 101 | 4 | Last commit (Aug 23, 2025) | SDKs & Tooling |
| odoo-solana-payments | Allows you to accept a variety of currencies (USDT, USDC, BTC, SOL) via the solana blockchain | https://github.com/t-900-a/odoo-solana-payments | 10 | 1 | Archived; Last commit (Nov 18, 2020) | SDKs & Tooling |
| solana-sign-with-payment | Prove ownership of a Solana address by asking the user to send a small amount | https://github.com/kizzx2/solana-sign-with-payment | 8 | 1 | Last commit (May 19, 2022) | SDKs & Tooling |
| pumpfun-smartcontract-solana | Pumpfun smart contract (Solana Pumpfun Smart Contract fork, Pumpfun smart contract development Tool, Pumpfun smart contract SDK) | https://github.com/printz-labs/pumpfun-smartcontract-solana | — | — | Active | SDKs & Tooling |
| Wallet Adapter | Modular TypeScript wallet adapters and UI components | https://github.com/anza-xyz/wallet-adapter | 1.9k | 115 | @solana/wallet-adapter-xdefi@0.1.11 (Jun 10, 2025) | Wallets & Mobile |
| Solana Mobile Stack SDK | Android SDKs: Mobile Wallet Adapter, Seed Vault | https://github.com/solana-mobile/solana-mobile-stack-sdk | 761 | 2 | Last commit (Jun 23, 2022) | Wallets & Mobile |
| Mobile Wallet Adapter | Protocol for connecting apps to mobile wallets | https://github.com/solana-mobile/mobile-wallet-adapter | 295 | 16 | v2.1.0 (Aug 18, 2025) | Wallets & Mobile |
| Seed Vault SDK | Secure key custody API/service for Android | https://github.com/solana-mobile/seed-vault-sdk | 85 | 6 | v0.3.3 (Aug 05, 2025) | Wallets & Mobile |
| Bonkfun-Bundler-Bonk.fun-Bundler | bonkfun bundler / bonk.fun bundler Letsbonk / Letsbonkfun bundler / Pump.fun bundler / pumpfun bundler / pumpdotfun bundler / bagsfm bundler/ bags.fm bundler trading bot. Multi-wallet bundler for Solana token launches. Uses Jito and Raydium SDK v2 for atomic one-block execution. | https://github.com/Tru3Bliss/Bonkfun-Bundler-Bonk.fun-Bundler | 205 | 1 | Last commit (Aug 26, 2025) | Wallets & Mobile |
| espresso-cash-public | Dart and Flutter apps and libraries maintained by Espresso Cash team for Solana. | https://github.com/espresso-cash/espresso-cash-public | 295 | 24 | Last commit (Aug 03, 2025) | Wallets & Mobile |
| reactor-wallet | 💳 Non-custodial cross-platform wallet for Solana | https://github.com/marc2332/reactor-wallet | 80 | 2 | Last commit (Dec 17, 2022) | Wallets & Mobile |
| crypto-trading-bot-mobile |  A cross-platform mobile crypto trading bot for Solana, built with Expo + React Native. Connect your Phantom Wallet, monitor coins, and automate trades in real time | https://github.com/0xTan1319/crypto-trading-bot-mobile | 10 | 1 | Last commit (Aug 07, 2025) | Wallets & Mobile |
| solacademy-wallet | Boilerplate to build Cross-Platform Apps with Expo, React Native & Solana Web3 | https://github.com/moviendome/solacademy-wallet | 13 | 1 | Last commit (Aug 10, 2022) | Wallets & Mobile |
| mobile-wallet-adapter-react-native | Solana Mobile Wallet Adapter for React Native & Expo | https://github.com/coral-xyz/mobile-wallet-adapter-react-native | 9 | 1 | Last commit (Feb 17, 2023) | Wallets & Mobile |
| expo-react-native-mwa-proof-of-concept | This repository demonstrates how to make a custom development build of Expo that includes the mobile wallet adapter, so that you can develop React Native Solana applications with Expo. | https://github.com/solana-mobile/expo-react-native-mwa-proof-of-concept | 9 | 1 | Last commit (Dec 21, 2022) | Wallets & Mobile |
| Kitepay-mobile | Kitepay🪁 : Solana Mobile Wallet | https://github.com/kytpay/Kitepay-mobile | 6 | 1 | Last commit (Jul 07, 2024) | Wallets & Mobile |
| Solana Program Library (legacy) | Historic collection of core on-chain programs; archived and migrated to new org | https://github.com/solana-labs/solana-program-library | 4.1k | 232 | Archived; stake-pool-v2.0.1 (Nov 20, 2024) | Programs (SPL) |
| SPL Libraries (new org) | Helper libraries/building blocks for on-chain programs | https://github.com/solana-program/libraries | 8 | 21 | type-length-value@v0.9.0 (Aug 11, 2025) | Programs (SPL) |
| Metaplex Token Metadata | Core NFT/fungible token metadata program & SDKs | https://github.com/metaplex-foundation/mpl-token-metadata | 210 | 32 | js@v3.4.0 (Feb 02, 2025) | NFTs & Programs |
| js | A JavaScript SDK for interacting with Metaplex's programs | https://github.com/metaplex-foundation/js | 374 | 39 | Archived; @metaplex-foundation/js-plugin-nft-storage@0.20.0 (Nov 09, 2023) | NFTs & Programs |
| gill | Solana JavaScript/TypeScript SDK - client library for interacting with the Solana blockchain | https://github.com/DecalLabs/gill | 315 | 17 | Last commit (Aug 12, 2025) | NFTs & Programs |
| solita | Genrates an SDK API from solana contract IDL. | https://github.com/metaplex-foundation/solita | 169 | 5 | Last commit (Nov 22, 2023) | NFTs & Programs |
| solana-candy-factory | Solana blockchain candy machine app boilerplate on top of Metaplex Candy Machine. NextJS, Tailwind, Anchor, SolanaLabs.React, dev/mainnet automation scripts. | https://github.com/kevinfaveri/solana-candy-factory | 296 | 4 | Last commit (May 17, 2023) | NFTs & Programs |
| anchorpy | The Python Anchor client. | https://github.com/kevinheavey/anchorpy | 272 | 11 | 0.21.0 (Mar 26, 2025) | NFTs & Programs |
| metaplex | A directory of what the Metaplex Foundation works on! | https://github.com/metaplex-foundation/metaplex | 3.3k | 155 | v1.2.0 (Mar 16, 2022) | NFTs & Programs |
| metaboss | The Metaplex NFT-standard Swiss Army Knife tool. | https://github.com/samuelvanderwaal/metaboss | 715 | 25 | v0.44.1 (Aug 25, 2025) | NFTs & Programs |
| metaplex-program-library | Smart contracts maintained by the Metaplex team | https://github.com/metaplex-foundation/metaplex-program-library | 635 | 63 | Last commit (Nov 01, 2024) | NFTs & Programs |
| treat-toolbox | Treat Toolbox: Generative NFT Utility for Candy Machine / Solana | https://github.com/theskeletoncrew/treat-toolbox | 270 | 11 | Last commit (Apr 25, 2022) | NFTs & Programs |
| shank | Extracts IDL from Solana Rust contracts | https://github.com/metaplex-foundation/shank | 187 | 7 | Last commit (Aug 21, 2025) | NFTs & Programs |
| compressed-nfts | Example code to use compressed NFTs (using state compression) on Solana | https://github.com/solana-developers/compressed-nfts | 125 | 2 | Last commit (Jan 18, 2024) | NFTs & Programs |
| fetch-nft | 🖼🎑🌠 A utility to fetch and easily display Ethereum & Solana NFTs in a common format given any wallet | https://github.com/AudiusProject/fetch-nft | 120 | 7 | Last commit (Jan 13, 2025) | NFTs & Programs |
| digital-asset-rpc-infrastructure | Reference implementation for Metaplex Digital Asset Standard API | https://github.com/metaplex-foundation/digital-asset-rpc-infrastructure | 109 | 18 | v0.6.8 (Feb 22, 2023) | NFTs & Programs |
| solana-anchor-react-minimal-example | Solana, Anchor, Metaplex, React Minimal Example. Out of the Box, easy to start! | https://github.com/256hax/solana-anchor-react-minimal-example | 96 | 3 | v1.1.0 (Nov 23, 2023) | NFTs & Programs |
| create-solana-dapp | The fastest way to create Solana apps 🚀 Templates 👉 https://github.com/solana-foundation/templates | https://github.com/solana-foundation/create-solana-dapp | 521 | 13 | Last commit (Aug 06, 2025) | NFTs & Programs |
| solana-tools | A bunch of tools to help people in the Solana ecosystem. This website includes an UI to burn Solana NFTs and an UI to create SPL-Tokens. More tools are scheduled... | https://github.com/cryptoloutre/solana-tools | 207 | 4 | Last commit (Dec 03, 2024) | NFTs & Programs |
| Candy Machine (Core) | Metaplex Core Candy Machine (Core assets) | https://github.com/metaplex-foundation/mpl-core-candy-machine | 28 | 5 | js@v0.3.0 (Jan 27, 2025) | NFTs & Minting |
| solana-payments-app | Solana Pay for Commerce Platforms | https://github.com/solana-labs/solana-payments-app | 97 | 5 | Archived; v2.0.0 (Aug 18, 2023) | Payments |
| solana-payment-processor | Solana payment processor for e-commerce applications | https://github.com/solpayments/solana-payment-processor | 20 | 2 | Last commit (Jul 13, 2021) | Payments |
| solana-payment-processor | About Solana payment processor for e-commerce applications | https://github.com/hylcore-V/solana-payment-processor | 17 | 1 | Last commit (Nov 24, 2024) | Payments |
| solpress-pay | Woocommerce Payment Gateway Plugin Using Solana Pay | https://github.com/solpressplugins/solpress-pay | 11 | 1 | Last commit (Aug 07, 2024) | Payments |
| wc-solana-pay | Solana Pay powered payment gateway for WordPress and WooCommerce | https://github.com/aztemi/wc-solana-pay | 9 | 1 | Last commit (Jul 12, 2025) | Payments |
| solana-pay-checkout | A point-of-sale web app that allows us to take payments from customers through QR Code in person using Solana Pay. | https://github.com/ronylucca/solana-pay-checkout | 8 | 1 | Last commit (Apr 10, 2022) | Payments |
| solana-pay-qrcode-generator | A simple way to generate QR Codes and easily accept payments in Solana, USCD or any other SPL-Token on the Solana Blockchain. | https://github.com/valentinmadrid/solana-pay-qrcode-generator | 6 | 1 | Last commit (Oct 25, 2022) | Payments |
| Jupiter Swap API | Jupiter V6 Swap API binaries and releases | https://github.com/jup-ag/jupiter-swap-api | 208 | 2 | v6.0.62 (Aug 18, 2025) | DeFi |
| carbon | Carbon is an indexing framework on Solana. | https://github.com/sevenlabs-hq/carbon | 434 | 27 | v0.9.1 (Jul 18, 2025) | DeFi |
| raydium-sdk-swap-example-typescript | An example to swap tokens on Solana using the Raydium SDK, TypeScript, and Chainstack | https://github.com/chainstacklabs/raydium-sdk-swap-example-typescript | 182 | 4 | Last commit (Aug 21, 2025) | DeFi |
| Solana-Arbitrage-Bot-Flash-Loan | Solana Arbitrage Bot cross dex like Raydium, Orca, Meteora swap program with rust language architecture using anchor frame work | https://github.com/deniyuda348/Solana-Arbitrage-Bot-Flash-Loan | 330 | 3 | Solana-Arbitrage-Bot (May 20, 2025) | DeFi |
| solana-txn-parser | An open-source transaction parser for popular DeFi applications on the Solana blockchain 🚀🤖.. | https://github.com/Tee-py/solana-txn-parser | 189 | 2 | v0.1.6 (Jul 18, 2025) | DeFi |
| Solana-Trading-Bot | Buy and Sell SPL tokens on the Raydium DEX and  Pump.fun using the Solana-Py SDK and Jito SDK | https://github.com/henrytirla/Solana-Trading-Bot | 290 | 1 | Last commit (Feb 15, 2025) | DeFi |
| pumpfun-raydium-cli-tools | solana pumpfun bundler, raydium bundler, pumpfun sniping bot, raydium sniping bot, pumpfun volume bot, raydium volume bot, pumpfun bundler, raydium bundler, jito bundler | https://github.com/hexnome/pumpfun-raydium-cli-tools | 160 | 1 | Last commit (Mar 25, 2025) | DeFi |
| solana-auto-sell-bot | This script continuously scans a Solana wallet for SPL tokens and tracks their age (time held) in seconds. Once a certain time has elapsed it will sell the token on raydium or pumpfun. | https://github.com/lorenzourera/solana-auto-sell-bot | 118 | 1 | Last commit (Jan 13, 2025) | DeFi |
| dex-v4 | Orderbook-based on-chain SPL token swap market | https://github.com/Bonfida/dex-v4 | 103 | 7 | Last commit (Feb 22, 2023) | DeFi |
| pirate-bootcamp | A pirate-theme bootcamp for getting up to speed on Solana programming! | https://github.com/solana-developers/pirate-bootcamp | 316 | 4 | Last commit (Sep 05, 2023) | DeFi |
| solana-escrow | Reference Implementation for the guide https://paulx.dev/blog/2021/01/14/programming-on-solana-an-introduction/ | https://github.com/paul-schaaf/solana-escrow | 312 | 3 | Archived; Last commit (Jan 23, 2022) | DeFi |
| Solana-Arbitrage-Bot | Solana Arbitrage Bot cross dex like Raydium, Orca, Meteora swap program with rust language architecture using anchor frame work | https://github.com/ChangeYourself0613/Solana-Arbitrage-Bot | 243 | 1 | solana-arbitrage-bot2 (May 26, 2025) | DeFi |
| sol-trade-sdk | A comprehensive Rust SDK for seamless interaction with Solana DEX trading programs. This SDK provides a robust set of tools and interfaces to integrate PumpFun, PumpSwap, Bonk, and Raydium CPMM functionality into your applications. | https://github.com/0xfnzero/sol-trade-sdk | 138 | 6 | Last commit (Aug 27, 2025) | DeFi |
| Payment-gateway | Payment gateway for solana with advanced Private key management and address sweeping via indexer | https://github.com/alxn787/Payment-gateway | 9 | 1 | Last commit (Jul 12, 2025) | DeFi |
| Solana-Arbitrage-Bot | Solana Arbitrage Bot cross dex like Raydium, Orca, Meteora swap program with rust language architecture using anchor frame work | https://github.com/deniyuda348/Solana-Arbitrage-Bot | 330 | 3 | Solana-Arbitrage-Bot (May 20, 2025) | DeFi |

- Stars/Contributors: Snapshot values; “—” indicates to-be-filled or varies (especially for org-level entries or during repo migrations).
- Last Activity: Typically last release or last commit; “Docs current” for documentation sources.

## How will i keep README “Live”

Option A — Manual refresh
- Periodically check each repo and update stars, contributors, and last activity.

Option B — Automated updates( implemented ) 
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

