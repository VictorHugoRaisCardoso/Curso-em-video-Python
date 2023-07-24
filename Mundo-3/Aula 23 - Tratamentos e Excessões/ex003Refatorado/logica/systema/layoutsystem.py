from time import sleep

class LayoutSystem():
    
    def decorador(self, mensagem):
        self.mensagem = mensagem
        print('=' * 60)
        print(f'{mensagem:^60}')
        print('=' * 60)
        return
    
    
    def menu(self):
        self.opção = ["NOVO CADASTRO", "PESSOAS CADASTRADAS", "SAIR"]
        for num, i in enumerate(self.opção):
            print(f'[ {num + 1} ] {i}')
        return
    
    
    def escolha(self):
        opção = str(input('Faça sua escolha: '))
        print("=" * 60)
        if (opção == "1"):
            return 1
        elif (opção == "2"):
            return 2
        elif (opção == "3"):
            print(f'Encerrando o sistema. Até logo.')
            return 3
        else:
            print(f"Erro! Opção inválida! Tente novamente.")
    
    
    def novoCadastros(self):
        try:
            self.nome = str(input("Digite seu nome: ")).strip()
            if (self.nome == ""):
                self.nome = "< Desconhecido >"
            self.idade = int(input("Informe sua idade: "))
            with open("cadastros.txt", 'a+') as file:
                file.write(f"{self.nome:<53}{self.idade} anos\n")
                file.close()
        except(ValueError):
            while True:
                self.idade = str(input("Erro! O valor inserido é inválido! Tente novamente: "))
                if (self.idade.isnumeric()):
                    int(self.idade)
                    return self.idade
                    break
                
                
    def verCadastros(self):
        with open('cadastros.txt', 'r+') as file:
            for cadastro in file:
                print(f'{cadastro}',end='')
            return
                
                
    def arquivoInexiste(self):
        try:
            with open('cadastros.txt', 'r+') as file:
                file.close()
        except(FileNotFoundError):
            with open('cadastros.txt', 'a+') as file:
                file.close()
                print(f"Arquivo {file.name} criado com sucesso!")
                return
        