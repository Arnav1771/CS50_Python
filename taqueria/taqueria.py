def main():
    # Define the menu
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
        try:
            # Prompt the user for an item
            item = input("Item: ").title()

            # Check if the item is in the menu
            if item in menu:
                total_cost += menu[item]
                # Print the total cost formatted to two decimal places
                print(f"${total_cost:.2f}")
        except EOFError:
            # Print a newline and break the loop when control-d is pressed
            print()
            break

if __name__ == "__main__":
    main()
