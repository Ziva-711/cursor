import streamlit as st
from openai import OpenAI

st.title("我的专属 AI 陪伴助手 🤖")

user_input = st.chat_input("请输入你想对我说的话...")

if user_input:
    
    with st.chat_message("user"):
        st.write(user_input)
    
    client = OpenAI(
        api_key=st.secrets["DEEPSEEK_API_KEY"],        
        base_url="https://api.deepseek.com"  
    )

    response = client.chat.completions.create(
        model="deepseek-chat",              
        messages=[
            {"role": "system", "content": "你是一位温柔耐心的儿童心理陪伴助手。"},
            {"role": "user", "content": user_input} 
        ]
    )
    
    ai_reply = response.choices[0].message.content
    
    with st.chat_message("assistant"):
        st.write(ai_reply)