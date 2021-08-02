import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SERVER_NAME": "exemple.com",
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "SECRET_KEY": "test"
    })

    client = app.test_client()
    with app.app_context():
        pass
    app.app_context().push()
    yield client


def test_index_noargs(client):
    """Test for the index page with no arguments
    """
    rv = client.get('/')
    assert rv.status_code == 400


def test_index_wrongargs(client):
    """Test for the index page with the wrong argument
    tf = 23
    """
    rv = client.get('/?tf=23')
    assert rv.status_code == 418


def test_index_goodargs(client):
    """Test for the index page with the correct argument tf
    """
    rv = client.get('/?tf=1')
    assert rv.status_code == 200
    assert "last_downs" in rv.json
    assert "last_ups" in rv.json
    assert len(rv.json["last_downs"]) == 10
    assert len(rv.json["last_ups"]) == 10

    rv = client.get('/?tf=7')
    assert rv.status_code == 200
    assert "last_downs" in rv.json
    assert "last_ups" in rv.json
    assert len(rv.json["last_downs"]) == 10
    assert len(rv.json["last_ups"]) == 10