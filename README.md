# Startup-Advisor-Chatbot

## Objective
Help founders describe their current challenge and receive structured AI advice using multi-agent reasoning.

## Tech & Requirements
- AutoGen, AG2[OpenAI]
- Streamlit
- Ollama
- Fix-busted-json

## Project Files
- **agents.py** → defines advisor agents
- **chat.py** → chat interface
- **health_code.py** → checks outputs & prevents broken JSON
- **main_app.py** → Streamlit app
- **model.py** → configures LLMs
- **requirements.txt** → lists Python dependencies for the project


## Challenges Faced
- Ensuring consistent, valid JSON outputs for agent responses.
- Balancing general advice vs. context-specific insights.

## Learnings
- Using health checks reduced invalid responses.
- AI works better for structured frameworks rather than vague advice.

## App Snippet
![image](https://github.com/Chandu-2122/Startup-Advisor-Chatbot/blob/788a973dc22a78edea3d0fe544eb191bba97c9d4/Screenshot%202025-09-17%20224133.png)
![image](https://github.com/Chandu-2122/Startup-Advisor-Chatbot/blob/788a973dc22a78edea3d0fe544eb191bba97c9d4/Screenshot%202025-09-17%20224143.png)

## Future Improvements
- Add memory for ongoing conversations
- Provide references for advice (case studies, frameworks).
