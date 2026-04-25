import streamlit as st
from duckduckgo_search import DDGS
from st_image_button import st_image_button
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent,AgentExecutor
from Tools import search_tool, wiki_tool
from duckduckgo_search import DDGS

load_dotenv()

def fetch_images(query):
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=10)
        return [r["image"] for r in results]

st.title("AI Research Agent")
st.header("Welcome User")

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
tools = [search_tool, wiki_tool]

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert Senior Research Assistant. 
    Your goal is to provide deep, structured, and exhaustive research reports.
    
    INSTRUCTIONS:
    1. Provide a high-level executive summary.
    2. Breakdown the topic into 3-5 key sub-sections (e.g., Background, Recent Developments, Key Figures).
    3. Always include a 'Sources and Citations' section at the end.
    4. Use professional, academic language.
    5. Aim for a minimum of 500 words. Do not stop until the topic is covered in depth.
    6. When user asks for difference based queries always generate the response in tabular format and not in paragraphs.
    7. Ask a follow up question related to the query or if user need anything else.
     
     
    """),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False, handle_tool_errors=True)

col1,col2 = st.columns([8,1],vertical_alignment="top")

with col1:
    user_input_query = st.text_input("HI What Can I Help You with Today?",placeholder="Please Enter Your Query")


with col2:
    st.write("")
    st.write("")
    submit_button = st_image_button(image=r"C:\Users\ritvi\Downloads\right-chevron.png",width=35)

with col1:
    if user_input_query:
        st.write("Query Submitted")
        with st.spinner("Researching..."):
            try:
                raw_response = agent_executor.invoke({"input": user_input_query, 
                                                    "tools":[search_tool, wiki_tool],
                                                    "tool_names": [t.name for t in tools], 
                                                    "agent_scratchpad": ""})
                final_text = raw_response["output"]
                st.success("Research Completed")
                st.subheader(f"Topic: {user_input_query}")
                st.info(final_text)

                with col2:
                    images = fetch_images(user_input_query)
                    st.subheader("Images:")
                    for img in images:
                        st.image(img)
                    
            except Exception as e:
                print(f"An Error Occured: {e}")
    else:
        st.warning("Please Enter a Query First.")
