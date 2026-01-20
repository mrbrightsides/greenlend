# GreenLend Micro - Setup Guide

Complete setup instructions for running **GreenLend Micro** locally or deploying to production.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Environment Variables](#environment-variables)
4. [Blockchain Setup](#blockchain-setup)
5. [Third-Party API Keys](#third-party-api-keys)
6. [Local Development](#local-development)
7. [Production Deployment](#production-deployment)
8. [Troubleshooting](#troubleshooting)

---

## 🔧 Prerequisites

### Required Software

- **Node.js** 18.x or higher ([Download](https://nodejs.org/))
- **npm** 9.x or **pnpm** 8.x
- **Git** ([Download](https://git-scm.com/))
- **MetaMask** browser extension ([Install](https://metamask.io/))

### Recommended Tools

- **VS Code** with TypeScript and ESLint extensions
- **Postman** or **Thunder Client** for API testing
- **Ethereum wallet** with Sepolia testnet ETH

### System Requirements

- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 500MB free space
- **Network**: Stable internet connection for blockchain interactions

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/mrbrightsides/greenlend.git
cd greenlend
```

### 2. Install Dependencies

Using npm:
```bash
npm install
```

Using pnpm (recommended for faster installs):
```bash
pnpm install
```

### 3. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env.local

# Edit .env.local with your API keys
nano .env.local  # or use your preferred editor
```

### 4. Run Development Server

```bash
npm run dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🔐 Environment Variables

Create a `.env.local` file in the root directory with the following variables:

### Required Variables

```bash
# Application
NEXT_PUBLIC_APP_URL=http://localhost:3000
NODE_ENV=development

# Blockchain - Ethereum Sepolia Testnet
NEXT_PUBLIC_CHAIN_ID=11155111
NEXT_PUBLIC_RPC_URL=https://sepolia.infura.io/v3/YOUR_INFURA_KEY
NEXT_PUBLIC_CONTRACT_ADDRESS=0xYourContractAddress

# ElevenLabs Voice AI
ELEVENLABS_API_KEY=your_elevenlabs_api_key
NEXT_PUBLIC_ELEVENLABS_AGENT_ID=your_agent_id

# Authentication
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your_nextauth_secret_generate_with_openssl

# Session
IRON_SESSION_PASSWORD=your_iron_session_password_min_32_chars
```

### Optional Variables

```bash
# Base Network (for LoanChain integration)
NEXT_PUBLIC_BASE_RPC_URL=https://mainnet.base.org
NEXT_PUBLIC_BASE_CHAIN_ID=8453

# Pinata IPFS (for document storage)
PINATA_API_KEY=your_pinata_api_key
PINATA_SECRET_KEY=your_pinata_secret_key

# Analytics (optional)
NEXT_PUBLIC_POSTHOG_KEY=your_posthog_key
NEXT_PUBLIC_POSTHOG_HOST=https://app.posthog.com

# Logging
LOG_LEVEL=info
```

### Generating Secrets

Generate secure secrets using OpenSSL:

```bash
# Generate NEXTAUTH_SECRET
openssl rand -base64 32

# Generate IRON_SESSION_PASSWORD (minimum 32 characters)
openssl rand -base64 48
```

---

## ⛓️ Blockchain Setup

### 1. MetaMask Configuration

1. **Install MetaMask** from [metamask.io](https://metamask.io/)
2. **Create or import** a wallet
3. **Add Sepolia Testnet**:
   - Network Name: `Sepolia Testnet`
   - RPC URL: `https://sepolia.infura.io/v3/YOUR_INFURA_KEY`
   - Chain ID: `11155111`
   - Currency Symbol: `SepoliaETH`
   - Block Explorer: `https://sepolia.etherscan.io`

### 2. Get Testnet ETH

Get free Sepolia ETH from faucets:
- [Alchemy Sepolia Faucet](https://sepoliafaucet.com/)
- [Infura Sepolia Faucet](https://www.infura.io/faucet/sepolia)
- [Chainlink Faucet](https://faucets.chain.link/)

### 3. Smart Contract Deployment

The GreenLend smart contract is deployed on Sepolia. If you need to deploy your own instance:

```bash
# Set your private key in .env.local (NEVER commit this!)
DEPLOYER_PRIVATE_KEY=your_private_key_with_sepolia_eth

# Deploy contract
npm run deploy:sepolia
```

Contract address will be displayed. Update `NEXT_PUBLIC_CONTRACT_ADDRESS` in `.env.local`.

### 4. Verify Contract (Optional)

```bash
# Verify on Etherscan
npm run verify:sepolia -- --contract-address 0xYourContractAddress
```

---

## 🔑 Third-Party API Keys

### ElevenLabs (Voice AI)

1. **Sign up** at [elevenlabs.io](https://elevenlabs.io/)
2. **Navigate to Profile** → **API Keys**
3. **Generate a new API key**
4. **Create a Conversational AI agent**:
   - Go to **Conversational AI** tab
   - Click **Create Agent**
   - Configure Maya's personality and prompts
   - Copy the **Agent ID**
5. **Add to `.env.local`**:
   ```bash
   ELEVENLABS_API_KEY=sk_...
   NEXT_PUBLIC_ELEVENLABS_AGENT_ID=agent_...
   ```

### Infura (Ethereum RPC)

1. **Sign up** at [infura.io](https://infura.io/)
2. **Create a new project**
3. **Select Ethereum** → **Sepolia**
4. **Copy the API endpoint**
5. **Add to `.env.local`**:
   ```bash
   NEXT_PUBLIC_RPC_URL=https://sepolia.infura.io/v3/YOUR_PROJECT_ID
   ```

### Pinata (IPFS Storage) - Optional

1. **Sign up** at [pinata.cloud](https://www.pinata.cloud/)
2. **Navigate to API Keys**
3. **Generate new key** with admin permissions
4. **Add to `.env.local`**:
   ```bash
   PINATA_API_KEY=your_api_key
   PINATA_SECRET_KEY=your_secret_key
   ```

### Alchemy (Alternative RPC) - Optional

1. **Sign up** at [alchemy.com](https://www.alchemy.com/)
2. **Create app** on Sepolia network
3. **Copy HTTPS endpoint**
4. **Update `.env.local`**:
   ```bash
   NEXT_PUBLIC_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
   ```

---

## 💻 Local Development

### Running the Development Server

```bash
# Standard mode
npm run dev

# With custom port
npm run dev -- -p 3001

# With turbo (faster rebuilds)
npm run dev -- --turbo
```

### File Structure

```
greenlend/
├── src/
│   ├── app/                    # Next.js app directory
│   │   ├── page.tsx            # Landing page
│   │   ├── borrower/           # Borrower dashboard
│   │   ├── lender/             # Lender dashboard
│   │   └── api/                # API routes
│   ├── components/             # React components
│   │   ├── borrower/           # Borrower-specific
│   │   ├── lender/             # Lender-specific
│   │   └── ui/                 # Shared UI components
│   ├── contexts/               # React contexts
│   ├── hooks/                  # Custom React hooks
│   ├── lib/                    # Utility libraries
│   └── utils/                  # Helper functions
├── public/                     # Static assets
├── .env.local                  # Environment variables (create this)
└── package.json                # Dependencies
```

### Development Commands

```bash
# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linter
npm run lint

# Type check
npx tsc --noEmit

# Format code (if prettier is configured)
npm run format
```

### Hot Reload

Next.js supports hot module replacement (HMR):
- **Save any file** → changes reflect immediately
- **No manual refresh** needed
- **Fast Refresh** preserves React state

### Debugging

#### Browser DevTools

1. Open Chrome DevTools (F12)
2. Navigate to **Sources** tab
3. Set breakpoints in your code
4. Inspect network requests in **Network** tab

#### VS Code Debugging

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: debug server-side",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev"
    },
    {
      "name": "Next.js: debug client-side",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000"
    }
  ]
}
```

---

## 🚢 Production Deployment

### Vercel (Recommended)

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel --prod
   ```

4. **Set environment variables** in Vercel dashboard:
   - Go to **Settings** → **Environment Variables**
   - Add all variables from `.env.local`
   - Ensure secrets are marked as **Sensitive**

### Environment Variables in Vercel

**Important**: Update these for production:

```bash
NEXT_PUBLIC_APP_URL=https://greenlend.elpeef.com
NODE_ENV=production
NEXTAUTH_URL=https://greenlend.elpeef.com
```

### Custom Domain

1. **Add domain** in Vercel dashboard
2. **Configure DNS** with your registrar:
   ```
   Type: CNAME
   Name: greenlend
   Value: cname.vercel-dns.com
   ```
3. **Wait for SSL** certificate provisioning (automatic)

### Build Optimization

```bash
# Analyze bundle size
npm run build
# Check .next/analyze output

# Optimize images
# Next.js automatically optimizes images via next/image
```

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "Module not found" errors

**Solution**:
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

#### Issue: MetaMask not connecting

**Solution**:
1. Ensure Sepolia network is added to MetaMask
2. Check `NEXT_PUBLIC_CHAIN_ID` matches `11155111`
3. Clear browser cache and reconnect wallet

#### Issue: ElevenLabs voice not playing

**Solution**:
1. Verify `ELEVENLABS_API_KEY` is correct
2. Check browser console for CORS errors
3. Ensure microphone permissions are granted
4. Test API key with ElevenLabs dashboard

#### Issue: Smart contract calls failing

**Solution**:
1. Verify contract address in `.env.local`
2. Ensure you have Sepolia ETH in your wallet
3. Check RPC URL is working: `curl $NEXT_PUBLIC_RPC_URL`
4. View transaction details on [Sepolia Etherscan](https://sepolia.etherscan.io/)

#### Issue: Build fails with TypeScript errors

**Solution**:
```bash
# Check for type errors
npx tsc --noEmit

# Fix common issues:
# - Missing type definitions
# - Incorrect prop types
# - Untyped imports
```

#### Issue: API routes returning 500 errors

**Solution**:
1. Check server logs in terminal
2. Verify environment variables are loaded
3. Test API endpoints with Postman
4. Enable debug logging:
   ```bash
   LOG_LEVEL=debug npm run dev
   ```

### Getting Help

If you encounter issues not covered here:

1. **Check existing issues**: [GitHub Issues](https://github.com/mrbrightsides/greenlend/issues)
2. **Create a new issue** with:
   - Error message
   - Steps to reproduce
   - Environment details (OS, Node version, etc.)
3. **Contact support**:
   - Email: [support@elpeef.com](mailto:support@elpeef.com)
   - Telegram: [@khudriakhmad](https://t.me/khudriakhmad)
   - Discord: [@khudri_61362](https://discord.com/channels/@khudri_61362)

### Performance Optimization

#### Slow Development Server

```bash
# Use pnpm instead of npm
npm i -g pnpm
pnpm install

# Enable SWC minification in next.config.js
# (already enabled by default in Next.js 15)
```

#### Large Bundle Size

```bash
# Analyze bundle
npm run build

# Check for:
# - Unused dependencies in package.json
# - Large third-party libraries
# - Unoptimized images

# Use dynamic imports for heavy components
import dynamic from 'next/dynamic';
const HeavyComponent = dynamic(() => import('./HeavyComponent'));
```

---

## 📚 Additional Resources

- **Next.js Documentation**: [nextjs.org/docs](https://nextjs.org/docs)
- **ElevenLabs Docs**: [elevenlabs.io/docs](https://elevenlabs.io/docs)
- **Ethereum Sepolia**: [sepolia.dev](https://sepolia.dev/)
- **wagmi Documentation**: [wagmi.sh](https://wagmi.sh/)
- **RainbowKit Docs**: [rainbowkit.com](https://www.rainbowkit.com/)

---

## ✅ Setup Checklist

- [ ] Node.js 18+ installed
- [ ] Repository cloned
- [ ] Dependencies installed (`npm install`)
- [ ] `.env.local` created with all required variables
- [ ] MetaMask installed and configured for Sepolia
- [ ] Sepolia testnet ETH obtained
- [ ] ElevenLabs API key added
- [ ] Development server running (`npm run dev`)
- [ ] App accessible at `http://localhost:3000`
- [ ] Wallet connection working
- [ ] Voice assistant (Maya) responding

---

**Need help?** Contact us at [support@elpeef.com](mailto:support@elpeef.com) or via [Telegram](https://t.me/khudriakhmad).

**Built with ❤️ for financial inclusion**
