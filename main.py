import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import ollama
import streamlit

MODEL = 'llama3.2'

class Website:
    url: str
    title: str
    text: str

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

system_prompt = "You are an excellent assistant that analyzes the content of a website and summarizes it. You are given several chunk summaries from the same source. Produce ONE cohesive, non-redundant summary with:\n A 2–3 sentence overview\n Key points (bullets)\n • If present, list important formulas/definitions\n • A short 'Why it matters' section\n\n"
    
def user_prompt(website):
    user_prompt = f"You are looking for this website titled {website.title}"
    user_prompt += "The contents of that website is as follow, please provide a summary of that website in markdown. If it includes news or announcements, then summarize it too"
    user_prompt += website.text
    return user_prompt
    
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt(website)}
    ]

def summarize(url):
    website = Website(url)
    messages = messages_for(website)
    response = ollama.chat(model=MODEL, messages=messages)
    return response['message']['content'].strip()

def display_summarize(url):
    summary = summarize(url)
    display(Markdown(summary))
    return summary


streamlit.title("Website Summary App")
streamlit.markdown("Enter below a URL to get its summarized content")

url = streamlit.text_input("Enter a URL:", "")

if streamlit.button("Summarize"):
    if url:
        with streamlit.spinner("Summarizing..."):
            summary = display_summarize(url)
        streamlit.markdown(summary)

    else:
        streamlit.waring("Please enter a valid URL")
