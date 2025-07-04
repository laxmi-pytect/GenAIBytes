###client.py####
from google import genai
import asyncio
import dotenv,os
import getpass

# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from langchain.chat_models import init_chat_model


dotenv.load_dotenv()

GEMINI_API_KEY = os.environ.get("gemini_key")

if not GEMINI_API_KEY:
    GEMINI_API_KEY = getpass.getpass("Enter API key for Google Gemini: ")

gemini_key=GEMINI_API_KEY


model = init_chat_model("gemini-2.0-flash", model_provider="google_genai", api_key=gemini_key)
import logging

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["../MCP/mcp_server.py"],)


async def agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            logging.info("session", session)
                
            # Get tools
            tools = await load_mcp_tools(session)
    
            # Create and run the agent
            agent = create_react_agent(model, tools)

            ###this invocation call add tools ###
            #agent_response = await agent.ainvoke({"messages": "what's 5+8 ?"})

            ###this invocation call multiple tools ###
            #agent_response = await agent.ainvoke({"messages": "what's 55 * 22 ?"})

            ###this invocation call both tools ###
            agent_response = await agent.ainvoke({"messages": "what's (-3 +8) * 12?"})
            return agent_response


if __name__=="__main__":
    result=asyncio.run(agent())
    print(result['messages'][-1])



