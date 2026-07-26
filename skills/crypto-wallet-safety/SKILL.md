---
name: crypto-wallet-safety
description: Guide users through safe crypto wallet operations and detect common scams
version: 1.0.0
metadata:
  hermes:
    tags: [crypto, security, web3]
    category: security
---

# Crypto Wallet Safety

## When to Use
Use this when the user mentions sending crypto, connecting a wallet, signing a transaction, or interacting with a smart contract.

## Procedure
1. Ask the user what action they are about to take (send, connect, sign, swap).
2. If sending: ask them to verify the recipient address character-by-character. Warn about clipboard hijacking.
3. If connecting: ask what site/app is requesting the connection. Check if it's a known phishing domain.
4. If signing: explain exactly what the signature authorizes. Warn if it's an "approve all" or unlimited token allowance.
5. If swapping: verify the token contract address on a block explorer (Etherscan, etc.).

## Pitfalls
- **Clipboard hijacking**: Malware swaps copied addresses. Always verify the first and last 6 characters visually.
- **Fake block explorers**: Scammers create lookalike sites. Only use etherscan.io, bscscan.com, etc.
- **Unlimited approvals**: Never sign "approve for all" unless it's a trusted DEX. Use limited amounts.
- **Gasless signatures**: Some scams use gasless signatures to drain wallets without a transaction. Never sign raw messages you don't understand.

## Verification
Ask the user to confirm they have double-checked the address/contract before proceeding.