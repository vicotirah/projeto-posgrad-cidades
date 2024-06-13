# Módulo de Entrada de Dados
def entrada_dados_cidade():
    cidade = input("Digite o nome da cidade: ")
    dimensao = float(input("Digite a dimensão territorial da cidade (em km²): "))
    populacao = int(input("Digite a população da cidade: "))
    return cidade, dimensao, populacao

# Módulo que Informa a Cidade Mais Extensa
def cidade_mais_extensa(cidades):
    cidade_extensa = max(cidades, key=lambda x: x[1])
    return cidade_extensa[0]

# Módulo que Informa a Cidade Mais Populosa
def cidade_mais_populosa(cidades):
    cidade_populosa = max(cidades, key=lambda x: x[2])
    return cidade_populosa[0]

# Função que Calcula a Média da População
def calcular_media_populacao(cidades):
    total_populacao = sum(cidade[2] for cidade in cidades)
    media_populacao = total_populacao / len(cidades)
    return media_populacao

# Procedimento que Mostra Todas as Informações
def mostrar_informacoes_cidades(cidades):
    print("Informações das Cidades:")
    for cidade in cidades:
        print(f"Nome: {cidade[0]}, Dimensão Territorial: {cidade[1]} km², População: {cidade[2]}")

# Método Principal com Menu de Opções
def main():
    cidades = []

    while len(cidades) < 100:
        print("\nMenu de Opções:")
        print("1. Adicionar cidade")
        print("2. Identificar cidade mais extensa")
        print("3. Identificar cidade mais populosa")
        print("4. Calcular média da população do estado")
        print("5. Mostrar informações das cidades")
        print("6. Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))

            if opcao == 1:
                cidade = entrada_dados_cidade()
                cidades.append(cidade)
                print("Cidade adicionada com sucesso!")
            elif opcao == 2:
                if cidades:
                    extensa = cidade_mais_extensa(cidades)
                    print(f"A cidade mais extensa é: {extensa}")
                else:
                    print("Não há cidades cadastradas.")
            elif opcao == 3:
                if cidades:
                    populosa = cidade_mais_populosa(cidades)
                    print(f"A cidade mais populosa é: {populosa}")
                else:
                    print("Não há cidades cadastradas.")
            elif opcao == 4:
                if cidades:
                    media = calcular_media_populacao(cidades)
                    print(f"A média da população do estado é: {media:.2f}")
                else:
                    print("Não há cidades cadastradas.")
            elif opcao == 5:
                if cidades:
                    mostrar_informacoes_cidades(cidades)
                else:
                    print("Não há cidades cadastradas.")
            elif opcao == 6:
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
if __name__ == "__main__":
    main()
