from flask import Flask, render_template, request, redirect, url_for
from config import Config
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user
import time

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

db = SQLAlchemy(app)

from service import userService, service

@app.route("/")
@login_required
def home():
    return render_template('home/home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/autenticar", methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']

    if userService.User.is_valid_credentials(db, email, senha):
        user = userService.User.load_user(email)
        login_user(user, remember=True)
        return redirect(url_for('home'))
    else:
        return 'Login invalido'
    
@login_manager.user_loader
def load_user(user_id):
    return userService.User.query.filter_by(id=user_id).first()

# USERS
@app.route("/me")
@login_required
def name():
    return service.userMe()

@app.route("/visitas/user/<userId>/dataInicio/<dataInicio>/dataFim/<dataFim>")
@login_required
def visitas(userId, dataInicio, dataFim):
    return service.visitas(userId, dataInicio, dataFim)

# Concorrência
@app.route("/concorrencia/detalheConcorrencia/<itemId>")
@login_required
def detalhesConcorrencia(itemId):
    return service.detalhesConcorrencia(itemId)

@app.route("/concorrencia/publicacoesCatalogo/<productId>")
@login_required
def publicacoesCatalogo(productId):
    return service.publicacoesCatalogo(productId)

@app.route("/concorrencia/publicacaoGanhadora/<productId>")
@login_required
def publicacaoGanhadora(productId):
    return service.publicacaoGanhadora(productId)

# Custos por venda
@app.route("/custoPorVenda/price/<price>/listingTypeId/<listingTypeId>")
@login_required
def precoPorTipo(price, listingTypeId):
    return service.precoPorTipo(price, listingTypeId)

@app.route("/custoPorVenda/price/<price>/categoryId/<categoryId>")
@login_required
def precoPorCategoria(price, categoryId):
    return service.precoPorCategoria(price, categoryId)

# Preços produto
@app.route("/precoProduto/<itemId>")
@login_required
def precoPreoduto(itemId):
    return service.precoProduto(itemId)

#Estoque Fullfilment
@app.route("/estoque/<inventoryId>")
@login_required
def estoqueVendedor(inventoryId):
    return service.estoqueVendedor(inventoryId)

@app.route("/estoque/<inventoryId>/atributos/<attributes>")
@login_required
def estoqueNaoDisponivel(inventoryId, attributes):
    return service.estoqueNaoDisponivel(inventoryId, attributes)

# Promoções
@app.route("/promocao/<userId>")
@login_required
def promocaoDisponivel(userId):
    return service.promocaoDisponivel(userId)

@app.route("/promocao/promocaoId/<promotionId>/tipo/<promotionType>")
@login_required
def itensPromocao(promotionId, promotionType):
    return service.itensPromocao(promotionId, promotionType)

@app.route("/promocao/campanhaTradicional/<promotionId>")
@login_required
def consultaCampanhaTradicional(promotionId):
    return service.campanhaTradicional(promotionId)

@app.route("/promocao/campanhaMl/<promotionId>/tipo/<promotionType>")
@login_required
def consultaCampanhaMl(promotionId, promotionType):
    return service.campanhaMl(promotionId, promotionType)

@app.route("/promocao/campanhaVolume/<promotionId>")
@login_required
def consultaCampanhaVolume(promotionId):
    return service.campanhaVolume(promotionId)

# Perguntas e Respostas 
@app.route("/perguntas/vendedor/<sellerId>")
@login_required
def perguntasRecebidas(sellerId):
    return service.perguntasRecebidas(sellerId)

@app.route("/perguntas/produto/<itemId>")
@login_required
def perguntasProduto(itemId):
    return service.perguntasProduto(itemId)

# Relatórios de faturamento
@app.route("/relatorio")
@login_required
def relatorio():
    return service.relatorio()

@app.route("/documento/periodo/<periodo>")
@login_required
def documentoPeriodo(periodo):
    return service.documento(periodo)

@app.route("/resumoFaturamento/periodo/<periodo>")
@login_required
def resumoFaturamento(periodo):
    return service.resumoFaturamento(periodo)

# Métricas de tendências
@app.route("/opinioes/produto/<produto>")
@login_required
def opinioesProduto(produto):
    return service.opinioesProduto(produto)

@app.route("/opinioes/produto/<produto>/catalogo/<catalogProductId>")
@login_required
def opinioesItemCatalogo(produto, catalogProductId):
    return service.opinioesItemCatalogo(produto, catalogProductId)

@app.route("/tendencias")
@login_required
def tendencias():
    return service.tendencias()

@app.route("/tendencias/categoria/<categoryId>")
@login_required
def tendenciasCategoria(categoryId):
    return service.tendenciasCategoria(categoryId)

@app.route("/qualidade/<itemId>")
@login_required
def qualidadeItem(itemId):
    return service.qualidadeItem(itemId)

@app.route("/melhorar-qualidade/<itemId>")
@login_required
def melhorarQualidadeItem(itemId):
    return service.melhorarQualidadeItem(itemId)

@app.route("/maisVendido/categoria/<categoryId>")
@login_required
def maisVendidoCategoria(categoryId):
    return service.maisVendidoCategoria(categoryId)

@app.route("/visitaTotal/anuncio/<itemId>")
@login_required
def visitasTotaisAnuncio(itemId):
    return service.visitasTotaisAnuncio(itemId)

# Reclamações e devoluções
@app.route("/reclamacoes")
@login_required
def reclamacoesTotais():
    return service.reclamacoesTotais()

@app.route("/devolucao/<claimId>")
def devolucaoProduto(claimId):
    return service.devolucaoProduto(claimId)


# Auth
@app.route("/errorToken")
@login_required
def errorToken():
    return service.errorToken()

@app.route("/auth")
@login_required
def auth():
    return service.auth()

# teste timeout
@app.route("/timeout")
def timeout():
    time.sleep(15)
    return "Hello, timeout!"
