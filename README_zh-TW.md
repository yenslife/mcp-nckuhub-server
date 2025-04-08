# mcp-nckuhub-server

這是一個使用 NCKUHub API 的 MCP 服務。

以下是 Demo 影片

[![IMAGE ALT TEXT](https://img.youtube.com/vi/ER6fYSY3aVE/0.jpg)](https://www.youtube.com/watch?v=ER6fYSY3aVE)

## 開發


### 啟動

```bash
uv run mcp dev src/mcp-nckuhub-server/server.py
```

### 測試

```bash
uv run pytest
```

## 使用方法

啟動伺服器

```bash
uv pip install -e .
uv run mcp-nckuhub-server
```

或者，如果你使用如 Windsurf 等 AI IDE
你可以在 `clime_mcp_settings.json` 檔案中新增以下設定

```json
{
  "mcpServers": {
    "mcp-nckuhub-server": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/mcp-nckuhub-server",
        "run",
        "mcp-nckuhub-server"
      ]
    }
  }
}
```