from functions import register, show, delete, exists, update, game

games = []

example = game("Game", 100.00, 1999)
games.append(example)

while (True):
    print("1. Apresentar jogos")
    print("2. Registrar jogo")
    print("3. Atualizar jogo")
    print("4. Buscar jogo (nome)")
    print("5. Deletar jogo")

    x = int(input("Escolha uma opção: "))

    if x == 1:
        show(games)
    if x == 2:
        register(games)
    if x == 3:
        update(games)
    if x == 4:
        exists(games)
    if x == 5:
        delete(games)
