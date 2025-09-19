


# analise_turma.py

# Lista de alunos fornecida na tarefa, cada aluno é representado por um dicionário
alunos = [
    {"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},
    {"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},
    {"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},
    {"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},
    {"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},
    {"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0, "status_matricula": "ativo"},
    {"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},
    {"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"}
]

# ----------------------------
# 1. Filtrar alunos elegíveis
# Critérios: frequência >= 75.0 e status_matricula == "ativo"
# Usando a função filter() com lambda
# ----------------------------
alunos_elegiveis = list(filter(
    lambda aluno: aluno["frequencia"] >= 75.0 and aluno["status_matricula"] == "ativo",
    alunos
))

# ----------------------------
# 2. Aplicar bônus de 10% na nota final
# A nota não pode ultrapassar 10.0
# Usando map() com lambda
# ----------------------------
alunos_com_bonus = list(map(
    lambda aluno: {
        **aluno,  # mantém os dados originais
        "nota_final": min(aluno["nota_final"] * 1.1, 10.0)  # aplica bônus e limita em 10.0
    },
    alunos_elegiveis
))

# ----------------------------
# 3. Identificar alunos destaque
# Critério: nota_final (já com bônus) >= 9.0
# ----------------------------
alunos_destaque = list(filter(
    lambda aluno: aluno["nota_final"] >= 9.0,
    alunos_com_bonus
))

# ----------------------------
# 4. Saída esperada
# Mostrar no console nome e nota final (com bônus) dos alunos destaque
# ----------------------------
print("Alunos Destaque:")
for aluno in alunos_destaque:
    print(f"{aluno['nome']} - Nota Final: {aluno['nota_final']:.2f}")
