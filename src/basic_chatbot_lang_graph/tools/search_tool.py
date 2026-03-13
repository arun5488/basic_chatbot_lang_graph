from src.basic_chatbot_lang_graph import logger
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv
import os
load_dotenv()

def get_tools():
    logger.info("Inside get_tools method")
    """
    return the list of tools to be used in the chatbot
    """
    tools = [TavilySearchResults(api_key=os.environ["TAVILY_API_KEY"], max_results = 2)]
    return tools

def create_tool_node(tools):
    logger.info("inside create_tool_node method")
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)