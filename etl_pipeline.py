import csv
from google import genai

# Configuração da API do Google Gemini
GOOGLE_API_KEY = "COLOQUE_SUA_CHAVE_AQUI"
client = genai.Client(api_key=GOOGLE_API_KEY)


# Extração/Extract
def extrair_dados(arquivo_entrada):
    clientes = []

    with open(arquivo_entrada, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            clientes.append(
                {
                    "nome": linha["Nome"],
                    "conta": linha["Conta"],
                    "cartao": linha["Cartao"],
                }
            )

    print(f"Foram encontrados {len(clientes)} clientes no arquivo de entrada.")

    return clientes


# Transformação/Transform
def gerar_mensagem_gemini(cliente):
    prompt = f"""Você é um assistente do banco Santander especializado em comunicação com clientes.

Crie uma mensagem personalizada curta e amigável para um cliente do banco Santander.
    
Informações do cliente:
- Nome: {cliente['nome']}
- Conta: {cliente['conta']}
- Cartão: {cliente['cartao']}

A mensagem deve:
- Ser acolhedora e profissional
- Mencionar que é cliente Santander
- Ter no máximo 2 frases
- Incentivar o uso dos serviços do banco"""

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Erro ao gerar mensagem para {cliente['nome']}: {e}")
        return f"Olá {cliente['nome']}! Obrigado por ser cliente Santander."


def transformar_dados(clientes):
    mensagens = []

    for i, cliente in enumerate(clientes, 1):
        print(f"Gerando mensagem {i}/{len(clientes)} para {cliente['nome']}...")

        mensagem_gerada = gerar_mensagem_gemini(cliente)

        mensagem = {
            "nome": cliente["nome"],
            "conta": cliente["conta"],
            "mensagem": mensagem_gerada,
        }
        mensagens.append(mensagem)

    return mensagens


# Carregamento/Load
def carregar_dados(mensagens, arquivo_saida):
    print(f"Salvando mensagens...")
    with open(arquivo_saida, mode="w", encoding="utf-8", newline="") as arquivo:
        campos = ["nome", "conta", "mensagem"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        for mensagem in mensagens:
            escritor.writerow(mensagem)

    print(f"{len(mensagens)} mensagens salvas com sucesso.")


# Script
def executar_pipeline():
    # Arquivos de entrada e saída
    arquivo_entrada = "dados_clientes.csv"
    arquivo_saida = "mensagens_clientes.csv"

    print("\nEtapa de Extração")
    clientes = extrair_dados(arquivo_entrada)

    print("\nEtapa de Transformação")
    mensagens = transformar_dados(clientes)

    print("\nEtapa de Carregamento")
    carregar_dados(mensagens, arquivo_saida)

    print("\nPipeline ETL finalizado.")

    print(f"As mensagens geradas foram salvas em {arquivo_saida}")


# Executa o pipeline ETL ao rodar o script
executar_pipeline()
