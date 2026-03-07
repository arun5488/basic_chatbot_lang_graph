from src.basic_chatbot_lang_graph import logger
import streamlit as st
from src.basic_chatbot_lang_graph.ui.streamlitui.loadui import LoadStreamlitUI

def load_chatbot_ui():
    logger.info(f"Inside load_chatbot_ui method inside main.py")


    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

