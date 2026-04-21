from pydantic.v1 import BaseModel,Field
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import Tool

# 1. DuckDuckGo Search Tool
class SearchInput(BaseModel):
    query: str = Field(description="The search query to look up on the internet")
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="duckduckgo_search",
    func=search.run,
    description="Useful for searching the internet. Input should be a search query string.",
    args_schema= SearchInput
)

# 2. Wikipedia Tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = Tool(
    name="wikipedia_search",
    func=WikipediaQueryRun(api_wrapper=api_wrapper).run,
    description="Useful for general knowledge and facts from Wikipedia.",
    args_schema= SearchInput
)