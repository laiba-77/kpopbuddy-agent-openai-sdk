import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv
      
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

my_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_api(my_client)
set_tracing_disabled(True)

my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=my_client
)

def run_agent():
    kpop_agent = Agent(
        name="KpopBuddy",
        instructions="""
        You are KpopBuddy, a friendly expert on K-pop music and culture.
        You help users learn about K-pop groups, songs, terminology, and fandoms.
        Explain concepts in simple language and provide helpful facts.
        Always answer enthusiastically, like a fellow K-pop fan!
        """,
        model=my_model
        )
    
    prompt="What is a K-pop comeback?"


    result = Runner.run_sync(kpop_agent, prompt)
    
    # Create or append to a Markdown file
    with open("Aioutput.md", "a", encoding="utf-8") as file:
        file.write(f"### Prompt:\n{prompt}\n\n")
        file.write(f"### Response:\n{result.final_output}\n\n---\n\n")


    print(f"Prompt: {prompt}")
    print(f"Response: {result.final_output}")

