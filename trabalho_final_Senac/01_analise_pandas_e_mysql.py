import pandas as pd
from sqlalchemy import create_engine

# ==============================================================================
# 1. CARREGAMENTO DOS DADOS DA LOCALIZA&CO (2025)
# ==============================================================================
print("1. Lendo os dados comerciais da Localiza&Co...")

# Nome exato do ficheiro CSV presente na sua pasta
NOME_ARQUIVO = r"C:\\Users\\elain\\OneDrive\\Documentos\\UC2\\trabalho_final_Senac\\LocalizaCo_Dados_Comerciais_2025 - Resumo_Comercial_2025.csv"

# Lendo o ficheiro CSV com Pandas
df = pd.read_csv(NOME_ARQUIVO)

print("   Dados carregados com sucesso! Total de registros:", len(df))


# ==============================================================================
# 2. ANÁLISE ESTATÍSTICA E TRATAMENTO COM PANDAS
# ==============================================================================
print("\n2. Executando análise exploratória e tratamento com Pandas...")

# Exibir informações das colunas
print("\n--- Estrutura das Colunas ---")
print(df.info())

# Exibir as primeiras 5 linhas
print("\n--- Exemplo de Dados ---")
print(df.head())

# Exibir estatísticas descritivas
print("\n--- Estatística Descritiva ---")
print(df.describe(include='all'))


# ==============================================================================
# 3. CONEXÃO E CARGA NO BANCO DE DADOS MYSQL
# ==============================================================================
print("\n3. Conectando ao MySQL e gravando os dados...")

# CONFIGURAÇÃO DE ACESSO AO MYSQL
# Substitua 'sua_senha' pela senha do seu utilizador no MySQL Workbench / DBeaver
USUARIO = "root"
SENHA = "082304"
HOST = "localhost"
PORTA = "3306"
BANCO = "projeto_bigdata"

# Criar a conexão com o banco de dados
string_conexao = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"
engine = create_engine(string_conexao)

# Exportar o DataFrame direto para a tabela do MySQL
df.to_sql(name="tb_comercial_localiza", con=engine, if_exists="replace", index=False)

print("   Tabela 'tb_comercial_localiza' gravada com sucesso no MySQL!")


# ==============================================================================
# 4. CONSULTA ESTRATÉGICA DE CONFIRMAÇÃO NO MYSQL
# ==============================================================================
print("\n4. Confirmando a carga de dados via consulta SQL...")

query = "SELECT * FROM tb_comercial_localiza LIMIT 10;"
resultado = pd.read_sql(query, con=engine)
print(resultado)

print("\nProcesso concluído com sucesso!")
