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

def campanhaMl(promotionId, promotionType):
    endpoint = endpoints.ITENS_CAMPANHA_ML.replace("{{promotionId}}", promotionId).replace("{{promotionType}}", promotionType)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.ITENS_CAMPANHA_ML.replace("{{promotionId}}", promotionId).replace("{{promotionType}}", promotionType)
    return parseResponse.download(response, name)

def campanhaVolume(promotionId):
    response = restTemplateHelper.executeGet(url, endpoints.CONSULTAR_PROMOCAO_VOLUME.replace("{{promotionId}}", promotionId))
    name = names.CONSULTAR_PROMOCAO_VOLUME.replace("{{promotionId}}", promotionId)
    return parseResponse.download(response, name)

# Perguntas e Respostas
def perguntasRecebidas(sellerId):
    response = restTemplateHelper.executeGet(url, endpoints.PERGUNTAS_RECEBIDAS.replace("{{sellerId}}", sellerId))
    name = names.PERGUNTAS_RECEBIDAS.replace("{{sellerId}}", sellerId)
    return parseResponse.download(response, name)

def perguntasProduto(itemId):
    response = restTemplateHelper.executeGet(url, endpoints.PERGUNTAS_EM_UM_PRODUTO.replace("{{itemId}}", itemId))
    name = names.PERGUNTAS_EM_UM_PRODUTO.replace("{{itemId}}", itemId)
    return parseResponse.download(response, name)

# Relatórios de faturamento
def relatorio():
    response = restTemplateHelper.executeGet(url, endpoints.RELATORIO_PERIODO)
    name = names.RELATORIO_PERIODO
    return parseResponse.download(response, name)

def documento(periodo):
    response = restTemplateHelper.executeGet(url, endpoints.DOCUMENTOS_PERIODO.replace("{{date}}", periodo))
    name = names.DOCUMENTOS_PERIODO.replace("{{date}}", periodo)
    return parseResponse.download(response, name)

def resumoFaturamento(periodo):
    response = restTemplateHelper.executeGet(url, endpoints.RESUMO_FATURAMENTO.replace("{{date}}", periodo))
    name = names.RESUMO_FATURAMENTO.replace("{{date}}", periodo)
    return parseResponse.download(response, name)

# Métricas de tendências
def opinioesProduto(produto):
    response = restTemplateHelper.executeGet(url, endpoints.OPINIOES_PRODUTO.replace("{{item_id}}", produto))
    return parseResponse.download(response, names.OPINIOES_PRODUTO.replace("{{itemId}}", produto))

def opinioesItemCatalogo(ItemId, catalogId):
    endpoint = endpoints.OPINIOES_ITEM_CATALOGO.replace("{{itemId}}", ItemId).replace("{{catalogProductId}}", catalogId)
    response = restTemplateHelper.executeGet(url, endpoint)
    name = names.OPINIOES_ITEM_CATALOGO.replace("{{itemId}}", ItemId).replace("{{catalogProductId}}", catalogId)
    return parseResponse.download(response, name)

def tendencias():
    response = restTemplateHelper.executeGet(url, endpoints.TENDENCIAS)
    name = names.TENDENCIAS
    return parseResponse.download(response, name)

def tendenciasCategoria(categoryId):
    response = restTemplateHelper.executeGet(url, endpoints.TENDENCIAS_CATEGORIA.replace("{{categoryId}}", categoryId))
    name = names.TENDENCIAS_CATEGORIA.replace("{{categoryId}}",categoryId)
    return parseResponse.download(response, name)

def qualidadeItem(itemId):
    response = restTemplateHelper.executeGet(url, endpoints.QUALIDADE_ITEM.replace("{{itemId}}", itemId))
    name = names.QUALIDADE_ITEM.replace("{{itemId}}", itemId)
    return parseResponse.download(response, name)

def melhorarQualidadeItem(itemId):
    response = restTemplateHelper.executeGet(url, endpoints.MELHORAR_QUALIDADE_ITEM.replace("{{itemId}}", itemId))
    name = names.MELHORAR_QUALIDADE_ITEM.replace("{{itemId}}", itemId)
    return parseResponse.download(response, name)

def maisVendidoCategoria(categoryId):
    response = restTemplateHelper.executeGet(url, endpoints.MAIS_VENDIDOS_CATEGORIA.replace("{{categoryId}}", categoryId))
    name = names.MAIS_VENDIDOS_CATEGORIA.replace("{{categoryId}}", categoryId)
    return parseResponse.download(response, name)

def visitasTotaisAnuncio(itemId):
    response = restTemplateHelper.executeGet(url, endpoints.VISITAS_TOTAIS_ANUNCIO.replace("{{itemId}}", itemId))
    name = names.VISITAS_TOTAIS_ANUNCIO.replace("{{itemyId}}", itemId)
    return parseResponse.download(response, name)

# Reclamações e devoluções
def reclamacoesTotais():
    response = restTemplateHelper.executeGet(url, endpoints.RECLAMACOES_TOTAIS)
    return parseResponse.download(response, names.RECLAMACOES_TOTAIS)

def devolucaoProduto(claimId):
    response = restTemplateHelper.executeGet(url, endpoints.RECLAMACOES_TOTAIS)
    name = names.DEVOLUÇÃO_PRODUTO.replace("{{claimId}}", claimId)
    return parseResponse.download(response, name)

# Auth
def errorToken():
    return restTemplateHelper.errorToken()

def auth():
    return restTemplateHelper.auth_ml()