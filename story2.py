import openai
import time
import requests
import pandas as pd
import os



openai.api_key = 'xxxxx'

def chat_with_gpt3(text):
    for i in range(3):  # 最多重试2次，所以总共尝试3次
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text}
                ]
            )
            return response
        except (openai.errors.RequestTimeoutError, requests.exceptions.ProxyError):  # 如果请求超时或者代理错误
            if i < 2:  # 如果还没重试2次
                time.sleep(3)  # 等待1秒后重试
            else:  # 如果已经重试2次
                raise  # 抛出异常




content = "I hope you, as a children's story creator, can help me write a Chinese idiom story about '天下无敌', and all the output will be in Chinese";
respon = chat_with_gpt3(content)
print(respon.choices[0].message.content)
