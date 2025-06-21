import asyncio
from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.request_params import RequestParams
from mcp_agent.core.prompt import Prompt

fast = FastAgent("Sampling Client Agent")

@fast.agent(
    name="client_sampler",
    instruction="Forward prompt …",
    servers=["sampling-server"],  # ASCII hyphen
    request_params=RequestParams(temperature=0.9),
)

async def client_sampler(prompt: str):
    return await client_sampler.send(prompt)

async def main():
    async with fast.run() as agent_client:
        # Use generate() to get structured response
        resp = await agent_client.client_sampler.generate(
            [Prompt.user("Write a short poem about Brussels.")]
        )
        # Now resp.content gives you parts you can iterate
        for part in resp.content:
            if part.type == "text":
                print("--- Sampled output ---")
                print(part.text)

if __name__ == "__main__":
    asyncio.run(main())
