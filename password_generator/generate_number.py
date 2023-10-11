import secrets
import string
import sys

# define the alphabet
digits = string.digits

def generate_password(pwd_length):
    # generate password meeting constraints
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(digits))
        if not (pwd.startswith("0")):
            break
    return pwd

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_password.py <pwd_length>")
        sys.exit(1)

    pwd_length = int(sys.argv[1])
    password = generate_password(pwd_length)
    print(password)
