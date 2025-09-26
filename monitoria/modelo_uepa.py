# ================================
# Arquivo: modelo_uepa.py
# Atividade Prática - Modelagem de Classes na UEPA
# Curso: Backend Python com Django
# Autor: Renato Nascimento Alho
# ================================

# Classe Base (Abstração)
class MembroUEPA:
    def __init__(self, nome, matricula, email):
        # Atributos comuns a todos os membros (aluno/professor)
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        # Método genérico que pode ser sobrescrito pelas classes filhas
        return f"Sou um membro da UEPA. Nome: {self.nome}"


# Classe Derivada - Aluno (Herança de MembroUEPA)
class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso):
        # Chamando o construtor da classe pai (MembroUEPA)
        super().__init__(nome, matricula, email)
        # Atributo específico do aluno
        self.curso = curso

    def verificar_notas(self):
        # Método fictício para simular verificação de notas
        return f"O aluno {self.nome} está verificando suas notas no curso de {self.curso}."

    def apresentar(self):
        # Sobrescrita do método apresentar() da classe pai
        return (f"Sou o aluno {self.nome}, matrícula {self.matricula}, "
                f"email {self.email}, do curso de {self.curso}.")


# Classe Derivada - Professor (Herança de MembroUEPA)
class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        # Chamando o construtor da classe pai (MembroUEPA)
        super().__init__(nome, matricula, email)
        # Atributo específico do professor
        self.departamento = departamento

    def lancar_frequencia(self):
        # Método fictício para simular lançamento de frequência
        return f"O professor {self.nome} lançou a frequência do departamento de {self.departamento}."

    def apresentar(self):
        # Sobrescrita do método apresentar() da classe pai
        return (f"Sou o professor {self.nome}, matrícula {self.matricula}, "
                f"email {self.email}, do departamento de {self.departamento}.")


# ================================
# Área de Testes
# Aqui criamos instâncias (objetos) para testar o código
# ================================
if __name__ == "__main__":
    # Criando um aluno
    aluno1 = Aluno("Maria Silva", "2025001", "maria.silva@uepa.br", "Engenharia da Computação")
    
    # Criando um professor
    professor1 = Professor("Carlos Souza", "P2025002", "carlos.souza@uepa.br", "Ciência da Computação")

    # Testando métodos
    print(aluno1.apresentar())         # Apresentação do aluno
    print(aluno1.verificar_notas())    # Método específico do aluno

    print(professor1.apresentar())     # Apresentação do professor
    print(professor1.lancar_frequencia())  # Método específico do professor
