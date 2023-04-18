from datetime import datetime

from sentence_transformers import SentenceTransformer, util
from torch import Tensor

model = SentenceTransformer("all-MiniLM-L6-v2")

class Memory:
    def __init__(self, content: str, importance: int):
        self.content = content
        self.importance = importance
        self.created = datetime.now()
        self.last_access = self.created
        self.vector = model.encode(self.content)

    def access_age(self):
        return datetime.now() - self.last_access

    def relevance(self, other_memory: "Memory"):
        """
        Returns the memory's relevance to another memory by calculating the cosine similarity between the
        embedding vectors of the two memories.
        """
        util.cos_sim(self.vector, other_memory.vector)

    def retrieval_score(self, other_memory: "Memory"):
        """
        Return the retrieval score for the memory with respect to another memory.
        Retrieval score = recency_weight * recency + importance_weight * importance + relevance_weight * relevance(other_memory)
        :param other_memory:
        :return:
        """
        ...


class PlanItem(Memory):
    def __init__(self, content: str, importance: int):
        super().__init__(content, importance)
        self.completed = False

    def mark_completed(self):
        self.completed = True


class Reflection(Memory):
    def __init__(self, content: str, importance: int, related_memories: list[Memory]):
        super().__init__(content, importance)
        self.related_memories = related_memories