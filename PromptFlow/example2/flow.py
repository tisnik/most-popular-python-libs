# See also:
# https://microsoft.github.io/promptflow/index.html

from promptflow.core import AzureOpenAIModelConfiguration, Prompty
from promptflow.tracing import trace


class ChatFlow:
    def __init__(self, model_config: AzureOpenAIModelConfiguration):
        self.model_config = model_config

    @trace
    def __call__(
        self,
        question: str = "What is ChatGPT?",
        first_name: str = "",
        last_name: str = "",
        chat_history: list = None,
    ) -> str:
        """Flow entry function."""
        chat_history = chat_history or []

        prompty = Prompty.load(
            source="chat.prompty",
        )

        # output is a generator of string as prompty enabled stream parameter
        output = prompty(question=question, chat_history=chat_history)

        return output


if __name__ == "__main__":
    from promptflow.tracing import start_trace

    start_trace()
    config = AzureOpenAIModelConfiguration(
        connection="open_ai_connection", azure_deployment="gpt-35-turbo"
    )
    flow = ChatFlow(model_config=config)
    result = flow("What is my name", "first_name" "last_name")

    # print result in stream manner
    for r in result:
        print(r, end="")
