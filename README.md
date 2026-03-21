# coda-io-mcp

A Coda.io MCP server built with FastMCP — expose your Coda docs, pages, and tables to any MCP client.

## Features

- **`list_docs`** — List all Coda docs accessible with your API key, with optional name filter
- **`search_docs`** — Search for Coda docs by name or keyword
- **`list_pages`** — List all pages in a given Coda doc
- **`get_page`** — Retrieve the full content of a Coda page as markdown
- **`update_page`** — Replace the full content of a Coda page
- **`list_rows`** — List rows from a Coda table, with optional query filter and limit
- **`upsert_row`** — Insert or update a row in a Coda table (supports key-column upsert)
- **`delete_row`** — Delete a row from a Coda table by row ID

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- A Coda API key — get yours at [coda.io/account](https://coda.io/account)

## Installation

```bash
git clone https://github.com/<user>/coda-io-mcp
cd coda-io-mcp
uv sync
cp .env.example .env
# edit .env and add your CODA_API_KEY
```

## Claude Desktop setup

Add the following to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "coda": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/coda-io-mcp", "coda-mcp"],
      "env": {
        "CODA_API_KEY": "your_token_here"
      }
    }
  }
}
```

## Claude Code setup

```bash
claude mcp add coda -e CODA_API_KEY=your_token_here -- uv run --directory /path/to/coda-io-mcp coda-mcp
```

## Example prompts

- "List all my Coda docs"
- "Search for docs related to project planning"
- "Show me all pages in doc `AbCdEfGh`"
- "Get the content of page `xyz` in doc `AbCdEfGh`"
- "Add a row to the Tasks table in my doc with column Status set to Done"

## Tool reference

| Tool | Description | Key parameters |
|------|-------------|----------------|
| `list_docs` | List all accessible Coda docs | `query` (optional filter) |
| `search_docs` | Search docs by name or keyword | `query` |
| `list_pages` | List all pages in a doc | `doc_id` |
| `get_page` | Get page content as markdown | `doc_id`, `page_id` |
| `update_page` | Replace full page content | `doc_id`, `page_id`, `content` |
| `list_rows` | List rows from a table | `doc_id`, `table_id`, `limit`, `query` |
| `upsert_row` | Insert or update a row | `doc_id`, `table_id`, `cells`, `key_columns` |
| `delete_row` | Delete a row by ID | `doc_id`, `table_id`, `row_id` |

## Contributing

Contributions are welcome! Open an issue or submit a pull request for bug fixes, new tools, or improvements. Please keep PRs focused and include a clear description of the change.

## License

MIT — Copyright Eduardo Brito 2026
