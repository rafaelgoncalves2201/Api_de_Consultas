import requests
import json
import jmespath
import pandas as pd

nome_socios = []

cnpj = input("Digite o cnpj que deseja pesquisar: ")
token = "00cf4010b59bda8955c84e27296f715fdbfce7b0"
link = f"https://www.empresaqui.com.br/api/{token}/{cnpj}"

response = requests.get(link)
data = response.json()

# with open("Palin.json" ) as arq:
#     data = json.load(arq)

razao_social = data.get("razao")
cn = data.get("cnpj")
telefone1 = f"{data.get('ddd_1')}{data.get('tel_1')}"
telefone2 = f"{data.get('ddd_2')}{data.get('tel_2')}"
email = data.get("email")
cnae1 = data.get("cnae_principal")
cnae2 = data.get("cnae_secundario")
cidade = data.get("log_municipio")
data_abertura = data.get("data_abertura")
situacao = data.get("situacao_cadastral")
for chave in data:
    if chave.isdigit():  # Verifica se a chave é um número
        socio = data[chave]
        nome_socio = socio.get('socios_nome')
        if nome_socio:
            nome_socios.append(nome_socio)
df = pd.DataFrame({
    "Razão Social": [razao_social],
    "CNPJ": [cn],
    "Telefone": [telefone1 + telefone2],
    "Email": [email],
    "Cnae": [cnae1 + cnae2],
    "Cidade": [cidade],
    "Data abertura": [data_abertura],
    "Situação Empresa": [situacao],
    "Sócios": [", ".join(nome_socios)]
})
df.to_excel('Informações.xlsx', index=False)
print("Processo Finalizado com sucesso")