import streamlit as st
import os
from openai import OpenAI


# 设置页面配置项
st.set_page_config(
    page_title="AI Chat",
    page_icon="🧊",

    # 布局
    layout="wide",

    # 侧边栏
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI Chat")

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 模型调用
client = OpenAI(
    # 本地部署的大模型不需要API_KEY
    api_key= "ollama",
    base_url="http://localhost:11434/v1",)


# 系统提示词
system_prompt = "你是一个智能助手"


# 消息输入
prompt = st.chat_input("请输入")
if prompt:
    st.chat_message("user").write(prompt)
    print(f"输入测试：{prompt}")

    # 记录用户聊天历史
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI进行交互
    response = client.chat.completions.create(
        model="deepseek-r1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=False,
        temperature=0.7
    )

    # 输出大模型结果
    print(f"输出测试：{response.choices[0].message.content}")
    st.chat_message("assistant").write(response.choices[0].message.content)

    # 记录大模型聊天历史
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})