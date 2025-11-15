import pytest

@pytest.mark.asyncio
async def test_create_and_get_answer(client):
    q_payload = {"text": "Question for answer"}
    response = await client.post("/questions/", json=q_payload)
    question_id = response.json()["id"]

    a_payload = {"text": "Answer text", "user_id": "user-123"}
    response = await client.post(f"/questions/{question_id}/answers/", json=a_payload)
    assert response.status_code == 201
    answer_id = response.json()["id"]

    response = await client.get(f"/answers/{answer_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == a_payload["text"]

@pytest.mark.asyncio
async def test_delete_answer(client):
    q_payload = {"text": "Question for delete answer"}
    response = await client.post("/questions/", json=q_payload)
    question_id = response.json()["id"]

    a_payload = {"text": "Answer to delete", "user_id": "user-456"}
    response = await client.post(f"/questions/{question_id}/answers/", json=a_payload)
    answer_id = response.json()["id"]

    response = await client.delete(f"/answers/{answer_id}")
    assert response.status_code == 204

    response = await client.get(f"/answers/{answer_id}")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_cascade_delete(client):
    q_payload = {"text": "Question for cascade delete"}
    response = await client.post("/questions/", json=q_payload)
    question_id = response.json()["id"]

    answer_texts = []
    for i in range(3):
        a_payload = {"text": f"Answer {i}", "user_id": f"user-{i}"}
        answer_texts.append(a_payload["text"])
        await client.post(f"/questions/{question_id}/answers/", json=a_payload)

    response = await client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    data = response.json()
    returned_texts = [a["text"] for a in data["answers"]]
    for text in answer_texts:
        assert text in returned_texts

    response = await client.delete(f"/questions/{question_id}")
    assert response.status_code == 204

    response = await client.get(f"/questions/{question_id}")
    assert response.status_code == 404

    for text in answer_texts:
        response = await client.get("/questions/")
        all_answers_texts = []
        for q in response.json():
            all_answers_texts.extend([a["text"] for a in q.get("answers", [])])
        assert text not in all_answers_texts

