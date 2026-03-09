import os
from src.basic_chatbot_lang_graph import logger
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st


class GroqLLM:
    def __init__(self, user_controls_input):
        logger.info("Initializing GroqLLM object")
        self.user_controls_input = user_controls_input
        logger.info(f"user_controls_input:{self.user_controls_input}")
        logger.info(f"loading the env file to get the api key")
        load_dotenv()
        self.groq_api_key = os.environ['GROQ_API_KEY']

    def get_llm_model(self):
        logger.info("inside get_llm_model method")
        try:
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            logger.info(f"selected_groq_model={selected_groq_model}")
            llm = ChatGroq(api_key=self.groq_api_key, model=selected_groq_model)

        except Exception as e:
            logger.error(f"Error occured inside get_llm_model:{e}")
            raise e
        return llm

