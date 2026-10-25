from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/beneficiarios')
def beneficiarios():
    return render_template('beneficiarios.html')

if __name__ == '__main__':
    app.run(debug=True)