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

Last updated: 2026-02-14

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
| Solana (archived; moved to Agave) | Web-scale blockchain reference implementation; now archived with development transitioned to Agave | https://github.com/solana-labs/solana | 14.8k | 353 | Archived; v1.18.26 (Oct 12, 2024) | Infrastructure |
| Agave (validator) | Current Solana validator implementation maintained by Anza | https://github.com/anza-xyz/agave | 1.7k | 360 | v3.1.8 (Jan 26, 2026) | Infrastructure |
| Solana SDK (Rust) | Rust SDK used by on-chain program developers and the Agave validator | https://github.com/anza-xyz/solana-sdk | 207 | 167 | nonce-account@v4.0.0 (Feb 14, 2026) | SDKs & Tooling |
| Anchor | Framework for building Solana programs (Rust eDSL, IDL, TS client, CLI) | https://github.com/coral-xyz/anchor | 4.9k | 315 | v0.32.1 (Oct 10, 2025) | SDKs & Tooling |
| Solana Web3.js (v1.x) | Official JavaScript SDK (maintenance branch; successor work referenced as @solana/kit) | https://github.com/solana-foundation/solana-web3.js | 2.7k | 127 | v1.98.4 (Jul 31, 2025) | SDKs & Tooling |
| Solders (Python) | High-performance Python toolkit for Solana (Rust-backed) | https://github.com/kevinheavey/solders | 433 | 12 | v0.27.1 (Nov 15, 2025) | SDKs & Tooling |
| anchor | ⚓ Solana Sealevel Framework | https://github.com/solana-foundation/anchor | 4.9k | 315 | v0.32.1 (Oct 10, 2025) | SDKs & Tooling |
| trident | Rust-based framework to Fuzz Solana programs, designed to help you ship secure code. | https://github.com/Ackee-Blockchain/trident | 368 | 20 | 0.12.0 (Nov 27, 2025) | SDKs & Tooling |
| solana-poc-framework | A framework for creating PoC's for Solana Smart Contracts in a painless and intuitive way | https://github.com/neodyme-labs/solana-poc-framework | 244 | 13 | Last commit (Oct 07, 2025) | SDKs & Tooling |
| steel | Solana smart contract framework. | https://github.com/regolith-labs/steel | 254 | 7 | 2.1.0 (Oct 23, 2024) | SDKs & Tooling |
| nautilus | SQL-native Solana program framework | https://github.com/nautilus-project/nautilus | 96 | 6 | Last commit (Nov 08, 2024) | SDKs & Tooling |
| znap | Performance-first Rust Framework to build APIs compatible with the Solana Actions Spec. | https://github.com/heavy-duty/znap | 70 | 4 | 0.1.36 (Aug 29, 2024) | SDKs & Tooling |
| sol-ctf-framework | Framework for Solana CTF challenges | https://github.com/otter-sec/sol-ctf-framework | 74 | 7 | Last commit (Dec 10, 2025) | SDKs & Tooling |
| ethereum-boilerplate | The ultimate NextJS Ethereum Dapp Boilerplate which gives you maximum flexibility and speed. Feel free to fork and contribute. Although this repo is called "Ethereum Boilerplate" it works with any EVM system and since it uses Moralis SDK You can even use it on Solana!  Happy BUIDL!👷‍♂️ | https://github.com/ethereum-boilerplate/ethereum-boilerplate | 4.2k | 12 | Last commit (Apr 26, 2023) | SDKs & Tooling |
| kit | Solana JavaScript SDK | https://github.com/anza-xyz/kit | 654 | 158 | v6.0.1 (Feb 05, 2026) | SDKs & Tooling |
| js-wallet-sdk | Multi-chain typescript signature sdk, supports bitcoin, ethereum, solana, cosmos, etc. | https://github.com/okx/js-wallet-sdk | 375 | 13 | Last commit (Jan 23, 2026) | SDKs & Tooling |
| program-examples | A repository of Solana program examples | https://github.com/solana-developers/program-examples | 1.4k | 50 | Last commit (Feb 09, 2026) | SDKs & Tooling |
| Solana_Dice_SmartContract | This project is a simple on-chain Dice Game smart contract built for the Solana blockchain using Rust and the Anchor framework. It demonstrates the fundamentals of Solana program development, including instruction handling, randomness simulation, state management, and token transfers. | https://github.com/kinexbt/Solana_Dice_SmartContract | 41 | 1 | Last commit (Dec 10, 2025) | SDKs & Tooling |
| Solana_Bita_Coinflip_SmartContract | A lightweight on-chain Coin Flip betting game built on the Solana blockchain using Rust and the Anchor framework. This contract allows users to wager SOL (or tokens) on a 50/50 coin flip outcome — win or lose instantly, with no intermediaries. | https://github.com/kinexbt/Solana_Bita_Coinflip_SmartContract | 26 | 2 | Last commit (Dec 16, 2025) | SDKs & Tooling |
| complete-guide-to-full-stack-solana-development | Code examples for the blog post titled The Complete Guide to Full Stack Solana Development with React, Anchor, Rust, and Phantom | https://github.com/dabit3/complete-guide-to-full-stack-solana-development | 489 | 2 | Last commit (Sep 18, 2021) | SDKs & Tooling |
| seahorse-lang | Write Anchor-compatible Solana programs in Python | https://github.com/ameliatastic/seahorse-lang | 345 | 4 | Last commit (Feb 24, 2023) | SDKs & Tooling |
| Solana-Prediction-Market | Solana Prediction Market where users can create market, add liquidity, and bet | https://github.com/HyperBuildX/Solana-Prediction-Market | 289 | — | Last commit (Feb 05, 2026) | SDKs & Tooling |
| awesome-solana-security | A collection of resources to help you build better and more secure Solana programs. Kept up to date. | https://github.com/0xMacro/awesome-solana-security | 554 | 2 | Last commit (Dec 06, 2025) | SDKs & Tooling |
| Pumpfun-solana-smart-contract | pump.fun clone: pumpfun smart contract fork (pump.fun fork), solana pump fun smart contract source code | https://github.com/cutupdev/Pumpfun-solana-smart-contract | 381 | 1 | Last commit (Dec 21, 2025) | SDKs & Tooling |
| anchor-go | Generate Go clients from anchor IDLs for Solana blockchain programs | https://github.com/gagliardetto/anchor-go | 296 | 4 | v1.0.0 (Jul 02, 2025) | SDKs & Tooling |
| solana-copy-bot | Copy any transaction at any address in Solana | https://github.com/Abraham-007/solana-copy-bot | — | — | Active | SDKs & Tooling |
| solana-trading-bot | Solana Trading Bot - RC: For Solana token sniping and trading, the latest version has completed all optimizations | https://github.com/warp-abbott/solana-trading-bot | — | — | Active | SDKs & Tooling |
| spl-token-ui | Interface for creating and managing SPL Tokens | https://github.com/paul-schaaf/spl-token-ui | 204 | 1 | Archived; Last commit (Jul 08, 2021) | SDKs & Tooling |
| solana-spl-token-sniper | Solana SPL-Token sniper for new Raydium liquidity pools | https://github.com/danbayk/solana-spl-token-sniper | 197 | 1 | Last commit (Mar 19, 2024) | SDKs & Tooling |
| solana-sniper-bot | AxisBot - Solana Sniper Bot. Snipe and sell SPL tokens at lightning speed.  Our sniping bot helps you maintain a higher level of security while also giving you the fastest sniping speed possible. Built by Traders for Traders. | https://github.com/AxisBotV2/solana-sniper-bot | 95 | 1 | Last commit (Jul 07, 2024) | SDKs & Tooling |
| solana-spl-tutorial | This repository contains full tutorial on Solana SPL token | https://github.com/YosephKS/solana-spl-tutorial | 76 | 1 | Last commit (Feb 12, 2022) | SDKs & Tooling |
| solana-playground | Quickly develop, deploy and test Solana programs from browsers | https://github.com/solana-playground/solana-playground | 916 | 30 | Last commit (Feb 13, 2026) | SDKs & Tooling |
| anchor-escrow | Escrow program implemented in Anchor | https://github.com/ironaddicteddog/anchor-escrow | 197 | 3 | Last commit (Aug 29, 2024) | SDKs & Tooling |
| pumpfun-rs | A comprehensive Rust SDK for seamless interaction with the PumpFun Solana program. | https://github.com/nhuxhr/pumpfun-rs | 161 | 5 | Last commit (Oct 01, 2025) | SDKs & Tooling |
| Solana-Auditors-Bootcamp | Learn to audit Solana programs and help secure the ecosystem. Take your security practices to the next level and get certified by Ackee Blockchain Security. It's free, too. | https://github.com/Ackee-Blockchain/Solana-Auditors-Bootcamp | 158 | 3 | Last commit (Nov 25, 2025) | SDKs & Tooling |
| radar | A static analysis tool for anchor rust programs. | https://github.com/Auditware/radar | 121 | 4 | Last commit (Feb 08, 2026) | SDKs & Tooling |
| odoo-solana-payments | Allows you to accept a variety of currencies (USDT, USDC, BTC, SOL) via the solana blockchain | https://github.com/t-900-a/odoo-solana-payments | 10 | 1 | Archived; Last commit (Nov 18, 2020) | SDKs & Tooling |
| solana-sign-with-payment | Prove ownership of a Solana address by asking the user to send a small amount | https://github.com/kizzx2/solana-sign-with-payment | 8 | 1 | Last commit (May 19, 2022) | SDKs & Tooling |
| pumpfun-smartcontract-solana | Pumpfun smart contract (Solana Pumpfun Smart Contract fork, Pumpfun smart contract development Tool, Pumpfun smart contract SDK) | https://github.com/printz-labs/pumpfun-smartcontract-solana | — | — | Active | SDKs & Tooling |
| star_frame | High performance, modular solana program framework | https://github.com/staratlasmeta/star_frame | 80 | 12 | v0.29.0 (Feb 11, 2026) | SDKs & Tooling |
| pumpfun-smart-contract-frontend-backend | Solana Pumpfun smart contract & Frontend & Backend | https://github.com/0xalberto/pumpfun-smart-contract-frontend-backend | 144 | 1 | Last commit (Sep 01, 2025) | SDKs & Tooling |
| Solana-Pumpfun-Smart-Contract-Token-2022 | pumpfun clone: tax token pump.fun smart contract (pumpfun fork), solana pump fun smart contract (token2022, raydium cpmm) | https://github.com/cutupdev/Solana-Pumpfun-Smart-Contract-Token-2022 | 194 | 1 | Last commit (Jun 30, 2025) | SDKs & Tooling |
| solana-pumpfun-trader | buy/sell functions for Solana SPL tokens created on pump.fun. | https://github.com/degenfrends/solana-pumpfun-trader | 74 | 2 | v0.0.16 (Jun 22, 2024) | SDKs & Tooling |
| typhoon | 🌪️ Solana Sealevel Framework | https://github.com/exotic-markets-labs/typhoon | 67 | 8 | Last commit (Feb 13, 2026) | SDKs & Tooling |
| Solana-Sniper-Memecoin-Bot | The combination project of sniper and shitcoin bot connecting with Raydium SDK on Solana. This bot includes numerous functions like Jito Service, Unwrapping Sol, Token creation, Auto Airdrop, Market creation, Token Acount Freeze, LP Token Burn, Pool creation, Buy/Sell Tokens, Add/Remove Liquidity. | https://github.com/justshiftjk/Solana-Sniper-Memecoin-Bot | — | — | Active | SDKs & Tooling |
| gamba | SDK for building web3 betting games on Solana | https://github.com/gamba-labs/gamba | 76 | 12 | Last commit (Dec 02, 2025) | SDKs & Tooling |
| sns-sdk | Solana Name Service SDKs monorepo | https://github.com/SolanaNameService/sns-sdk | 67 | 10 | @bonfida/spl-name-service@3.0.1 (Aug 07, 2024) | SDKs & Tooling |
| Solana-Token-Staking-Smart-Contract | Solana token staking smart contract  | https://github.com/cutupdev/Solana-Token-Staking-Smart-Contract | 142 | 1 | Last commit (Dec 21, 2025) | SDKs & Tooling |
| Solana-Token-Presale-Smart-Contract | Solana presale smart contract | https://github.com/cutupdev/Solana-Token-Presale-Smart-Contract | 142 | 1 | Last commit (Jun 27, 2025) | SDKs & Tooling |
| poseidon | A Transpiler to convert your Solana programs from Typescript to Anchor | https://github.com/Turbin3/poseidon | 151 | 12 | Last commit (May 20, 2025) | SDKs & Tooling |
| native-to-anchor | Generate Anchor IDL for Native Solana Programs. | https://github.com/acheroncrypto/native-to-anchor | 144 | 1 | Last commit (Aug 21, 2022) | SDKs & Tooling |
| solana-token-kit | Solana Token Kit for creating, launching and managing Solana SPL Tokens | https://github.com/wurambo/solana-token-kit | 47 | 1 | Last commit (May 10, 2024) | SDKs & Tooling |
| spl-token-faucet | Solana program that makes Token Faucets possible | https://github.com/paul-schaaf/spl-token-faucet | 41 | 1 | Last commit (Dec 15, 2020) | SDKs & Tooling |
| pumpfun-sdk | A comprehensive Rust SDK for seamless interaction with the PumpFun Solana program. This SDK provides a robust set of tools and interfaces to integrate PumpFun functionality into your applications.  Resources | https://github.com/0xfnzero/pumpfun-sdk | 76 | 2 | Last commit (Oct 08, 2025) | SDKs & Tooling |
| IDLGuesser | IDL Guesser is an open-source tool that automatically recovers the IDL information from closed-source Anchor-based Solana programs. | https://github.com/sec3-service/IDLGuesser | 162 | 3 | Last commit (Nov 30, 2025) | SDKs & Tooling |
| Pump.fun-Smart-Contract | This is a forked version of Pump.fun smart contract (Solana Pumpfun Smart Contract fork, Pumpfun smart contract development Tool, Pumpfun smart contract SDK) | https://github.com/justshiftjk/Pump.fun-Smart-Contract | — | — | Active | SDKs & Tooling |
| solana-cli-program-template | A template with cookie cutter CLI, Program and Integration tests for Solana blockchain | https://github.com/hashblock/solana-cli-program-template | 51 | 1 | Last commit (Dec 31, 2022) | SDKs & Tooling |
| pumpfun-laserstream-sniper-rust | Ultra Fast Rust PumpFun Sniper Bot is a high-performance, low-latency sniper bot built in Rust designed for the Solana blockchain pumpfun-sniper-bot pumpfun-sniper-bot pumpfun-sniper-bot pumpfun-sniper-bot pumpfun-sniper-bot pumpfun-sniper-bot pumpfun-sniper-bot | https://github.com/0xalberto/pumpfun-laserstream-sniper-rust | 127 | 1 | Last commit (Aug 29, 2025) | SDKs & Tooling |
| launch-solana-token | an all-in-one toolkit for experimenting with custom assets and configurations on the **Solana blockchain**. It includes logic for configuring token parameters, simulating liquidity setups (e.g., with **Raydium**) and minimal overhead. Built in **Rust**, provided as a single native application for testing and educational use. | https://github.com/lacydebuger/launch-solana-token | 2 | 1 | sol (Jul 11, 2025) | SDKs & Tooling |
| Bita_Contract | A lightweight on-chain Coin Flip betting game built on the Solana blockchain using Rust and the Anchor framework. This contract allows users to wager SOL (or tokens) on a 50/50 coin flip outcome — win or lose instantly, with no intermediaries. | https://github.com/kinexbt/Bita_Contract | 26 | 2 | Last commit (Dec 16, 2025) | SDKs & Tooling |
| solana-trading-bot | Solana Trading Bot is an algorithmic trading bot designed to automate the trading process of Solana specific ecosystem tokens. | https://github.com/bytemagi/solana-trading-bot | — | — | Active | SDKs & Tooling |
| solana-starter-kit | Open-source Solana dApp template with Anchor program, TypeScript client, and Next.js UI. | https://github.com/SolanaUpdateTools/solana-starter-kit | 346 | 1 | Last commit (Nov 06, 2025) | SDKs & Tooling |
| solana-pumpfun-smart-contract-token2022 | 💊Solana Pumpfun Smart Contract🟣: This Solana Pumpfun Smart Contract utilizes the new SPL token standard, TOKEN2022. Forked and Customized pumpfun smart contract. Pumpfun smart contract development Tool, Pumpfun smart contract SDK | https://github.com/soulcrancerdev/solana-pumpfun-smart-contract-token2022 | — | — | Active | SDKs & Tooling |
| solana-trading-bot | Solana Trading Bot is an algorithmic trading bot designed to automate the trading process of Solana specific ecosystem tokens. | https://github.com/ivorn42/solana-trading-bot | — | — | Active | SDKs & Tooling |
| solana-casino-game-contract | On-chain casino smart contract built on Solana, enabling provably fair games with transparent randomness and instant settlement. Supports multiple game types (e.g., dice, coinflip, roulette) with fully decentralized logic and SPL token integration. | https://github.com/ivorn42/solana-casino-game-contract | — | — | Active | SDKs & Tooling |
| token-presale-smart-contract | On-chain token presale smart contract built on Solana, enabling secure, transparent, and automated fundraising for new SPL tokens. Designed for teams launching tokens with trustless contribution tracking, tiered sale rounds, and instant token distribution. | https://github.com/ivorn42/token-presale-smart-contract | — | — | Active | SDKs & Tooling |
| solana-fun-token-launch-pad | A comprehensive Next.js-based token launchpad platform for creating and managing SPL tokens on the Solana blockchain. This application provides an intuitive interface for token creation, liquidity management, market creation, and token authority management | https://github.com/BlackSky-Jose/solana-fun-token-launch-pad | — | — | Active | SDKs & Tooling |
| bypass-bubblemap | This project is solana program to bypass bubblemap. | https://github.com/FroganBee/bypass-bubblemap | — | — | Active | SDKs & Tooling |
| bypass-bubblemap | This project is solana program to bypass bubblemap. | https://github.com/Solzen33/bypass-bubblemap | — | — | Active | SDKs & Tooling |
| solana-fun-token-launch-pad | A comprehensive Next.js-based token launchpad platform for creating and managing SPL tokens on the Solana blockchain. This application provides an intuitive interface for token creation, liquidity management, market creation, and token authority management | https://github.com/Mist-kail/solana-fun-token-launch-pad | — | — | Active | SDKs & Tooling |
| Prediction-Market-Smart-Contract-Solana | A decentralized prediction market platform built on Solana, inspired by Polymarket. This project lets users create prediction markets, trade in prediction markets, and settle outcomes based on real events in a growing prediction market ecosystem. Built for Solana, EVM, Monad, Sui, Abstraqt, Ronin. | https://github.com/Tru3Bliss/Prediction-Market-Smart-Contract-Solana | 222 | 1 | Last commit (Mar 21, 2025) | SDKs & Tooling |
| EVM-Solana-Casino-Games | Blockchain Web3 Solana Casino Game | 🌐Multi-Chain Casino Platform | EVM + Sui |  10 Provably Fair Games | ORAO + Chainlink VRF |  Crash, Plinko, Dice, Blackjack, Roulette, Poker, Hi-Lo, Limbo, Coinflip. Contact for solana casino game building and solana casino game customization evm solana evm solana evm solana evm solana evm solana evm solana | https://github.com/LaChance-Lab/EVM-Solana-Casino-Games | 302 | 1 | Last commit (Feb 03, 2026) | SDKs & Tooling |
| solana-poker-casino-game | A Solana Poker Casino Game is an online casino-style poker game built on the Solana blockchain, where players use crypto (like SOL or SPL tokens) instead of fiat money. | https://github.com/0xRustPro/solana-poker-casino-game | — | — | Active | SDKs & Tooling |
| solana-pumpfun-sniper-bot | solana bot || solana pumpfun bot || solana pumpfun sniper bot || solana pumpfun trading bot | https://github.com/ahmedrabby13/solana-pumpfun-sniper-bot | — | — | Active | SDKs & Tooling |
| Web3-EVM-Solana-Casino-Games | Blockchain Web3 Solana Casino Game | 🌐Multi-Chain Casino Platform | EVM + Sui |  10 Provably Fair Games | ORAO + Chainlink VRF |  Crash, Plinko, Dice, Blackjack, Roulette, Poker, Hi-Lo, Limbo, Coinflip. Contact for solana casino game building and solana casino game customization evm solana evm solana evm solana evm solana evm solana evm solana | https://github.com/LaChance-Lab/Web3-EVM-Solana-Casino-Games | 302 | 1 | Last commit (Feb 03, 2026) | SDKs & Tooling |
| Wallet Adapter | Modular TypeScript wallet adapters and UI components | https://github.com/anza-xyz/wallet-adapter | 2.0k | 113 | @solana/wallet-adapter-xdefi@0.1.11 (Jun 10, 2025) | Wallets & Mobile |
| Solana Mobile Stack SDK | Android SDKs: Mobile Wallet Adapter, Seed Vault | https://github.com/solana-mobile/solana-mobile-stack-sdk | 760 | 2 | Last commit (Jun 23, 2022) | Wallets & Mobile |
| Mobile Wallet Adapter | Protocol for connecting apps to mobile wallets | https://github.com/solana-mobile/mobile-wallet-adapter | 316 | 19 | v2.1.0 (Aug 18, 2025) | Wallets & Mobile |
| Seed Vault SDK | Secure key custody API/service for Android | https://github.com/solana-mobile/seed-vault-sdk | 91 | 8 | v0.4.0 (Oct 06, 2025) | Wallets & Mobile |
| Bonkfun-Bundler-Bonk.fun-Bundler | bonkfun bundler / bonk.fun bundler Letsbonk / Letsbonkfun bundler / Pump.fun bundler / pumpfun bundler / pumpdotfun bundler / bagsfm bundler/ bags.fm bundler trading bot. Multi-wallet bundler for Solana token launches. Uses Jito and Raydium SDK v2 for atomic one-block execution. | https://github.com/Tru3Bliss/Bonkfun-Bundler-Bonk.fun-Bundler | 173 | 1 | Last commit (Oct 15, 2025) | Wallets & Mobile |
| espresso-cash-public | Dart and Flutter apps and libraries maintained by Espresso Cash team for Solana. | https://github.com/espresso-cash/espresso-cash-public | 301 | 24 | Last commit (Jan 02, 2026) | Wallets & Mobile |
| reactor-wallet | 💳 Non-custodial cross-platform wallet for Solana | https://github.com/marc2332/reactor-wallet | 79 | 2 | Last commit (Dec 17, 2022) | Wallets & Mobile |
| crypto-trading-bot-mobile |  A cross-platform mobile crypto trading bot for Solana, built with Expo + React Native. Connect your Phantom Wallet, monitor coins, and automate trades in real time | https://github.com/0xTan1319/crypto-trading-bot-mobile | 9 | 1 | Last commit (Aug 07, 2025) | Wallets & Mobile |
| solacademy-wallet | Boilerplate to build Cross-Platform Apps with Expo, React Native & Solana Web3 | https://github.com/moviendome/solacademy-wallet | 12 | 1 | Last commit (Aug 10, 2022) | Wallets & Mobile |
| mobile-wallet-adapter-react-native | Solana Mobile Wallet Adapter for React Native & Expo | https://github.com/coral-xyz/mobile-wallet-adapter-react-native | 10 | 1 | Last commit (Feb 17, 2023) | Wallets & Mobile |
| expo-react-native-mwa-proof-of-concept | This repository demonstrates how to make a custom development build of Expo that includes the mobile wallet adapter, so that you can develop React Native Solana applications with Expo. | https://github.com/solana-mobile/expo-react-native-mwa-proof-of-concept | 9 | 1 | Last commit (Dec 21, 2022) | Wallets & Mobile |
| Kitepay-mobile | Kitepay🪁 : Solana Mobile Wallet | https://github.com/kytpay/Kitepay-mobile | 6 | 1 | Last commit (Jul 07, 2024) | Wallets & Mobile |
| solana-app-wallet | Solana APP is another version of sollet wallet for mobile  Solana Pay is the entry point into the system. It lives directly between web2 & web3, receiving web2 payloads & converting them into web3 transactions. The power of this really can’t be overstated. The contours of this design space are unexplored and sure to hold amazing things. | https://github.com/0xPleiades/solana-app-wallet | 17 | 1 | Last commit (Aug 05, 2025) | Wallets & Mobile |
| On_chain | Streamline Ethereum, Solana, Cardano, Aptos, Sui and Tron operations. Effortlessly create transactions, interact with smart contracts, sign, and send transactions for a seamless blockchain experience. | https://github.com/mrtnetwork/On_chain | 49 | 2 | v3.2.0 (Apr 30, 2024) | Wallets & Mobile |
| solana-token-bundler-pumpfun-pump.fun-bonkfun-bonk.fun | Multi-wallet bundler for Solana token launches on pump.fun/pumpfun, bonk.fun/bonkfun, letsbonk, and bags.fm. Atomic execution with Jito bundles and Raydium SDK v2. MEV-protected trading bot with dual Jito/Lil Jito support. | https://github.com/Tru3Bliss/solana-token-bundler-pumpfun-pump.fun-bonkfun-bonk.fun | 173 | 1 | Last commit (Oct 15, 2025) | Wallets & Mobile |
| crypto-trading-bot-mobile |  A cross-platform mobile crypto trading bot for Solana, built with Expo + React Native. Connect your Phantom Wallet, monitor coins, and automate trades in real time | https://github.com/0xMurk/crypto-trading-bot-mobile | 9 | 1 | Last commit (Aug 07, 2025) | Wallets & Mobile |
| espresso-cash-public | Dart and Flutter apps and libraries maintained by Espresso Cash team for Solana. | https://github.com/brij-digital/espresso-cash-public | 301 | 24 | Last commit (Jan 02, 2026) | Wallets & Mobile |
| Solana Program Library (legacy) | Historic collection of core on-chain programs; archived and migrated to new org | https://github.com/solana-labs/solana-program-library | 4.2k | 233 | Archived; stake-pool-v2.0.1 (Nov 20, 2024) | Programs (SPL) |
| SPL Libraries (new org) | Helper libraries/building blocks for on-chain programs | https://github.com/solana-program/libraries | 13 | 21 | tlv-account-resolution@v0.11.1 (Oct 08, 2025) | Programs (SPL) |
| Metaplex Token Metadata | Core NFT/fungible token metadata program & SDKs | https://github.com/metaplex-foundation/mpl-token-metadata | 243 | 33 | js@v3.4.0 (Feb 02, 2025) | NFTs & Programs |
| js | A JavaScript SDK for interacting with Metaplex's programs | https://github.com/metaplex-foundation/js | 388 | 39 | Archived; @metaplex-foundation/js-plugin-nft-storage@0.20.0 (Nov 09, 2023) | NFTs & Programs |
| gill | Solana JavaScript/TypeScript SDK - client library for interacting with the Solana blockchain | https://github.com/DecalLabs/gill | 409 | 26 | Last commit (Nov 16, 2025) | NFTs & Programs |
| solita | Genrates an SDK API from solana contract IDL. | https://github.com/metaplex-foundation/solita | 178 | 5 | Last commit (Nov 22, 2023) | NFTs & Programs |
| solana-candy-factory | Solana blockchain candy machine app boilerplate on top of Metaplex Candy Machine. NextJS, Tailwind, Anchor, SolanaLabs.React, dev/mainnet automation scripts. | https://github.com/kevinfaveri/solana-candy-factory | 298 | 4 | Last commit (May 17, 2023) | NFTs & Programs |
| anchorpy | The Python Anchor client. | https://github.com/kevinheavey/anchorpy | 276 | 10 | 0.21.0 (Mar 26, 2025) | NFTs & Programs |
| metaplex | A directory of what the Metaplex Foundation works on! | https://github.com/metaplex-foundation/metaplex | 3.4k | 155 | v1.2.0 (Mar 16, 2022) | NFTs & Programs |
| metaboss | The Metaplex NFT-standard Swiss Army Knife tool. | https://github.com/samuelvanderwaal/metaboss | 719 | 26 | v0.45.0 (Jan 06, 2026) | NFTs & Programs |
| metaplex-program-library | Smart contracts maintained by the Metaplex team | https://github.com/metaplex-foundation/metaplex-program-library | 645 | 64 | Last commit (Oct 02, 2025) | NFTs & Programs |
| treat-toolbox | Treat Toolbox: Generative NFT Utility for Candy Machine / Solana | https://github.com/theskeletoncrew/treat-toolbox | 269 | 11 | Last commit (Apr 25, 2022) | NFTs & Programs |
| shank | Extracts IDL from Solana Rust contracts | https://github.com/metaplex-foundation/shank | 222 | 10 | Last commit (Feb 12, 2026) | NFTs & Programs |
| compressed-nfts | Example code to use compressed NFTs (using state compression) on Solana | https://github.com/solana-developers/compressed-nfts | 125 | 2 | Last commit (Jan 18, 2024) | NFTs & Programs |
| fetch-nft | 🖼🎑🌠 A utility to fetch and easily display Ethereum & Solana NFTs in a common format given any wallet | https://github.com/AudiusProject/fetch-nft | 119 | 7 | Last commit (Jan 13, 2025) | NFTs & Programs |
| digital-asset-rpc-infrastructure | Reference implementation for Metaplex Digital Asset Standard API | https://github.com/metaplex-foundation/digital-asset-rpc-infrastructure | 117 | 18 | v0.6.8 (Feb 22, 2023) | NFTs & Programs |
| solana-anchor-react-minimal-example | Solana, Anchor, Metaplex, React Minimal Example. Out of the Box, easy to start! | https://github.com/256hax/solana-anchor-react-minimal-example | 96 | 3 | v1.1.0 (Nov 23, 2023) | NFTs & Programs |
| create-solana-dapp | The fastest way to create Solana apps 🚀 Templates 👉 https://github.com/solana-foundation/templates | https://github.com/solana-foundation/create-solana-dapp | 610 | 17 | Last commit (Jan 08, 2026) | NFTs & Programs |
| solana-tools | A bunch of tools to help people in the Solana ecosystem. This website includes an UI to burn Solana NFTs and an UI to create SPL-Tokens. More tools are scheduled... | https://github.com/cryptoloutre/solana-tools | 210 | 4 | Last commit (Dec 03, 2024) | NFTs & Programs |
| gill | Solana JavaScript/TypeScript SDK - client library for interacting with the Solana blockchain | https://github.com/gillsdk/gill | 409 | 26 | Last commit (Nov 16, 2025) | NFTs & Programs |
| Solana-Unreal-SDK | A complete Unreal plugin and toolkit for building blockchain games on Solana with Unreal Engine 5. | https://github.com/Bifrost-Technologies/Solana-Unreal-SDK | 81 | 1 | Last commit (Mar 30, 2024) | NFTs & Programs |
| solana-mint-ui | Mint UI for NFTs on Solana | https://github.com/edceds/solana-mint-ui | 50 | 2 | Archived; Last commit (Feb 06, 2024) | NFTs & Programs |
| digital-asset-validator-plugin | The NFT Geyser plugin that powers metaplex APIs | https://github.com/metaplex-foundation/digital-asset-validator-plugin | 47 | 19 | v2.0.0 (Mar 26, 2025) | NFTs & Programs |
| solana-nft-anchor | Code for minting nfts on Solana using anchor and metaplex | https://github.com/687c/solana-nft-anchor | 35 | 2 | Last commit (Nov 24, 2023) | NFTs & Programs |
| mpl-candy-guard | Access control logic for Metaplex Candy Machine. | https://github.com/metaplex-foundation/mpl-candy-guard | 27 | 9 | Last commit (Apr 06, 2023) | NFTs & Programs |
| cnft-minter-demo | A demo application that shows how to mint compressed NFTs using Solana Pay QR codes. Powered by the Solana blockchain. | https://github.com/solana-developers/cnft-minter-demo | 19 | 1 | Last commit (Sep 16, 2023) | NFTs & Programs |
| dynamic-nft-metadata | Dynamic NFT Metadata - About a collection of libraries and smart contracts to facilitate dynamic NFT metadata and image generation on Solana with the Metaplex standard. This is used in a variety of ways in the ecosystem to create dynamic and on-chain NFTs | https://github.com/roswelly/dynamic-nft-metadata | 21 | 1 | Last commit (Feb 02, 2026) | NFTs & Programs |
| candy-machine-ui | Easily customizable Solana Candy Machine V2 with WL support. | https://github.com/crusaderincode/candy-machine-ui | 17 | — | v1.1.1 (Aug 05, 2022) | NFTs & Programs |
| solana-copytrading-bot | copytrading bot for the Solana blockchain. It monitors transactions like swaps, transfers, and NFTs across platforms like Raydium, PUMP.FUN, Photon, BonkBot, and more — with support for sniping, liquidity management, and token creation filters. | https://github.com/knightlightst/solana-copytrading-bot | 47 | 1 | Release (Apr 11, 2025) | NFTs & Programs |
| solanaArtGuard-AI-nft-marketplace | AI-driven NFT validation system designed to verify the authenticity and originality of artworks minted on the Solana blockchain. | https://github.com/machenxi/solanaArtGuard-AI-nft-marketplace | 137 | 1 | Last commit (Aug 02, 2023) | NFTs & Programs |
| Candy Machine (Core) | Metaplex Core Candy Machine (Core assets) | https://github.com/metaplex-foundation/mpl-core-candy-machine | 30 | 5 | js@v0.3.0 (Jan 27, 2025) | NFTs & Minting |
| solana-payments-app | Solana Pay for Commerce Platforms | https://github.com/solana-labs/solana-payments-app | 96 | 5 | Archived; v2.0.0 (Aug 18, 2023) | Payments |
| solana-payment-processor | Solana payment processor for e-commerce applications | https://github.com/solpayments/solana-payment-processor | 22 | 2 | Last commit (Jul 13, 2021) | Payments |
| solana-payment-processor | About Solana payment processor for e-commerce applications | https://github.com/hylcore-V/solana-payment-processor | 17 | 1 | Last commit (Nov 24, 2024) | Payments |
| solpress-pay | Woocommerce Payment Gateway Plugin Using Solana Pay | https://github.com/solpressplugins/solpress-pay | 11 | 1 | Last commit (Aug 07, 2024) | Payments |
| wc-solana-pay | Solana Pay powered payment gateway for WordPress and WooCommerce | https://github.com/aztemi/wc-solana-pay | 9 | 1 | Last commit (Dec 24, 2025) | Payments |
| solana-pay-checkout | A point-of-sale web app that allows us to take payments from customers through QR Code in person using Solana Pay. | https://github.com/ronylucca/solana-pay-checkout | 8 | 1 | Last commit (Apr 10, 2022) | Payments |
| solana-pay-qrcode-generator | A simple way to generate QR Codes and easily accept payments in Solana, USCD or any other SPL-Token on the Solana Blockchain. | https://github.com/valentinmadrid/solana-pay-qrcode-generator | 7 | 1 | Last commit (Oct 25, 2022) | Payments |
| solana-pay-minimal-example | Solana Pay(@solana/pay) minimal examples and docs. | https://github.com/256hax/solana-pay-minimal-example | 4 | 1 | Last commit (Aug 31, 2023) | Payments |
| Solana-Token-Payment-Gateway | Process Solana Net-assembly Token payments and setup Solana webhook for payment notifications. HTML payment form to embed into website, payment QRcode, or payment link. | https://github.com/paracetamol951/Solana-Token-Payment-Gateway | 4 | 1 | Last commit (Nov 12, 2025) | Payments |
| woocommerce-payment-gateway | StreamPay - WooCommerce + Solana and USDC Payment Gateway | https://github.com/stream-protocol/woocommerce-payment-gateway | 4 | 2 | Last commit (Dec 30, 2022) | Payments |
| svm-pay | pay and accept payments from anywhere in the world from any solana-vm based network!  works in any country even in space! | https://github.com/openSVM/svm-pay | 3 | 2 | v1.1.0 (Jun 27, 2025) | Payments |
| StablePay | Enterprise-grade stablecoin payment processor built on Solana that leverages Perena's stablecoin infrastructure. | https://github.com/FarseenSh/StablePay | 9 | 2 | Last commit (May 27, 2025) | Payments |
| Solana-Pay-enables-crypto-payments | Businesses can integrate Solana Pay to accept fast and low-cost cryptocurrency payments worldwide | https://github.com/VomicInevallar3422/Solana-Pay-enables-crypto-payments | 7 | — | No releases | Payments |
| x402-Triton-Gateway | A production-ready micropayment gateway that implements HTTP 402 (Payment Required) to monetize access to historical Solana blockchain data via Old Faithful. Users pay micro-amounts in USDC to query historical transactions and blocks. | https://github.com/praptisharma28/x402-Triton-Gateway | 17 | 2 | Last commit (Dec 03, 2025) | Payments |
| solana-x402-payment | x402 payment on solana | https://github.com/Now-Or-Neverr/solana-x402-payment | 29 | 1 | Last commit (Oct 30, 2025) | Payments |
| solana-casino-smart-contract | A Solana casino smart contract is a blockchain program that safely holds player money, runs casino rules fairly, and automatically pays winnings without trusting a central server. | https://github.com/FroganBee/solana-casino-smart-contract | — | — | Active | Payments |
| solana-casino-smart-contract | A Solana casino smart contract is a blockchain program that safely holds player money, runs casino rules fairly, and automatically pays winnings without trusting a central server. | https://github.com/Solzen33/solana-casino-smart-contract | — | — | Active | Payments |
| Jupiter Swap API | Jupiter V6 Swap API binaries and releases | https://github.com/jup-ag/jupiter-swap-api | 240 | 3 | v7.0.6 (Feb 12, 2026) | DeFi |
| carbon | Carbon is an indexing framework on Solana. | https://github.com/sevenlabs-hq/carbon | 552 | 39 | v0.12.0 (Nov 27, 2025) | DeFi |
| raydium-sdk-swap-example-typescript | An example to swap tokens on Solana using the Raydium SDK, TypeScript, and Chainstack | https://github.com/chainstacklabs/raydium-sdk-swap-example-typescript | 185 | 4 | Last commit (Aug 21, 2025) | DeFi |
| Solana-Arbitrage-Bot-Flash-Loan | Solana Arbitrage Bot cross dex like Raydium, Orca, Meteora swap program with rust language architecture using anchor frame work | https://github.com/deniyuda348/Solana-Arbitrage-Bot-Flash-Loan | — | — | Active | DeFi |
| solana-txn-parser | An open-source transaction parser for popular DeFi applications on the Solana blockchain 🚀🤖.. | https://github.com/Tee-py/solana-txn-parser | 203 | 2 | v0.1.6 (Jul 18, 2025) | DeFi |
| Solana-Trading-Bot | Buy and Sell SPL tokens on the Raydium DEX and  Pump.fun using the Solana-Py SDK and Jito SDK | https://github.com/henrytirla/Solana-Trading-Bot | 289 | 1 | Last commit (Feb 15, 2025) | DeFi |
| pumpfun-raydium-cli-tools | solana pumpfun bundler, raydium bundler, pumpfun sniping bot, raydium sniping bot, pumpfun volume bot, raydium volume bot, pumpfun bundler, raydium bundler, jito bundler | https://github.com/hexnome/pumpfun-raydium-cli-tools | 173 | 1 | Last commit (Mar 25, 2025) | DeFi |
| solana-auto-sell-bot | This script continuously scans a Solana wallet for SPL tokens and tracks their age (time held) in seconds. Once a certain time has elapsed it will sell the token on raydium or pumpfun. | https://github.com/lorenzourera/solana-auto-sell-bot | 127 | 1 | Last commit (Sep 18, 2025) | DeFi |
| dex-v4 | Orderbook-based on-chain SPL token swap market | https://github.com/Bonfida/dex-v4 | 103 | 7 | Last commit (Feb 22, 2023) | DeFi |
| pirate-bootcamp | A pirate-theme bootcamp for getting up to speed on Solana programming! | https://github.com/solana-developers/pirate-bootcamp | 332 | 4 | Last commit (Sep 05, 2023) | DeFi |
| solana-escrow | Reference Implementation for the guide https://paulx.dev/blog/2021/01/14/programming-on-solana-an-introduction/ | https://github.com/paul-schaaf/solana-escrow | 315 | 3 | Archived; Last commit (Jan 23, 2022) | DeFi |
| Solana-Arbitrage-Bot | Solana Arbitrage Bot cross dex like Raydium, Orca, Meteora swap program with rust language architecture using anchor frame work | https://github.com/ChangeYourself0613/Solana-Arbitrage-Bot | 286 | 1 | solana-arbitrage-bot2 (May 26, 2025) | DeFi |
| sol-trade-sdk | A comprehensive Rust SDK for seamless interaction with Solana DEX trading programs. This SDK provides a robust set of tools and interfaces to integrate PumpFun, PumpSwap, Bonk, and Raydium CPMM functionality into your applications. | https://github.com/0xfnzero/sol-trade-sdk | 271 | 10 | v3.4.0 (Jan 27, 2026) | DeFi |
| Payment-gateway | Payment gateway for solana with advanced Private key management and address sweeping via indexer | https://github.com/alxn787/Payment-gateway | 14 | 1 | Last commit (Jul 12, 2025) | DeFi |
| Solana-Arbitrage-Bot | Solana Arbitrage Bot cross dex like Raydium, Orca, Meteora swap program with rust language architecture using anchor frame work | https://github.com/deniyuda348/Solana-Arbitrage-Bot | — | — | Active | DeFi |
| Solana-Arbitrage-Bot | Solana Arbitrage Bot on Pump Swap, Raydium, Orca, Meteora swap program with rust language | https://github.com/AV1080p/Solana-Arbitrage-Bot | 485 | 1 | Last commit (Jan 26, 2026) | DeFi |
| profit-script | Calculate PnL for a Solana SPL Token (10x faster than others) | https://github.com/tymur999/profit-script | 40 | 1 | Last commit (Jun 21, 2024) | DeFi |
| Solana-Memecoin-CLI | Solana Memecoin CLI is a powerful tool designed for volume booster and this is a copy bot for trading dev integrated with Jito bundles, Jupiter, Raydium, and Pump.fun | https://github.com/earthskyorg/Solana-Memecoin-CLI | — | — | Active | DeFi |
| solana-streamer | A lightweight Rust library for real-time event streaming from Solana DEX trading programs. This library provides efficient event parsing and subscription capabilities for PumpFun, PumpSwap, Bonk, and Raydium CPMM protocols. | https://github.com/0xfnzero/solana-streamer | 150 | 11 | v1.2.0 (Jan 27, 2026) | DeFi |
| solana-txn | A simple transaction listener that subscribes to blocks on Solana using the Rust programming language | https://github.com/JoshuaSum/solana-txn | 70 | 1 | Last commit (Jun 13, 2024) | DeFi |
| identity-swap | An Automatic Money Market (AMM) dApp that  demonstrates the concept of Decentralised Identity on the  Solana SPL Token-Swap program. | https://github.com/civicteam/identity-swap | 32 | 2 | Last commit (Nov 12, 2020) | DeFi |
| Solana-Arbitrage-Trading-Bot | Atomic, fast, and pragmatic Solana arbitrage with Jito bundles, Jupiter (ULTRA/SWAP). | https://github.com/ApexArb/Solana-Arbitrage-Trading-Bot | 71 | 1 | Last commit (Sep 17, 2025) | DeFi |
| Four.meme-Pump.fun-Fork-Fourmeme-Pumpfun | Multichain Web3 Framework — supports Pump.fun (Solana), Four.meme (BNB), and Xpad.fun (EVM) with smart contracts, backend, and frontend integrations. Compatible with Raydium, Meteora, Pumpswap, and Uniswap on Solana & EVM (Monad, BNB, Ethereum L1/L2). | https://github.com/Tru3Bliss/Four.meme-Pump.fun-Fork-Fourmeme-Pumpfun | 195 | 1 | Last commit (Oct 10, 2025) | DeFi |
| pumpfun-amm-bundler-volumn-maker-bot | Automated PumpFun/Raydium bundler and volume bot for Solana using Jito, multi-wallet distribution, and randomized buy/sell cycles to simulate organic liquidity and improve execution reliability. | https://github.com/Luukogood/pumpfun-amm-bundler-volumn-maker-bot | 17 | 2 | Last commit (Sep 04, 2025) | DeFi |
| solana-x402-payment | A modern, refactored Solana trading bot for Pumpswap that features automated market cap monitoring, risk management, comprehensive error handling, and a clean TypeScript architecture with full testing coverage. | https://github.com/michalstefanow/solana-x402-payment | 29 | 1 | Last commit (Oct 30, 2025) | DeFi |
| solana-copy-trading-bot | --Solana copy trading bot-- Advanced Solana copy trading bot with non-blocking parallel execution, must-selling protection, and multi-DEX fallback (Raydium, PumpFun, Jupiter) for secure high-speed DeFi trading.  --Solana copy trading bot | https://github.com/AlphaFox000/solana-copy-trading-bot | — | — | Active | DeFi |
| moonit-sdk | NPM package and code examples for creating buy/sell and mint transactions, and calculating the price of any moon.it tokens on Solana. | https://github.com/gomoonit/moonit-sdk | 60 | 6 | v1.5.0 (Feb 11, 2026) | Oracles |
| Prediction-Market | A Solana-native decentralized prediction market protocol that allows users to create custom markets, supply liquidity, and place tokenized bets, leveraging Switchboard oracles and Anchor smart contracts for trust-minimized outcome settlement. | https://github.com/novustch/Prediction-Market | — | — | Active | Oracles |

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

