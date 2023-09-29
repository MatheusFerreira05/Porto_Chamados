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
            return redirect('/form')
        else:
            print("Erro")
            return redirect('/')

@app.route("/form")
def form_page():
    return render_template('form.html')

@app.route("/chamado",methods=["POST"])
def form():
    apolice = request.form.get('apolice')
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    veiculo = request.form.get("veiculo")
    placa = request.form.get("placa")
    cep = request.form.get("cep")
    numero = request.form.get("numero")
    estado_veiculo = request.form.get("estado_veiculo")
    tipo_acidente = request.form.get("tipo_acidente")
    extra = request.form.get("possui_extra")
    locomover = request.form.get("consegue_locomover")
    lista = [apolice,nome,cpf,veiculo,placa,cep,numero,estado_veiculo,tipo_acidente,extra,locomover]
    for index,lista in bancoDados.apolices.items():
        if apolice == lista[1]:
            return modal(lista)
        else:
            return render_template('form.html')
        
@app.route("/modal")
def modal(lista):
    if lista[9] == None and lista[10] == None:
        return render_template('modal.html',apolice = lista[0],nome = lista[1],cpf = lista[2],veiculo = lista[3],placa = lista[4],cep = lista[5],numero = lista[6],estado_veiculo = lista[7],tipo_acidente = lista[8],extra = "Não",locomover = "Não")
if __name__ == "__main__":
    app.run(debug=True)