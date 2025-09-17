
llm_config = {
    "config_list": [
        {
            "model": "llama3.2:latest",  # Ensure this matches your Ollama model name
            "base_url": "http://127.0.0.1:11434/v1",
            "api_key": "ollama", #silences the api error
            "api_type": "ollama" # Tells AutoGen this is not OpenAI

        }
    ]
}
