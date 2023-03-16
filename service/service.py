from controller.restTemplate import restTemplateHelper
from controller.endpoint import endpoints
from model import parseResponse, names

url = "https://api.mercadolibre.com"

# Users
def userMe():
    response = restTemplateHelper.executeGet(url, endpoints.USER_ME)
    return parseResponse.download(response, names.USER_ME)

def visitas(userId, dateFrom, dateTo):
    endpoint = endpoints.VISITAS.replace("{{userId}}", userId).replace("{{dateFrom}}", dateFrom).replace("{{dateTo}}", dateTo)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.VISITAS.replace("{{userId}}", userId).replace("{{dateFrom}}", dateFrom).replace("{{dateTo}}", dateTo)
    return parseResponse.download(response, name)

# Concorrência
def detalhesConcorrencia(itemId):
    response = restTemplateHelper.executeGet(url, endpoints.DETALHES_CONCORRENCIA.replace("{{itemId}}", itemId))
    return parseResponse.download(response, names.DETALHES_CONCORRENCIA.replace("{{itemId}}", itemId))

def publicacoesCatalogo(productId):
    response = restTemplateHelper.executeGet(url, endpoints.PUBLICACOES_CATALOGO.replace("{{productId}}", productId))
    return parseResponse.download(response, names.PUBLICACOES_CATALOGO.replace("{{productId}}", productId))

def publicacaoGanhadora(productId):
    response = restTemplateHelper.executeGet(url, endpoints.PUBLICACAO_GANHADORA.replace("{{productId}}", productId))
    return parseResponse.download(response, names.PUBLICACAO_GANHADORA)

# Custos por venda
def precoPorTipo(price, listingTypeId):
    endpoint = endpoints.PRECO_POR_TIPO.replace("{{price}}", price).replace("{{listingTypeId}}", listingTypeId)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.PRECO_POR_TIPO.replace("{{price}}", price).replace("{{listingTypeId}}", listingTypeId)
    return parseResponse.download(response, name)

def precoPorCategoria(price, categoryId):
    endpoint = endpoints.PRECO_POR_CATEGORIA.replace("{{price}}", price).replace("{{categoryId}}", categoryId)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.PRECO_POR_CATEGORIA.replace("{{price}}", price).replace("{{categoryId}}", categoryId)
    return parseResponse.download(response, name)

# Preços produto
def precoProduto(itemId):
    response = restTemplateHelper.executeGet(url, endpoints.PRECO_PRODUTO.replace("{{itemId}}", itemId))
    name = names.PRECO_PRODUTO.replace("{{itemId}}", itemId)
    return parseResponse.download(response, name)

# Estoque Fullfilment
def estoqueVendedor(inventoryId):
    response = restTemplateHelper.executeGet(url, endpoints.ESTOQUE_VENDEDOR.replace("{{inventoryId}}", inventoryId))
    name = names.ESTOQUE_VENDEDOR.replace("{{inventoryId}}", inventoryId)
    return parseResponse.download(response, name)

def estoqueNaoDisponivel(inventoryId, attributes):
    endpoint = endpoints.ESTOQUE_VENDEDOR.replace("{{inventoryId}}", inventoryId).replace("{{attributes}}", attributes)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.ESTOQUE_VENDEDOR.replace("{{inventoryId}}", inventoryId).replace("{{attributes}}", attributes)
    return parseResponse.download(response, name)

# Promoção
def promocaoDisponivel(userId):
    response = restTemplateHelper.executeGet(url, endpoints.PROMOCOES_DISPONIVEIS.replace("{{userId}}", userId))
    name = names.PROMOCOES_DISPONIVEIS.replace("{{UserId}}", userId)
    return parseResponse.download(response, name)

def itensPromocao(promotionId, promotionType):
    endpoint = endpoints.ITENS_PROMOCAO.replace("{{promotionId}}", promotionId).replace("{{promotionType}}", promotionType)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.ITENS_PROMOCAO.replace("{{promotionId}}", promotionId).replace("{{promotionType}}", promotionType)
    return parseResponse.download(response, name)

def campanhaTradicional(promotionId):
    response = restTemplateHelper.executeGet(url, endpoints.PROMOCOES_DISPONIVEIS.replace("{{promotionId}}", promotionId))
    name = names.CONSULTAR_CAMPANHA_TRADICIONAL.replace("{{campanhaId}}", promotionId)
    return parseResponse.download(response, name)

# Reclamações e devoluções
def reclamacoesTotais():
    response = restTemplateHelper.executeGet(url, endpoints.RECLAMACOES_TOTAIS)
    return parseResponse.download(response, names.RECLAMACOES_TOTAIS)

# Métricas de tendências
def opinioesProduto(produto):
    response = restTemplateHelper.executeGet(url, endpoints.OPINIOES_PRODUTO.replace("{{item_id}}", produto))
    return parseResponse.download(response, names.OPINIOES_PRODUTO.replace("{{itemId}}", produto))

# Auth
def errorToken():
    return restTemplateHelper.errorToken()

def auth():
    return restTemplateHelper.auth_ml()