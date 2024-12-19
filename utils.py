import os 
import google.generativeai as genai
import ollama
import time,sys
from schemas import *
def generate_response_general_agent(message,language):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-pro')
    messages = [{'role':'model','parts':["Youre a translation expert in all the languages around the world"]}]
    messages.append({'role':'user','parts':[f'Translate text : {message} in Language : {language} and give a normal day to day result for having conversation and give only translated output']})
    response = model.generate_content(messages)
    return response.text

def generate_content_ollama(prompt,tokens):
    start_time = time.time()
    prompt = prompt
    prompt_mode = """You are an Coding AI assistant. Respond to the query in valid JSON format **only**, adhering to the exact structure below:

                {
                "response": {
                    "status": <integer>,        // 1 for success, 0 for failure
                    "message": "<string>",      // A description of the result
                    "data": {
                    "language": "<string>",   // The programming language of the response
                    "code": "<string>" ,       // The actual Python code (or relevant data)
                    "usage": <string>         // The Usage of code as a example
                    }
                }
                }

                ### Rules:
                1. Do not include any extra text, explanations, or preamble before or after the JSON.
                2. Ensure all strings are properly escaped.
                3. Replace `<integer>` and `<string>` placeholders with actual values based on the query.

                Query:
                """ + prompt

    
    print("_________________________________")
    print(prompt_mode)
    print("_________________________________")

    model = "qwen2.5-coder:7b-instruct"
    response = ollama.generate(model=model,prompt=prompt_mode,format='json')

    end_time = time.time()
    query_time = end_time - start_time
    # print(response)
    print(query_time)
    return response