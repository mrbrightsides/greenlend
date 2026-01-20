# GreenLend Micro - Architecture Documentation

Comprehensive system architecture documentation for **GreenLend Micro**, the voice-powered microfinance platform within the LoanChain Ledger ecosystem.

---

## 📋 Table of Contents

1. [System Overview](#system-overview)
2. [Technology Stack](#technology-stack)
3. [Architecture Patterns](#architecture-patterns)
4. [Frontend Architecture](#frontend-architecture)
5. [Backend Architecture](#backend-architecture)
6. [Blockchain Integration](#blockchain-integration)
7. [Voice AI Integration](#voice-ai-integration)
8. [Data Flow](#data-flow)
9. [Security Architecture](#security-architecture)
10. [Scalability & Performance](#scalability--performance)

---

## 🏗️ System Overview

GreenLend Micro is a **full-stack Web3 application** built on a modern, scalable architecture:

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Interface Layer                      │
│  (Next.js 15 App Router, React 19, Tailwind CSS, shadcn/ui)    │
└─────────────────┬───────────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────────┐
│                   Application Logic Layer                        │
│  • React Contexts (Auth, Data, Maya, Language)                  │
│  • Custom Hooks (Blockchain, Voice, Authentication)             │
│  • Component Library (Borrower, Lender, Shared UI)              │
└─────────────────┬───────────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────────┐
│                      API Layer (Next.js)                         │
│  • RESTful API Routes                                            │
│  • Server-side validation (Zod)                                  │
│  • Proxy for external services                                   │
└──────┬──────────┬───────────────┬───────────────┬───────────────┘
       │          │               │               │
       ▼          ▼               ▼               ▼
┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────────┐
│Blockchain│ │ElevenLabs│ │  Pinata    │ │  Authentication│
│(Sepolia, │ │ Voice AI │ │   IPFS     │ │  (SIWE, Auth) │
│  Base)   │ │          │ │            │ │               │
└──────────┘ └──────────┘ └────────────┘ └──────────────┘
```

### Key Characteristics

- **Serverless Architecture** - Next.js API routes deployed on Vercel Edge Network
- **Blockchain-First** - All transactions verified on-chain for transparency
- **Voice-Native** - Conversational UX via ElevenLabs AI
- **Type-Safe** - End-to-end TypeScript with strict mode
- **Mobile-First** - Responsive design optimized for emerging markets
- **Modular** - Component-based architecture for maintainability

---

## 🛠️ Technology Stack

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| **Next.js** | 15.3.8 | React framework with App Router |
| **React** | 19.1.0 | UI library |
| **TypeScript** | 5.8.3 | Type safety |
| **Tailwind CSS** | 4.1.17 | Utility-first styling |
| **shadcn/ui** | Latest | Accessible component library |
| **Framer Motion** | 12.12.1 | Animations |
| **Lucide React** | 0.511.0 | Icon library |

### Blockchain & Web3

| Technology | Version | Purpose |
|------------|---------|---------|
| **ethers.js** | 6.16.0 | Ethereum interaction |
| **wagmi** | 2.15.5 | React hooks for Ethereum |
| **viem** | 2.43.3 | TypeScript Ethereum library |
| **RainbowKit** | 2.2.3 | Wallet connection UI |
| **OnchainKit** | 0.38.5 | Coinbase Base integration |
| **SIWE** | 3.0.0 | Sign-In with Ethereum |

### Voice AI

| Technology | Version | Purpose |
|------------|---------|---------|
| **@elevenlabs/client** | 0.13.0 | Voice AI SDK |
| **@11labs/client** | 0.2.0 | Alternative SDK |

### State Management

| Technology | Version | Purpose |
|------------|---------|---------|
| **React Context** | Built-in | Global state |
| **TanStack Query** | 5.67.0 | Server state management |
| **Zod** | 3.24.4 | Schema validation |

### Authentication

| Technology | Version | Purpose |
|------------|---------|---------|
| **NextAuth** | 4.24.11 | Authentication framework |
| **iron-session** | 8.0.4 | Encrypted session cookies |
| **SIWE** | 3.0.0 | Web3 authentication |

### DevOps & Tooling

| Technology | Version | Purpose |
|------------|---------|---------|
| **Vercel** | Latest | Hosting & deployment |
| **PostHog** | 1.242.2 | Analytics |
| **Winston** | 3.17.0 | Server-side logging |

---

## 🎨 Architecture Patterns

### 1. **App Router Pattern (Next.js 15)**

We use Next.js App Router for improved performance and developer experience:

```typescript
// App directory structure
src/app/
├── layout.tsx           // Root layout
├── page.tsx             // Landing page
├── borrower/
│   └── page.tsx         // Borrower dashboard
├── lender/
│   └── page.tsx         // Lender dashboard
└── api/
    ├── score/
    │   └── route.ts     // Credit scoring API
    └── disburse/
        └── route.ts     // Loan disbursement API
```

**Benefits**:
- Server Components by default (faster initial load)
- Built-in layouts and templates
- Improved SEO
- Streaming and suspense support

### 2. **Context-Based State Management**

Four primary contexts manage global state:

```typescript
// AuthContext - User authentication state
interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  login: (address: string) => Promise<void>;
  logout: () => void;
}

// DataContext - Application data
interface DataContextType {
  loans: Loan[];
  portfolio: Portfolio;
  refreshData: () => Promise<void>;
}

// MayaContext - Voice assistant state
interface MayaContextType {
  isListening: boolean;
  transcript: string;
  startConversation: () => void;
  stopConversation: () => void;
}

// LanguageContext - Internationalization
interface LanguageContextType {
  language: 'en' | 'id';
  setLanguage: (lang: 'en' | 'id') => void;
  t: (key: string) => string;
}
```

### 3. **Component Composition Pattern**

Reusable components follow atomic design principles:

```
components/
├── ui/                  # Atoms (Button, Input, Card)
├── borrower/            # Molecules (CreditScoreResult, LoanStatus)
├── lender/              # Molecules (PortfolioImpact, TransactionHistory)
└── VoiceAssistant.tsx   # Organism (Complex component)
```

### 4. **API Route Pattern**

RESTful API design with consistent structure:

```typescript
// src/app/api/[endpoint]/route.ts
import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    // 1. Parse and validate request
    const body = await request.json();
    
    // 2. Business logic
    const result = await processRequest(body);
    
    // 3. Return response
    return NextResponse.json(result);
  } catch (error) {
    // 4. Error handling
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
```

### 5. **Blockchain Abstraction Layer**

Smart contract interactions abstracted into clean interfaces:

```typescript
// lib/blockchain.ts
export interface BlockchainAdapter {
  disburseLoan(loanId: string, amount: bigint): Promise<TransactionHash>;
  recordRepayment(loanId: string, amount: bigint): Promise<TransactionHash>;
  getLoanStatus(loanId: string): Promise<LoanStatus>;
}

// Implementation uses ethers.js
export class EthereumAdapter implements BlockchainAdapter {
  // Implementation details
}
```

---

## 💻 Frontend Architecture

### Component Structure

```typescript
// Example: Score Decomposition Dashboard
'use client';

import type { FC } from 'react';
import { Card } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';

interface ScoreDecompositionProps {
  score: CreditScore;
}

export const ScoreDecompositionDashboard: FC<ScoreDecompositionProps> = ({ score }) => {
  return (
    <Card className="p-6">
      <h2 className="text-2xl font-bold mb-4">Credit Score Breakdown</h2>
      
      {/* Score components */}
      <div className="space-y-4">
        <ScoreComponent 
          label="Business Viability"
          score={score.businessViability}
          weight={0.3}
        />
        <ScoreComponent 
          label="Social Impact"
          score={score.socialImpact}
          weight={0.25}
        />
        {/* More components */}
      </div>
    </Card>
  );
};
```

### Routing Structure

```typescript
// Next.js App Router
/                          → Landing page
/borrower                  → Borrower dashboard
/lender                    → Lender dashboard
/methodology               → Scoring methodology
/transparency              → Blockchain transparency
/about                     → About page
/api/*                     → API routes
```

### State Management Flow

```
User Action → Component → Context Update → Re-render
                ↓
          API Call (if needed)
                ↓
          Server Response
                ↓
          Context Update → Re-render
```

---

## 🖥️ Backend Architecture

### API Routes Structure

```typescript
src/app/api/
├── chat/                  # AI conversation
│   └── route.ts
├── chat-extract/          # Extract loan data from chat
│   └── route.ts
├── score/                 # Credit scoring
│   └── route.ts
├── disburse/              # Loan disbursement
│   └── route.ts
├── repayment/             # Repayment processing
│   └── route.ts
├── portfolio/             # Portfolio analytics
│   └── route.ts
├── elevenlabs/            # Voice AI integration
│   ├── route.ts
│   └── signed-url/
│       └── route.ts
├── maya/                  # Maya assistant
│   └── process/
│       └── route.ts
└── siwe/                  # Web3 authentication
    └── verify/
        └── route.ts
```

### Business Logic Layer

```typescript
// lib/creditScoring.ts
export interface CreditScoreComponents {
  businessViability: number;
  socialImpact: number;
  environmentalImpact: number;
  financialHealth: number;
  repaymentCapacity: number;
}

export function calculateCreditScore(
  application: LoanApplication
): CreditScoreComponents {
  // Transparent, SDG-aligned scoring algorithm
  const businessViability = assessBusinessViability(application);
  const socialImpact = assessSocialImpact(application);
  const environmentalImpact = assessEnvironmentalImpact(application);
  const financialHealth = assessFinancialHealth(application);
  const repaymentCapacity = assessRepaymentCapacity(application);

  return {
    businessViability,
    socialImpact,
    environmentalImpact,
    financialHealth,
    repaymentCapacity,
  };
}
```

### Data Validation

All API inputs validated with Zod:

```typescript
import { z } from 'zod';

const LoanApplicationSchema = z.object({
  amount: z.number().positive().max(100000),
  term: z.number().int().min(1).max(60),
  purpose: z.string().min(10).max(500),
  businessType: z.enum(['agriculture', 'retail', 'services', 'manufacturing']),
  annualRevenue: z.number().positive(),
  employeeCount: z.number().int().nonnegative(),
});

type LoanApplication = z.infer<typeof LoanApplicationSchema>;
```

---

## ⛓️ Blockchain Integration

### Smart Contract Architecture

```solidity
// Simplified GreenLend contract structure
contract GreenLend {
  struct Loan {
    address borrower;
    address lender;
    uint256 amount;
    uint256 interestRate;
    uint256 term;
    uint256 disbursedAt;
    uint256 repaidAmount;
    LoanStatus status;
  }

  mapping(bytes32 => Loan) public loans;
  
  function disburseLoan(bytes32 loanId) external payable;
  function recordRepayment(bytes32 loanId) external payable;
  function getLoanDetails(bytes32 loanId) external view returns (Loan memory);
}
```

### Contract Interaction Layer

```typescript
// lib/greenlend-contract.ts
import { ethers } from 'ethers';
import type { TransactionResponse } from 'ethers';

export class GreenLendContract {
  private contract: ethers.Contract;

  constructor(provider: ethers.Provider, contractAddress: string) {
    this.contract = new ethers.Contract(
      contractAddress,
      GreenLendABI,
      provider
    );
  }

  async disburseLoan(
    loanId: string,
    amount: bigint,
    signer: ethers.Signer
  ): Promise<TransactionResponse> {
    const contractWithSigner = this.contract.connect(signer);
    return await contractWithSigner.disburseLoan(loanId, { value: amount });
  }

  async getLoanDetails(loanId: string): Promise<LoanDetails> {
    const loan = await this.contract.getLoanDetails(loanId);
    return {
      borrower: loan.borrower,
      lender: loan.lender,
      amount: loan.amount,
      status: loan.status,
    };
  }
}
```

### Blockchain Networks

| Network | Chain ID | Purpose |
|---------|----------|---------|
| **Ethereum Sepolia** | 11155111 | Primary testnet for loan contracts |
| **Base** | 8453 | LoanChain Ledger integration |

---

## 🎙️ Voice AI Integration

### ElevenLabs SDK Architecture

```typescript
// contexts/MayaContext.tsx
import { Conversation } from '@elevenlabs/client';
import type { FC, ReactNode } from 'react';
import { createContext, useContext, useState } from 'react';

interface MayaContextType {
  conversation: Conversation | null;
  isListening: boolean;
  transcript: string;
  startConversation: () => Promise<void>;
  stopConversation: () => void;
}

export const MayaContext = createContext<MayaContextType | undefined>(undefined);

export const MayaProvider: FC<{ children: ReactNode }> = ({ children }) => {
  const [conversation, setConversation] = useState<Conversation | null>(null);
  const [isListening, setIsListening] = useState<boolean>(false);
  const [transcript, setTranscript] = useState<string>('');

  const startConversation = async (): Promise<void> => {
    const conv = await Conversation.startSession({
      agentId: process.env.NEXT_PUBLIC_ELEVENLABS_AGENT_ID!,
      onMessage: (message) => {
        setTranscript(prev => prev + ' ' + message.text);
      },
      onError: (error) => {
        console.error('Maya error:', error);
      },
    });

    setConversation(conv);
    setIsListening(true);
  };

  const stopConversation = (): void => {
    conversation?.endSession();
    setIsListening(false);
  };

  return (
    <MayaContext.Provider value={{
      conversation,
      isListening,
      transcript,
      startConversation,
      stopConversation,
    }}>
      {children}
    </MayaContext.Provider>
  );
};
```

### Conversation Flow

```
1. User clicks "Talk to Maya"
   ↓
2. Start ElevenLabs session
   ↓
3. User speaks → Real-time transcription
   ↓
4. AI processes intent (loan application, query, etc.)
   ↓
5. Extract entities (amount, term, purpose)
   ↓
6. Send to /api/maya/process
   ↓
7. Generate response
   ↓
8. Text-to-speech playback
   ↓
9. Loop until user ends conversation
```

---

## 📊 Data Flow

### Loan Application Flow

```
1. User fills form OR talks to Maya
   ↓
2. Frontend validates input
   ↓
3. POST /api/score
   ↓
4. Server calculates credit score
   ↓
5. Return score decomposition
   ↓
6. If approved:
   - POST /api/disburse
   - Smart contract call
   - Transaction confirmation
   ↓
7. Update UI with loan status
```

### Authentication Flow

```
1. User clicks "Connect Wallet"
   ↓
2. RainbowKit modal opens
   ↓
3. User selects MetaMask
   ↓
4. Sign message (SIWE)
   ↓
5. POST /api/siwe/verify
   ↓
6. Server verifies signature
   ↓
7. Create session (iron-session)
   ↓
8. Set AuthContext state
   ↓
9. Redirect to dashboard
```

---

## 🔒 Security Architecture

### Authentication Layers

1. **Wallet Connection** - MetaMask signature
2. **SIWE Verification** - Cryptographic proof of wallet ownership
3. **Session Management** - Encrypted cookies (iron-session)
4. **API Authorization** - Session validation on every request

### Data Protection

- **Environment Variables** - Secrets in `.env.local`, never committed
- **API Keys** - Server-side only, never exposed to client
- **Input Validation** - Zod schemas on all API routes
- **SQL Injection** - N/A (no SQL database, blockchain only)
- **XSS Protection** - React's built-in escaping

### Smart Contract Security

- **Access Control** - Only authorized addresses can disburse
- **Reentrancy Guards** - Prevent reentrancy attacks
- **Integer Overflow** - Solidity 0.8+ built-in checks
- **Testnet First** - Deployed on Sepolia before mainnet

---

## 🚀 Scalability & Performance

### Frontend Optimization

- **Server Components** - Reduce client-side JavaScript
- **Code Splitting** - Dynamic imports for heavy components
- **Image Optimization** - Next.js `next/image` automatic optimization
- **Font Optimization** - Local font files, no external requests

### Backend Optimization

- **Edge Functions** - Deployed on Vercel Edge Network (low latency)
- **Caching** - API responses cached where appropriate
- **Lazy Loading** - Load blockchain data on demand

### Blockchain Optimization

- **Batch Transactions** - Multiple operations in single transaction
- **Gas Estimation** - Calculate gas before transaction
- **Optimistic UI** - Update UI before blockchain confirmation

### Performance Metrics

| Metric | Target | Current |
|--------|--------|---------|
| **First Contentful Paint** | < 1.5s | ~1.2s |
| **Time to Interactive** | < 3s | ~2.5s |
| **Lighthouse Score** | > 90 | 94 |
| **Bundle Size** | < 500KB | ~380KB |

---

## 🔄 Integration with LoanChain Ledger

GreenLend Micro integrates with LoanChain Ledger through:

1. **Base Network Bridge** - Cross-chain capital allocation
2. **IPFS Document Storage** - Pinata for loan documents
3. **Real-time Risk API** - Shared portfolio monitoring
4. **Compliance Tracking** - Automated ESG reporting

```typescript
// Integration architecture
GreenLend Micro (Sepolia)
      ↓
   Bridge Contract
      ↓
LoanChain Ledger (Base)
      ↓
Syndicated Loan Pool ($6T market)
```

---

## 📚 Additional Documentation

- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Contribution guidelines
- **[SETUP.md](./SETUP.md)** - Setup instructions
- **[THIRD_PARTY_APIs.md](./THIRD_PARTY_APIs.md)** - API integrations

---

**Questions?** Contact [support@elpeef.com](mailto:support@elpeef.com)

**Built with ❤️ for transparent, inclusive finance**
