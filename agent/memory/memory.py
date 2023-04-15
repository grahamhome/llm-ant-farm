class Memory:
    def __init__(self, content: str, importance: int):
        self.content = content
        self.importance = importance
        # TODO store creation time, last access time, embedding vector


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