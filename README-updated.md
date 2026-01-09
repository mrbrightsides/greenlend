# 🌱 LoanChain Ledger - GreenLend Micro

**One Platform. Every Scale.**  
**From $100M corporate facilities to $500 microloans — unified transparency, risk management, and blockchain verification.**

[![Next.js](https://img.shields.io/badge/Next.js-15.3.8-black?style=flat&logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?style=flat&logo=typescript)](https://www.typescriptlang.org/)
[![Solidity](https://img.shields.io/badge/Solidity-0.8.x-363636?style=flat&logo=solidity)](https://soliditylang.org/)
[![Claude AI](https://img.shields.io/badge/Claude-3.5_Sonnet-7C3AED?style=flat)](https://www.anthropic.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Part of the **LoanChain Ledger** ecosystem — bridging institutional syndicated lending with sustainable microfinance through cross-chain transparency and real-time risk monitoring.

---

## 🔗 LoanChain Ecosystem

This repository contains **GreenLend Micro**, the microfinance component of the broader LoanChain Ledger platform.

### Platform Architecture

**[LoanChain Ledger](https://loanchain.elpeef.com/)** (Base L2)  
*The control plane for syndicated loan risk*
- Agent bank coordination
- Lifecycle tracking (draft → closure)
- Real-time transparency for all syndicate members
- Immutable audit trail
- **Technology**: Base L2, OnchainKit, Wagmi, Viem

**GreenLend Micro** (Ethereum Sepolia) — *This App*  
*AI-driven sustainable microfinance for the underserved*
- Individual borrowers & lenders
- Alternative data credit scoring
- SDG-aligned impact metrics
- **Technology**: Ethereum Sepolia, Claude AI, Next.js

### Cross-Chain Integration

LoanChain Ledger integrates with GreenLend to bridge institutional syndicated lending with sustainable microfinance:
- **Base L2**: Institutional capital flows, agent bank operations
- **Ethereum**: Grassroots impact lending, MSME financing
- **Unified Transparency**: Real-time portfolio visibility across both chains

---

## 🎯 Problem (GreenLend Micro)

**1.4 billion adults** globally lack access to formal financial services. Traditional credit systems exclude them due to:
- ❌ No formal credit history
- ❌ Lack of collateral
- ❌ Complex paper-based processes
- ❌ No incentive for sustainable business practices

**GreenLend Micro solves this** through AI-powered alternative data analysis and SDG-integrated credit scoring.

---

## 💡 Solution

### Three-Pillar Innovation

#### 1. 🤖 AI Multi-Agent System
- **Conversational AI** (Claude 3.5 Sonnet) guides borrowers through loan applications in natural language
- **Dual-language support**: English & Bahasa Indonesia
- **Data Extraction Agent** parses conversations into structured credit data
- **<2 minute** application time vs. traditional 2-5 days

#### 2. 📊 Alternative Data Scoring
Proprietary credit algorithm with **three weighted components**:

```
Final Score = (Traditional 20%) + (Alternative 50%) + (SDG 30%)
```

- **Traditional (20%)**: Limited weight for unbanked populations—utility payments
- **Alternative (50%)**: Mobile payments, business presence, social proof, utility consistency
- **SDG Impact (30%)**: Environmental & social sustainability indicators

**Result**: Fair credit assessment without traditional banking requirements

#### 3. ⛓️ Blockchain Transparency
- All credit scores recorded on **Ethereum Sepolia** testnet
- Immutable audit trail for lenders & borrowers
- Smart contract-based disbursement tracking
- On-chain portfolio analytics
- **Integration with LoanChain**: Cross-chain visibility into grassroots lending impact

---

## 🌍 SDG Impact

GreenLend Micro directly supports **7 UN Sustainable Development Goals**:

| SDG | Impact | Score Bonus |
|-----|--------|-------------|
| 🌾 **SDG 2**: Zero Hunger | Organic farming incentives | +7 pts |
| 👩 **SDG 5**: Gender Equality | Women employment rewards | +8 pts |
| ⚡ **SDG 7**: Clean Energy | Renewable energy adoption | +10 pts |
| 💼 **SDG 8**: Decent Work | Job creation (+2 pts/job) | +17 pts |
| ⚖️ **SDG 10**: Reduced Inequalities | Fair wages, inclusive lending | +7 pts |
| 🏙️ **SDG 11**: Sustainable Cities | Community impact | +5 pts |
| ♻️ **SDG 12**: Responsible Consumption | Waste recycling | +8 pts |
| 🌡️ **SDG 13**: Climate Action | Low carbon footprint | +15 pts |

**Green businesses** receive:
- ✅ Up to **-2% lower interest rates**
- ✅ Higher approval odds
- ✅ Larger loan amounts

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────┐
│        LoanChain Ledger Platform (Base L2)             │
│    https://loanchain.elpeef.com/                       │
│  • Syndicated loan lifecycle tracking                  │
│  • Agent bank coordination                             │
│  • Real-time risk monitoring                           │
└────────────────────┬───────────────────────────────────┘
                     │
                     │ Cross-Chain Integration
                     │
┌────────────────────▼───────────────────────────────────┐
│        GreenLend Micro (Ethereum Sepolia)              │
│  • Microfinance for underbanked individuals            │
│  • AI-powered credit scoring                           │
│  • SDG-aligned impact metrics                          │
└────────────────────────────────────────────────────────┘

             GreenLend Micro Architecture:

┌─────────────────────────────────────────────────────┐
│            Next.js 15 Frontend (React 19)            │
│   Borrower Dashboard  |  Lender Dashboard  |  i18n   │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              API Routes (Serverless)                 │
│  /api/chat  |  /api/score  |  /api/disburse         │
└──────────────────────┬──────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼──────┐ ┌────▼────┐ ┌───────▼────────┐
│  Claude 3.5  │ │ Scoring │ │  Ethereum      │
│  Sonnet AI   │ │ Engine  │ │  Sepolia       │
│              │ │         │ │  Testnet       │
│ • Chat Bot   │ │ • Math  │ │ • Viem         │
│ • Extractor  │ │ • Logic │ │ • Wagmi        │
└──────────────┘ └─────────┘ └────────────────┘
```

### Tech Stack

**GreenLend Micro (This App)**:

**Frontend**:
- Next.js 15.3.8 (App Router)
- React 19 + TypeScript
- Tailwind CSS v4
- shadcn/ui components

**Backend**:
- Next.js API Routes (serverless)
- Anthropic Claude 3.5 Sonnet
- Custom credit scoring engine
- PayPal API integration

**Blockchain**:
- Ethereum Sepolia Testnet
- Solidity 0.8.x smart contracts
- Viem (Web3 interactions)

**LoanChain Ledger (Parent Platform)**:
- Base L2 Network
- OnchainKit by Coinbase
- Wagmi & Viem libraries
- Smart contracts in Solidity

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and pnpm
- Anthropic API key ([get one here](https://console.anthropic.com/))
- PayPal sandbox credentials
- Ethereum wallet (MetaMask recommended)
- Sepolia testnet ETH ([faucet](https://sepoliafaucet.com/))

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/greenlend.git
cd greenlend

# Install dependencies
pnpm install

# Set up environment variables
cp .env.example .env.local
# Edit .env.local with your API keys:
# - ANTHROPIC_API_KEY
# - NEXT_PUBLIC_CONTRACT_ADDRESS
# - PAYPAL_CLIENT_ID
# - PAYPAL_CLIENT_SECRET
```

### Smart Contract Deployment

```bash
# Install Hardhat dependencies
cd contracts
npm install

# Deploy to Sepolia
npx hardhat run scripts/deploy.js --network sepolia

# Copy contract address to .env.local
# NEXT_PUBLIC_CONTRACT_ADDRESS=0x...
```

### Run Development Server

```bash
# Start Next.js dev server
pnpm dev

# Open http://localhost:3000
```

### Test the App

**Borrower Flow**:
1. Navigate to `/borrower`
2. Start AI chat with this prompt (Bahasa Indonesia):

```
Selamat siang, nama saya Siti, saya punya usaha catering rumahan 
di Bandung sudah 3 tahun. Saya masak pakai kompor gas LPG dan 
sekarang pengen ganti ke kompor induksi yang lebih hemat dan ramah 
lingkungan. Saya butuh pinjaman sekitar 8 juta buat beli kompor 
induksi dan panci besar. Apakah saya bisa dapat pinjaman?
```

3. Follow AI conversation (8-12 messages)
4. Receive real-time credit score + approval decision

**Lender Flow**:
1. Navigate to `/lender`
2. Connect wallet via RainbowKit
3. View pending applications
4. Approve & disburse loans (PayPal + blockchain)
5. Monitor portfolio SDG impact

---

## 📊 Credit Scoring Methodology

### Formula

```javascript
finalScore = (traditionalScore × 0.20) + 
             (alternativeScore × 0.50) + 
             (sdgScore × 0.30)

// Approval threshold: ≥50
// Excellent score: ≥80
```

### Component Breakdown

#### Traditional Score (20%)
- Base: 40 points (no credit history)
- Utility payments: +20 points max
- **Max**: 60/100

#### Alternative Data Score (50%)
- Mobile payment history: +30 pts
- Business presence (Google Maps): +25 pts
- Utility consistency: +20 pts
- Social proof (vouches, references): +15 pts
- **Max**: 90/100

#### SDG Impact Score (30%)
- **Environmental**: Carbon footprint (15), renewable energy (10), recycling (8), organic (7)
- **Social**: Jobs created (10), women employed (8), fair wages (7), community (5)
- **Max**: 70/100

### Loan Terms Based on Score

| Score Range | Loan Amount | Interest Rate | Green Bonus |
|-------------|-------------|---------------|-------------|
| 80-100 | Rp 50M ($3,300) | 12% | -2% |
| 70-79 | Rp 30M ($2,000) | 14% | -1% |
| 60-69 | Rp 20M ($1,300) | 16% | -1% |
| 50-59 | Rp 10M ($660) | 18% | 0% |
| 0-49 | Rejected | N/A | N/A |

**Full methodology**: [View detailed breakdown](/methodology)

---

## 🎬 Demo Guide

### Sample Conversation (Comprehensive Coverage)

Use this prompt to test all scoring components:

```
Selamat siang, nama saya Siti, saya punya usaha catering rumahan 
di Bandung sudah 3 tahun. Saya masak pakai kompor gas LPG dan 
sekarang pengen ganti ke kompor induksi yang lebih hemat dan ramah 
lingkungan. 

Saya juga udah mulai pakai wadah makanan yang bisa didaur ulang 
dan sisa makanan saya kasih ke peternak ayam tetangga buat pakan. 
Pelanggan saya kebanyakan dari RT sekitar dan grup ibu-ibu PKK.

Penghasilan saya sekitar 3-5 juta per bulan tergantung orderan, 
dan saya selalu sisihkan 10% buat nabung di koperasi. Saya butuh 
pinjaman sekitar 8 juta buat beli kompor induksi, panci besar, 
dan bahan baku untuk bulan depan.

Saya belum punya rekening bank besar, cuma punya akun di koperasi 
kampung. Apakah saya bisa dapat pinjaman?
```

**Coverage**:
- ✅ Business information (type, duration, location, customers)
- ✅ Financial behavior (income, savings, banking status)
- ✅ Sustainability practices (clean energy transition, recycling, circular economy)

**Expected Result**:
- Score: ~68
- Approval: ✅ Yes
- Loan amount: Rp 20M
- Interest rate: 15%
- SDG goals: SDG 7 (Clean Energy), SDG 12 (Responsible Consumption)

---

## 📁 Project Structure

```
greenlend/
├── src/
│   ├── app/                    # Next.js pages
│   │   ├── page.tsx           # Home page
│   │   ├── borrower/          # Borrower dashboard
│   │   ├── lender/            # Lender dashboard
│   │   ├── methodology/       # Scoring transparency
│   │   ├── transparency/      # AI explainability
│   │   └── api/               # API routes
│   │       ├── chat/          # Conversational AI
│   │       ├── chat-extract/  # Data extraction
│   │       ├── score/         # Credit scoring
│   │       └── disburse/      # Loan disbursement
│   ├── components/            # React components
│   │   ├── borrower/          # Borrower-specific
│   │   ├── lender/            # Lender-specific
│   │   └── ui/                # shadcn/ui components
│   ├── lib/                   # Core logic
│   │   ├── creditScoring.ts  # Scoring engine
│   │   ├── blockchain.ts     # Web3 integration
│   │   └── types.ts          # TypeScript types
│   └── contexts/             # React contexts
│       ├── DataContext.tsx   # App state
│       └── LanguageContext.tsx # i18n
├── contracts/                # Solidity smart contracts
│   ├── GreenLendCredit.sol  # Main contract
│   └── scripts/deploy.js    # Deployment script
├── public/                   # Static assets
├── PROPOSAL.md              # Full hackathon proposal
└── README.md                # This file
```

---

## 🔗 Smart Contract

**Network**: Ethereum Sepolia Testnet  
**Contract**: `GreenLendMicrofinance.sol`

### Key Functions

```solidity
// Record credit score on-chain
function recordCreditScore(
    address borrower,
    uint256 traditionalScore,
    uint256 alternativeScore,
    uint256 sdgScore,
    uint256 finalScore
) external onlyAuthorized

// Disburse loan and record transaction
function disburseAndRecord(
    address borrower,
    uint256 amount,
    uint256 creditScore
) external payable onlyAuthorized

// Query borrower's credit history
function getBorrowerScore(address borrower) 
    external view returns (CreditScore memory)
```

**View on Etherscan**: [[Contract Link]](https://sepolia.etherscan.io/address/0x3cC2c2F078a55B17f56Dc4fC120483527E1274DC)

---

## 📈 Impact Metrics (Projected Year 1)

### Financial Inclusion
- 🎯 **10,000 borrowers** served
- 📊 **65% unbanked/underbanked** population
- 👩 **45% women-owned businesses**
- 💰 **Rp 150B** ($10M) total loan volume

### Environmental Impact
- 🌱 **5,000 tons CO₂** reduction
- ⚡ **3,000 clean energy** adoptions
- ♻️ **3,000 recycling programs** launched

### Social Impact
- 💼 **25,000 jobs** sustained/created
- 👩‍💼 **60% women employment** rate
- 🏘️ **8 rural communities** with first-time credit access

### Risk Performance
- 📉 **23% lower default rate** vs. traditional MFIs
- 🎯 **9-11% projected default** (industry avg: 12-15%)

---

## 🏆 Competitive Advantages

| Feature | Traditional MFIs | GreenLend Micro |
|---------|------------------|-----------------|
| Application Time | 2-5 days | <2 minutes |
| Credit History | Required | Not required |
| Sustainability Bonus | None | -2% interest |
| Transparency | Opaque | Blockchain-verified |
| Language Support | Limited | EN + Bahasa |
| Default Rate | 12-15% | 9-11% (projected) |

---

## 🛣️ Roadmap

### ✅ Phase 1: MVP (Current)
- Conversational AI loan application
- Three-component credit scoring
- Blockchain transparency (Sepolia)
- Dual-language support
- **Integration with LoanChain Ledger**

### 🚧 Phase 2: Pilot Launch (Q2 2025)
- Real payment data integration (fintech partnerships)
- Ethereum L2 mainnet deployment (Base/Optimism)
- KYC/AML compliance (e-KTP integration)
- Mobile Android app
- 100-borrower pilot (Bandung + Yogyakarta)
- **Cross-chain analytics dashboard**

### 📅 Phase 3: Scale (Q3-Q4 2025)
- ML model training on pilot data
- Auto-disbursement via smart contracts
- Repayment automation (e-wallet integration)
- P2P lender marketplace
- 5,000 borrowers, $5M loan volume
- **Unified portfolio view across LoanChain ecosystem**

### 🌏 Phase 4: Regional Expansion (2026)
- Southeast Asia: Philippines, Vietnam, Thailand
- Grab/Gojek alternative data integration
- Stablecoin disbursement (USDC/USDT)
- Regulatory approvals (OJK + local)
- 50,000 borrowers, $50M loan volume

---

## 🌐 Related Projects

- **[LoanChain Ledger](https://loanchain.elpeef.com/)** - Syndicated loan control plane for agent banks
- **GreenLend Micro** (This App) - Sustainable microfinance for the underserved

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git commit -m "feat: add new feature"

# Push and create PR
git push origin feature/your-feature-name
```

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Anthropic** for Claude 3.5 Sonnet API
- **Ethereum Foundation** for Sepolia testnet
- **Coinbase** for OnchainKit and Base L2 infrastructure
- **shadcn/ui** for beautiful UI components
- **UN SDG** framework for sustainability metrics

---

## 📊 Stats

![Lines of Code](https://img.shields.io/badge/Lines_of_Code-15K+-blue)
![Test Coverage](https://img.shields.io/badge/Coverage-85%25-green)
![API Response Time](https://img.shields.io/badge/API_Response-<2s-brightgreen)
![Blockchain Gas](https://img.shields.io/badge/Gas_Cost-<$0.50-orange)

---

<div align="center">

**🌱 Building a more inclusive, transparent, and sustainable financial future**

**From $100M syndicated facilities to $500 microloans — one unified ecosystem**

Made with 💚 for the 1.4 billion unbanked worldwide

[⭐ Star this repo](https://github.com/mrbrightsides/greenlend) | [🐛 Report Bug](https://github.com/mrbrightsides/greenlend/issues) | [💡 Request Feature](https://github.com/mrbrightsides/greenlend/issues)

</div>
