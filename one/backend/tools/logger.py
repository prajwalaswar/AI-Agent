import json, os
from datetime import datetime

class InteractionLogger:
    def log(self, agent: str, action: str, details: dict):
        os.makedirs("logs", exist_ok=True)
        entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent,
            "action": action,
            "details": details
        }
        with open("logs/interactions.log", "a") as f:
            f.write(json.dumps(entry) + "\n")