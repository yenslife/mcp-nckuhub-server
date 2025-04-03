# nckuhub-mcp

這是一個提供課程相關資訊的 NCKUHub MCP 服務。

## 開發


### 啟動

```base
uv run mcp dev src/nckuhub_mcp/server.py
```

### 測試

```bash
uv run pytest
```

## 使用方法

啟動伺服器

```bash
uv pip install -e .
uv run server.py
```

或者，如果你使用如 Windsurf 等 AI IDE
你可以在 `clime_mcp_settings.json` 檔案中新增以下設定

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