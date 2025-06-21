import os
import asyncio
from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.request_params import RequestParams
from mcp_agent.core.prompt import Prompt
from dotenv import load_dotenv

# Load API key from .env or system
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY environment variable is required")

fast = FastAgent("OpenAI GPT-4.1 Client Agent")

@fast.agent(
    name="client_sampler",
    instruction="Use GPT‑4.1 for sampling via OpenAI",
    servers=["sampling-server"],
    request_params=RequestParams(
        temperature=0.9,
    ),
)
async def client_sampler(prompt: str):
    return await client_sampler.send(prompt)

async def main():
    async with fast.run() as agent_client:
        resp = await agent_client.client_sampler.generate([Prompt.user("Write a short poem about Brussels.")])
        for part in resp.content:
            if part.type == "text":
                print(part.text)

if __name__ == "__main__":
    asyncio.run(main())
