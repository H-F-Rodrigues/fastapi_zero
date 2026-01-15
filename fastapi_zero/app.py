from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='1ª API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/HW', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_world():
    return """
    <html>
      <head>
        <title> Meu Olá Mundo!</title>
      </head>
      <body>
        <h1> Hello World! </h1>
        <h1> Te amo Jhennyfer!!! <3</h1>
      </body>
    </html>"""
