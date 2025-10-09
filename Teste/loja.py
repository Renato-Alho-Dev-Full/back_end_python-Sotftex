# ==========================================================
#  loja.py
#  Atividade Prática - Modelagem de Produtos em um E-commerce
#  Curso: Backend Python com Django - UEPA
#  Autor: Renato Nascimento Alho
#  Data: 02/10/2025
#
#  Objetivo:
#  Implementar um sistema de modelagem de produtos
#  usando Programação Orientada a Objetos (POO),
#  aplicando Abstração, Herança e Polimorfismo.
#
#  O sistema simula um carrinho de compras que pode conter
#  tanto produtos físicos quanto digitais, e calcula
#  corretamente o preço final de cada item.
# ==========================================================

# Importações necessárias
from abc import ABC, abstractmethod


# ==========================================================
# Classe Abstrata Base
# ==========================================================
class Produto(ABC):
    """
    Classe abstrata que representa um Produto genérico.
    Todo produto possui um nome e um preço base.
    Essa classe define um contrato que obriga as subclasses
    a implementar o método 'calcular_preco_final()'.
    """

    def __init__(self, nome: str, preco_base: float):
        """
        Construtor da classe Produto.

        :param nome: Nome do produto
        :param preco_base: Preço base do produto (sem taxas ou frete)
        """
        self.nome = nome
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco_final(self) -> float:
        """
        Método abstrato que deve ser implementado pelas subclasses.
        Ele calcula e retorna o preço final do produto.
        """
        pass


# ==========================================================
# Classe Produto Físico (Herda de Produto)
# ==========================================================
class ProdutoFisico(Produto):
    """
    Representa um produto físico (exemplo: livro, caneca).
    Além do preço base, ele possui o custo de frete.
    """

    def __init__(self, nome: str, preco_base: float, custo_frete: float):
        """
        Construtor da classe ProdutoFisico.

        :param nome: Nome do produto
        :param preco_base: Preço base do produto
        :param custo_frete: Custo adicional do frete
        """
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete

    def calcular_preco_final(self) -> float:
        """
        Retorna o preço final do produto físico,
        que é a soma do preço base + custo de frete.
        """
        return self.preco_base + self.custo_frete


# ==========================================================
# Classe Produto Digital (Herda de Produto)
# ==========================================================
class ProdutoDigital(Produto):
    """
    Representa um produto digital (exemplo: e-book, curso online).
    Além do preço base, ele possui uma taxa de serviço.
    """

    def __init__(self, nome: str, preco_base: float, taxa_servico: float):
        """
        Construtor da classe ProdutoDigital.

        :param nome: Nome do produto
        :param preco_base: Preço base do produto
        :param taxa_servico: Taxa de serviço adicionada ao preço
        """
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico

    def calcular_preco_final(self) -> float:
        """
        Retorna o preço final do produto digital,
        que é a soma do preço base + taxa de serviço.
        """
        return self.preco_base + self.taxa_servico


# ==========================================================
# Área de Testes (Simulação do Carrinho de Compras)
# ==========================================================
if __name__ == "__main__":
    """
    Aqui simulamos um carrinho de compras com diferentes
    tipos de produtos (físicos e digitais).
    O sistema deve calcular o preço final de cada item
    e somar o valor total da compra.
    """

    # Criando os produtos
    livro = ProdutoFisico(nome="Livro Python", preco_base=50.0, custo_frete=10.0)
    caneca = ProdutoFisico(nome="Caneca Dev", preco_base=30.0, custo_frete=5.0)
    ebook = ProdutoDigital(nome="E-book Django", preco_base=40.0, taxa_servico=2.0)
    curso = ProdutoDigital(nome="Curso Online de POO", preco_base=200.0, taxa_servico=15.0)

    # Lista simulando o carrinho de compras
    carrinho = [livro, caneca, ebook, curso]

    # Variável para acumular o total da compra
    total_compra = 0.0

    print("=== Carrinho de Compras ===\n")

    # Percorrendo os produtos e exibindo os preços finais
    for produto in carrinho:
        preco_final = produto.calcular_preco_final()
        print(f"Produto: {produto.nome} | Preço Final: R$ {preco_final:.2f}")
        total_compra += preco_final

    # Exibindo o valor total da compra
    print("\n===========================")
    print(f"TOTAL DA COMPRA: R$ {total_compra:.2f}")
    print("===========================\n")