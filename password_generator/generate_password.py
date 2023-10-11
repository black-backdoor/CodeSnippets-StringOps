import secrets
import string
import sys

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

def generate_password(pwd_length):
    # generate password meeting constraints
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        if (sum(char in special_chars for char in pwd) > pwd_length / 10 and
                any(char in digits for char in pwd)):
            break
    return pwd

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_password.py <pwd_length>")
        sys.exit(1)

    pwd_length = int(sys.argv[1])
    password = generate_password(pwd_length)
    print(password)
