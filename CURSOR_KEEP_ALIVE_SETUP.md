# Cursor Keep-Alive Setup

## Quick Start

1. **Get your Cursor API Key:**
   - Go to https://cursor.com/dashboard
   - Navigate to Integrations section
   - Create/generate an API key

2. **Set the API key (choose one method):**

   **Option A: Environment variable (Windows PowerShell):**
   ```powershell
   $env:CURSOR_API_KEY="your_api_key_here"
   ```

   **Option B: Create .env file:**
   ```
   CURSOR_API_KEY=your_api_key_here
   ```

3. **Run the script:**
   ```powershell
   python cursor_keep_alive.py --interval 5 --message "continue"
   ```

## Usage

```powershell
# Send "continue" every 5 seconds (default)
python cursor_keep_alive.py

# Custom interval and message
python cursor_keep_alive.py --interval 10 --message "keep going"

# Run for limited iterations
python cursor_keep_alive.py --interval 5 --max-iterations 100
```

## Note

The script uses Cursor's Background Agents API. If the API endpoint or format has changed, you may need to update the `send_continue_message()` function in `cursor_keep_alive.py` based on the latest API documentation at https://docs.cursor.com/background-agent/api/overview















