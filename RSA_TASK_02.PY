# Import required libraries from PyCryptodome
from Crypto.PublicKey import RSA      # For RSA key generation
from Crypto.Cipher import PKCS1_OAEP  # For secure RSA encryption with padding
import binascii                       # For converting binary to hexadecimal

# Generate 2048-bit RSA key pair
# RSA.generate() creates both public and private keys
key = RSA.generate(2048)          # 2048 bits = secure key size
public_key = key.publickey()      # Extract public key (e, n)
private_key = key                 # Keep private key (d, n, p, q)

print("=== 2048-bit RSA Key Pair Generated ===")
print(f"Key Size: {key.size_in_bits()} bits")  # Should show 2048

# Message to encrypt
message = "Hello, Attiqa!"  # <-- Message changed here

# ENCRYPTION: Convert message to ciphertext using public key
cipher = PKCS1_OAEP.new(public_key)        # Create cipher with OAEP padding
encrypted = cipher.encrypt(message.encode())  # Encrypt message (string → bytes)
hex_encrypted = binascii.hexlify(encrypted).decode()  # Convert bytes to hex string

print(f"\nOriginal: '{message}'")
print(f"Encrypted (hex): {hex_encrypted[:50]}...")  # Show first 50 hex chars

# DECRYPTION: Convert ciphertext back to message using private key
cipher = PKCS1_OAEP.new(private_key)      # Create cipher with private key
decrypted = cipher.decrypt(encrypted).decode()  # Decrypt and convert bytes → string

print(f"\nDecrypted: '{decrypted}'")
print(f"Success: {message == decrypted}")  # Verify encryption/decryption worked


