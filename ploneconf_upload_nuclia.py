# Script to upload a file to NucliaDB using Nuclia.cloud service
# NucliaDB needs to be running with an API key
# You can download the example file at:
# https://www.quintagroup.com/cms/plone/plone_brochure.pdf/@@download/file/Plone_brochure.pdf

# Create NucliaDB Client

from nucliadb_client.client import NucliaDBClient
import requests
import base64

client = NucliaDBClient(host="localhost", grpc=8030, http=8080, train=8031)

kb = client.get_kb(slug="ploneconf2022_nuclia")
if kb is None:
    kb = client.create_kb(slug="ploneconf2022_nuclia", title="Plone Conference 2022")

data = open("Plone_brochure.pdf", "rb").read()

resp = requests.post(
    f"http://localhost:8080/api/v1/kb/{kb.kbid}/upload",
    data=data,
    headers={
        "X-FILENAME": base64.b64encode("Plone_brochure.pdf".encode()),
        "X-NUCLIADB-ROLES": "WRITER",
    },
)

print(f"Done created resources")

# Search on widget: http://localhost:8080/widget
# quines bases de dades usa el programari
# SQL injection