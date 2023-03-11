import pandas as pd
from flask import make_response
import io

def download(json, name):
    bytes = io.BytesIO()
    df = pd.json_normalize(json)
    df.to_csv(bytes, index=False, encoding="utf8")
    bytes.seek(0)   
    download = downloadCsv(bytes, name)
    return download

def downloadCsv(bytes, name):
    response = make_response(bytes.read())
    response.headers.set('Content-Disposition', 'attachment', filename=name)
    response.headers.set('Content-Type', 'text/csv')
    response.headers.set('Pragma', 'public')
    response.headers.set('Cache-Control', 'max-age=0')
    response.headers.set('Expires', '0')
    return response