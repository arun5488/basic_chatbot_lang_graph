from langgraph.graph import StateGraph, START, END
from src.basic_chatbot_lang_graph.nodes.basic_chatbot_node import BasicChatbotNode
from src.basic_chatbot_lang_graph.state.state import State
from src.basic_chatbot_lang_graph import logger
from src.basic_chatbot_lang_graph.tools.search_tool import create_tool_node, get_tools
from src.basic_chatbot_lang_graph.nodes.chatbot_with_tool import ChatbotWithToolNode
from langgraph.prebuilt import tools_condition, ToolNode

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
    
    def chatbot_with_websearch_build_graph(self):
        logger.info("inside chatbot_with_websearch method")
        """
        Builds a chat bot using langgraph with tools integration.
        the tool node will initialize the tool capabilities in the chatbot and sets up
        conditional and direct edges between nodes
        """
        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm

        chatbot_with_tool_node = ChatbotWithToolNode(llm).create_chatbot_with_tools(tools)
        self.graph_builder.add_node("chatbot",chatbot_with_tool_node)
        self.graph_builder.add_node("tools",tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)



    def setup_graph(self, usecase:str):
        logger.info("sets up the graph for selected use case.")
        """
        Sets up the graph for the selected use case
        """
        if usecase == "Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Agent":
            self.chatbot_with_websearch_build_graph()
        
        return self.graph_builder.compile()