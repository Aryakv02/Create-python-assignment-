def has_unique_chars(input_str):

    input_str = input_str.replace(" ", "").lower()
    

    return len(input_str) == len(set(input_str))

def main():
    input_str = input("Enter a string: ")
    result = has_unique_chars(input_str)
    print(result)

if __name__ == "__main__":
    main()