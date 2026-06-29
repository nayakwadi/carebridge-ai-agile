def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_list_patients_seeded(client):
    r = client.get("/api/patients")
    assert r.status_code == 200
    data = r.json()
    assert len(data) >= 5
    assert any(p["mrn"] == "MRN-100247" for p in data)


def test_get_patient_404(client):
    assert client.get("/api/patients/99999").status_code == 404


def test_create_patient_and_reject_duplicate(client):
    payload = {
        "mrn": "MRN-TEST01",
        "full_name": "Test Patient",
        "date_of_birth": "1990-01-01",
        "primary_condition": "Observation",
        "risk_level": "low",
    }
    r = client.post("/api/patients", json=payload)
    assert r.status_code == 201
    assert r.json()["mrn"] == "MRN-TEST01"

    dup = client.post("/api/patients", json=payload)
    assert dup.status_code == 409


def test_move_task_across_kanban_columns(client):
    tasks = client.get("/api/tasks").json()
    assert tasks, "expected seeded tasks"
    task_id = tasks[0]["id"]
    r = client.patch(f"/api/tasks/{task_id}", json={"status": "done"})
    assert r.status_code == 200
    assert r.json()["status"] == "done"


def test_reject_invalid_task_status(client):
    tasks = client.get("/api/tasks").json()
    task_id = tasks[0]["id"]
    r = client.patch(f"/api/tasks/{task_id}", json={"status": "not-a-real-status"})
    assert r.status_code == 422


def test_stats_endpoint(client):
    r = client.get("/api/stats")
    assert r.status_code == 200
    body = r.json()
    assert body["patients"] >= 5
    assert "open_tasks" in body
