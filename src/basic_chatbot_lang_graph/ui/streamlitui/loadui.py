import streamlit as st
import os 
from src.basic_chatbot_lang_graph import logger 
from src.basic_chatbot_lang_graph.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        logger.info(f"Initialized LoadStreamlitUI")
        self.config = Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        logger.info(f"inside load_streamlit_ui")
        st.set_page_config(page_title=self.config.get_page_title(),layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
            logger.info(f"creating sidebar")
            llm_options = self.config.get_llm_options()
            logger.info(f"llm_options: {llm_options}")
            usecase_options = self.config.get_usecase_options()
            logger.info(f"usecase_options:{usecase_options}")

            # LLM selection
            self.user_controls["selected_llm"]=st.selectbox("Select LLM",llm_options)
            logger.info(f"selected_llm: {self.user_controls["selected_llm"]}")

            if self.user_controls["selected_llm"] == "Groq":
                logger.info(f"llm_option selected is Groq")
                model_options = self.config.get_groq_model_options()
                logger.info(f"model_options:{model_options}")
                self.user_controls["selected_groq_model"]= st.selectbox("Select Model", model_options)
                logger.info(f"selected_groq_model:{self.user_controls["selected_groq_model"]}")
            
            
            elif self.user_controls["selected_llm"] == "OpenAI":
                logger.info(f"llm_option selected is OpenAI")
                model_options = self.config.get_openai_model_options()
                logger.info(f"model_options:{model_options}")
                self.user_controls["selected_openai_model"]=st.selectbox("Select Model", model_options)
                logger.info(f"selected openai model:{self.user_controls["selected_openai_model"]}")
            
            # usecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select usecase",usecase_options)
            


            return self.user_controls