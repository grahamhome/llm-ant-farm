from agent.memory.memory import Memory


class MemoryStream:

    def __init__(self):
        ...

    def ready_to_reflect(self) -> bool:
        """
        Queries the memory store to determine if the importance score of
        the most recent memories exceeds a specific threshold.
        :return:
        """
        ...

    def most_recent_memories(self) -> list[Memory]:
        # TODO: retrieve memories from past day
        ...

    def completed_plans(self) -> list[Memory]:
        # TODO: retrieve memories of completed plans
        ...

    def query(self, query_memory: Memory) -> list[Memory]:
        # TODO: Get related memories by embedding vector comparison
        ...
