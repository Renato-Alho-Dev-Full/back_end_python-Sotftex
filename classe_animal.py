# modelar objeto animal, programção orienteda a objeto. 


class Animal(): # método construtor... constroi os atributos do processo
    # chamar e declarar as 
    def __init__(self, especie: str, nome: str, idade:int):
        self.especie = especie
        self.nome = nome
        self.idade = idade
        self.vivo = True
        self.fome = 50

    # É a parte de construtor que vai dizer as construção
    # das funções

    def comer(self):
        if self.vivo == True:
           self.fome += 10
           return f"{self.nome} já comeu!"
        else: 
           return f" O animal não pode comer"



    def dormir(self):
        if self.vivo and self.fome > 30:
            self.fome -= 10
            return f"{self.nome} está dormindo"
        else:
            return f"{self.nome} não pode dormir"
        

        
    def emitir_som(self):
        if self.vivo:
            return f"{self.nome} emite um som"
        else:
            return  f"{self.nome} não pode emitir som"
        



    def mover (self):
        if self.vivo:
            return  f"{self.nome} O animal está se movento"
        else:
            return  f"{self.nome} está parado"
        

especie = input("Qual o espécie do cachorro?")
nome = input("Qual o nome do cachorro?")
idade = input("Qual a idade do cachorro?")


cachorro = Animal( especie, nome, idade)
print(cachorro.especie)
print(cachorro.nome)
print(cachorro.idade)

a = cachorro.emitir_som()
b = cachorro.vivo()

print(a)


print(b)