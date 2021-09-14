import sys

import requests


def main():
    print("#" * 30)
    print("#" * 7, " Consulta CEP ", "#" * 7)
    print("#" * 30, "\n")

<<<<<<< HEAD
    while 1:
        cep = input("Digite o CEP para a consulta: ")

        if len(cep) == 8:
            break
        print("Quantidade de Dígitos Inválida")
=======
    cep = input("Digite o CEP para a consulta: ")

    if len(cep) != 8:
        print("Quantidade de Dígitos Inválida")
        exit()
>>>>>>> c7b906a92d9008c8ddf2c2789c393761ed0cd0db

    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

    address_data = request.json()

<<<<<<< HEAD
    if "erro" not in address_data:
        print("### CEP ENCONTRADO ###")
        print("CEP: {}".format(address_data["cep"]))
        print("Logradouro: {}".format(address_data["logradouro"]))
        print("Complemento: {}".format(address_data["complemento"]))
        print("Bairro: {}".format(address_data["bairro"]))
        print("Cidade: {}".format(address_data["localidade"]))
        print("Estado: {}".format(address_data["uf"]))
=======
    if "erro" not in addressData:
        print("### CEP ENCONTRADO ###")
        print("CEP: {}".format(addressData["cep"]))
        print("Logradouro: {}".format(addressData["logradouro"]))
        print("Complemento: {}".format(addressData["complemento"]))
        print("Bairro: {}".format(addressData["bairro"]))
        print("Cidade: {}".format(addressData["localidade"]))
        print("Estado: {}".format(addressData["uf"]))
>>>>>>> c7b906a92d9008c8ddf2c2789c393761ed0cd0db

    else:
        print("{}: CEP Inválido".format(cep))

<<<<<<< HEAD
    option = int(input("Deseja realizar uma nova consulta? \n1. Sim\n2. Sair\n"))
=======
    option = int(
        input("Deseja realizar uma nova consulta? \n1. Sim\n2. Sair\n"))
>>>>>>> c7b906a92d9008c8ddf2c2789c393761ed0cd0db
    if option == 1:
        main()
    else:
        print("Saindo...")


if __name__ == "__main__":
    main()
