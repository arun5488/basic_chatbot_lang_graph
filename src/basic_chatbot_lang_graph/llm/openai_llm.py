import os
from src.basic_chatbot_lang_graph import logger
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

class OpenAiLLM:
    def __init__(self, user_controls_input) -> None:
        logger.info("initialized OpenAiLLM object")
        self.user_controls_input = user_controls_input
        logger.info(f"user_controls_input = {self.user_controls_input}")
        load_dotenv()
        self.openai_api_key = os.environ["OPENAI_API_KEY"]

    def get_llm_model(self):
        logger.info("inside get_llm_model method")
        try:
            selected_openai_model = self.user_controls_input["selected_openai_model"]
            logger.info(f"selected openai model:{selected_openai_model}")
            llm = ChatOpenAI(api_key=self.openai_api_key, model = selected_openai_model)

        except Exception as e:
            logger.error(f"error occured inside get_llm_method:{e}")
            raise e
        return llm