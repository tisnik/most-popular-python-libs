from langchain import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

llm = OpenAI(temperature=0)

tools = load_tools(
    ["graphql"],
    graphql_endpoint="http://0.0.0.0:8000/graphql",
)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

graphql_fields = """
  upgradePrediction {
    recommended,
    lastCheckedAt
  }
}

"""

suffix = "Find out if upgrade is recommended for upgrade predictions stored in the graphql database that has this schema "


agent.run(suffix + graphql_fields)

