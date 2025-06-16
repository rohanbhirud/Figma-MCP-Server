# SimplePy MCP Figma Integration

## Getting Started

1. **Install dependencies**

   Using [uv](https://github.com/astral-sh/uv):
   ```sh
   uv venv
   uv pip install -r requirements.txt
   .venv\Scripts\activate
   ```
   Or, using pip:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set up your Figma token**

    Add your Figma token to a `.env` file in the project root:
    ```env
    FIGMA_TOKEN=your_actual_figma_token_here
    ```

3. **Run the MCP Inspector**

   ```sh
   mcp dev server.py
   ```

---

- Make sure you have [uv](https://github.com/astral-sh/uv) installed if you use the uv commands.
- For Windows, use `.venv\Scripts\activate`. For Mac/Linux, use `source .venv/bin/activate`.