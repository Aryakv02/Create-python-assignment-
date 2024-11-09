
def sort_dictionary_by_keys(input_dict):
    return dict(sorted(input_dict.items()))

def main():

    num_items = int(input("Enter number of items in dictionary: "))
    input_dict = {}
    
    for i in range(num_items):
        key = input(f"Enter key {i+1}: ")
        value = input(f"Enter value for key '{key}': ")
        input_dict[key] = value


    sorted_dict = sort_dictionary_by_keys(input_dict)


    print("\nSorted Dictionary:")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()


