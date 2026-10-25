# 📦 Ação Social - Gestão de Estoque e Beneficiários (UFBRA)

Sistema web desenvolvido como Projeto de Extensão Universitária para a **Paróquia São Pedro e São Paulo** (Vila São Pedro - São Bernardo do Campo/SP). A aplicação permite o controle de entrada e saída de doações de alimentos e o cadastro de famílias beneficiadas.

🔗 **Aplicação em Produção:** [https://acao-social-estoque-web.onrender.com](https://acao-social-estoque-web.onrender.com)

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Framework Web:** Flask 3.0
* **Servidor de Aplicação:** Gunicorn
* **Banco de Dados:** PostgreSQL (Supabase) via `psycopg2-binary`
* **Hospedagem / Cloud:** Render (Web Service)
* **Front-end:** HTML5, CSS3, Bootstrap / Tailwind CSS

---

## 📌 Funcionalidades

- [x] **Dashboard:** Visão geral do total de alimentos em estoque e famílias atendidas.
- [x] **Controle de Estoque:** Cadastro de doações de alimentos, categorias e controle de datas de vencimento.
- [x] **Gestão de Beneficiários:** Registro de responsáveis familiares, quantidade de membros e bairros atendidos.
- [x] **Persistência na Nuvem:** Conexão segura com banco de dados relacional PostgreSQL via Supabase Session Pooler.

---

## 🛠️ Como rodar o projeto localmente

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/RafaelTSa/acao-social-estoque-web.git](https://github.com/RafaelTSa/acao-social-estoque-web.git)
   cd acao-social-estoque-web

---

1. Criar e ativar o ambiente virtual:

    Bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

---

2. Instalar as dependências:

    Bash
p   ip install -r requirements.txt

---

3. Configurar as Variáveis de Ambiente:
Crie um arquivo .env na raiz do projeto contendo:

    Snippet de código
    DATABASE_URL=postgresql://postgres:[SUA_SENHA]@[aws-0-us-east-2.pooler.supabase.com:6543/postgres](https://aws-0-us-east-2.pooler.supabase.com:6543/postgres)

---

4. Executar a aplicação:

    Bash
    python app.py

---

5. Acesse no navegador: http://127.0.0.1:5000

---

📍 Informações do Projeto Extensionista
Instituição: UFBRA

Desenvolvedor: Rafael Teixeira dos Santos

Comunidade Atendida: Vila São Pedro, São Bernardo do Campo - SP