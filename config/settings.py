import os
from dotenv import load_dotenv
from autogen_core.models import ModelInfo
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model= MODEL,  
        api_key=api_key,
        
        model_info=ModelInfo(
            vision=True,
            function_calling=True,
            json_output=True,
            structured_output=True,
            family="gemini"
        )
    )
    return model_client