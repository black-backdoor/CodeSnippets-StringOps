import argparse

def get_every_nth_letter(input_string, n):
    result = ""
    for i in range(0, len(input_string), n):
        result += input_string[i]
    return result

def get_all_every_nth_letter(input_string, n):
    result = []
    for i in range(n):
        result.append(get_every_nth_letter(input_string, n))
        if len(input_string) > 1:
            input_string = input_string[1:]
    return result

def main():
    parser = argparse.ArgumentParser(description="Extract every nth letter from a string.")
    parser.add_argument("input_string", help="The input string from which to extract characters.")
    parser.add_argument("n", type=int, help="The value of n for character extraction.")
    args = parser.parse_args()

    result = get_all_every_nth_letter(args.input_string, args.n)
    print(result)

if __name__ == "__main__":
    main()
