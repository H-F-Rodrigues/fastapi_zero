from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    AAA
    A - Arrange - Prepara
    A - Act - Age
    A - Assert - Garante
    """

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_hello_world_deve_retornar_html(client):

    response = client.get('/HW')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title> Meu Olá Mundo!</title>
      </head>
      <body>
        <h1> Hello World! </h1>
        <h1> Te amo Jhennyfer!!! <3</h1>
      </body>
    </html>"""
    )
