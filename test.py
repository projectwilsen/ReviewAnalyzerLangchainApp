import json
import requests

headers = {
    "accept":"application/json",
    "Content-Type":"application/json"
}


api_url = 'http://127.0.0.1:8000/result/1/81'
response = requests.get(api_url)
data = response.json()
source = data[0]

json_data = {
    "question": "summarize my video performance",
    "videoid" : source['videoid'],
    "videotitle": source['videotitle'],
    "view" : source['view'],
    "like" : source['like'],
    "comment" : source['comment'],
    "total_positive_comment" : source['total_positive_comment'],
    "positive_comment" : source['positive_comment'],
    "total_negative_comment" : source['total_negative_comment'],
    "negative_comment" : source['negative_comment'],
    "total_neutral_comment" : source['total_neutral_comment'],
    "neutral_comment" : source['neutral_comment']
}

print(json_data)

response = requests.post(
    "http://localhost:3000/chatbot_chain.chat/run", headers = headers, json = json_data
)

data = response.text
parsed_data = json.loads(data)
print(parsed_data)
print(parsed_data['output'])