client_id = "2854379993590279"
code = "TG-640c66890e38ce000154592c-307027133"

# endpoints
url = "https://api.mercadolibre.com"
url_auth = "https://auth.mercadolivre.com.br"
user_redirect = "http://localhost:9090"
users_me = "/users/me"
auth = "/authorization?response_type=code&client_id={}&redirect_uri=".format(client_id) + user_redirect
