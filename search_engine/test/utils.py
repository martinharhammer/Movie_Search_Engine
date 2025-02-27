import json

from ir_exercise import search_service

test_client = search_service.app.test_client()


def send_request(text, size):
    path = "/ir-search-service"
    response = test_client.get(
        path,
        data=json.dumps({"text": text, "size": size}),
        headers={"Content-Type": "application/json"},
    )
    return [doc["_id"] for doc in response.json["documents"]]
