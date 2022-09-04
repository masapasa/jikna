import streamlit as st
from docarray import Document
from jina import Flow, Client
from config import HOST
import streamlit as st
# def search_by_text(input, server=HOST):
#     client = Client(host=server)
#     response = client.search(
#         Document(text=input),
#         parameters={"traversal_path": "@r"},
#     )
#     #matches = response[0].matches
#     for match in response[0].matches:
#         st.markdown(match.text)
#         st.markdown(match.tags)
# user_input = st.text_input("What's your query?", "", key="input")
# search_button = st.button("Search")
# if search_button:
#     search_by_text(user_input)
def search_grpc(string: str):
    doc = Document(text=string)
    with flow:
        results = flow.search(doc)

    print(results[0].matches)

    for match in results[0].matches:
        print(match.text)