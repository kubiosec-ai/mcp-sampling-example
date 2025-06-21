import asyncio
from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.request_params import RequestParams

fast = FastAgent("Sampling Server Agent")

@fast.agent(
    name="client_sampler",
    instruction="Respond using GPT‑4o sampling mode",
    request_params=RequestParams(temperature=0.9),
)
async def client_sampler(prompt: str):
    # When called by client, forward to GPT-4o and return output
    return await client_sampler.send(prompt)

async def main():
    # Start as an HTTP MCP server (or SSE)
    await fast.start_server(
        transport="http",
        host="0.0.0.0",
        port=8080,
        server_name="sampling-server",  # ASCII hyphen
        server_description="Server using GPT‑4o for sampling",  # Note: em dash is okay in descriptions
    )

if __name__ == "__main__":
    asyncio.run(main())
