import random

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def encode(string):
    result = [ord(char)-65 if 65<=ord(char)<=90 else ord(char)-22 for char in string]
    return result
def decode(string):
    result = [chr(int(char)+65) if int(char)<=25 else chr(int(char)+22) for char in string]
    return result

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [((char ** key) % n) for char in ciphertext]
    plain = decode(plain)
    #Return the array of bytes as a string
    return ''.join(plain)

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    plaintext = encode(plaintext)
    cipher = [(int(char) ** key) % n for char in plaintext]
    return cipher

def get_private_key(e, tot):
    d=1
    while (e*d)%tot != 1 or d == e:
        d+=1
    return d

def get_public_key(tot):
    e=2
    e_li = []
    while e<tot:
        #  e와 totient가 서로수일경우
        if gcd(e, tot) == 1:
            e_li.append(e)
        e += 1
    lg = random.randrange(0,len(e_li))
    print(e_li, e_li[lg])
    return e_li[lg]
    

# Input message to be encrypted
m = input("Enter the text to be encrypted:")
print(m)

# Step 1. Choose two prime numbers
p = 3
q = 5

print("Two prime numbers(p and q) are:", str(p), "and", str(q))

# Step 2. Compute n = pq which is the modulus of both the keys
n = p * q
print("n(p*q)=", str(p), "*", str(q), "=", str(n))

# Step 3. Calculate totient
totient = (p-1)*(q-1)
print("(p-1)*(q-1)=", str(totient))

# Step 4. Find public key e
e = get_public_key(totient)
print("Public key(n, e):("+str(n)+","+str(e)+")")

# Step 5. Find private key d
d = get_private_key(e, totient)
print("Private key(n, d):("+str(n)+","+str(d)+")")

# Step 6.Encrypt message
encrypted_msg = encrypt((e,n), m)
print('Encrypted Message:', ''.join(map(lambda x: str(x), encrypted_msg)))

print('Decrypted Message:', decrypt((d,n),encrypted_msg))
