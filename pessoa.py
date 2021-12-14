class Pessoa():
    def __init__(self, nome, idade, cpf, sexo, telefone, logradouro):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sexo = sexo
        self.telefone = telefone
        self.logradouro = logradouro

    def repetir(self, msg):
        print(f'{self.nome}: {msg}')

    def comer(self, comida):
        print(f'Estou comendo {comida}')    

    def ouvir(self, ouvindo):
        print(f'Estou ouvindo {ouvindo}')

# livia = Pessoa('Livia', 49, 'xxx.xxx.xxx-xx', 'F', '7199999','Rua Tal')
# livia.repetir(f'Oi, sou a livia, eu tenho {livia.idade} anos e moro na {livia.logradouro}'

nome = input('Insira o seu nome: ')
idade = input('Insira o sua idade: ')
cpf = input('Insira o seu cpf: ')
sexo = input('Insira o seu sexo: ')
telefone = input('Insira o seu telefone: ')
logradouro = input('Insira o seu logradouro: ')
comida = input('O que você está comendo: ')
ouvindo = input('O que você está ouvindo: ')

usuario = Pessoa(nome, idade, cpf, sexo, telefone, logradouro)
frase = f'Oi meu nome é {usuario.nome}, eu tenho {usuario.idade} anos e moro na {usuario.logradouro}'
usuario.repetir(frase)
usuario.comer(comida)
usuario.ouvir(ouvindo)

# Continuar com (Fazer uma herança).