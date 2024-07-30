import json
import pandas as pd

def buscar_informacoes_empresa(razao_social_desejada, data):
    dados = []

    for registro in data:
        if registro["razao_social"].upper() == razao_social_desejada.upper():
            dicionario_registro = {
                "CNPJ": registro["cnpj"],
                "Razão Social": registro["razao_social"],
                "Cidade": registro["city"]
                # Adicione mais campos conforme necessário
            }
            dados.append(dicionario_registro)

    return dados

def buscar_cnpj_empresa(cnpj_desejado, data):
    dados = []

    for registro in data:
        if registro["cnpj"] == cnpj_desejado:
            dicionario_registro = {
                "CNPJ": registro["cnpj"],
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
            }
            dados.append(dicionario_registro)

    return dados

# Carregar os dados do arquivo JSON com informações das empresas
with open("empresasPALIN&MARTINS.json", "r") as f:
    data_razao_social = json.load(f)

# Definir a razão social desejada
razao_social_desejada = "PALIN & MARTINS ORGANIZACAO TRIBUTARIA LTDA"

# Buscar informações da empresa pelo nome
dados_empresa_razao_social = buscar_informacoes_empresa(razao_social_desejada, data_razao_social)

# Se encontrou a empresa pelo nome, obter o CNPJ dela
if dados_empresa_razao_social:
    cnpj_desejado = dados_empresa_razao_social[0]["CNPJ"]

    # Carregar os dados do arquivo JSON com informações das empresas por CNPJ
    with open("empresascnpjPALIN&MARTINS.json", "r") as f:
        data_cnpj = json.load(f)

    # Buscar informações da empresa pelo CNPJ
    dados_empresa_cnpj = buscar_cnpj_empresa(cnpj_desejado, data_cnpj)

    # Se encontrou a empresa pelo CNPJ, salvar os dados em um arquivo Excel
    if dados_empresa_cnpj:
        df = pd.DataFrame(dados_empresa_cnpj)
        df.to_excel("informacoes_empresa3.xlsx", index=False)
    else:
        print("Empresa não encontrada no JSON de CNPJ.")
else:
    print("Empresa não encontrada no JSON de razão social.")

