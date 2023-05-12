import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import faiss
from langchain.docstore import InMemoryDocstore
from langchain.vectorstores import FAISS
from os import environ

EMBEDDING_SIZE = 1536
LLM = OpenAI(temperature=environ.get("AGENT_LLM_TEMPERATURE", 0.5))

_DEFAULT_TEMPLATE = """You are a character in a small community. Here are some memories from your recent past:
{history}
"""

_ACTION_PROMPT = """Using these memories if they are relevant, answer the following question as your character. Provide your response in the third person present tense and include your name in your response.

Question: {input}
Your response:"""

_DIALOG_PROMPT = """Using these memories if they are relevant, provide the next line of dialog as your character.

{name} says to you, """

_DIALOG_PROMPT_END = """"{input}". What is your response?"""

class GenerativeAgent:
    """An LLM agent which generates new plans, actions and dialog based on current and past experiences"""
    def __init__(self, name: str, initial_memories_filepath: str = None, debug=os.environ.get("DEBUG", False)):
        """
        Set up the agent's vector-store-based memory and insert any initial memories.
        """
        self.name = name
        self.debug = debug
        self.memory = VectorStoreRetrieverMemory(retriever=FAISS(OpenAIEmbeddings().embed_query, faiss.IndexFlatL2(EMBEDDING_SIZE), InMemoryDocstore({}), {}).as_retriever(search_kwargs=dict(k=3)))
        # Load initial memories
        if initial_memories_filepath:
            self._load_memories(initial_memories_filepath)

    def _load_memories(self, memories_filepath):
        """
        Load semicolon-separated memories from the given filepath into memory.
        """
        for memory in open(memories_filepath, "r").read().split(";"):
            self.memory.save_context({"input": memory}, {"output": ""})

    def get_action(self, question: str):
        """
        Generate an action in character, drawing upon relevant memories.
        """
        return ConversationChain(llm=LLM, prompt=PromptTemplate(
    input_variables=["history", "input"],
    template=f"Your name is {self.name}. {_DEFAULT_TEMPLATE} {_ACTION_PROMPT}"
), memory=self.memory, verbose=self.debug).predict(input=question)

    def get_dialog(self, agent_name, prompt: str):
        """
        In character, generate a line of dialog in response to the given prompt from the given character, drawing upon relevant memories.
        """
        return ConversationChain(llm=LLM, prompt=PromptTemplate(
            input_variables=["history", "input"],
            template=f"Your name is {self.name}. {_DEFAULT_TEMPLATE} {_DIALOG_PROMPT.format(name=agent_name)} {_DIALOG_PROMPT_END}"
        ), memory=self.memory, verbose=self.debug).predict(input=prompt)