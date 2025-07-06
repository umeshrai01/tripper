from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import TavilySearchResults
import os
from dotenv import load_dotenv
load_dotenv()

class hotels:
    def __init__(self):
        #self.duck_search = DuckDuckGoSearchRun()
        self.tavily = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"), max_results=10)

    def summarizer(self,results, instruction):
        input_messages = [{"role": "user", "content": f"{instruction}: {results}"}]
        summarizer = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
        summary=summarizer.invoke(input_messages)
        return summary
        
    def find_hotels(self, location):
        hotel_search_results = self.tavily.run(f"Good Hotels for tourist to lodge in {location}")
        print(f'hotel_search_results: {hotel_search_results}')
        instruction = "Extract the Possible hotel/lodging details & associated costs & highlights for a tourist from the provided context. You can take 3 hotels in expensive segment, 3 hotels in budget segment. Later this will be used for travel & trip planning"
        if isinstance(hotel_search_results, list):
            full_string = '\n'.join(rec['content'] for rec in hotel_search_results)
            hotel_results = self.summarizer(full_string, instruction)
        else:
            hotel_results = self.summarizer(hotel_search_results, instruction)
        return hotel_results 