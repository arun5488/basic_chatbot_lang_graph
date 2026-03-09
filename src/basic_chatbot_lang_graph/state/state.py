from typing_extensions import TypedDict, List
from src.basic_chatbot_lang_graph import logger
from typing import Annotated
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List, add_messages]