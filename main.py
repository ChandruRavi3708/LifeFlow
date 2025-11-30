from memory.session_memory import SessionMemory
from memory.long_term_memory import LongTermMemory
from agents.orchestrator import Orchestrator

def main():
    print("🌟 LifeFlow Personal Assistant 🌟")

    session = SessionMemory()
    memory = LongTermMemory()

    # Example stored preferences
    memory.write("preferences", {
        "diet": "high-protein",
        "work_hours": "9am-5pm"
    })

    orchestrator = Orchestrator(session, memory)

    while True:
        query = input("\nAsk LifeFlow something → ")

        if query.lower() in ["quit", "exit"]:
            break

        response = orchestrator.run(query)
        print("\n💬 Response:\n", response)


if __name__ == "__main__":
    main()
