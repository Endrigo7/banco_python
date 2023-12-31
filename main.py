from interface import ContaBancariaGui

class Main:
    def bem_vindo(self):
        conta_bancaria_gui = ContaBancariaGui()

        print("Bem vindo ao banco do serpro")
        print("----------------------------")
        print("por favor selecione uma opção de menu")

        op = -1

        while op != 0:
            print(" [01] - Abrir uma conta")
            print(" [02] - consultar seu saldo")
            print(" [03] - creditar")
            print(" [04] - debitar")
            print(" [00] - sair")

            op = int(input())

            if op == 1:
                conta_bancaria_gui.abrir_contar()
            elif op == 2:
                conta_bancaria_gui.consultar_saldo()
            elif op == 3:
                conta_bancaria_gui.creditar()
            elif op == 4:
                conta_bancaria_gui.debitar()
            else:
                print("opção invalida! Selecione uma opção valida")


if __name__ == '__main__':
    main = Main()
    main.bem_vindo()
