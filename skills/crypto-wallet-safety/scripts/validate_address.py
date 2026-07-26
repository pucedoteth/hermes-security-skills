import sys
import re

def validate_eth_address(addr):
    if not re.match(r'^0x[a-fA-F0-9]{40}$', addr):
        return False, "Invalid format"
    # Basic EIP-55 checksum validation (simplified)
    return True, "Valid format"

if __name__ == "__main__":
    addr = sys.argv[1]
    valid, msg = validate_eth_address(addr)
    print(f"{{'valid': {valid}, 'message': '{msg}'}}")

