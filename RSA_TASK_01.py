import random

def is_prime(n):
    """Simple primality test"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    """Generate two different small primes"""
    primes = [p for p in range(50, 150) if is_prime(p)]
    p = random.choice(primes)
    q = random.choice(primes)
    
    while p == q:   # ensure p and q are different
        q = random.choice(primes)
    
    return p, q

def gcd(a, b):
    """Greatest Common Divisor"""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Find d where (d * e) % phi == 1"""
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keys():
    """Generate RSA keys manually"""
    
    # 1. Choose two primes
    p, q = generate_primes()
    print(f"Primes chosen: p = {p}, q = {q}")
    
    # 2. Compute n and φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"n = {n}, φ(n) = {phi}")
    
    # 3. Choose e such that gcd(e, phi)=1
    possible_e = [3, 5, 7, 11, 13, 17, 19]
    e = random.choice(possible_e)
    
    while gcd(e, phi) != 1:
        e = random.choice(possible_e)
    
    # 4. Compute d = modular inverse of e
    d = mod_inverse(e, phi)
    
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")
    
    return (e, n), (d, n)

def encrypt(message, public_key):
    """Encrypt message using RSA"""
    e, n = public_key
    encrypted = []
    
    for ch in message:
        m = ord(ch)               # convert to ASCII
        c = pow(m, e, n)          # m^e mod n
        encrypted.append(c)
    
    return encrypted

def decrypt(encrypted, private_key):
    """Decrypt RSA ciphertext"""
    d, n = private_key
    decrypted = ""
    
    for c in encrypted:
        m = pow(c, d, n)          # c^d mod n
        decrypted += chr(m)       # back to character
    
    return decrypted


# ===================== MAIN PROGRAM =====================

print("\n=== SIMPLE RSA DEMO ===\n")

# 1. Generate RSA keys
public_key, private_key = generate_keys()

# 2. Test on your name "ATTIQA"
print("\n--- Testing on Your Name ---")
name = "ATTIQA"
print(f"Original message: {name}")

encrypted = encrypt(name, public_key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, private_key)
print("Decrypted:", decrypted)

# Show RSA math for the first letter
print("\n--- RSA Math for first letter 'A' ---")
e, n = public_key
d, _ = private_key

m = ord('A')
c = pow(m, e, n)

print(f"A = ASCII {m}")
print(f"Encrypt: {m}^{e} mod {n} = {c}")
print(f"Decrypt: {c}^{d} mod {n} = {pow(c, d, n)}")