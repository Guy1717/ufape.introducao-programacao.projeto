from exceptions import InvalidScore

def getList(filename):
    file = open(filename, 'r')
    games = []

    for line in file:
        params = line.split(';')
        name, year, score = params[0], params[1], params[2]
        games.append({'name': name, 'year': year, 'score': score})
    
    file.close()

    return games

def readName():
    name = input('Nome: ')
    return name

def readYear():
    year = int(input('Ano de lançamento: '))
    return year

def readScore():
    score = int(input('Pontuação (1 ~ 10): '))

    if score < 0 or score > 10:
        raise InvalidScore('Pontuação deve ser entre 0 e 10')
    return score

def readParams():
    name = readName()
    year = readYear()
    score = readScore()
    
    params = [name,year,score]

    return params

def register(filename):
    try:
        games = getList(filename)

        newData = readParams()
        name, year, score = newData[0], newData[1], newData[2]

        file = open(filename, 'w')
        for game in games:
            file.write(f"{game['name']};{game['year']};{game['score']}")
            
        file.write(f"{name};{year};{score}\n")
        file.close()

    except FileNotFoundError:
        file = open(filename, 'w')
        
        newData = readParams()
        name, year, score = newData[0], newData[1], newData[2]
        
        file.write(f"{name};{year};{score}\n")
        file.close()
    except InvalidScore:
        print('[!] Pontuação deve ser entre 0 e 10')
    except:
        print("[!] Erro inesperado ao registrar item")

def show(filename):
    try:
        games = getList(filename)

        i=1
        print('================================================================')
        for game in games:
            print(f"[{i}]: {game['name']} | {game['year']} | {game['score']}")
            i += 1
        print('================================================================')
    except FileNotFoundError:
        print('[!] Arquivo inexistente')
    except:    
        print('[!] Erro inesperado ao mostrar lista')

def edit(filename):
    try:
        games = getList(filename)
        show(filename)

        index = int(input('Qual item deseja editar? '))-1

        print("1. Nome\n2. Ano\n3. Pontuação\n4. Todos\n")
        change = int(input('O que deseja editar? '))

        if change == 1:
            games[index]['name'] = readName()
        elif change == 2:
            games[index]['year'] = readYear()
        elif change == 3:
            games[index]['score'] = f"{readScore()}\n"
        elif change == 4:
            params = readParams()
            name, year, score = params[0], params[1], params[2]

            games[index]['name'], games[index]['year'], games[index]['score'] = name, year, score

        file = open(filename, 'w')
        for game in games:
            file.write(f"{game['name']};{game['year']};{game['score']}")

        file.close()
    except InvalidScore:
        print('[!] Pontuação deve ser entre 0 e 10')
    except:
        print("[!] Erro inesperado ao editar item")

def delete(filename):
    try:
        show(filename)
        
        games = getList(filename)

        index = int(input('Qual item deseja deletar? '))-1

        deleted = games.pop(index)
        print(f"Item {index} ({deleted['name']}) deletado com sucesso!")

        file = open(filename, 'w')
        for game in games:
            file.write(f"{game['name']};{game['year']};{game['score']}")
        file.close()

    except:
        print('[!] Erro inesperado ao deletar item')

def search(filename):
    games = getList(filename)

    # Escolher propriedade de busca
    print('1. Nome\n2. Ano\n3. Pontuação')
    searchBy = int(input('Selecione uma opção: '))

    # Name
    if searchBy == 1:
        search = input('Nome do jogo para buscar: ')
        itemExists = False
        for game in games:
            if game['name'] == search:
                index = games.index(game)
                itemExists = True

        if itemExists:
            print(f'» Item presente na lista')
            game = games[index]
            name,year,score = game['name'], game['year'], game['score']
            print(f"{name} | {year} | {score}")
        else:
            print('» Item inexistente')
    # Year
    elif searchBy == 2:
        search = int(input('Ano do jogo para buscar: '))
        found = []

        for game in games:
            if int(game['year']) == search:
                index = games.index(game)
                found.append(f"[{index+1}]: {game['name']} | {game['year']} | {game['score']}")
        if len(found) > 0:
            print("» Itens encontrados: ")
            for game in found:
                print(game)
        else:
            print("» Item inexistente")
    # Score
    elif searchBy == 3:
        search = int(input('Pontuação do jogo para buscar: '))
        
def run(filename):
    while(True):
        print("1. Mostrar lista\n2. Registrar item\n3. Editar item\n4. Deletar item\n5. Buscar item (nome)\n0. Encerrar programa")
        option = int(input('Selecione uma opção: '))

        if option == 0:
            exit()
        elif option == 1:
            show(filename)
        elif option == 2:
            register(filename)
        elif option == 3:
            edit(filename)
        elif option == 4:
            delete(filename)
        elif option == 5:
            search(filename)
        else:
            print('Opção inválida')