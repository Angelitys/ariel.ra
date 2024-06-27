# Lista para armazenar os alunos
alunos = []

def menu():
    print("\n---------------- Menu ----------------")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Procurar aluno por RA")
    print("5 - Listar alunos aprovados")
    print("6 - Listar alunos reprovados")
    print("7 - Procurar aluno por nome")
    print("8 - Média da turma B1")
    print("9 - Média da turma B2")
    print("10 - Média da turma geral")
    print("11 - Diário da turma")
    print("0 - Sair")
    print("-------------------------------------")

def adicionar_aluno():
    print("\nAdicionar aluno:")
    ra = input("RA (5 caracteres): ").strip()
    while len(ra) != 5:
        print("RA deve ter exatamente 5 caracteres.")
        ra = input("RA (5 caracteres): ").strip()

    nome = input("Nome (até 27 caracteres): ").strip()
    while len(nome) > 27:
        print("Nome deve ter até 27 caracteres.")
        nome = input("Nome (até 27 caracteres): ").strip()

    nota_b1 = float(input("Nota B1 (0 a 10): "))
    while nota_b1 < 0 or nota_b1 > 10:
        print("Nota fora do intervalo válido. Digite novamente.")
        nota_b1 = float(input("Nota B1 (0 a 10): "))

    nota_b2 = float(input("Nota B2 (0 a 10): "))
    while nota_b2 < 0 or nota_b2 > 10:
        print("Nota fora do intervalo válido. Digite novamente.")
        nota_b2 = float(input("Nota B2 (0 a 10): "))

    alunos.append({
        'ra': ra,
        'nome': nome,
        'nota_b1': nota_b1,
        'nota_b2': nota_b2
    })
    print(f"Aluno '{nome}' adicionado com sucesso!")

def listar_alunos():
    print("\nListagem de alunos:")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}")

def remover_aluno():
    ra = input("\nDigite o RA do aluno que deseja remover: ").strip()
    for aluno in alunos:
        if aluno['ra'] == ra:
            alunos.remove(aluno)
            print(f"Aluno com RA {ra} removido.")
            return
    print(f"Aluno com RA {ra} não encontrado.")

def procurar_aluno_por_ra():
    ra = input("\nDigite o RA do aluno que deseja procurar: ").strip()
    for aluno in alunos:
        if aluno['ra'] == ra:
            print(f"Aluno encontrado:")
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}")
            return
    print(f"Aluno com RA {ra} não encontrado.")

def listar_aprovados():
    print("\nListagem de alunos aprovados:")
    aprovados = [aluno for aluno in alunos if (aluno['nota_b1'] + aluno['nota_b2']) / 2 >= 7]
    if not aprovados:
        print("Nenhum aluno aprovado encontrado.")
    else:
        for aluno in aprovados:
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Média: {(aluno['nota_b1'] + aluno['nota_b2']) / 2:.2f}")

def listar_reprovados():
    print("\nListagem de alunos reprovados:")
    reprovados = [aluno for aluno in alunos if (aluno['nota_b1'] + aluno['nota_b2']) / 2 < 7]
    if not reprovados:
        print("Nenhum aluno reprovado encontrado.")
    else:
        for aluno in reprovados:
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Média: {(aluno['nota_b1'] + aluno['nota_b2']) / 2:.2f}")

def procurar_aluno_por_nome():
    nome = input("\nDigite o nome do aluno que deseja procurar: ").strip()
    encontrados = [aluno for aluno in alunos if aluno['nome'].lower() == nome.lower()]
    if not encontrados:
        print(f"Aluno com nome '{nome}' não encontrado.")
    else:
        print(f"Alunos encontrados com nome '{nome}':")
        for aluno in encontrados:
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}")

def calcular_media_b1():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
    media_b1 = sum(aluno['nota_b1'] for aluno in alunos) / len(alunos)
    print(f"Média da turma B1: {media_b1:.2f}")

def calcular_media_b2():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
    media_b2 = sum(aluno['nota_b2'] for aluno in alunos) / len(alunos)
    print(f"Média da turma B2: {media_b2:.2f}")

def calcular_media_geral():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
    media_geral = sum((aluno['nota_b1'] + aluno['nota_b2']) / 2 for aluno in alunos) / len(alunos)
    print(f"Média da turma geral: {media_geral:.2f}")

def diario_da_turma():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
    
    print("\n--------------------------------------------------------")
    print("                   Diário da turma")
    print("--------------------------------------------------------")
    print("RA    Nome                      Nota B1  Nota B2   Média")
    print("--------------------------------------------------------")
    for aluno in alunos:
        print(f"{aluno['ra']}    {aluno['nome'].ljust(27)}    {aluno['nota_b1']:.2f}     {aluno['nota_b2']:.2f}     {(aluno['nota_b1'] + aluno['nota_b2']) / 2:.2f}")
    print("--------------------------------------------------------")
    
    # Calculando médias da turma
    media_b1 = sum(aluno['nota_b1'] for aluno in alunos) / len(alunos)
    media_b2 = sum(aluno['nota_b2'] for aluno in alunos) / len(alunos)
    media_geral = sum((aluno['nota_b1'] + aluno['nota_b2']) / 2 for aluno in alunos) / len(alunos)
    
    print(f"                  Médias da Turma  {media_b1:.2f}     {media_b2:.2f}     {media_geral:.2f}")
    print("--------------------------------------------------------")

# Função principal para executar o menu
def main():
    while True:
        menu()
        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            remover_aluno()
        elif opcao == '4':
            procurar_aluno_por_ra()
        elif opcao == '5':
            listar_aprovados()
        elif opcao == '6':
            listar_reprovados()
        elif opcao == '7':
            procurar_aluno_por_nome()
        elif opcao == '8':
            calcular_media_b1()
        elif opcao == '9':
            calcular_media_b2()
        elif opcao == '10':
            calcular_media_geral()
        elif opcao == '11':
            diario_da_turma()
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução principal
if __name__ == "__main__":
    main()
