clientes_cadastrados = []


class Cliente:
    def __init__(self) -> None:
        self.primeiro_nome:str
        self.sobrenome: str
        self.status:str
        self.nome_completo: str
        self.idade:int
        self.renda:float

    
    def ler_nome(self):
        nome:str
        while True:
            nome = input('Digite seu primeiro nome: ').title()
            if nome.isalpha() and len(nome) >= 3:
                self.primeiro_nome = nome
                print(f'Nome "{nome}" cadastrado com sucesso!')
                break
            else:
                print('Digite um nome válido!')
    

    def ler_sobrenome(self):
        sobrenome: str
        while True:
            sobrenome = input('Digite seu sobrenome: ').title()
            if sobrenome.isalpha() and len(sobrenome) >= 3:
                self.sobrenome = sobrenome
                self.nome_completo = ' '.join([self.primeiro_nome, self.sobrenome])
                print(f'Sobrenome "{sobrenome}" cadastrado com sucesso!')
                break
            else:
                print('Digite um sobrenome válido!')


    def ler_idade(self):
        while True:
            entrada:str = input('Informe sua idade: ')
            if entrada.isnumeric():
                entrada = int(entrada)
                if entrada >= 18:
                    self.idade = entrada
                    print('Idade cadastrada com sucesso!')
                    break
                print('Desculpe, apenas pessoas com 18 anos ou mais podem se cadastrar.')
            print('Digite uma idade válida!')


    def ler_renda(self):
        while True:
            entrada:str = input('Informe sua renda liquida atual sem casas decimais: R$')
            try:
                entrada = float(int(entrada))
            except AttributeError:
                print('Digite apenas um valor inteiro: ')
                continue
            self.renda = entrada
            print('Renda cadastrada com sucesso!')
            break


class Simulador():
    def __init__(self) -> None:
        self.status:str
        self.renda:float
        self.trinta_porcento_da_renda: float
        self.valor_do_imovel:float
        self.valor_das_parcelas:float
        self.PARCELAS:int = 360


    def receber_valor_do_imovel(self):
        while True:
            entrada:str = input('Informe o valor total do imovel sem ponto flutuante: R$')
            try:
                self.valor_do_imovel = float(int(entrada))
            except Exception(ValueError):
                print('Valor informado é inválido!')
                continue
            break


    def calcula_valor_minimo_necessario_para_financiamento(self):
        self.valor_das_parcelas = self.valor_do_imovel / self.PARCELAS


    def calcula_valor_equivalente_a_um_terco_da_renda(self):
        self.trinta_porcento_da_renda = self.renda*30/100

    
    def retorna_o_status(self):
        return 'Aprovado' if self.trinta_porcento_da_renda >= self.valor_das_parcelas else 'Reprovado'

    
    def calcula_valor_das_parcelas(self):
        self.valor_das_parcelas = self.valor_do_imovel / self.PARCELAS


def MainApp():
    pessoa = Cliente()
    simulador = Simulador()
    while True:
        print('='*50)
        print(f'{"SIMULADOR DE FINANCIAMENTO":^50}')
        print('='*50)
        print('[ I ] INICIAR SIMULAÇÂO')
        print('[ S ] SAIR')
        print('='*50)
        entrada: str = input('-> ').upper()
        entrada = entrada[0]
        match entrada:
            case 'I':
                pessoa.ler_nome()
                pessoa.ler_sobrenome()
                pessoa.ler_idade()
                pessoa.ler_renda()

                simulador.renda = pessoa.renda

                simulador.receber_valor_do_imovel()
                simulador.calcula_valor_das_parcelas()
                simulador.calcula_valor_equivalente_a_um_terco_da_renda()
                simulador.calcula_valor_minimo_necessario_para_financiamento()
                pessoa.status = simulador.retorna_o_status()

                clientes_cadastrados.append([pessoa.nome_completo, pessoa.idade, pessoa.renda, pessoa.status])
                print(clientes_cadastrados)
            case 'S':
                break
        print('Até aqui está tudo caminhando')

MainApp()
