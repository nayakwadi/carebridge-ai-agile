def test_token_then_me(client):
    r = client.post(
        "/api/auth/token",
        data={"username": "a.okafor@carebridge.example", "password": "demo"},
    )
    assert r.status_code == 200
    token = r.json()["access_token"]

    me = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == 200
    assert me.json()["subject"] == "a.okafor@carebridge.example"


def test_bad_password_rejected(client):
    r = client.post("/api/auth/token", data={"username": "x", "password": "nope"})
    assert r.status_code == 401


def test_me_requires_token(client):
    assert client.get("/api/auth/me").status_code == 401
