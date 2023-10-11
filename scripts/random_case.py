import random
import sys

def random_case(string):
    result = ''
    for char in string:
        if random.randint(0, 1) == 0:
            result += char.lower()
        else:
            result += char.upper()
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python random_case.py <string>")
        sys.exit(1)

    string = sys.argv[1]
    randomized = random_case(string)
    print(randomized)
