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


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'Henrique',
            'email': 'hfr@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Henrique',
        'email': 'hfr@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Henrique',
                'email': 'hfr@example.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Jhenny',
            'email': 'jhenny@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Jhenny',
        'email': 'jhenny@example.com',
        'id': 1,
    }


def test_update_user_error(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'Jhenny',
            'email': 'jhenny@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }


def test_get_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Jhenny',
        'email': 'jhenny@example.com',
        'id': 1,
    }


def test_get_user_error(client):
    response = client.get('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Jhenny',
        'email': 'jhenny@example.com',
        'id': 1,
    }


def test_delete_user_error(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }
