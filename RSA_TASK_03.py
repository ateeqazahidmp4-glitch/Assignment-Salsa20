from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# Step 1: Generate RSA key pair
print("=== Step 1: Generate 2048-bit RSA Keys ===")
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()
print(f"Key size: {key.size_in_bits()} bits")

# Step 2: Original message
original_msg = "Transfer $2000 to account Y"
print(f"\n=== Step 2: Original Message ===")
print(f"Message: '{original_msg}'")

# Step 3: Create digital signature
print(f"\n=== Step 3: Create Signature ===")
hash_obj = SHA256.new(original_msg.encode())
signer = pkcs1_15.new(private_key)
signature = signer.sign(hash_obj)
print(f"SHA256 hash: {hash_obj.hexdigest()}")
print(f"Signature (hex): {binascii.hexlify(signature).decode()[:50]}...")

# Step 4: Verify original signature (should succeed)
print(f"\n=== Step 4: Verify Original ===")
try:
    verifier = pkcs1_15.new(public_key)
    verifier.verify(SHA256.new(original_msg.encode()), signature)
    print("✓ Signature VALID")
except:
    print("✗ Signature INVALID")

# Step 5: Modify message and show verification fails
print(f"\n=== Step 5: Test with Modified Message ===")
modified_msg = "Transfer $5000 to account X"
print(f"Original: '{original_msg}'")
print(f"Modified: '{modified_msg}'")

try:
    verifier = pkcs1_15.new(public_key)
    verifier.verify(SHA256.new(modified_msg.encode()), signature)
    print("✗ ERROR: Signature verified (should fail!)")
except:
    print("✓ CORRECT: Signature verification failed")
    print("  (Any change to message breaks the signature)")