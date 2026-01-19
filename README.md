# 🏦 Pipeline ETL - Mensagens Personalizadas Santander

Pipeline de ETL (Extract, Transform, Load) que gera mensagens personalizadas para clientes do Santander utilizando Inteligência Artificial (Google Gemini).

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do **Bootcamp Santander** e implementa um pipeline automatizado que:

- **Extrai** dados de clientes de um arquivo CSV
- **Transforma** os dados gerando mensagens personalizadas usando IA
- **Carrega** as mensagens geradas em um novo arquivo CSV

## 🚀 Funcionalidades

- ✅ Leitura automática de dados de clientes
- ✅ Geração de mensagens personalizadas com Google Gemini AI
- ✅ Exportação dos resultados em CSV
- ✅ Tratamento de erros e feedback em tempo real

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Google Gemini API** - IA Generativa para criar mensagens personalizadas
- **CSV** - Manipulação de arquivos de dados
- **genai** - Biblioteca oficial do Google para acesso à API Gemini

## 📦 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Conta Google Cloud com acesso à API Gemini
- Chave de API do Google Gemini

### Passos para instalação

1. **Clone o repositório:**

```bash
git clone <url-do-repositorio>
cd "etl-bootcamp-santander"
```

2. **Instale as dependências:**

```bash
pip install google-genai
```

3. **Configure sua API Key:**

Substitua a API Key no código por uma variável de ambiente:

```python
import os
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
```

E defina a variável no seu terminal:

```bash
export GOOGLE_API_KEY="sua-chave-aqui"
```

OBS: Eu gerei minha chave de API por meio do seguinte link: [Google AI Studio](https://aistudio.google.com/api-keys)

## 📂 Estrutura do Projeto

```
etl-bootcamp-santander/
│
├── etl_pipeline.py          # Script principal do pipeline ETL
├── dados_clientes.csv       # Arquivo de entrada com dados dos clientes
├── mensagens_clientes.csv   # Arquivo de saída com mensagens geradas
└── README.md                # Documentação do projeto
```

## 💾 Formato dos Arquivos

### dados_clientes.csv (Entrada)

```csv
Nome,Conta,Cartao
João Silva,12345-6,Gold
Maria Santos,78910-1,Platinum
```

### mensagens_clientes.csv (Saída)

```csv
nome,conta,mensagem
João Silva,12345-6,"Olá João! Como cliente Santander, você tem acesso a benefícios exclusivos..."
Maria Santos,78910-1,"Maria, aproveite todas as vantagens do seu cartão Platinum Santander..."
```

## 🎯 Como Usar

1. **Prepare o arquivo de entrada:**
   - Certifique-se de que `dados_clientes.csv` existe no diretório
   - O arquivo deve ter as colunas: Nome, Conta, Cartao

2. **Execute o pipeline:**

```bash
python etl_pipeline.py
```

3. **Acompanhe o processo:**
   - O script mostrará o progresso de cada etapa
   - Mensagens de status serão exibidas no terminal

4. **Verifique os resultados:**
   - As mensagens geradas estarão em `mensagens_clientes.csv`

## 🔄 Funcionamento do Pipeline

### 1️⃣ Extract (Extração)

```python
def extrair_dados(arquivo_entrada)
```

- Lê o arquivo CSV com dados dos clientes
- Converte os dados em uma lista de dicionários
- Retorna os dados estruturados para processamento

### 2️⃣ Transform (Transformação)

```python
def transformar_dados(clientes)
```

- Para cada cliente, gera uma mensagem personalizada
- Utiliza a API do Google Gemini para criar conteúdo único
- Aplica prompt engineering para mensagens profissionais

### 3️⃣ Load (Carregamento)

```python
def carregar_dados(mensagens, arquivo_saida)
```

- Salva as mensagens geradas em um novo arquivo CSV
- Mantém a estrutura organizada com nome, conta e mensagem
- Utiliza codificação UTF-8 para suportar acentos

## 👨‍💻 Autor

**Felipe Kucharski De Barbosa**

Desenvolvido durante o Bootcamp Santander 2025
