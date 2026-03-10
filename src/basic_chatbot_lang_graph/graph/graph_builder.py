from langgraph.graph import StateGraph, START, END
from src.basic_chatbot_lang_graph.nodes.basic_chatbot_node import BasicChatbotNode
from src.basic_chatbot_lang_graph.state.state import State
from src.basic_chatbot_lang_graph import logger

class GraphBuilder:
    def __init__(self, model) -> None:
        logger.info("initialized GraphBuilder object")
        self.llm = model
        logger.info(f"llm={self.llm}")
        self.graph_builder = StateGraph(State)


    def basic_chatbot_build_graph(self):
        logger.info("Inside basic_chatbot_build_graph method")
        """
        Builds a basic chatbot using langgraph.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates into a graph. The chatbot node is set as both entry and exit point of the graph
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def setup_graph(self, usecase:str):
        logger.info("sets up the graph for selected use case.")
        """
        Sets up the graph for the selected use case
        """
        if usecase == "Chatbot":
            self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()