# Query Uploaded conference talks on local NucliaDB

# http://loclahost:8080/widget
# Widget will only show fulltext search

from sentence_transformers import SentenceTransformer  # type: ignore


def show_result(data):
    resources = data.get("resources")
    print("  - SEMANTIC")
    for sentence in data.get("sentences").get("results"):
        print(f"{sentence.get('field')}: {sentence.get('text')}")
    print("  - FUZZY")
    for paragraph in data.get("paragraphs").get("results"):
        print(f"{paragraph.get('field')}: {paragraph.get('text')}")


model = SentenceTransformer("paraphrase-MiniLM-L6-v2")


QUERY1 = "How to migrate lots of pages super fast"
QUERY1V = model.encode([QUERY1])[0]

QUERY2 = "moving from a draw to a project"
QUERY2V = model.encode([QUERY2])[0]

QUERY3 = "Compatible framework with actual API"
QUERY3V = model.encode([QUERY3])[0]

# Create NucliaDB Client

from nucliadb_client.client import NucliaDBClient

client = NucliaDBClient(host="localhost", grpc=8030, http=8080, train=8031)

kb = client.get_kb(slug="ploneconf2022")

import requests

resp = requests.post(
    f"http://localhost:8080/api/v1/kb/{kb.kbid}/search",
    json={
        "vector": QUERY1V.tolist(),
        "query": QUERY1,
        "min_score": 0.2,
        "page_size": 1,
    },
    headers={"X-NUCLIADB-ROLES": "READER"},
)
print(QUERY1)
show_result(resp.json())

print(" ---------- ")


resp = requests.post(
    f"http://localhost:8080/api/v1/kb/{kb.kbid}/search",
    json={
        "vector": QUERY2V.tolist(),
        "query": QUERY2,
        "min_score": 0.2,
        "page_size": 1,
    },
    headers={"X-NUCLIADB-ROLES": "READER"},
)
print(QUERY2)
show_result(resp.json())

print(" ---------- ")


resp = requests.post(
    f"http://localhost:8080/api/v1/kb/{kb.kbid}/search",
    json={
        "vector": QUERY3V.tolist(),
        "query": QUERY3,
        "min_score": 0.2,
        "page_size": 1,
    },
    headers={"X-NUCLIADB-ROLES": "READER"},
)
print(QUERY3)
show_result(resp.json())

print(" ---------- ")