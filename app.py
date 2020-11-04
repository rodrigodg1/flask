from flask import Flask,render_template,request,redirect,session,flash

app = Flask(__name__)
app.secret_key="teste"


class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 =  Jogo("Dragon Ball","Acao","PC")
jogo2 = Jogo("Super Mario","Aventura","PS3")
jogo3 = Jogo("PES","Esporte","PS4")
lista = [jogo1,jogo2,jogo3]

@app.route('/')
def index():

    return render_template('lista.html',titulo="Jogos",
    jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',]) 
def autenticar():
    if request.form['senha'] == 'mestra':
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + "logou com sucesso!")
        return redirect('/')
    else:
        flash("Dados invalidos !")
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuaario_logado']=None
    flash('Nenhum usuario logado!')
    return redirect('/')
app.run(host='0.0.0.0',debug=True)