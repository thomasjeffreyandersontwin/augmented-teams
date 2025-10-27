from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(title="MCP Proxy")

class ToolCall(BaseModel):
    name: str
    input: dict

@app.post("/mcp_proxy")
async def call_mcp(tool: ToolCall):
    mcp_base = "https://api.github.com/mcp/tools"
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{mcp_base}/call", json=tool.dict())
        if response.status_code != 200:
            raise HTTPException(response.status_code, response.text)
        return response.json()
