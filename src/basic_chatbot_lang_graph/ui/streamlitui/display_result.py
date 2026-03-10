
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json
from src.basic_chatbot_lang_graph import logger

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message) -> None:
        logger.info("initialized DisplayResultStreamlit")
        self.usecase = usecase
        logger.info(f"usecase:{self.usecase}")
        self.graph = graph
        logger.info(f"graph:{graph}")
        self.user_message = user_message
        logger.info(f"user_message:{user_message}")
    
    def display_result_on_ui(self):
        logger.info("inside display_result_on_ui method")
        if self.usecase == "Chatbot":
            for event in self.graph.stream({'messages':("user",self.user_message)}):
                logger.info(f"event:{event}")
                for value in event.values():
                    logger.info(f"value['messages]:{value['messages']}")
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(value['messages'].content)
