
def main():
    c = 300000000

    mass = int(input("m: "))

    # Calculate the energy using E = mc^2
    energy = mass * c**2

    # Output the energy in Joules
    print(energy)

if __name__ == "__main__":
    main()
