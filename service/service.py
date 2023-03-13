from controller.restTemplate import restTemplateHelper
from controller.endpoint import endpoints
from model import parseResponse, names

url = "https://api.mercadolibre.com"

# Users
def userMe():
    response = restTemplateHelper.executeGet(url, endpoints.USER_ME)
    csv = parseResponse.download(response, names.USER_ME)
    return csv

def visitas(userId, dateFrom, dateTo):
    endpoint = endpoints.VISITAS.replace("{{userId}}", userId).replace("{{dateFrom}}", dateFrom).replace("{{dateTo}}", dateTo)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.VISITAS.replace("{{userId}}", userId).replace("{{dateFrom}}", dateFrom).replace("{{dateTo}}", dateTo)
    csv = parseResponse.download(response, name)
    return csv

# Concorrência
def detalhesConcorrencia(itemId):
    response = restTemplateHelper.executeGet(url, endpoints.DETALHES_CONCORRENCIA.replace("{{itemId}}", itemId))
    csv = parseResponse.download(response, names.DETALHES_CONCORRENCIA.replace("{{itemId}}", itemId))
    return csv

def publicacoesCatalogo(productId):
    response = restTemplateHelper.executeGet(url, endpoints.PUBLICACOES_CATALOGO.replace("{{productId}}", productId))
    csv =  parseResponse.download(response, names.PUBLICACOES_CATALOGO.replace("{{productId}}", productId))
    return csv


# Reclamações e devoluções
def reclamacoesTotais():
    response = restTemplateHelper.executeGet(url, endpoints.RECLAMACOES_TOTAIS)
    csv = parseResponse.download(response, names.RECLAMACOES_TOTAIS)
    return csv

# Métricas de tendências
def opinioesProduto(produto):
    response = restTemplateHelper.executeGet(url, endpoints.OPINIOES_PRODUTO.replace("{{item_id}}", produto))
    csv = parseResponse.download(response, names.OPINIOES_PRODUTO.replace("{{itemId}}", produto))
    return csv

# Auth
def errorToken():
    return restTemplateHelper.errorToken()

def auth():
    return restTemplateHelper.auth_ml()