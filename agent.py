from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.book_recommender.agent import book_recommender
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.crypto_analyst.agent import crypto_analyst
from .tools.tools import get_current_time

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent responsible for overseeing and delegating work 
    to the appropriate specialized agents.

    Always delegate the user's request to the most suitable sub-agent.
    Use your best judgment to decide which agent can best accomplish the task.

    You can delegate tasks to the following agents:
    - crypto_analyst
    - book_recommender

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents=[crypto_analyst, book_recommender],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)