import datetime

agora = datetime.datetime.now()
data_formatada = agora.strftime('%Y-%m-%d')

# Users
USER_ME = "userMe.csv"
VISITAS = "visitas-{{userId}}/{{dateFrom}}/{{dateTo}}.csv"

# Concorrência
DETALHES_CONCORRENCIA = "detalhesConcorrencia-{{itemId}}.csv"
PUBLICACOES_CATALOGO = "publicacoesCatalogo-{{productId}}.csv"
PUBLICACAO_GANHADORA = "publicacaoGanhadora.csv"

# Custos por venda
PRECO_POR_TIPO = "preco-{{price}}-Tipo-{{listingTypeId}}.csv"
PRECO_POR_CATEGORIA = "precoPorCategoria-{{categoryId}}.csv"

# Preços produto
PRECO_PRODUTO = "precoProduto-{{itemId}}.csv"

# Estoque Fullfilment
ESTOQUE_VENDEDOR = "estoqueVendedor-{{inventoryId}}.csv"
ESTOQUE_NAO_DISPONIVEL = "estoqueNaoDisponivel-{{inventoryId}}-{{attributes}}.csv"

# Promoções
PROMOCOES_DISPONIVEIS = "promocoesDisponiveis-{{userId}}.csv"
ITENS_PROMOCAO = "itensPromocao-{{promotionId}}-{{promotionType}}.csv"
CONSULTAR_CAMPANHA_TRADICIONAL = "consultaCampanhaTradicional-{{campanhaId}}.csv"
ITENS_CAMPANHA_ML = "itensDeCampanhaDoMl-{{promotionId}}-{{promotionType}}.csv"
CONSULTAR_PROMOCAO_VOLUME = "consultaPromocaoDeVolume-{{promotionId}}.csv"

# Perguntas e respostas
PERGUNTAS_RECEBIDAS = "perguntasRecebidas-{{sellerId}}.csv"
PERGUNTAS_EM_UM_PRODUTO = "perguntasEmUmProduto-{{itemId}}.csv"

# Relatórios de faturamento
RELATORIO_PERIODO = "relatorioDeUmPeriodo-{{date}}.csv"
DOCUMENTOS_PERIODO = "documentosDeUmPeriodo-{{date}}.csv"
RESUMO_FATURAMENTO = "resumoFaturamento.csv"

# Métricas de tendências
OPINIOES_PRODUTO = "opinioesProduto-{{itemId}}.csv"
OPINIOES_ITEM_CATALOGO = "opinioesItemCatalogo-{{itemId}}-{{catalogProductId}}.csv"
TENDENCIAS = "tendencias-{}.csv".format(data_formatada)
TENDENCIAS_CATEGORIA = "tendenciasCategoria-{{categoryId}}.csv"
QUALIDADE_ITEM = "qualidadeItem-{{itemId}}.csv"
MELHORAR_QUALIDADE_ITEM = "melhorarQualidadeItem-{{itemId}}.csv"
MAIS_VENDIDOS_CATEGORIA = "maisVendidosCategoria-{{categoryId}}.csv"
VISITAS_TOTAIS_ANUNCIO = "visitasTotaisAnuncio-{{itemId}}.csv"

# Reclamações e devoluções
RECLAMACOES_TOTAIS = "reclamacoesTotais.csv"
DEVOLUÇÃO_PRODUTO = "devolucaoProduto-{{claimId}}.csv"