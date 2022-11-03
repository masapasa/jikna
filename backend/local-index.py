from docarray import DocumentArray
from jina import Flow

docs = DocumentArray.from_csv(
        "/home/aswin/documents/example-knowledge-base-search/backend/data/community.csv", field_resolver={"question": "text"}
    )
flow = Flow.load_config("flow.yml")
with flow:
    flow.index(docs, show_progress=True)