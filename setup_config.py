import json
import os

# 1. NEW PATHS (Safe from OneDrive)
python_path = r"C:\Users\nikhi\quant-mind\venv\Scripts\python.exe"
server_path = r"C:\Users\nikhi\quant-mind\server.py"
config_path = os.path.expandvars(r"%APPDATA%\Claude\claude_desktop_config.json")

# 2. Create the configuration
config = {
    "mcpServers": {
        "quant-mind": {
            "command": python_path,
            "args": [server_path]
        }
    }
}

# 3. Write the file
print(f"Attempting to write config to: {config_path}")
try:
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    print("✅ SUCCESS! Config updated to SAFE location.")
except Exception as e:
    print(f"❌ ERROR: {e}")