# ===============================================================
# ARQUIVO: batalha.py
# ATIVIDADE: Tarefa Monitoria 07 - Formação Acelerada em Programação
# CURSO: Backend Python com Django - UEPA
# PROFESSOR: —
# ALUNO: Renato Nascimento Alho
# DATA: 09/10/2025
# ===============================================================
# OBJETIVO:
# Desenvolver o núcleo de um sistema de batalha RPG utilizando os
# princípios da Programação Orientada a Objetos:
# Abstração, Herança, Polimorfismo e Encapsulamento.
# ===============================================================

# Importações necessárias
from abc import ABC, abstractmethod
from random import randint
import time

# ===============================================================
# CLASSE ABSTRATA BASE
# ===============================================================

class Personagem(ABC):
    """
    Classe abstrata que representa um personagem genérico no jogo.
    Serve como base para as classes Guerreiro e Mago.
    """

    def __init__(self, nome: str, vida: int, ataque_base: int):
        # Atributos públicos e protegidos
        self.nome = nome                # público
        self._vida = vida               # protegido (acesso restrito)
        self._ataque_base = ataque_base # protegido (acesso restrito)

    def receber_dano(self, dano: int):
        """
        Método responsável por aplicar dano ao personagem.
        A vida nunca pode ficar negativa (encapsulamento).
        """
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self._vida}")

    def esta_vivo(self) -> bool:
        """
        Retorna True se o personagem ainda estiver com vida > 0.
        """
        return self._vida > 0

    @abstractmethod
    def atacar(self, alvo):
        """
        Método abstrato que define o contrato de ataque.
        Cada subclasse deve implementar sua própria forma de atacar.
        """
        pass


# ===============================================================
# CLASSE GUERREIRO (HERDA DE PERSONAGEM)
# ===============================================================

class Guerreiro(Personagem):
    """
    Classe que representa o Guerreiro, herdeiro de Personagem.
    Possui o atributo privado __furia e métodos de ataque e ataque especial.
    """

    def __init__(self, nome: str, vida: int, ataque_base: int):
        super().__init__(nome, vida, ataque_base)
        self.__furia = 50  # atributo privado (encapsulado)

    def atacar(self, alvo):
        """
        Ataque básico do guerreiro.
        O dano é calculado com base no ataque base + um bônus aleatório.
        """
        dano = self._ataque_base + randint(5, 15)
        print(f"{self.nome} ataca {alvo.nome} com sua espada causando {dano} de dano!")
        alvo.receber_dano(dano)
        # Ao atacar, o guerreiro ganha um pouco de fúria
        self.__furia += 10
        if self.__furia > 100:
            self.__furia = 100
        print(f"Fúria atual de {self.nome}: {self.__furia}")

    def ataque_especial(self, alvo):
        """
        Ataque especial que consome fúria.
        Só pode ser usado se o guerreiro tiver pelo menos 40 de fúria.
        """
        if self.__furia >= 40:
            dano = self._ataque_base * 2 + randint(10, 25)
            print(f"{self.nome} usa ATAQUE ESPECIAL em {alvo.nome}, causando {dano} de dano devastador!")
            alvo.receber_dano(dano)
            self.__furia -= 40
            print(f"Fúria restante: {self.__furia}")
        else:
            print(f"{self.nome} tentou usar ataque especial, mas não tem fúria suficiente!")


# ===============================================================
# CLASSE MAGO (HERDA DE PERSONAGEM)
# ===============================================================

class Mago(Personagem):
    """
    Classe que representa o Mago, herdeiro de Personagem.
    Possui o atributo privado __mana e um ataque que consome mana.
    """

    def __init__(self, nome: str, vida: int, ataque_base: int):
        super().__init__(nome, vida, ataque_base)
        self.__mana = 100  # atributo privado (encapsulado)

    def atacar(self, alvo):
        """
        Ataque mágico que consome mana.
        Se a mana for insuficiente, o ataque não ocorre.
        """
        if self.__mana >= 20:
            dano = self._ataque_base + randint(10, 20)
            print(f"{self.nome} lança uma bola de fogo em {alvo.nome}, causando {dano} de dano mágico!")
            alvo.receber_dano(dano)
            self.__mana -= 20
            print(f"Mana restante de {self.nome}: {self.__mana}")
        else:
            print(f"{self.nome} tentou lançar magia, mas não tem mana suficiente!")
            # Regenera um pouco de mana se não atacar
            self.__mana += 10
            print(f"{self.nome} se concentra e recupera 10 de mana. Mana atual: {self.__mana}")


# ===============================================================
# SIMULAÇÃO DE BATALHA
# ===============================================================

if __name__ == "__main__":
    # Criação dos personagens
    guerreiro = Guerreiro("Thorin", vida=120, ataque_base=25)
    mago = Mago("Gandalf", vida=100, ataque_base=30)

    print("\n===== INÍCIO DA BATALHA =====\n")

    # Laço de batalha
    turno = 1
    while guerreiro.esta_vivo() and mago.esta_vivo():
        print(f"\n--- TURNO {turno} ---")
        time.sleep(1)

        # Guerreiro ataca primeiro
        if randint(1, 4) == 4:  # chance de usar ataque especial
            guerreiro.ataque_especial(mago)
        else:
            guerreiro.atacar(mago)

        # Verifica se o mago morreu
        if not mago.esta_vivo():
            print(f"\n⚔️ {mago.nome} foi derrotado! {guerreiro.nome} é o vencedor!")
            break

        time.sleep(1)

        # Mago contra-ataca
        mago.atacar(guerreiro)

        # Verifica se o guerreiro morreu
        if not guerreiro.esta_vivo():
            print(f"\n🔥 {guerreiro.nome} foi derrotado! {mago.nome} é o vencedor!")
            break

        turno += 1
        time.sleep(1)

    print("\n===== FIM DA BATALHA =====\n")
