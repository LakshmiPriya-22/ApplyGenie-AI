from app.utils.security import hash_password, verify_password

password = "Renuka@123"

hashed = hash_password(password)

print("Original Password :", password)
print("Hashed Password   :", hashed)
print("Password Match    :", verify_password(password, hashed))