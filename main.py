from src.basic_chatbot_lang_graph import logger
import streamlit as st
from src.basic_chatbot_lang_graph.ui.streamlitui.loadui import LoadStreamlitUI
from src.basic_chatbot_lang_graph.llm.groqllm import GroqLLM
from src.basic_chatbot_lang_graph.llm.openai_llm import OpenAiLLM
from src.basic_chatbot_lang_graph.graph.graph_builder import GraphBuilder
from src.basic_chatbot_lang_graph.ui.streamlitui.display_result import DisplayResultStreamlit


def load_chatbot_ui():
    logger.info(f"Inside load_chatbot_ui method inside main.py")


    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        logger.info("Error: failed to load user input from UI")
        st.error("Error: failed to load user input from UI")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            logger.info(f"user_input selected llm:{user_input["selected_llm"]}")
            model = ""
            graph = ""

            if user_input["selected_llm"] == 'Groq':
                obj_llm_config = GroqLLM(user_controls_input=user_input)
                logger.info(f"obj_llm_config:{obj_llm_config}")
                model = obj_llm_config.get_llm_model()
                logger.info(f"model:{model}")
                if not model:
                    st.error("Error: LLM model couldnt be initialized")
                    return

                usecase = user_input.get("selected_usecase")
                logger.info(f"usecase:{usecase}")
                if not usecase:
                    st.error("Error: no usecase selected")
                    return
                            

            elif user_input["selected_llm"] == "OpenAI":
                obj_llm_config = OpenAiLLM(user_controls_input= user_input)
                logger.info(f"obj_llm_config:{obj_llm_config}")
                model = obj_llm_config.get_llm_model()
                logger.info(f"model:{model}")
                if not model:
                    st.error("Error: LLM model could not be initialized")
                    return
                usecase = user_input.get("selected_usecase")
                logger.info(f"use case: {usecase}")
                if not usecase:
                    st.error("Error: use case not selected")
                    return
                



            
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase=usecase)
                logger.info(f"user_message:{user_message}")
                DisplayResultStreamlit(usecase=usecase, graph=graph, user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed: {e}")
                return
        except Exception as e:
            logger.info(f"Error occured in main: {e}")
            st.error(f"Error occured in main: {e}")
            return


