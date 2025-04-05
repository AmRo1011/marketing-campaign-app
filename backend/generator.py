import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from utils.prompts import get_prompt

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192",
    temperature=0.7
)

def generate_campaign(age_group: str, product: str, tone: str, length: str) -> str:
    prompt_template = get_prompt(age_group, tone, length)
    prompt = PromptTemplate.from_template(prompt_template)
    chain = prompt | llm
    result = chain.invoke({"product": product, "tone": tone, "length": length})
    return result.content if hasattr(result, "content") else str(result)

