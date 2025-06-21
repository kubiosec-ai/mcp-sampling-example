## Expose keys 
```
export OPENAI_API_KEY=xxxxxxxxx
export ANTHROPIC_API_KEY=xxxxxxxxx
```
## Run the server
```
uv run server.py --server --transport http --port 8080
```

## Run the clients
```
uv run client.py
```
```
uv run clientopenai.py
```
