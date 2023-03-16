
# Users
        # Formato date_from = 2023-01-01T00:00:00.000-00:00
USER_ME = "/users/me" #OK
VISITAS = "/users/{{userId}}/items_visits?date_from={{dateFrom}}&date_to={{dateTo}}"

# Concorrência
DETALHES_CONCORRENCIA = "/items/{{itemId}}/price_to_win?&version=v2"
PUBLICACOES_CATALOGO = "/products/{{productId}}/items"
PUBLICACAO_GANHADORA = "/products/{{productId}}"

# Custos por venda
PRECO_POR_TIPO = "/sites/site_id/listing_prices?price={{price}}&listing_type_id={{listingTypeId}}"
PRECO_POR_CATEGORIA = "/sites/site_id/listing_prices?price={{price}}&category_id={{categoryId}}"

# Preços produto
PRECO_PRODUTO = "/items/{{item_id}}/prices?"

# Estoque Fullfilment
ESTOQUE_VENDEDOR = "/inventories/{{inventoryId}}/stock/fulfillment"
ESTOQUE_NAO_DISPONIVEL = "/inventories/{{inventoryId}}/stock/fulfillment?include_attributes={{attributes}}"

# Promoções
PROMOCOES_DISPONIVEIS = "/seller-promotions/users/{{userId}}"
ITENS_PROMOCAO = "/seller-promotions/promotions/{{promotionId}}/items?promotion_type={{promotionType}}"
CONSULTAR_CAMPANHA_TRADICIONAL = "/seller-promotions/promotions/{{promotionId}}/items?promotion_type=DEAL"
ITENS_CAMPANHA_ML = "/seller-promotions/promotions/{{promotionId}}/items?promotion_type={{promotionType}}"
CONSULTAR_PROMOCAO_VOLUME = "/seller-promotions/promotions/{{promotionId}}/items?promotion_type=VOLUME"

# Perguntas e respostas
PERGUNTAS_RECEBIDAS = "/questions/search?seller_id={{sellerId}}&api_version=4"
PERGUNTAS_EM_UM_PRODUTO = "/questions/search?item={{itemId}}&api_version=4"

# Relatórios de faturamento
RELATORIO_PERIODO = "/billing/integration/periods?group=ML&document_type=BILL&offset=1&limit=12"
DOCUMENTOS_PERIODO = "/billing/integration/periods/{{date}}/documents?group=MP&document_type=BILL&limit=12"
RESUMO_FATURAMENTO = "/billing/integration/periods/{{date}}/summary?group=MP&document_type=BILL"

# Métricas de tendências
OPINIOES_PRODUTO = "/reviews/item/{{itemId}}" #OK
OPINIOES_ITEM_CATALOGO = "/reviews/item/{{itemId}}?catalog_product_id={{catalogProductId}}"
TENDENCIAS = "/trends/MLB"
TENDENCIAS_CATEGORIA = "/trends/MLB/{{categoryId}}"
QUALIDADE_ITEM = "/items/{{itemId}}/health"
MELHORAR_QUALIDADE_ITEM = "/items/{{itemId}}/health/actions"
MAIS_VENDIDOS_CATEGORIA = "/highlights/MLB/category/{{categoryId}}"
VISITAS_TOTAIS_ANUNCIO = "/visits/items?ids={{itemId}}"

# Reclamações e devoluções
RECLAMACOES_TOTAIS = "/v1/claims/search?site_id=MLB" #OK
DEVOLUÇÃO_PRODUTO = "/v1/claims/{{claimId}}/returns"