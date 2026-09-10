from openai import OpenAI

client = OpenAI(
    api_key="sk-35a39583f62f454b8804d444d6ce0a9b", 
    base_url="https://api.deepseek.com"

)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一位温柔耐心的儿童心理陪伴助手。"},
        {"role": "user", "content": "我今天在学校被同学笑话了，我不想去上学了。"}
    ]
)

print(response.choices[0].message.content)