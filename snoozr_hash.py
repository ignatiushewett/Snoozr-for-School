import bcrypt

password = input("Enter a password: ")

password_bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password_bytes, salt)

print(f"\nSalt:   {salt.decode('utf-8')}")
print(f"Hash:   {hashed.decode('utf-8')}")
