# nckuhub-mcp

中文版請見 [README_zh-TW.md](README_zh-TW.md)

This is a NCKUHub MCP service, providing course-related information.

## Development

### start

```base
uv run mcp dev src/nckuhub_mcp/server.py
```

### test

```bash
uv run pytest
```

## Usage

Start server

```bash
uv pip install -e .
uv run server.py
```

or, if you use the AI IDE such as Windsurf
You can add the following configuration to your `clime_mcp_settings.json` file

```json
{
  "mcpServers": {
    "nckuhub-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/mac/SideProject/nckuhub-mcp/src/nckuhub_mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```