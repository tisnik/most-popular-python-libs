"""Example how to use ClientSecretCredential class to gain access to Azure OpenAI."""

from azure.identity import ClientSecretCredential
from openai import AzureOpenAI

tenant_id = "" # needs to be set
client_id = "" # needs to be set
client_secret = "" # needs to be set

credential = ClientSecretCredential(tenant_id, client_id, client_secret)

token = credential.get_token("https://cognitiveservices.azure.com/.default")

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
