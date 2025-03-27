# See also:
# https://microsoft.github.io/promptflow/index.html

import os
from pathlib import Path

from dotenv import load_dotenv
from promptflow.core import Prompty
from promptflow.tracing import trace

BASE_DIR = Path(__file__).absolute().parent
print(BASE_DIR)

@trace
def chat(question: str = "What's the capital of France?") -> str:
    """Flow entry function."""

    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        # load environment variables from .env file
        load_dotenv()

    prompty = Prompty.load(source=BASE_DIR / "chat.prompty")
    # trigger a llm call with the prompty obj
    output = prompty(question=question)
    return output


print(chat())
