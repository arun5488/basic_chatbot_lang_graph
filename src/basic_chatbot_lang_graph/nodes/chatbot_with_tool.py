from src.basic_chatbot_lang_graph.state.state import State
from src.basic_chatbot_lang_graph import logger

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """

    def __init__(self, model) -> None:
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a response with tool integration
        """
        logger.info("inside process method")
        user_input = state["messages"][-1] if state["messages"] else ""
        logger.info(f"user_input:{user_input}")

        llm_response = self.llm.invoke([{"role":"user","content":user_input}])

        tools_response = f"Tool Integration for: '{user_input}'"

        return {"messages":[llm_response, tools_response]}
    
    def create_chatbot_with_tools(self, tools):
        """
        Returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response
            """
            return {"messages":[llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node




