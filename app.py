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

@app.route("/custoPorVenda/price/<price>/categoryId/<categoryId>")
def precoPorCategoria(price, categoryId):
    return service.precoPorCategoria(price, categoryId)

# Preços produto
@app.route("/precoProduto/<itemId>")
def precoPreoduto(itemId):
    return service.precoProduto(itemId)

#Estoque Fullfilment
@app.route("/estoque/<inventoryId>")
def estoqueVendedor(inventoryId):
    return service.estoqueVendedor(inventoryId)

@app.route("/estoque/<inventoryId>/atributos/<attributes>")
def estoqueNaoDisponivel(inventoryId, attributes):
    return service.estoqueNaoDisponivel(inventoryId, attributes)

# Promoções
@app.route("/promocao/<userId>")
def promocaoDisponivel(userId):
    return service.promocaoDisponivel(userId)

@app.route("/promocao/promocaoId/<promotionId>/tipo/<promotionType>")
def itensPromocao(promotionId, promotionType):
    return service.itensPromocao(promotionId, promotionType)

@app.route("/promocao/campanhaTradicional/<promotionId>")
def consultaCampanhaTradicional(promotionId):
    return service.campanhaTradicional(promotionId)

@app.route("/promocao/campanhaMl/<promotionId>/tipo/<promotionType>")
def consultaCampanhaMl(promotionId, promotionType):
    return service.campanhaMl(promotionId, promotionType)

@app.route("/promocao/campanhaVolume/<promotionId>")
def consultaCampanhaVolume(promotionId):
    return service.campanhaVolume(promotionId)

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

