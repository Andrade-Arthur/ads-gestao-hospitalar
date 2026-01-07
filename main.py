import os

# Lista para armazenar os dicionários de pacientes
pacientes = []

def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTE ---")
    nome = input("Nome do paciente: ")
    try:
        idade = int(input("Idade: "))
        telefone = input("Telefone: ")
        
        # Dicionário do paciente
        paciente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }
        pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")
    except ValueError:
        print("Erro: A idade deve ser um número inteiro.")

def ver_estatisticas():
    print("\n--- ESTATÍSTICAS ---")
    total = len(pacientes)
    if total == 0:
        print("Nenhum paciente cadastrado.")
        return

    soma_idades = sum(p["idade"] for p in pacientes)
    media_idade = soma_idades / total
    
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Média de idade: {media_idade:.1f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente():
    print("\n--- BUSCAR PACIENTE ---")
    nome_busca = input("Digite o nome para buscar: ").lower()
    encontrado = False
    for p in pacientes:
        if nome_busca in p["nome"].lower():
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
            encontrado = True
    if not encontrado:
        print("Paciente não encontrado.")

def listar_todos():
    print("\n--- LISTA GERAL ---")
    if not pacientes:
        print("Lista vazia.")
    else:
        for p in pacientes:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")

# Loop Principal
while True:
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_paciente()
    elif opcao == '2':
        ver_estatisticas()
    elif opcao == '3':
        buscar_paciente()
    elif opcao == '4':
        listar_todos()
    elif opcao == '5':
        print("Saindo do sistema...")
        break
    else: print("Opção inválida!")
