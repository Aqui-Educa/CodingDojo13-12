class Pessoa():
    def __init__(self, nome, idade, cpf, sexo, telefone, logradouro):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sexo = sexo
        self.telefone = telefone
        self.logradouro = logradouro

    def repetir(self, msg):
        print(msg)

livia = Pessoa('Livia', '49', 'xxx.xxx.xxx-xx', 'F' '7199999','Rua Tal')
print(livia)

