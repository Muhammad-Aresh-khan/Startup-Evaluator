from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os
from litellm import completion
from langchain_community.chat_models import ChatLiteLLM

# Load environment variables
load_dotenv()

# Setup LangChain's Google Gemini LLM
llm =ChatLiteLLM(
    model="groq/llama-3.1-8b-instant",  
    provider="Groq",
    google_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5
)

# Define agents
idea_analyst = Agent(
    role="Startup Idea Analyst",
    goal="Understand and break down the startup idea into features",
    backstory="You are great at interpreting user startup pitches.",
    verbose=True,
    llm=llm
)

name_creator = Agent(
    role="Brand Name Generator",
    goal="Generate unique, short and brandable names",
    backstory="Expert in marketing and catchy naming strategies.",
    verbose=True,
    llm=llm
)

market_researcher = Agent(
    role="Market Research Analyst",
    goal="Evaluate product market fit and suggest ideal audience",
    backstory="Specializes in early-stage startup market analysis.",
    verbose=True,
    llm=llm
)

# Task creation
def create_tasks(user_idea):
    return [
        Task(
            description=f"Analyze this idea: {user_idea}",
            agent=idea_analyst,
            expected_output="A detailed analysis of the startup idea, including its core features and value proposition."
        ),
        Task(
            description=f"Create a catchy startup name for: {user_idea}",
            agent=name_creator,
            expected_output="A short, brandable, and memorable startup name based on the idea."
        ),
        Task(
            description=f"Evaluate the market fit and ideal users for: {user_idea}",
            agent=market_researcher,
            expected_output="An evaluation of the potential market, user segments, and product-market fit."
        )
    ]

# Run the crew
def run_crew(user_idea):
    tasks = create_tasks(user_idea)
    crew = Crew(
        agents=[idea_analyst, name_creator, market_researcher],
        tasks=tasks,
        llm=llm,
        llm_type="langchain",
        verbose=True
    )
    return crew.kickoff()


