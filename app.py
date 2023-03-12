from flask import Flask
from service import service

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Mercado Livre!"

# USERS
@app.route("/me")
def name():
    return service.userMe()

@app.route("/visitas/user/<userId>/dataInicio/<dataInicio>/dataFim/<dataFim>")
def visitas(userId, dataInicio, dataFim):
    return service.visitas(userId, dataInicio, dataFim)


@app.route("/reclamacoes")
def reclamacoesTotais():
    return service.reclamacoesTotais()

@app.route("/opinioes/produto/<produto>")
def opinioesProduto(produto):
    return service.opinioesProduto(produto)

@app.route("/redirect")
def redirect():
    return service.errorToken()

@app.route("/auth")
def auth():
    return service.auth()

