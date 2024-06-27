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

def init_llm():
    if api_key is not None:
        llm = AzureOpenAI(api_key = api_key)
        return
    if any(tenant_id, client_id, client_secret):
        credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        token = credential.get_token("...")
        llm = AzureOpenAI(azure_ad_token = token.token)
        return
    if env_variables_set():
        credential = EnvironmentCredential()
        token = credential.get_token("...")
        llm = AzureOpenAI(azure_ad_token = token.token)
        return
    token_credential = DefaultAzureCredential()
    token = token_credential.get_token("...")
    llm = AzureOpenAI(azure_ad_token = token.token)
    return
