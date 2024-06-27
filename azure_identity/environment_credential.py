"""Example how to use EnvironmentCredential to gain access to Azure OpenAI."""

#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from azure.identity import EnvironmentCredential
from openai import AzureOpenAI

# following environment variables should be set
# AZURE_TENANT_ID: ID of the service principal's tenant. Also called its 'directory' ID.
# AZURE_CLIENT_ID: the service principal's client ID
# AZURE_CLIENT_SECRET: one of the service principal's client secrets
credential = EnvironmentCredential()

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
