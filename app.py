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

# Perguntas e Respostas 
@app.route("/perguntas/vendedor/<sellerId>")
def perguntasRecebidas(sellerId):
    return service.perguntasRecebidas(sellerId)

@app.route("/perguntas/produto/<itemId>")
def perguntasProduto(itemId):
    return service.perguntasProduto(itemId)

# Relatórios de faturamento
@app.route("/relatorio")
def relatorio():
    return service.relatorio()

@app.route("/documento/periodo/<periodo>")
def documentoPeriodo(periodo):
    return service.documento(periodo)

@app.route("/resumoFaturamento/periodo/<periodo>")
def resumoFaturamento(periodo):
    return service.resumoFaturamento(periodo)

# Métricas de tendências
@app.route("/opinioes/produto/<produto>")
def opinioesProduto(produto):
    return service.opinioesProduto(produto)

@app.route("/opinioes/produto/<produto>/catalogo/<catalogProductId>")
def opinioesItemCatalogo(produto, catalogProductId):
    return service.opinioesItemCatalogo(produto, catalogProductId)

@app.route("/tendencias")
def tendencias():
    return service.tendencias()

@app.route("/tendencias/categoria/<categoryId>")
def tendenciasCategoria(categoryId):
    return service.tendenciasCategoria(categoryId)

@app.route("/qualidade/<itemId>")
def qualidadeItem(itemId):
    return service.qualidadeItem(itemId)

@app.route("/melhorar-qualidade/<itemId>")
def melhorarQualidadeItem(itemId):
    return service.melhorarQualidadeItem(itemId)

@app.route("/maisVendido/categoria/<categoryId>")
def maisVendidoCategoria(categoryId):
    return service.maisVendidoCategoria(categoryId)

@app.route("/visitaTotal/anuncio/<itemId>")
def visitasTotaisAnuncio(itemId):
    return service.visitasTotaisAnuncio(itemId)

# Reclamações e devoluções
@app.route("/reclamacoes")
def reclamacoesTotais():
    return service.reclamacoesTotais()

def devolucaoProduto(claimId):
    return service.devolucaoProduto(claimId)


# Auth
@app.route("/redirect")
def redirect():
    return service.errorToken()

@app.route("/auth")
def auth():
    return service.auth()

