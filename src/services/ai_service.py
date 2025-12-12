from integrations.ollama_client import OllamaClient

class AIService:
    def __init__(self):
        self.client = OllamaClient()

    def generate_response(self, payload):
        result = self.client.generate(payload.prompt)
        return {
            "response": result
        }
