class game:
    def __init__(self, name, price, yearLaunch):
        self.name = name
        self.price = price
        self.yearLaunch = yearLaunch


def readParameters(option):
    parameters = {}

    if option == 1:
        name = input("Insira o nome do jogo: ")
        parameters['name'] = name
    elif option == 2:
        price = input("Insira o preço do jogo: ")
        parameters['price'] = float(price)
    elif option == 3:
        year = input("Insira o ano de lançamento do jogo: ")
        parameters['year'] = int(year)
    elif option == 4:
        name = input("Insira o nome do jogo: ")
        price = input("Insira o preço do jogo: ")
        year = input("Insira o ano de lançamento do jogo: ")
        parameters['name'] = name
        parameters['price'] = float(price)
        parameters['year'] = int(year)

    return parameters


def register(gameList):
    param = readParameters(4)
    name, price, year = param['name'], param['price'], param['year']

    gameList.append(game(name, price, year))


def show(gameList):
    print('================================================================')
    for e in gameList:
        print(f"{gameList.index(e)+1}: {e.name} ; R${e.price} : {e.yearLaunch}")
    print('================================================================')


def exists(gameList):
    bool = False
    search = input("Buscar por nome: ")
    for e in gameList:
        if e.name == search:
            bool = True

    if bool:
        print(f"{search} está na lista!")
    else:
        print(f"{search} não está na lista!")


def delete(gameList):

    show(gameList)

    index = int(input("Qual item deseja remover?\n"))-1
    removedItem = gameList.pop(index).name

    print(f"Item {index+1} ({removedItem}) removido!")


def update(gameList):

    show(gameList)
    index = int(input("Qual item deseja atualizar?\n"))-1

    editParam = int(input(
        "O que deseja atualizar?\n1. Nome\n2. Preço\n3. Ano de lançamento\n4. Todas as opçoes\n"))

    param = readParameters(editParam)

    if 'name' in param:
        gameList[index].name = param['name']
    if 'price' in param:
        gameList[index].price = param['price']
    if 'year' in param:
        gameList[index].yearLaunch = param['year']
