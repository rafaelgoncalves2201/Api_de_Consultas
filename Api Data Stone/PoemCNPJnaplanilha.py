import json
import pandas as pd

cn = "PALIN & MARTINS CONSULTORES ASSOCIADOS LTDA"



# Abre o arquivo JSON
with open("empresasPALIN&MARTINS.json", "r") as f:
    # Lê e desserializa o conteúdo do arquivo JSON
    data = json.load(f)

if ( cn == cn):
    # Define uma lista de dicionários para armazenar os dados
    dados = []

    # Itera sobre os registros no JSON
    for registro in data:
        # Extrai os campos desejados e os armazena em um dicionário
        dicionario_registro = {            
            """
            "Razão Social": registro["company_name"],
            "Endereço": f"{registro['addresses'][0]['city']}, {registro['addresses'][0]['district']}",
            "Cidade": registro['addresses'][0]['city'],
            "CNAE": registro["cnae_description"],
            "Data de Abertura": registro["creation_date"],
            "Emails": ", ".join([email['email'] for email in registro['emails']]),
            "Tipo (Filial/Matriz)": registro["headquarter_type"],
            "Telefone Fixo": ", ".join([f"({telefone['ddd']}) {telefone['number']}" for telefone in registro.get('land_lines', [])]),
            "Telefone Móvel": ", ".join([f"({telefone['ddd']}) {telefone['number']}" for telefone in registro.get('mobile_phones', [])]),
            "Sócios": ", ".join([f"{socio['name']}" for socio in registro.get('related_persons', [])])
            """
            
            
        }
        # Adiciona o dicionário de registro à lista de dados
        dados.append(dicionario_registro)
        
else :
    print('Cn não encontrado')

    # Cria um DataFrame pandas com os dados
df = pd.DataFrame(dados)

    # Escreve o DataFrame em um arquivo Excel
df.to_excel("informacoes_empresas2.xlsx", index=False)