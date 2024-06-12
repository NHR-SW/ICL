from openai import AzureOpenAI

llm_config={
    "model": "gpt-35-turbo",
    "api_type": "azure",
    "api_key": "13d8d0888405404b9c1ee4407ad19226",
    "base_url": "https://openai-resource-for-multilingual.openai.azure.com/",
    "api_version": "2023-07-01-preview",
}

client = AzureOpenAI(
  api_key = "13d8d0888405404b9c1ee4407ad19226",
  api_version = "2023-07-01-preview",
  azure_endpoint =  "https://openai-resource-for-multilingual.openai.azure.com/"
)