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
PRECO_POR_TIPO = "precoPorTipo.csv"
PRECO_POR_CATEGORIA = "precoPorCategoria-{{categoryId}}.csv"

# Preços produto
PRECO_PRODUTO = "precoProduto-{{productId}}.csv"

# Estoque Fullfilment
ESTOQUE_VENDEDOR = "estoqueVendedor.csv"
ESTOQUE_NAO_DISPONIVEL = "estoqueNaoDisponivel.csv"

# Promoções
PROMOCOES_DISPONIVEIS = "promocoesDisponiveis.csv"
ITENS_PROMOCAO = "itensPromocao.csv"
CONSULTAR_CAMPANHA_TRADICIONAL = "consultaCampanhaTradicional-{{campanhaId}}.csv"
ITENS_CAMPANHA_ML = "itensDeCampanhaDoMl.csv"
CONSULTAR_PROMOCAO_VOLUME = "consultaPromocaoDeVolume-{{promocaoId}}.csv"

# Perguntas e respostas
PERGUNTAS_RECEBIDAS = "perguntasRecebidas.csv"
PERGUNTAS_EM_UM_PRODUTO = "perguntasEmUmProduto-{{productId}}.csv"

# Relatórios de faturamento
RELATORIO_PERIODO = "relatorioDeUmPeriodo-{{date}}.csv"
DOCUMENTOS_PERIODO = "documentosDeUmPeriodo-{{date}}.csv"
RESUMO_FATURAMENTO = "resumoFaturamento.csv"

# Métricas de tendências
OPINIOES_PRODUTO = "opinioesProduto-{{itemId}}.csv"
OPINIOES_ITEM_CATALOGO = "opinioesItemCatalogo.csv"
TENDENCIAS = "tendencias-{}.csv".format(data_formatada)
TENDENCIAS_CATEGORIA = "tendenciasCategoria-{{categoryId}}.csv"
QUALIDADE_ITEM = "qualidadeItem-{{itemId}}.csv"
MELHORAR_QUALIDADE_ITEM = "melhorarQualidadeItem-{{itemId}}.csv"
MAIS_VENDIDOS_CATEGORIA = "maisVendidosCategoria-{{categoryId}}.csv"
VISITAS_TOTAIS_ANUNCIO = "visitasTotaisAnuncio-{{anuncioId}}.csv"

# Reclamações e devoluções
RECLAMACOES_TOTAIS = "reclamacoesTotais.csv"
DEVOLUÇÃO_PRODUTO = "devolucaoProduto-{{productId}}.csv"