import os
import requests
from bs4 import BeautifulSoup
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def fetch_website_text(url: str) -> str:
    """Fetch website HTML and return plain text."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup.get_text()


def extract_information(text: str, question: str) -> str:
    """Use an LLM to extract information from text."""
    llm = OpenAI()  # uses OPENAI_API_KEY environment variable

    template = """{text}

Extract the following information: {question}
"""
    prompt = PromptTemplate(
        input_variables=["text", "question"],
        template=template,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"text": text, "question": question})


if __name__ == "__main__":
    url = os.environ.get("TARGET_URL", "https://example.com")
    query = os.environ.get(
        "QUESTION", "Summarize the main content of this page in one sentence."
    )

    page_text = fetch_website_text(url)
    result = extract_information(page_text, query)
    print(result)
