import pytest


@pytest.mark.asyncio
async def test_create_and_get_question(client):
    payload = {"text": "Test question"}

    response = await client.post("/questions/", json=payload)
    assert response.status_code == 201
    data = response.json()
    question_id = data["id"]
    assert data["text"] == payload["text"]

    response = await client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == payload["text"]


@pytest.mark.asyncio
async def test_list_questions(client):
    payload = {"text": "Another question"}
    await client.post("/questions/", json=payload)

    response = await client.get("/questions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(q["text"] == payload["text"] for q in data)


@pytest.mark.asyncio
async def test_delete_question(client):
    payload = {"text": "Delete me"}
    response = await client.post("/questions/", json=payload)
    question_id = response.json()["id"]

    response = await client.delete(f"/questions/{question_id}")
    assert response.status_code == 204

    response = await client.get(f"/questions/{question_id}")
    assert response.status_code == 404
