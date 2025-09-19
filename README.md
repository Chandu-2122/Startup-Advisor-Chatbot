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

## Challenges Faced
- Ensuring consistent, valid JSON outputs for agent responses.
- Balancing general advice vs. context-specific insights.

## Learnings
- Using health checks reduced invalid responses.
- AI works better for structured frameworks rather than vague advice.

## Future Improvements
- Add memory for ongoing conversations
- Provide references for advice (case studies, frameworks).
