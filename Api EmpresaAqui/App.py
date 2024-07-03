# Importações necessarias 
import requests
import os
import pandas as pd

print("------Menu------")
print("1. Pesquisar CNPJ")
print("2. Sair")
        
escolha = input("Digite sua opção: ")

if escolha == '1':
    while True:
        # Variaveis
        nome_socios = []

        # Entrada de dados
        cnpj = input("Digite o cnpj que deseja pesquisar: ")

        # Trata a entrada de dados para ficar assim 9999999999999 conforme solicita a API
        cn = cnpj.replace(".", "").replace("'", "").replace("-", "").replace("/", "").replace("_", "").replace("&", "")
        if len(cn) == 14:
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
            cnae = data.get("cnae_principal")
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
                        
            if os.path.exists('Informações.xlsx'):
                df_antigo = pd.read_excel('Informações.xlsx')
            else:
                df_antigo = pd.DataFrame()

            # Aqui estou usando o pandas para criar um dataframe e por as informações nume planilha
            df = pd.DataFrame({
                "Razão Social": [razao_social],
                "CNPJ": [cn],
                "Telefone": [telefone1 + " " + telefone2],
                "Email": [email],
                "Cnae": [cnae],
                "Cidade": [cidade],
                "Data abertura": [data_abertura],
                "Situação Empresa": [situacao],
                "Sócios": [", ".join(nome_socios)]
            })

            df = pd.concat([df_antigo, df], ignore_index=True)

            # Estou usando o pandas para salvar a planilha com o nome desejado
            df.to_excel('Informações.xlsx', index=False)

            # Aqui estou enviando uma mensagem para o usuario ficar sabendo que finalizou o processo
            print("Processo Finalizado com sucesso")
            outra_consulta = input("Deseja consultar outro CNPJ? (s/n): ")
            if outra_consulta.lower() != 's':
                print("Fechando aplicação")
                break
        else:
            print("Cnpj não identificado digite novamente")
            
elif escolha == '2':
    print("Encerrando")
else:
    print("Opção invalida.")
