def buscar_nome(lista_nomes, nome_busca):
    """
    Função para buscar um nome em uma lista de nomes.
    
    Args:
        lista_nomes: Lista contendo os nomes
        nome_busca: Nome que deseja encontrar
        
    Returns:
        True se o nome for encontrado, False caso contrário
    """
    # Convertendo o nome buscado para minúsculo para comparação
    nome_busca = nome_busca.lower()
    
    # Verificando se o nome está na lista
    for nome in lista_nomes:
        if nome.lower() == nome_busca:
            return True
            
    # Se chegou aqui, o nome não foi encontrado
    return False


# Exemplo de uso
nomes = ["Maria", "João", "Pedro", "Ana", "Carlos"]

# Loop principal
while True:
    nome_para_buscar = input("Digite o nome que deseja buscar: ")
    
    if buscar_nome(nomes, nome_para_buscar):
        print(f"O nome '{nome_para_buscar}' foi encontrado na lista!")
        break  # Sai do loop se encontrar o nome
    else:
        print(f"O nome '{nome_para_buscar}' não foi encontrado na lista.")
        continuar = input("Deseja tentar outro nome? (s/n): ").lower()
        
        if continuar != 's':
            print("Busca encerrada.")
            break  # Sai do loop se o usuário não quiser continuar)