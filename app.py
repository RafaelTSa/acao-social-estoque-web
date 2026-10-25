import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from database import inicializar_banco

app = Flask(__name__)

# Garante que o banco e as tabelas existam ao iniciar o servidor
inicializar_banco()

def conectar_banco():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row  # Permite aceder às colunas pelo nome (ex: item['nome'])
    return conexao

@app.route('/')
def home():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Busca todos os itens de estoque para exibir no dashboard de alertas
    estoque = cursor.execute("SELECT * FROM estoque ORDER BY data_vencimento ASC").fetchall()
    
    # Contadores para os cards do dashboard
    total_itens = sum(item['quantidade'] for item in estoque)
    familias = cursor.execute("SELECT COUNT(*) FROM beneficiarios").fetchone()[0]
    
    conexao.close()
    return render_template('index.html', estoque=estoque, total_itens=total_itens, familias=familias)

@app.route('/estoque', methods=['GET', 'POST'])
def estoque():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Se o formulário do modal for enviado (POST)
    if request.method == 'POST':
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        quantidade = request.form.get('quantidade')
        data_vencimento = request.form.get('data_vencimento')

        if nome and quantidade and data_vencimento:
            cursor.execute(
                "INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES (?, ?, ?, ?)",
                (nome, categoria, quantidade, data_vencimento)
            )
            conexao.commit()
        conexao.close()
        return redirect(url_for('estoque'))

    # Se for carregamento da página (GET)
    itens = cursor.execute("SELECT * FROM estoque ORDER BY data_vencimento ASC").fetchall()
    conexao.close()
    return render_template('estoque.html', itens=itens)

@app.route('/beneficiarios')
def beneficiarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    familias = cursor.execute("SELECT * FROM beneficiarios").fetchall()
    conexao.close()
    return render_template('beneficiarios.html', familias=familias)

if __name__ == '__main__':
    app.run(debug=True)