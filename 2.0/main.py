from flask import Flask , render_template, request,redirect
import bancoDados
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/login", methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    for index,adm in bancoDados.usuario.items():
        if usuario == adm[0] and senha == adm[1]:
            return "logou"
        else:
            print("Erro")
            return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)