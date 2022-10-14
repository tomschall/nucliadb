# Upload plone conference talks to NucliaDB

from typing import Any, Dict, List
import requests


# LOAD a simple Vectorizer
from sentence_transformers import SentenceTransformer  # type: ignore

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
print("Loaded vectorizer")


# Create NucliaDB Client
from nucliadb_client.client import NucliaDBClient
from nucliadb.models import (
    CreateResourcePayload,
    InputMetadata,
    TextField,
    UserMetadata,
    Classification,
    TextFormat,
)
from devtools import debug
from nucliadb.models.labels import LabelSet, Label, LabelSetKind
from nucliadb_protos.resources_pb2 import FieldType
from nucliadb_protos.utils_pb2 import Vector
from bs4 import BeautifulSoup  # type: ignore

client = NucliaDBClient(host="localhost", grpc=8030, http=8080, train=8031)

kb = client.get_kb(slug="ploneconf2022")
if kb is None:
    kb = client.create_kb(slug="ploneconf2022", title="Plone Conference 2022")

# Plone Conf Audiencies
AUDIENCES = requests.get(
    "https://2022.ploneconf.org/++api++/@vocabularies/ploneconf.core.vocabularies.slot_audiences"
).json()

labels = [
    Label(title=item.get("title"))
    for item in AUDIENCES.get("items", [])
    if item.get("title")
]
ls_payload = LabelSet(title="Audiencies", kind=[LabelSetKind.RESOURCES], labels=labels)
debug(ls_payload)
resp = requests.post(
    f"http://localhost:8080/api/v1/kb/{kb.kbid}/labelset/audiencies",
    headers={"X-NUCLIADB-ROLES": "WRITER"},
    json=ls_payload.dict(),
)

assert resp.status_code == 200
print("Uploaded Ontology")
input("Enter to continue")


# Get all talks

DEBUG = False
POSTS: List[Dict[str, Any]] = requests.get(
    "https://2022.ploneconf.org/++api++/@talks"
).json()

for post in POSTS:

    title = post.get("title")

    talk_payload = requests.get(
        post.get("@id").replace(
            "https://2022.ploneconf.org/", "https://2022.ploneconf.org/++api++/"
        )
    ).json()

    if talk_payload is None:
        continue
    body_text = talk_payload.get("text", {})
    if body_text is None:
        continue
    body = body_text.get("data")
    if body is None:
        continue

    payload = CreateResourcePayload()

    payload.title = title
    payload.icon = "ploneconf/talk"
    payload.metadata = InputMetadata()
    payload.metadata.language = "en"
    payload.slug = talk_payload.get("id")

    payload.usermetadata = UserMetadata()
    for audience in talk_payload.get("session_audience"):
        payload.usermetadata.classifications.append(
            Classification(labelset="audiencies", label=audience.get("title"))
        )

    field = TextField(body=body)
    field.format = TextFormat.HTML
    payload.texts["body"] = field

    if DEBUG:
        debug(payload)
        input("Enter to continue")

    # Only title is automated indexing
    resource = kb.create_resource(payload)

    # Now add index information
    tree = BeautifulSoup(body, features="html.parser")
    good_text = tree.get_text().replace("\n", " \n ")
    resource.add_text("body", FieldType.TEXT, good_text)  # type: ignore

    embeddings = model.encode([title, body])

    # Title
    vector = Vector(
        start=0,
        end=len(title),
        start_paragraph=0,
        end_paragraph=len(title),
    )
    vector.vector.extend(embeddings[0])

    resource.add_vectors(
        "title",
        FieldType.GENERIC,  # type: ignore
        [vector],
    )

    # Body
    vector = Vector(
        start=0,
        end=len(body),
        start_paragraph=0,
        end_paragraph=len(body),
    )
    vector.vector.extend(embeddings[1])

    resource.add_vectors(
        "body",
        FieldType.TEXT,  # type: ignore
        [vector],
    )

    resource.sync_commit()
    print(f"Uploaded {title}")

print(f"Done created {len(POSTS)} resources")


# Search at http://localhost:8080/widget for Victor