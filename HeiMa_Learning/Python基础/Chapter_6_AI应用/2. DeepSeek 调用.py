# Please install OpenAI SDK first: `pip3 install openai`

import os
from openai import OpenAI

# 创建与AI交互的客户端（DEEPSEEK_API_KEY 环境变量的名字，值是DeepSeek的 API_KEY 的值）
client = OpenAI(
    # 本地部署的大模型不需要API_KEY
    api_key= "ollama",
    base_url="http://localhost:11434/v1",)

# 与AI进行交互
response = client.chat.completions.create(
    model="deepseek-r1:8b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    temperature=0.7
)

print(response.choices[0].message.content)