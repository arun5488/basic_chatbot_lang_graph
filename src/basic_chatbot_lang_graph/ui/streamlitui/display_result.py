
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
        elif self.usecase == "Agent":
            initial_state = {"messages":[self.user_message]}
            res = self.graph.invoke(initial_state)
            for message in res['messages']:
                if type(message)== HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool call starts")
                        st.write(message.content)
                        st.write("tool call ends")
                elif type(message)==AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)