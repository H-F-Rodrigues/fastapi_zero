from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.username, 'password': user.clean_password},
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token


def test_incorret_username(client):
    response = client.post(
        '/auth/token',
        data={'username': 'invalid-user', 'password': 'invalid-password'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorret username'}


def test_incorret_password(client, token, user):
    response = client.post(
        '/auth/token',
        data={'username': user.username, 'password': 'invalid-password'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Invalid password'}
