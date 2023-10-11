import argparse

def caesar_encrypt(string, shift):
    result = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description="Caesar encrypt a given string with a specified shift.")
    parser.add_argument("string", help="The string to encrypt.")
    parser.add_argument("shift", type=int, help="The Caesar cipher shift value.")
    args = parser.parse_args()

    encrypted_string = caesar_encrypt(args.string, args.shift)
    print(encrypted_string)

if __name__ == "__main__":
    main()
