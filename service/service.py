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