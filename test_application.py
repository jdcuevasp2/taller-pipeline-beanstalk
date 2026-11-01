from application import application

def test_lista_heroes():
    r = application.test_client().get("/")
    assert r.status_code == 200
    assert "0" in r.get_json()

def test_heroe():
    r = application.test_client().get("/0")
    assert r.status_code == 200
    assert r.get_json()["name"] == "A-Bomb"

def test_heroe_no_encontrado():
    r = application.test_client().get("/999")
    assert r.status_code == 404