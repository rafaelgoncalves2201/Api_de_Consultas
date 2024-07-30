import json
import pandas as pd
import requests

# Pede o CNPJ para consulta
cn = input("Digite o CNPJ que deseja pesquisar: ")

# Remove caracteres especiais do CNPJ
cn = cn.replace("-", "").replace(".", "").replace("/", "")

if len(cn) == 14:
    # Acessa a API com o token
    #link = f'https://api.datastone.com.br/v1/company/list/?razao_social={cn}&uf=SP'
    #headers = {"Authorization": "Token 2a466789-1dc2-491f-9098-cbc99dcbed38"}

    # Obtém os dados da API
    response = requests.get(link, headers=headers)
    
    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200:
        # Converte a resposta JSON para um dicionário
        data = response.json()
        
        # Lista para armazenar os dados
        dados = []

        for registro in data:
            # Dicionário para armazenar os campos desejados
            dicionario_registro = {
                "Razão Social": registro.get("company_name", ""),
                "CNPJ": registro.get("cnpj", ""),
                "Endereço": f"{registro['addresses'][0]['city']}, {registro['addresses'][0]}" if registro.get("addresses") else "",
                "Cidade": registro['addresses'][0]['city'] if registro.get("addresses") else "",
                "CNAE": registro.get("cnae_description", ""),
                "Data de Abertura": registro.get("creation_date", ""),
                "Emails": ", ".join([email.get('email', "") for email in registro.get('emails', [])]),
                "Tipo (Filial/Matriz)": registro.get("headquarter_type", ""),
                "Telefone Fixo": ", ".join([f"({telefone['ddd']}) {telefone['number']}" for telefone in registro.get('land_lines', [])]),
                "Telefone Móvel": ", ".join([f"({telefone['ddd']}) {telefone['number']}" for telefone in registro.get('mobile_phones', [])]),
                "Sócios": ", ".join([f"{socio['name']}" for socio in registro.get('related_persons', [])])
            }
            # Adiciona o dicionário de registro à lista de dados
            dados.append(dicionario_registro)

        # Converte os dados em um DataFrame do pandas
        df = pd.DataFrame(dados)
        print(df)
    else:
        print("Erro ao acessar a API.")
else:
    print("CNPJ inválido.")
 
df = pd.DataFrame(dados)
        # Escreve o DataFrame em um arquivo Excel
with open("empresascnpj.json", "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)