# nckuhub-mcp

中文版請見 [README_zh-TW.md](README_zh-TW.md)

This is an MCP service using the NCKUHub API.

Demo video

[![IMAGE ALT TEXT](https://img.youtube.com/vi/ER6fYSY3aVE/0.jpg)](https://www.youtube.com/watch?v=ER6fYSY3aVE)

## Development

### Start

```bash
uv run mcp dev src/nckuhub_mcp/server.py
```

### Test

```bash
uv run pytest
```

## Usage

Start server

```bash
uv pip install -e .
uv run nckuhub-mcp
```

Or, if you use an AI IDE such as Windsurf
You can add the following configuration to your `clime_mcp_settings.json` file

```json
{
  "mcpServers": {
    "nckuhub-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/nckuhub-mcp",
        "run",
        "nckuhub-mcp"
      ]
    }
  }
}
```