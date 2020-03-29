class JogoDaVelha:
    jogo = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    __jogador1_h = 0
    __jogador1_v = 0
    __jogador2_h = 0
    __jogador2_v = 0
    __pontos1 = 0
    __pontos2 = 0
    __pontosVelha = 0
    __contador = 0

    def __init__(self):
        pass

    @staticmethod
    def verificaX():
        if JogoDaVelha.jogo[0][0] == 'x' and JogoDaVelha.jogo[0][1] == 'x' and JogoDaVelha.jogo[0][2] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[1][0] == 'x' and JogoDaVelha.jogo[1][1] == 'x' and JogoDaVelha.jogo[1][2] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[2][0] == 'x' and JogoDaVelha.jogo[2][1] == 'x' and JogoDaVelha.jogo[2][2] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][0] == 'x' and JogoDaVelha.jogo[1][0] == 'x' and JogoDaVelha.jogo[2][0] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][1] == 'x' and JogoDaVelha.jogo[1][1] == 'x' and JogoDaVelha.jogo[2][1] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][2] == 'x' and JogoDaVelha.jogo[1][2] == 'x' and JogoDaVelha.jogo[2][2] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][0] == 'x' and JogoDaVelha.jogo[1][1] == 'x' and JogoDaVelha.jogo[2][2] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][2] == 'x' and JogoDaVelha.jogo[1][1] == 'x' and JogoDaVelha.jogo[2][0] == 'x':
            print("Jogador 1 ganhou")
            JogoDaVelha.__pontos1 += 1
            JogoDaVelha.zerar()
            return True
        return False

    @staticmethod
    def verificaO():
        if JogoDaVelha.jogo[0][0] == 'o' and JogoDaVelha.jogo[0][1] == 'o' and JogoDaVelha.jogo[0][2] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[1][0] == 'o' and JogoDaVelha.jogo[1][1] == 'o' and JogoDaVelha.jogo[1][2] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[2][0] == 'o' and JogoDaVelha.jogo[2][1] == 'o' and JogoDaVelha.jogo[2][2] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][0] == 'o' and JogoDaVelha.jogo[1][0] == 'o' and JogoDaVelha.jogo[2][0] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][1] == 'o' and JogoDaVelha.jogo[1][1] == 'o' and JogoDaVelha.jogo[2][1] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][2] == 'o' and JogoDaVelha.jogo[1][2] == 'o' and JogoDaVelha.jogo[2][2] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][0] == 'o' and JogoDaVelha.jogo[1][1] == 'o' and JogoDaVelha.jogo[2][2] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        elif JogoDaVelha.jogo[0][2] == 'o' and JogoDaVelha.jogo[1][1] == 'o' and JogoDaVelha.jogo[2][0] == 'o':
            print("Jogador 2 ganhou")
            JogoDaVelha.__pontos2 += 1
            JogoDaVelha.zerar()
            return True
        return False

    @staticmethod
    def escolha1():
        print("JOGADOR1 - X")
        print()

        if not JogoDaVelha.verificaX() and not JogoDaVelha.verificaO():
            try:
                JogoDaVelha.jogador1_h = int(input("Digite valor na horizontal: "))
                JogoDaVelha.jogador1_v = int(input("Digite valor na vertical: "))
            except:
                print("Apenas numeros inteiros")
            try:
                if JogoDaVelha.jogo[JogoDaVelha.jogador1_h][JogoDaVelha.jogador1_v] == "x" or JogoDaVelha.jogo[JogoDaVelha.jogador1_h][JogoDaVelha.jogador1_v] == "o":
                    print("Não é possivel, já está preenchido")
                    JogoDaVelha.escolha1()
                else:
                    JogoDaVelha.jogo[JogoDaVelha.jogador1_h][JogoDaVelha.jogador1_v] = 'x'
            except AttributeError:
                print("Apenas numeros inteiros")
                JogoDaVelha.escolha1()
            except IndexError:
                print("Apenas numeros entre 0 e 3")
                JogoDaVelha.escolha1()


    @staticmethod
    def escolha2():
        print("JOGADOR2 - O")
        print()

        if not JogoDaVelha.verificaX() and not JogoDaVelha.verificaO():
            try:
                try:
                    JogoDaVelha.jogador2_h = int(input("Digite valor na horizontal: "))
                    JogoDaVelha.jogador2_v = int(input("Digite valor na vertical: "))
                except:
                    print("Apenas numeros inteiros")
                if JogoDaVelha.jogo[JogoDaVelha.jogador2_h][JogoDaVelha.jogador2_v] == "x" or JogoDaVelha.jogo[JogoDaVelha.jogador2_h][JogoDaVelha.jogador2_v] == "o":
                    print("Não é possivel, já está preenchido")
                    JogoDaVelha.escolha2()
                else:
                    JogoDaVelha.jogo[JogoDaVelha.jogador2_h][JogoDaVelha.jogador2_v] = 'o'
            except AttributeError:
                print("Apenas numeros inteiros")
                JogoDaVelha.escolha2()
            except IndexError:
                print("Apenas numeros entre 0 e 3")
                JogoDaVelha.escolha2()

    @staticmethod
    def imprimir():
        for n in JogoDaVelha.jogo:
            print(n)

    @staticmethod
    def velha():
        for n in JogoDaVelha.jogo:
            if '*' in n:
                return False
            else:
                print("Deu velha")
                JogoDaVelha.__pontosVelha += 1
                return True

    @staticmethod
    def pontos():
        print(f"Jogador 1: {JogoDaVelha.__pontos1} pontos")
        print(f"Jogador 2: {JogoDaVelha.__pontos2} pontos")
        print(f"Velha: {JogoDaVelha.__pontosVelha} pontos")

    @staticmethod
    def zerar():
        JogoDaVelha.jogo = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

    @staticmethod
    def jogar():
        while True:
            escolha = input("Jogar, Pontos, parar: ")
            if escolha == "jogar":
                JogoDaVelha.__contador += 1
                if JogoDaVelha.__contador % 2 == 0:
                    while True:
                        JogoDaVelha.escolha1()
                        JogoDaVelha.imprimir()
                        if JogoDaVelha.verificaX() or JogoDaVelha.verificaO() or JogoDaVelha.velha() :
                            break
                        JogoDaVelha.velha()
                        JogoDaVelha.escolha2()
                        JogoDaVelha.imprimir()
                        if JogoDaVelha.verificaX() or JogoDaVelha.verificaO() or JogoDaVelha.velha():
                            break
                else:
                    while True:
                        JogoDaVelha.escolha2()
                        JogoDaVelha.imprimir()
                        if JogoDaVelha.verificaX() or JogoDaVelha.verificaO() or JogoDaVelha.velha() :
                            break
                        JogoDaVelha.velha()
                        JogoDaVelha.escolha1()
                        JogoDaVelha.imprimir()
                        if JogoDaVelha.verificaX() or JogoDaVelha.verificaO() or JogoDaVelha.velha():
                            break

            elif escolha == 'pontos':
                JogoDaVelha.pontos()

            elif escolha == 'parar':
                print('Adeus <3')
                exit(1)

            else:
                print("Invalido")

JogoDaVelha.jogar()

