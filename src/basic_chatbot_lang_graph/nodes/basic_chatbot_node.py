from src.basic_chatbot_lang_graph import logger
from src.basic_chatbot_lang_graph.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot node implementation
    """
    logger.info("initialized basicChatbotNode")
    def __init__(self, model) -> None:
        self.llm = model
    
    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """
        logger.info("inside process method of BasicChatbotNode")
        return {"messages":self.llm.invoke(state['messages'])}