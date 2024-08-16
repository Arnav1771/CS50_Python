# emojize.py

import emoji

def main():
    # Prompt the user for a string
    user_input = input("Input: ")

    # Convert emoji codes and aliases to their corresponding emoji characters
    emojized_string = emoji.emojize(user_input, use_aliases=True)

    # Print the emojized string
    print("Output:", emojized_string)

if __name__ == "__main__":
    main()
