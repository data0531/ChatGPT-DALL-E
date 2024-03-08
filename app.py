import streamlit as st  
from openai import OpenAI

client =  OpenAI(
    api_key = st.secrets["API_KEY"]
    )

st.title("CHATGPT_이미지 생성기 ver1.0")

with st.form("form"):
    user_input = st.text_input("생성하고 싶은 이미지를 입력하시오.")
    submit = st.form_submit_button("button")
    
if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "If Korean, translate to English; if English, proceed. Briefly imagine detailed appearance. Respond concisely in around 20 words."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Doing now"):
        gpt_response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages  = gpt_prompt
        )
    
    prompt = gpt_response.choices[0].message.content.strip()
    st.write(prompt)
    with st.spinner("Doing now"):
        dalle_response = client.images.generate(
            prompt=prompt,
            size="256x256"
        )

    st.image(dalle_response.data[0].url)