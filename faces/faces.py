def convert(input_string):
    # Replace :) with 🙂
    input_string = input_string.replace(':)', '🙂')
    # Replace :( with 🙁
    input_string = input_string.replace(':(', '🙁')
    return input_string

def main():
    # Prompt the user for input
    user_input = input("")

    # Convert the input string
    converted_input = convert(user_input)

    # Print the converted string
    print(converted_input)

if __name__ == "__main__":
    main()
