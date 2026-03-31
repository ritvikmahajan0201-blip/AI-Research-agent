from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from langchain_groq import ChatGroq
from pydantic.v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent,AgentExecutor
from Tools import search_tool, wiki_tool

load_dotenv()
console = Console()

# 1. Define Schema
class ResearchResponse(BaseModel):
    topic: str = Field(description="The main subject of research")
    full_report: str = Field(description="The detailed research paragraph")
    sources: list[str] = Field(description="List of URLs or names of sources used")
    tools_used: list[str] = Field(description="List of tools used during research")

# 2. Setup LLM and Tools 
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
tools = [search_tool, wiki_tool]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful research assistant. Use tools to find information."),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 3. Initialize Agent
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False, handle_tool_errors=True)

# 4. Structured output wrapper
structured_llm = llm.with_structured_output(ResearchResponse)

while True:
    query = console.input("\n[bold yellow]What can I help you research? (type 'quit' to exit): [/bold yellow]")
    
    if query.lower() == 'quit':
        break

    with console.status("[bold green]Agent is researching...", spinner="bouncingBar"):
        raw_response = agent_executor.invoke({"query": query})
        final_text = raw_response["output"]

        # Step B: Structure the data (This ensures your print statements don't fail)
        structured_response = structured_llm.invoke(final_text)

    # 5. Styled Output
    console.print(f"\n[bold magenta]Topic:[/bold magenta] {structured_response.topic}")

    summary_panel = Panel(
        structured_response.full_report,
        title="[bold cyan]Research Summary[/bold cyan]",
        border_style="blue",
        padding=(1, 2)
    )
    console.print(summary_panel)

    console.print(f"[bold green]Sources:[/bold green] {', '.join(structured_response.sources)}")
    console.print(f"[bold green]Tools:[/bold green] {', '.join(structured_response.tools_used)}")

    choice = console.input("\n[bold white]Do you want to continue? (Y/N): [/bold white]")
    if choice.upper() != 'Y':
        break

console.print('[bold red]Thank you for using Research AI Assistant. Goodbye![/bold red]')