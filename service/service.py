from controller.restTemplate import restTemplateHelper
from controller.endpoint import endpoints
from model import parseResponse, names

url = "https://api.mercadolibre.com"

def userMe():
    response = restTemplateHelper.executeGet(url, endpoints.USER_ME)
    csv = parseResponse.download(response, names.USER_ME)
    return csv

def reclamacoesTotais():
    response = restTemplateHelper.executeGet(url, endpoints.RECLAMACOES_TOTAIS)
    csv = parseResponse.download(response, names.RECLAMACOES_TOTAIS)
    return csv

def opinioesProduto(produto):
    response = restTemplateHelper.executeGet(url, endpoints.OPINIOES_PRODUTO.replace("{{item_id}}", produto))
    csv = parseResponse.download(response, names.OPINIOES_PRODUTO.replace("{{itemId}}", produto))
    return csv

def errorToken():
    return restTemplateHelper.errorToken()

def auth():
    return restTemplateHelper.auth_ml()