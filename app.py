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

# Concorrência
@app.route("/concorrencia/detalheConcorrencia/<itemId>")
def detalhesConcorrencia(itemId):
    return service.detalhesConcorrencia(itemId)

@app.route("/concorrencia/publicacoesCatalogo/<productId>")
def publicacoesCatalogo(productId):
    return service.publicacoesCatalogo(productId)

@app.route("/concorrencia/publicacaoGanhadora/<productId>")
def publicacaoGanhadora(productId):
    return service.publicacaoGanhadora(productId)

# Custos por venda
@app.route("/custoPorVenda/price/<price>/listingTypeId/<listingTypeId>")
def precoPorTipo(price, listingTypeId):
    return service.precoPorTipo(price, listingTypeId)

# Reclamações e devoluções
@app.route("/reclamacoes")
def reclamacoesTotais():
    return service.reclamacoesTotais()

# Métricas de tendências
@app.route("/opinioes/produto/<produto>")
def opinioesProduto(produto):
    return service.opinioesProduto(produto)

# Auth
@app.route("/redirect")
def redirect():
    return service.errorToken()

@app.route("/auth")
def auth():
    return service.auth()

