import json
import pandas as pd
import requests

# Pede o CNPJ para consulta
cn = input("Digite o CNPJ que deseja pesquisar: ")

# Remove caracteres especiais do CNPJ



# Acessa a API com o token
#link = f'https://api.datastone.com.br/v1/company/list/?razao_social={cn}&uf=SP'
#headers = {"Authorization": "Token 2a466789-1dc2-491f-9098-cbc99dcbed38"}

# Obtém os dados da API
response = requests.get(link, headers=headers)
    
# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta JSON para um dicionário
        data = response.json()

        # Escreve os dados em um arquivo JSON
        with open("empresas5.json", "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print("Dados salvos em empresas.json com sucesso!")
else:
    print("Erro ao acessar a API.")

