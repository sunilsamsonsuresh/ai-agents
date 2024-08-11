from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv
import ollama
import os

load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

llm = ollama.chat(model='llama3')
scrape_tool = ScrapeWebsiteTool(website_url='https://www.make-it-in-germany.com/en/')
search_tool = SerperDevTool()