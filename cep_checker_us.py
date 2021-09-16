import requests


def main():
    print("#" * 30)
    print("#" * 7, " Zip Code Checker ", "#" * 7)
    print("#" * 30, "\n")

    while 1:
        zip_code = input("Type the Zip Code for search: ")

        if len(zip_code) == 5:
            break
        print("Invalid digit quantity")

    request = requests.get("api.zippopotam.us/us/{}".format(zip_code))

    address_data = request.json()

    if "erro" not in address_data:
        print("### Zip Code Found ###")
        print("CEP: {}".format(address_data["post code"]))
        print("Country: {}".format(address_data["country"]))
        print("State: {}".format(address_data["places"]["state"]))
        print("State Abbreviation: {}".format(
            address_data["places"]["state abbreviation"]))
        print("Place: {}".format(address_data["places"]["place name"]))
    else:
        print("{}: Invalid Zip Code".format(zip_code))

    option = int(
        input("Do you want to make a new search?? \n1. Yes\n2. Exit\n"))
    if option == 1:
        main()
    else:
        print("Quitting...")


if __name__ == "__main__":
    main()
