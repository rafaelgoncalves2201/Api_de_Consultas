# Importações necessarias 
import requests
import pandas as pd

# Variaveis
nome_socios = []

# Entrada de dados
cnpj = input("Digite o cnpj que deseja pesquisar: ")

# Trata a entrada de dados para ficar assim 9999999999999 conforme solicita a API
cn = cnpj.replace(".", "").replace("'", "").replace("-", "").replace("/", "").replace("_", "").replace("&", "")

# Token para acesso a API de consulta
token = "87df04458e30c64eeb8eac4a0348b6483d90e76c"

# Junta a entrada de dados com o link e o token da api para a consulta
link = f"https://www.empresaqui.com.br/api/{token}/{cn}"

# Faz a pesquisa do link
response = requests.get(link)

# Converte o conteudo para Json
data = response.json()


# Aqui a gente ta pegando as informações do Json
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

# Aqui fiz um loop para pegar todos os socios que tiver
for chave in data:
    if chave.isdigit():
        socio = data[chave]
        nome_socio = socio.get('socios_nome')
        if nome_socio:
            nome_socios.append(nome_socio)

# Aqui estou usando o pandas para criar um dataframe e por as informações nume planilha
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

# Estou usando o pandas para salvar a planilha com o nome desejado
df.to_excel('Informações.xlsx', index=False)

# Aqui estou enviando uma mensagem para o usuario ficar sabendo que finalizou o processo
print("Processo Finalizado com sucesso")
