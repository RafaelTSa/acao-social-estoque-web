import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, redirect, url_for
from database_supabase import inicializar_banco, SUPABASE_URL

app = Flask(__name__)

# Inicializa as tabelas na nuvem ao iniciar
try:
    inicializar_banco()
except Exception as e:
    print("Erro ao inicializar banco:", e)

def conectar_banco():
    conexao = psycopg2.connect(SUPABASE_URL, sslmode='require', cursor_factory=RealDictCursor)
    return conexao

@app.route('/')
def home():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM estoque ORDER BY data_vencimento ASC")
        estoque = cursor.fetchall()
        
        total_itens = sum(item['quantidade'] for item in estoque)
        
        cursor.execute("SELECT COUNT(*) as total FROM beneficiarios")
        res_familias = cursor.fetchone()
        familias = res_familias['total'] if res_familias else 0
        
        conexao.close()
        return render_template('index.html', estoque=estoque, total_itens=total_itens, familias=familias)
    except Exception as e:
        print("Erro na rota home:", e)
        return render_template('index.html', estoque=[], total_itens=0, familias=0)

@app.route('/estoque', methods=['GET', 'POST'])
def estoque():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    if request.method == 'POST':
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        quantidade = request.form.get('quantidade')
        data_vencimento = request.form.get('data_vencimento')

        if nome and quantidade and data_vencimento:
            cursor.execute(
                "INSERT INTO estoque (nome, categoria, quantidade, data_vencimento) VALUES (%s, %s, %s, %s)",
                (nome, categoria, quantidade, data_vencimento)
            )
            conexao.commit()
        conexao.close()
        return redirect(url_for('estoque'))

    cursor.execute("SELECT * FROM estoque ORDER BY data_vencimento ASC")
    itens = cursor.fetchall()
    conexao.close()
    return render_template('estoque.html', itens=itens)

@app.route('/beneficiarios', methods=['GET', 'POST'])
def beneficiarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    if request.method == 'POST':
        nome_responsavel = request.form.get('nome_responsavel')
        membros = request.form.get('membros')
        bairro = request.form.get('bairro')
        ultima_retirada = request.form.get('ultima_retirada')

        if nome_responsavel and membros and bairro:
            cursor.execute(
                "INSERT INTO beneficiarios (nome_responsavel, membros, bairro, ultima_retirada) VALUES (%s, %s, %s, %s)",
                (nome_responsavel, membros, bairro, ultima_retirada or 'Primeira Entrega')
            )
            conexao.commit()
        conexao.close()
        return redirect(url_for('beneficiarios'))

    cursor.execute("SELECT * FROM beneficiarios")
    familias = cursor.fetchall()
    conexao.close()
    return render_template('beneficiarios.html', familias=familias)

if __name__ == '__main__':
    app.run(debug=True)