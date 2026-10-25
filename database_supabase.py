import os
import psycopg2

# Cola aqui a tua URL do Supabase (ou usa variável de ambiente)
SUPABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:AcaoSocial2026@db.gnmbdwtbnyuoapzmcwtx.supabase.co:5432/postgres")

def conectar_banco():
    # Conecta ao PostgreSQL do Supabase
    conexao = psycopg2.connect(SUPABASE_URL, sslmode='require')
    return conexao

def inicializar_banco():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # 1. Tabela de Estoque
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estoque (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            categoria VARCHAR(50) NOT NULL,
            quantidade INT NOT NULL,
            data_vencimento VARCHAR(20) NOT NULL
        )
    ''')

    # 2. Tabela de Beneficiários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS beneficiarios (
            id SERIAL PRIMARY KEY,
            nome_responsavel VARCHAR(100) NOT NULL,
            membros INT NOT NULL,
            bairro VARCHAR(50) NOT NULL,
            ultima_retirada VARCHAR(20) NOT NULL
        )
    ''')

    # Inserir dados iniciais se as tabelas estiverem vazias
    cursor.execute("SELECT COUNT(*) FROM estoque")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES ('Arroz Agulhinha 5kg', 'Grãos / Cereais', 30, '2026-12-10')")
        cursor.execute("INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES ('Feijão Carioca 1kg', 'Grãos / Cereais', 15, '2026-10-28')")

    cursor.execute("SELECT COUNT(*) FROM beneficiarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO beneficiarios (nome_responsavel, membros, bairro, ultima_retirada) VALUES ('Maria Aparecida da Silva', 4, 'Vila São Pedro', '10/10/2026')")

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Tabelas criadas e configuradas com sucesso no Supabase!")

if __name__ == '__main__':
    inicializar_banco()