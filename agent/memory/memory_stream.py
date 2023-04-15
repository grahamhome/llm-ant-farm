from redis.client import Redis
from agent.memory.memory import Memory

# TODO Switch to SQLAlchemy so I can query by different attributes e.g. time ranges more easily
redis = Redis(host="localhost", port=6379, decode_responses=True)

class MemoryStream:

    def __init__(self, agent_id):
        self.stream_name = agent_id

    def store_memory(self, new_memory: Memory):
        redis.xadd(name=self.stream_name, fields=new_memory.__dict__)

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
        # TODO: Get related memories (memories with highest retrieval scores relative to query memory)
        redis.xrange(name=self.stream_name)
