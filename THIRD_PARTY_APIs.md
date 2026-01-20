# Third-Party APIs & Integrations

Complete documentation of all external services and APIs integrated into **GreenLend Micro**.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [ElevenLabs Voice AI](#elevenlabs-voice-ai)
3. [Ethereum & Blockchain](#ethereum--blockchain)
4. [Base Network](#base-network)
5. [Pinata IPFS](#pinata-ipfs)
6. [Authentication Services](#authentication-services)
7. [Analytics & Monitoring](#analytics--monitoring)
8. [API Rate Limits & Costs](#api-rate-limits--costs)

---

## 🌐 Overview

GreenLend Micro integrates with multiple third-party services to deliver transparent, voice-powered microfinance:

| Service | Purpose | Tier | Cost |
|---------|---------|------|------|
| **ElevenLabs** | Voice AI (Maya assistant) | Pro | $22/mo |
| **Infura/Alchemy** | Ethereum RPC provider | Free | $0 |
| **Base Network** | LoanChain integration | Mainnet | Gas fees |
| **Pinata** | IPFS document storage | Free | $0 |
| **Vercel** | Hosting & deployment | Hobby | $0 |
| **PostHog** | Analytics | Free | $0 |

**Total Monthly Cost**: ~$22 + gas fees

---

## 🎙️ ElevenLabs Voice AI

### Overview

ElevenLabs powers **Maya**, our conversational AI assistant for loan applications.

- **Website**: [elevenlabs.io](https://elevenlabs.io/)
- **Documentation**: [docs.elevenlabs.io](https://elevenlabs.io/docs)
- **Dashboard**: [elevenlabs.io/app](https://elevenlabs.io/app)

### Integration Details

**SDK Version**: `@elevenlabs/client` v0.13.0

**Features Used**:
- Conversational AI agents
- Real-time voice synthesis
- Speech-to-text transcription
- Custom voice profiles

### API Configuration

```typescript
// Environment variables
ELEVENLABS_API_KEY=sk_xxxxxxxxxxxxxxxxxxxxx
NEXT_PUBLIC_ELEVENLABS_AGENT_ID=agent_xxxxxxxxxxxxxxxxxxxxx
```

### Code Implementation

```typescript
// contexts/MayaContext.tsx
import { Conversation } from '@elevenlabs/client';

const startConversation = async (): Promise<void> => {
  const conversation = await Conversation.startSession({
    agentId: process.env.NEXT_PUBLIC_ELEVENLABS_AGENT_ID!,
    onMessage: (message) => {
      console.log('Maya:', message.text);
    },
    onError: (error) => {
      console.error('Error:', error);
    },
  });
  
  await conversation.startRecording();
};
```

### Rate Limits

| Tier | Characters/Month | Concurrent Sessions |
|------|------------------|---------------------|
| Free | 10,000 | 1 |
| Starter | 30,000 | 3 |
| **Pro** | 100,000 | 10 |

**Current Plan**: Pro ($22/month)

### Error Handling

```typescript
try {
  await conversation.startSession({ agentId });
} catch (error) {
  if (error.code === 'RATE_LIMIT_EXCEEDED') {
    // Show user-friendly message
    toast.error('Maya is currently busy. Please try again in a moment.');
  } else if (error.code === 'INVALID_API_KEY') {
    // Log to monitoring
    console.error('Invalid ElevenLabs API key');
  }
}
```

### Best Practices

1. **Session Management** - Always end sessions to avoid orphaned connections
2. **Error Recovery** - Implement reconnection logic for network failures
3. **User Feedback** - Show loading states during voice processing
4. **Privacy** - Don't log sensitive conversation data

### Monitoring

Track usage in ElevenLabs dashboard:
- Characters consumed
- Session duration
- Error rates
- Voice quality metrics

---

## ⛓️ Ethereum & Blockchain

### Sepolia Testnet

**Primary blockchain for loan contracts**

- **Chain ID**: 11155111
- **Explorer**: [sepolia.etherscan.io](https://sepolia.etherscan.io/)
- **Faucets**: 
  - [sepoliafaucet.com](https://sepoliafaucet.com/)
  - [faucets.chain.link](https://faucets.chain.link/)

### RPC Providers

#### Option 1: Infura

- **Website**: [infura.io](https://infura.io/)
- **Tier**: Free (100K requests/day)

```bash
NEXT_PUBLIC_RPC_URL=https://sepolia.infura.io/v3/YOUR_PROJECT_ID
```

#### Option 2: Alchemy

- **Website**: [alchemy.com](https://www.alchemy.com/)
- **Tier**: Free (300M compute units/month)

```bash
NEXT_PUBLIC_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY
```

### Smart Contract

**GreenLend Contract Address** (Sepolia):
```
0xYourContractAddress
```

**ABI**: See `src/lib/greenlend-contract.ts`

### Integration Code

```typescript
// lib/blockchain.ts
import { ethers } from 'ethers';

const provider = new ethers.JsonRpcProvider(
  process.env.NEXT_PUBLIC_RPC_URL
);

const contract = new ethers.Contract(
  process.env.NEXT_PUBLIC_CONTRACT_ADDRESS!,
  GreenLendABI,
  provider
);

// Disburse loan
export async function disburseLoan(
  loanId: string,
  amount: bigint,
  signer: ethers.Signer
): Promise<TransactionResponse> {
  const contractWithSigner = contract.connect(signer);
  return await contractWithSigner.disburseLoan(loanId, { value: amount });
}
```

### Gas Optimization

- **Batch transactions** - Multiple operations in one transaction
- **Gas estimation** - Calculate before sending:
  ```typescript
  const gasEstimate = await contract.disburseLoan.estimateGas(loanId, { value: amount });
  const gasPrice = await provider.getFeeData();
  const totalCost = gasEstimate * gasPrice.gasPrice;
  ```

### Error Handling

```typescript
try {
  const tx = await disburseLoan(loanId, amount, signer);
  await tx.wait(); // Wait for confirmation
} catch (error) {
  if (error.code === 'INSUFFICIENT_FUNDS') {
    toast.error('Insufficient ETH for gas fees');
  } else if (error.code === 'REJECTED') {
    toast.error('Transaction rejected by user');
  } else {
    toast.error('Transaction failed. Please try again.');
  }
}
```

---

## 🔗 Base Network

### Overview

Base is Coinbase's Ethereum L2, used for **LoanChain Ledger integration**.

- **Website**: [base.org](https://base.org/)
- **Chain ID**: 8453
- **Explorer**: [basescan.org](https://basescan.org/)
- **Documentation**: [docs.base.org](https://docs.base.org/)

### Integration with OnchainKit

```typescript
// lib/wagmi.ts
import { base } from 'wagmi/chains';
import { createConfig } from 'wagmi';

export const config = createConfig({
  chains: [base],
  transports: {
    [base.id]: http(process.env.NEXT_PUBLIC_BASE_RPC_URL),
  },
});
```

### LoanChain Bridge

```typescript
// Cross-chain capital allocation
interface BridgeTransaction {
  sourceLoan: string;        // GreenLend Micro loan ID
  destinationPool: string;   // LoanChain pool address
  amount: bigint;
  timestamp: number;
}

export async function bridgeToLoanChain(
  loanId: string,
  amount: bigint
): Promise<TransactionHash> {
  // Implementation
}
```

### Base Features Used

- **Low gas fees** - ~$0.01 per transaction vs ~$1+ on Ethereum mainnet
- **Fast confirmations** - ~2 seconds vs ~12 seconds on Ethereum
- **EVM compatible** - Same smart contract code as Ethereum

---

## 📦 Pinata IPFS

### Overview

Pinata provides **decentralized storage** for loan documents via IPFS.

- **Website**: [pinata.cloud](https://www.pinata.cloud/)
- **Dashboard**: [app.pinata.cloud](https://app.pinata.cloud/)
- **Tier**: Free (1GB storage)

### Use Cases

1. **Loan agreements** - Immutable contract PDFs
2. **Identity documents** - Encrypted KYC files
3. **Business plans** - Supporting documentation
4. **Repayment proofs** - Transaction receipts

### API Configuration

```bash
PINATA_API_KEY=your_api_key
PINATA_SECRET_KEY=your_secret_key
```

### Upload Implementation

```typescript
// lib/ipfs.ts
import axios from 'axios';

export async function uploadToPinata(
  file: File
): Promise<{ ipfsHash: string; url: string }> {
  const formData = new FormData();
  formData.append('file', file);

  const response = await axios.post(
    'https://api.pinata.cloud/pinning/pinFileToIPFS',
    formData,
    {
      headers: {
        'pinata_api_key': process.env.PINATA_API_KEY!,
        'pinata_secret_api_key': process.env.PINATA_SECRET_KEY!,
      },
    }
  );

  return {
    ipfsHash: response.data.IpfsHash,
    url: `https://gateway.pinata.cloud/ipfs/${response.data.IpfsHash}`,
  };
}
```

### Encryption

Sensitive documents are encrypted before upload:

```typescript
import { encrypt } from 'crypto-js/aes';

const encryptedFile = encrypt(fileContent, walletAddress);
await uploadToPinata(encryptedFile);
```

### Rate Limits

| Tier | Requests/Min | Storage |
|------|--------------|---------|
| Free | 30 | 1GB |
| Picnic | 60 | 100GB |
| Submarine | 180 | 1TB |

---

## 🔐 Authentication Services

### Sign-In with Ethereum (SIWE)

**Protocol**: [EIP-4361](https://eips.ethereum.org/EIPS/eip-4361)

**Library**: `siwe` v3.0.0

```typescript
// lib/siwe.ts
import { SiweMessage } from 'siwe';

export async function generateSiweMessage(
  address: string,
  statement: string
): Promise<SiweMessage> {
  return new SiweMessage({
    domain: window.location.host,
    address,
    statement,
    uri: window.location.origin,
    version: '1',
    chainId: 11155111, // Sepolia
  });
}

export async function verifySiweMessage(
  message: SiweMessage,
  signature: string
): Promise<boolean> {
  const result = await message.verify({ signature });
  return result.success;
}
```

### NextAuth.js

**Version**: 4.24.11

**Providers**:
- Credentials (SIWE)

```typescript
// app/api/auth/[...nextauth]/route.ts
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

export const authOptions = {
  providers: [
    CredentialsProvider({
      name: 'Ethereum',
      credentials: {
        message: { label: 'Message', type: 'text' },
        signature: { label: 'Signature', type: 'text' },
      },
      async authorize(credentials) {
        const verified = await verifySiweMessage(
          credentials.message,
          credentials.signature
        );
        return verified ? { id: extractAddress(credentials.message) } : null;
      },
    }),
  ],
};

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };
```

### iron-session

**Version**: 8.0.4

**Purpose**: Encrypted session cookies

```typescript
import { getIronSession } from 'iron-session';

const session = await getIronSession(req, res, {
  password: process.env.IRON_SESSION_PASSWORD!,
  cookieName: 'greenlend_session',
  ttl: 60 * 60 * 24 * 7, // 7 days
});

session.address = walletAddress;
await session.save();
```

---

## 📊 Analytics & Monitoring

### PostHog

**Version**: `posthog-js` v1.242.2

**Features**:
- Event tracking
- User analytics
- Feature flags
- Session recording

```typescript
// app/providers.tsx
import posthog from 'posthog-js';

if (typeof window !== 'undefined') {
  posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY!, {
    api_host: process.env.NEXT_PUBLIC_POSTHOG_HOST,
    loaded: (ph) => {
      if (process.env.NODE_ENV === 'development') {
        ph.opt_out_capturing();
      }
    },
  });
}

// Track events
posthog.capture('loan_application_submitted', {
  amount: 5000,
  term: 12,
});
```

### Custom Logging (Winston)

**Version**: 3.17.0

```typescript
// lib/logger.ts
import winston from 'winston';

export const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'app.log' }),
  ],
});

logger.info('Loan disbursed', { loanId, amount });
logger.error('Contract call failed', { error, loanId });
```

---

## 💰 API Rate Limits & Costs

### Summary Table

| Service | Tier | Rate Limit | Monthly Cost |
|---------|------|------------|--------------|
| **ElevenLabs** | Pro | 100K chars/mo | $22 |
| **Infura** | Free | 100K req/day | $0 |
| **Alchemy** | Free | 300M CU/mo | $0 |
| **Pinata** | Free | 30 req/min | $0 |
| **Vercel** | Hobby | 100GB bandwidth | $0 |
| **PostHog** | Free | 1M events/mo | $0 |

**Total**: ~$22/month

### Rate Limit Handling

```typescript
// Exponential backoff for rate-limited requests
async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3
): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (error.status === 429 && i < maxRetries - 1) {
        const delay = Math.pow(2, i) * 1000; // 1s, 2s, 4s
        await new Promise(resolve => setTimeout(resolve, delay));
      } else {
        throw error;
      }
    }
  }
  throw new Error('Max retries exceeded');
}

// Usage
const result = await retryWithBackoff(() =>
  fetch('/api/elevenlabs/signed-url')
);
```

---

## 🔧 Development & Testing

### Mock Services (for testing)

```typescript
// __mocks__/elevenlabs.ts
export const mockConversation = {
  startSession: jest.fn().mockResolvedValue({
    startRecording: jest.fn(),
    endSession: jest.fn(),
  }),
};

// __tests__/voice-assistant.test.tsx
import { mockConversation } from '@/__mocks__/elevenlabs';

jest.mock('@elevenlabs/client', () => ({
  Conversation: mockConversation,
}));

test('starts conversation on button click', async () => {
  // Test implementation
});
```

### API Testing

```bash
# Test ElevenLabs signed URL
curl https://greenlend.elpeef.com/api/elevenlabs/signed-url

# Test credit scoring
curl -X POST https://greenlend.elpeef.com/api/score \
  -H "Content-Type: application/json" \
  -d '{"amount": 5000, "term": 12, "purpose": "expansion"}'

# Test blockchain transaction
curl https://greenlend.elpeef.com/api/contract-info
```

---

## 📚 Additional Resources

- **ElevenLabs API Docs**: [docs.elevenlabs.io](https://elevenlabs.io/docs)
- **Ethereum JSON-RPC**: [ethereum.org/en/developers/docs/apis/json-rpc](https://ethereum.org/en/developers/docs/apis/json-rpc/)
- **Base Documentation**: [docs.base.org](https://docs.base.org/)
- **Pinata API Reference**: [docs.pinata.cloud](https://docs.pinata.cloud/)
- **SIWE Specification**: [eips.ethereum.org/EIPS/eip-4361](https://eips.ethereum.org/EIPS/eip-4361)

---

## 🆘 Support

**Issues with third-party services?**

1. **Check service status pages**:
   - ElevenLabs: [status.elevenlabs.io](https://status.elevenlabs.io/)
   - Infura: [status.infura.io](https://status.infura.io/)
   - Vercel: [www.vercel-status.com](https://www.vercel-status.com/)

2. **Contact support**:
   - Email: [support@elpeef.com](mailto:support@elpeef.com)
   - Telegram: [@khudriakhmad](https://t.me/khudriakhmad)
   - Discord: [@khudri_61362](https://discord.com/channels/@khudri_61362)

---

**Built with ❤️ using best-in-class APIs for financial inclusion**
