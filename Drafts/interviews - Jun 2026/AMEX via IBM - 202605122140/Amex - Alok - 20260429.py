from pydantic import BaseModel
from typing import List, Dict
# list, dict 


def func(List) -> Dict:
    # takes list as input, outputs a dict
    # strong typing
    return 0 # TypeError

# WHAT HAPPENS IN BELOW TWO FUNCTION CALLS
func([])
func(0)

def func():
    return []
    return {}
    return 0
    return "abc"


# Define state variable

class AgentState(BaseModel):
    msgs: List<Dict>



from langraph import startnode, node, endnode, graph

def take_user_query(str) -> AgentState:
    # remove special characters
    # returns the formatted string
    return {"msgs": [<some list of messages>]}

def call_llm()
    import openai
    client = OpenAI()


graph.add_node("take_user_query", take_user_query)
graph.add_node()

"""

1. Anything can be asked
2. RAG
3. ML Concepts
4. Interview is a random process

"""