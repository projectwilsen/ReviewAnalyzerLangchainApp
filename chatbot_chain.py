import os

from langchain import HuggingFaceHub
from langchain import PromptTemplate,  LLMChain

from dotenv import load_dotenv, find_dotenv


load_dotenv()

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("huggingfacehub_api_token")


repo_id = "tiiuae/falcon-7b-instruct"  
falcon_llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_new_tokens": 425}
)


template = """
You are an intelligent chatbot that act as a senior data consultant. 
Here is report of youtube video performance from your client:
The video title is {videotitle} with video id is {videoid}. 

Here are some statistic of the video performance:
Total view (people viewing client's video): {view}
Total like (people liking client's video): {like}
Total comment (people commenting client's video): {comment}
Total negative comment (people giving negative comments to client's video): {total_negative_comment}
Total positive comment (people giving positive comments to client's video): {total_positive_comment}
Total neutral comment (people giving neutral comments to client's video): {total_neutral_comment}

Positive comments: {positive_comment}
Negative comments: {negative_comment} 
Neutral comments: {neutral_comment} 

Answer the following question with the fact based on the report provided above. Don't hallucinating! Be concise and don't repeating the same thing
Question: {question}
Answer: your answer here be concise and specific

"""

prompt = PromptTemplate(
    template=template, 
    input_variables=[
            "question","videoid","videotitle","view","like","comment",
            "total_positive_comment", "positive_comment", 
            "total_negative_comment", "negative_comment", 
            "total_neutral_comment", "neutral_comment"
            ]
    )

chat = LLMChain(prompt=prompt, llm=falcon_llm)

if __name__ == "__main__":
    print(chat.run(
        question="What is the video title?", videoid = "videoid", videotitle = "learning django", 
        view = "view", like = "like", comment = "comment", 
        total_positive_comment = "total_positive_comment", positive_comment = "positive_comment", 
        total_negative_comment = "total_negative_comment", negative_comment = "negative_comment", 
        total_neutral_comment = "total_neutral_comment", neutral_comment = "neutral_comment")
    )



