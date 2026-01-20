# Contributing to GreenLend Micro

Welcome to **GreenLend Micro** - the voice-powered microfinance platform that bridges institutional capital with grassroots lending through transparent, SDG-native scoring.

We're building the future of ethical, transparent, and inclusive finance as part of the **LoanChain Ledger ecosystem**.

---

## 🌐 Project Links

- **Live Demo**: [https://greenlend.elpeef.com](https://greenlend.elpeef.com)
- **GitHub Repository**: [https://github.com/mrbrightsides/greenlend](https://github.com/mrbrightsides/greenlend)
- **LoanChain Ledger Platform**: [https://loanchain.elpeef.com](https://loanchain.elpeef.com)
- **Contact**: [support@elpeef.com](mailto:support@elpeef.com)
- **Telegram**: [@khudriakhmad](https://t.me/khudriakhmad)
- **Discord**: [@khudri_61362](https://discord.com/channels/@khudri_61362)

---

## 📖 Table of Contents

1. [About the Project](#about-the-project)
2. [Key Features & Innovations](#key-features--innovations)
3. [Getting Started](#getting-started)
4. [Development Workflow](#development-workflow)
5. [Code Standards](#code-standards)
6. [Architecture Overview](#architecture-overview)
7. [Testing](#testing)
8. [Submitting Changes](#submitting-changes)
9. [Community Guidelines](#community-guidelines)

---

## 🎯 About the Project

**GreenLend Micro** is a voice-powered microfinance platform designed for MSMEs (Micro, Small, and Medium Enterprises) with a focus on:

- **SDG-native credit scoring** - Transparent, ethical assessment aligned with UN Sustainable Development Goals
- **Voice-first UX** - Conversational loan applications via Maya, our AI assistant powered by ElevenLabs
- **Blockchain transparency** - All transactions verified on Ethereum Sepolia testnet and Base network
- **Rejection with Dignity** - Actionable improvement pathways for declined applicants
- **Score Decomposition Dashboard** - Full formula transparency for credit decisions
- **LoanChain Integration** - Bridge to the $6+ trillion syndicated loan market

### Part of LoanChain Ledger Ecosystem

GreenLend Micro serves as the **microfinance layer** within LoanChain Ledger's shared control plane, enabling:
- Real-time risk monitoring across institutional and grassroots lending
- IPFS-based decentralized document storage via Pinata
- 40% operational cost reduction through blockchain automation
- Seamless capital flow from syndicated loans to microfinance

---

## 🚀 Key Features & Innovations

### 1. **Maya - Voice AI Assistant**
- Powered by **ElevenLabs SDK v0.13.0**
- Real-time conversational signing and intent classification
- Entity extraction from natural language loan applications
- Structured interaction prompting for guided applications

### 2. **Score Decomposition Dashboard**
- Transparent credit formula breakdown
- Real-time visualization of scoring factors
- Educational tooltips for each component
- Complete auditability for borrowers

### 3. **Rejection with Dignity**
- Personalized improvement recommendations
- Actionable steps to qualify for future loans
- Educational resources aligned with SDGs
- Compassionate UX design

### 4. **Blockchain Verification**
- Ethereum Sepolia testnet integration
- Base network for institutional bridge
- IPFS storage via Pinata for loan documents
- Real-time transaction tracking

### 5. **Multi-language Support**
- English and Bahasa Indonesia
- Cultural sensitivity in financial messaging
- Localized educational content

---

## 🛠️ Getting Started

### Prerequisites

- **Node.js** 18.x or higher
- **npm** or **pnpm** package manager
- **Git** for version control
- **MetaMask** or compatible Web3 wallet for blockchain testing

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/mrbrightsides/greenlend.git
cd greenlend

# Install dependencies
npm install
# or
pnpm install

# Set up environment variables (see SETUP.md for details)
cp .env.example .env.local

# Run development server
npm run dev
```

Visit `http://localhost:3000` to see the app running.

For detailed setup instructions, see **[SETUP.md](./SETUP.md)**.

---

## 💻 Development Workflow

### Branch Strategy

We use a simplified Git workflow:

- **`main`** - Production-ready code (protected)
- **`develop`** - Integration branch for features
- **`feature/*`** - Individual feature branches
- **`fix/*`** - Bug fix branches
- **`docs/*`** - Documentation updates

### Creating a Feature Branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### Making Changes

1. **Follow code standards** (see below)
2. **Write clear commit messages**
   ```
   feat: add SDG impact scoring to credit algorithm
   fix: resolve Maya voice playback issue on mobile
   docs: update API documentation for score endpoint
   ```
3. **Test thoroughly** before committing
4. **Update relevant documentation**

### Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

---

## 📏 Code Standards

### TypeScript

- **Strict mode enabled** - No implicit `any` types
- **Explicit typing** for all functions and variables
- **Interface definitions** for complex types
- **Type imports** using `import type` syntax

```typescript
// ✅ Good
interface LoanApplication {
  amount: number;
  term: number;
  purpose: string;
}

const processLoan = async (application: LoanApplication): Promise<boolean> => {
  // implementation
};

// ❌ Bad
const processLoan = async (application: any) => {
  // implementation
};
```

### React Components

- **Functional components** with hooks
- **TypeScript interfaces** for props
- **Client components** marked with `'use client'` directive
- **Proper error boundaries** for API calls

```typescript
'use client';

import type { FC } from 'react';

interface LoanCardProps {
  amount: number;
  status: 'pending' | 'approved' | 'rejected';
}

const LoanCard: FC<LoanCardProps> = ({ amount, status }) => {
  return (
    <div className="p-4 border rounded">
      {/* component content */}
    </div>
  );
};

export default LoanCard;
```

### Styling

- **Tailwind CSS** for all styling
- **Mobile-first** responsive design
- **Dark mode support** where applicable
- **Accessibility** - WCAG 2.1 AA compliance

### API Routes

- **RESTful conventions**
- **Proper error handling** with status codes
- **Type-safe request/response** interfaces
- **Server-side validation** using Zod

```typescript
import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';
import { z } from 'zod';

const LoanSchema = z.object({
  amount: z.number().positive(),
  term: z.number().min(1).max(60),
});

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    const body = await request.json();
    const validated = LoanSchema.parse(body);
    
    // Process loan
    
    return NextResponse.json({ success: true });
  } catch (error) {
    return NextResponse.json(
      { error: 'Invalid request' },
      { status: 400 }
    );
  }
}
```

---

## 🏗️ Architecture Overview

GreenLend Micro is built on a modern, scalable architecture:

### Technology Stack

- **Frontend**: Next.js 15.3.8, React 19, TypeScript 5.8
- **Styling**: Tailwind CSS 4.1, shadcn/ui components
- **Blockchain**: ethers.js, wagmi, RainbowKit, OnchainKit
- **Voice AI**: ElevenLabs SDK v0.13.0
- **Authentication**: SIWE (Sign-In with Ethereum), NextAuth
- **State Management**: React Context API
- **API Layer**: Next.js API Routes

### Key Architectural Patterns

1. **Context-based State Management** - `AuthContext`, `DataContext`, `MayaContext`, `LanguageContext`
2. **Server Components** - Default for optimal performance
3. **API Route Handlers** - Centralized in `/src/app/api`
4. **Blockchain Abstraction** - Contract adapters in `/src/lib`
5. **Component Library** - Reusable UI components in `/src/components/ui`

For detailed architecture documentation, see **[ARCHITECTURE.md](./ARCHITECTURE.md)**.

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

### Testing Guidelines

1. **Unit Tests** - For utility functions and business logic
2. **Component Tests** - For React components
3. **Integration Tests** - For API routes and blockchain interactions
4. **E2E Tests** - For critical user flows

### Test Coverage Goals

- **Minimum 80%** code coverage
- **100%** coverage for credit scoring algorithm
- **Critical paths** must have integration tests

---

## 📤 Submitting Changes

### Pull Request Process

1. **Create a feature branch** from `develop`
2. **Make your changes** following code standards
3. **Write/update tests** for your changes
4. **Update documentation** if needed
5. **Commit with conventional messages**
6. **Push to your fork**
7. **Open a Pull Request** to `develop` branch

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows project standards
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### Code Review Process

- **At least one approval** required
- **All CI checks** must pass
- **Resolve all comments** before merging
- **Squash commits** for clean history

---

## 🤝 Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment:

1. **Be respectful** - Treat everyone with respect and consideration
2. **Be collaborative** - Work together towards common goals
3. **Be professional** - Maintain professionalism in all interactions
4. **Be inclusive** - Welcome diverse perspectives and backgrounds
5. **Focus on impact** - Prioritize solutions that benefit MSMEs and underserved communities

### Getting Help

- **Documentation**: Check [SETUP.md](./SETUP.md), [ARCHITECTURE.md](./ARCHITECTURE.md), and [THIRD_PARTY_APIs.md](./THIRD_PARTY_APIs.md)
- **Issues**: Search existing issues or create a new one
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Email**: [support@elpeef.com](mailto:support@elpeef.com)
- **Telegram**: [@khudriakhmad](https://t.me/khudriakhmad)
- **Discord**: [@khudri_61362](https://discord.com/channels/@khudri_61362)

### Reporting Bugs

Use the bug report template when creating issues:

```markdown
**Describe the bug**
Clear description of the bug

**To Reproduce**
Steps to reproduce the behavior

**Expected behavior**
What you expected to happen

**Screenshots**
If applicable

**Environment**
- OS: [e.g. macOS, Windows]
- Browser: [e.g. Chrome, Safari]
- Version: [e.g. 1.0.0]
```

---

## 🌟 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **Project documentation**

---

## 📜 License

This project is part of the LoanChain Ledger ecosystem, built for the LMA Edge Hackathon 2026.

---

## 🙏 Thank You

Thank you for contributing to GreenLend Micro! Together, we're building a more transparent, inclusive, and sustainable financial future for MSMEs worldwide.

For questions or support, reach out via:
- Email: [support@elpeef.com](mailto:support@elpeef.com)
- Telegram: [@khudriakhmad](https://t.me/khudriakhmad)
- Discord: [@khudri_61362](https://discord.com/channels/@khudri_61362)

---

**Built with ❤️ for financial inclusion and sustainability**
