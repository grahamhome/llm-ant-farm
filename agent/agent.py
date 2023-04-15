from agent.memory.memory import Memory
from agent.memory.memory_stream import MemoryStream


class Agent:
    def __init__(self):
        self.memory_stream = MemoryStream()

    def loop_once(self):
        """
        Agent's main loop.
        """
        while self.memory_stream.ready_to_reflect():
            self.reflect(memories=self.memory_stream.query(query_memory=max(self.memory_stream.most_recent_memories(), key=Memory.importance)))
        if not self.have_plan():
            self.make_plan(memories=self.memory_stream.most_recent_memories() + self.memory_stream.completed_plans())
        elif self.plan_needs_update():
            self.make_plan(memories=self.memory_stream.most_recent_memories() + self.memory_stream.completed_plans())
        if audience := self.in_conversation():
            self.speak_next_dialog_line(audience=audience)

    def reflect(self, memories: list[Memory]):
        # TODO pass memories to LLM as prompt for high-level analysis
        ...

    def have_plan(self):
        # TODO pass recent memories to LLM to determine if any plan items are not yet completed.
        ...

    def make_plan(self, memories: list[Memory], start_time, end_time):
        # TODO pass memories, start and end times to LLM as prompt for schedule of actions
        ...

    def plan_needs_update(self):
        # TODO pass most recent memories and current plan to LLM as prompt to determine if plan should change
        # TODO and if so, what the new schedule of actions should be, then decompose with make_plan
        ...

    def next_action(self):
        # TODO: Determine if next action is high-level (longer duration than the time represented by 1 loop?)
        # TODO: If so, call decompose_action_into_plan() until next action is low-level
        ...

    def decompose_action_into_plan(self, action: Memory):
        # TODO: call make_plan() with action start & end times & memories related to action.
        ...

    def speak_next_dialog_line(self, audience):
        # TODO send previous dialog lines, relevant memories to LLM as prompt to produce next dialog line
        ...

    def in_conversation(self):
        # TODO send most recent memories to LLM to determine if in conversation, or use flag?
        ...

