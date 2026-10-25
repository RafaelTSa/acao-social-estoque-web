import sqlite3

def inicializar_banco():
    # Conecta ou cria o arquivo do banco de dados SQLite
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # 1. Tabela de Estoque de Alimentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            data_vencimento TEXT NOT NULL
        )
    ''')

    # 2. Tabela de Beneficiários (Famílias)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS beneficiarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_responsavel TEXT NOT NULL,
            membros INTEGER NOT NULL,
            bairro TEXT NOT NULL,
            ultima_retirada TEXT NOT NULL
        )
    ''')

    # Inserir alguns dados iniciais de exemplo se as tabelas estiverem vazias
    cursor.execute("SELECT COUNT(*) FROM estoque")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES ('Arroz Agulhinha 5kg', 'Grãos / Cereais', 30, '2026-12-10')")
        cursor.execute("INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES ('Feijão Carioca 1kg', 'Grãos / Cereais', 15, '2026-10-28')")
        cursor.execute("INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES ('Leite Integral (Caixa)', 'Laticínios', 24, '2026-11-15')")
        cursor.execute("INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES ('Macarrão Galo 500g', 'Massas', 8, '2026-10-25')")

    cursor.execute("SELECT COUNT(*) FROM beneficiarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO beneficiarios (nome_responsavel, membros, bairro, ultima_retirada) VALUES ('Maria Aparecida da Silva', 4, 'Vila São Pedro', '10/10/2026')")
        cursor.execute("INSERT INTO beneficiarios (nome_responsavel, membros, bairro, ultima_retirada) VALUES ('José Carlos de Oliveira', 3, 'Vila São Pedro', '12/10/2026')")
        cursor.execute("INSERT INTO beneficiarios (nome_responsavel, membros, bairro, ultima_retirada) VALUES ('Ana Lúcia Santos', 5, 'Parque Selecta', '15/09/2026')")

    conexao.commit()
    conexao.close()
    print("Banco de dados SQLite inicializado com sucesso!")

if __name__ == '__main__':
    inicializar_banco()