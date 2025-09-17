from model import llm_config
from autogen import ConversableAgent, GroupChat, GroupChatManager

founder_agent = ConversableAgent(
    name="founder",
    system_message="You are a startup founder describing current business challenges.",
    llm_config=llm_config
)

problem_analysis_agent = ConversableAgent(
    name="problem_analysis",
    system_message=(
        "You analyze the founder's message to identify startup challenges."
        "Summarize the key business issues, such as product-market fit, cash flow, team dynamics, etc."
        "Do not provide any recommendations."
    ),
    llm_config=llm_config
)

strategy_agent = ConversableAgent(
    name="strategy_advisor",
    system_message=(
        "You suggest business strategies based only on the Problem Analysis Agent's response."
        "Do not analyze the user's original message, only give actionable advice based on the analysis."
    ),
    llm_config=llm_config
)

groupchat = GroupChat(
    agents=[problem_analysis_agent, strategy_agent],
    messages=[],
    max_round=3,
    speaker_selection_method="round_robin"
)

manager = GroupChatManager(
    name="manager",
    groupchat=groupchat
)
