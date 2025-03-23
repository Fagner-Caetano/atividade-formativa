def buscar_nome(lista_nomes, nome_busca):
    """
    Função para buscar um nome em uma lista de nomes.
    
    Args:
        lista_nomes: Lista contendo os nomes.
        nome_busca: Nome que deseja encontrar.
        
    Returns:
        True se o nome for encontrado, False caso contrário.
    """
    return nome_busca.lower() in (nome.lower() for nome in lista_nomes)


def exibir_mensagem(msg, cor="\033[0m"):
    """Exibe uma mensagem formatada com cor no terminal."""
    print(f"{cor}{msg}\033[0m")


# Lista de nomes cadastrados
nomes = ["Maria", "João", "Pedro", "Ana", "Carlos"]

# Cores ANSI
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"

# Cabeçalho
exibir_mensagem("\n=== Sistema de Busca de Nomes ===", AZUL)

# Loop principal
while True:
    nome_para_buscar = input("\nDigite o nome que deseja buscar: ").strip()

    if buscar_nome(nomes, nome_para_buscar):
        exibir_mensagem(f"O nome '{nome_para_buscar}' foi encontrado na lista!", VERDE)
        break  # Sai do loop se encontrar o nome
    else:
        exibir_mensagem(f"O nome '{nome_para_buscar}' não foi encontrado na lista.", VERMELHO)
        continuar = input("Deseja tentar outro nome? (s/n): ").strip().lower()

        if continuar != 's':
            exibir_mensagem("\nObrigado por usar o sistema. Até logo!", AZUL)
            break  # Sai do loop se o usuário não quiser continuar
