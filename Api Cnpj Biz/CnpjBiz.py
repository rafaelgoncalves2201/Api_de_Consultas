import json
import jmespath
import pandas as pd
import requests

nome_socios = []
numeros_de_telefone = []
# cn = input("Digite o CNPJ que deseja pesquisar: ")
# cnpj = cn.replace(".", " ").replace("'", " ").replace("-", " ").replace("/", " ").replace("_", " ").replace("&", " ")


# token = 'oHhXK4iUjztEkrZwQsZG8CEvT0faY3MJOlWybq4dZSuCXlHHviWONnrhwghO'

# url = "https://cnpj.biz/api/v2/empresas/cnpj"

# payload = json.dumps({
#   "cnpj": f'{cnpj}'
# })
# headers = {
#   'Content-Type': 'application/json',
#   'authorization': f'Bearer {token}',
#   'Accept': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)
# data = response.json()  

with open("BuscaCNPJ.json") as arq:
    data = json.load(arq)
        
razao_social = data.get("razao_social")
cnpj = data.get("cnpj")
for telefone in data['telefones']:
    numero = telefone['telefone']
    numeros_de_telefone.append(numero)

email = data.get("email")
data_abertura = data.get("data_abertura")
cidade = jmespath.search('endereco.cidade.nome', data)
cnae_principal = jmespath.search('atividades.principal[0].nome', data)
cnae_secundario = jmespath.search('atividades.secundaria[0].nome', data)
situacao = data.get("situacao")

for socio in data["socios"]:
    nome_socio = socio["nome"]
    nome_socios.append(nome_socio)
    
cnae_principal = cnae_principal or ""
cnae_secundario = cnae_secundario or ""

# Criar o DataFrame com os dados coletados
df = pd.DataFrame({            
    "Razão Social": [razao_social], 
    "CNPJ": [cnpj], 
    "Telefone": [", ".join(numeros_de_telefone)],
    "Email": [email], 
    "Data Abertura": [data_abertura],
    "Situação Cadastral": [situacao], 
    "Cidade": [cidade], 
    "Cnae": [cnae_principal + ", " + cnae_secundario], 
    "Socio": [", ".join(nome_socios)]
})

# Salvar o DataFrame em um arquivo Excel
df.to_excel('Informações_empresas.xlsx', index=False)
print("Processo concluído")