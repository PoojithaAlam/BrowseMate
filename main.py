import asyncio
import os
import streamlit as st
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM
from mcp_agent.workflows.llm.augmented_llm import RequestParams
from ui import render_ui
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Streamlit session state
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.mcp_app = MCPApp(name="streamlit_mcp_agent")
    st.session_state.mcp_context = None
    st.session_state.mcp_agent_app = None
    st.session_state.browser_agent = None
    st.session_state.llm = None
    st.session_state.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(st.session_state.loop)

# Setup the MCP agent and attach LLM
async def setup_agent():
    if not st.session_state.initialized:
        try:
            st.session_state.mcp_context = st.session_state.mcp_app.run()
            st.session_state.mcp_agent_app = await st.session_state.mcp_context.__aenter__()

            st.session_state.browser_agent = Agent(
                name="browser",
                instruction="""You are a helpful web browsing assistant that can interact with websites using Puppeteer.
                - Navigate to websites and perform browser actions (click, scroll, type)
                - Extract information from web pages
                - Take screenshots of page elements when useful
                - Provide concise summaries of web content using markdown
                - Follow multi-step browsing sequences to complete tasks
                """,
                server_names=["puppeteer"]
            )

            await st.session_state.browser_agent.initialize()
            st.session_state.llm = await st.session_state.browser_agent.attach_llm(OpenAIAugmentedLLM)

            logger = st.session_state.mcp_agent_app.logger
            tools = await st.session_state.browser_agent.list_tools()
            logger.info("Tools available:", data=tools)

            st.session_state.initialized = True
        except Exception as e:
            return f"Error during initialization: {str(e)}"
    return None

# Run the agent and fetch a response from the LLM
async def run_mcp_agent(message):
    if not os.getenv("OPENAI_API_KEY"):
        return "❌ Error: OPENAI_API_KEY not found in environment variables."

    try:
        error = await setup_agent()
        if error:
            return error

        result = await st.session_state.llm.generate_str(
            message=message,
            request_params=RequestParams(use_history=True)
        )

        return result if result else "⚠️ No response received from LLM."
    except Exception as e:
        return f"❌ Agent execution error: {str(e)}"

# Synchronous wrapper to call async LLM agent
def run_agent_sync(query):
    return st.session_state.loop.run_until_complete(run_mcp_agent(query))

# Render UI and get input
query = render_ui("", run_agent_sync)


