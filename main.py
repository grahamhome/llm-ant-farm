from dotenv import load_dotenv

load_dotenv()
from agent.generative_agent import GenerativeAgent

def test_character():
    john = GenerativeAgent(name="John Lin", initial_memories_filepath="agent/memories/john.txt")
    print("Hi, I'm John Lin!")
    while True:
        print(john.get_action(question=input("action prompt > ")))
        print(john.get_dialog(prompt=input("dialog prompt from Tom Moreno > "), agent_name="Tom Moreno"))

if __name__ == "__main__":
    test_character()