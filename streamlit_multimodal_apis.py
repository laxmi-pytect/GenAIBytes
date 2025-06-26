
### testing multimodal features on streamlit ###
import streamlit as st
import os, io
from dotenv import load_dotenv
from google import genai

from google.genai import types
from PIL import Image
from io import BytesIO

load_dotenv()

GEMINI_API_KEY = os.getenv("gemini_key")


client = genai.Client(api_key = GEMINI_API_KEY)
print(client)


st.title("AI Image Generator")
user_prompt = st.text_input("What do you want to generate image for?")

if st.button("generate image"):
    if (not user_prompt):
        st.warning("Please enter the prompt")
    else:
        st.spinner("generating the image")
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=user_prompt,
            config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE']))
        st.subheader("generated image")
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = Image.open(BytesIO((part.inline_data.data)))
                st.image(image)
                


##image upload and generate caption
st.title("AI image caption generator")


uploaded_img=st.file_uploader("upload img with caption")
if uploaded_img : 
    image=Image.open(uploaded_img)
    st.image(image, "uploaded image")
    
    if st.button("generate caption"):
        with st.spinner ("Generating captions.."):
            
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[ "caption the image", image])

            st.title(response.text)

        


