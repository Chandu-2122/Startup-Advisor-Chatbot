from agents import founder_agent, manager

def run_startup_chat(user_input):
    message = f"As a founder, I'm currently dealing with: {user_input}"
    _ = founder_agent.initiate_chat(manager, message=message)

    # After conversation finishes, get the last message from groupchat
    final_message = manager.groupchat.messages[-1]['content'] if manager.groupchat.messages else "Conversation complete."
    return final_message
