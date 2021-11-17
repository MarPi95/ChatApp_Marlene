import hashlib

password = "12345"

pw="123"
hashed_password = hashlib.sha256(password.encode()).hexdigest()

hashed_password1 = hashlib.sha256(pw.encode()).hexdigest()

print(hashed_password)
print(hashed_password1)