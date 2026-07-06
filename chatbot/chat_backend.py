from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Chatstate(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]
    
    
def chatnode(state:Chatstate):
    messages=state["messages"]
    response=llm.invoke(messages)
    return {"messages":[response]}


#checkpointer 
checkpointer=InMemorySaver()

graph=StateGraph(Chatstate)
graph.add_node('chat_node',chatnode)
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot=graph.compile(checkpointer=checkpointer)
