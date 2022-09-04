from jina import Flow, Document

#f = Flow().add(uses='jinahub://TransformerTorchEncoder').add(uses='jinahub://SimpleIndexer')
f = Flow.load_config("flows/flow.yml")
doc = Document(content='my sentence to be encoded')

with f:
    f.index(doc)