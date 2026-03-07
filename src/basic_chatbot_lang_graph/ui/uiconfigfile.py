from configparser import ConfigParser
from src.basic_chatbot_lang_graph import logger
from src.basic_chatbot_lang_graph import constants as const
from pathlib import Path

class Config:
    def __init__(self, config_file = Path(const.UICONFIG_FILE_PATH)):
        logger.info(f"initializing Config object from file:{config_file}")
        self.config = ConfigParser()
        self.config.read(config_file)
    
    def get_llm_options(self):
        logger.info(f"inside get_llm_options method")
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        logger.info(f"Inside get_usecase_options method")
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_page_title(self):
        logger.info(f"Inside get_page_title method")
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    def get_groq_model_options(self):
        logger.info("inside get_groq_model_options method")
        return const.GROQ_MODEL_OPTIONS
    
    def get_openai_model_options(self):
        logger.info("inside get_openai_model_options method")
        return const.GROQ_MODEL_OPTIONS


