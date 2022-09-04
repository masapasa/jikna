from docarray import DocumentArray, Document
from jina import Flow
import click


flow = (
    Flow(protocol="http")
    .add(
        name="encoder",
        uses="jinahub://TransformerTorchEncoder",
        uses_with={
            "pretrained_model_name_or_path": "sentence-transformers/paraphrase-mpnet-base-v2"
        },
        install_requirements=True,
    )
    .add(uses="jinahub://SimpleIndexer", install_requirements=True)
)

qa_docs = Document(content='my sentence to be encoded')
def index():
    with flow:
        flow.index(qa_docs, show_progress=True)


def search_grpc(string: str):
    doc = Document(text=string)
    with flow:
        results = flow.search(doc)

    print(results[0].matches)

    for match in results[0].matches:
        print(match.text)


def search():
    with flow:
        flow.block()


@click.command()
@click.option(
    "--task",
    "-t",
    type=click.Choice(["index", "search"], case_sensitive=False),
)
@click.option("--num_docs", "-n",)
def main(task: str, num_docs):
    if task == "index":
        index()
    elif task == "search":
        search()
    else:
        print("Please add '-t index' or '-t search' to your command")


if __name__ == "__main__":
    main()