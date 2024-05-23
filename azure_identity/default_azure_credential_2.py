"""Example how to use DefaultAzureCredential to gain access to Azure OpenAI."""

from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI

# user needs to be logged in via "az" CLI tool
token_credential = DefaultAzureCredential()
token = token_credential.get_token("https://cognitiveservices.azure.com/.default")

client = AzureOpenAI(
    api_version="2024-02-15-preview",
    azure_endpoint="https://ols-test.openai.azure.com/",
    azure_ad_token = token.token,
)

response = client.chat.completions.create(
    model="gpt-35-turbo-0125", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)
