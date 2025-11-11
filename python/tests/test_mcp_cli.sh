### Test Command CLI



install


cd ./python
pip install -e .
pip install mcp-marketplace[mcp_tool_use] -e .


```
mcpm run --port 5000
```

```
mcp run --host 0.0.0.0 --port 5000
```
## Go to 'http://0.0.0.0:5000/mcp' for MCP Admin
## Go to 'http://0.0.0.0:5000' for Chat UI to navigate

### Initialize MCP Client From Local Config.json file
```
mcpm run  --port 5000 --config "./mcp_config_onekey.json"
```