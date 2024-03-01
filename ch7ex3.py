airport_data = {}
while True:
    print("Choose any Option :")
    print("1. Enter a new airport")
    print("2. Fetch information of an existing airport")
    print("3. Quit")

    choice = input("Enter your choice mentioned above: ")

    if choice == '1':
        icao = input("Enter the ICAO code of the airport: ")
        name = input("Enter the name of the airport: ")
        airport_data[icao] = name
        print("Airport added successfully.")
    elif choice == '2':
        icao = input("Enter the ICAO code of the airport: ")
        if icao in airport_data:
            print(f"The name of the airport with ICAO code {icao} is {airport_data[icao]}.")
        else:
            print("Airport not found.")
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")