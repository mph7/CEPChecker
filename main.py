import requests

def main():
    print('#'*30)
    print('#'*7, ' Consulta CEP ', '#'*7)
    print('#'*30,'\n')

    cep = input('Digite o CEP para a consulta: ')

    if len(cep) != 8:
        print('Quantidade de Dígitos Inválida')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    addressData = request.json()

    if 'erro' not in addressData:
        print('### CEP ENCONTRADO ###')
        print('CEP: {}'.format(addressData['cep']))
        print('Logradouro: {}'.format(addressData['logradouro']))
        print('Complemento: {}'.format(addressData['complemento']))
        print('Bairro: {}'.format(addressData['bairro']))
        print('Cidade: {}'.format(addressData['localidade']))
        print('Estado: {}'.format(addressData['uf']))

    else:
        print('{}: CEP Inválido'.format(cep))

    option = int(input('Deseja realizar uma nova consulta? \n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')


if __name__ == '__main__':
    main()
