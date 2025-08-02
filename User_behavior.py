import json
from datetime import datetime

def save_user_log(user_id, message, event_info):
    log_data = {
        "user_id": user_id,
        "message": message,
        "event_info": event_info,
        "timestamp": datetime.now().isoformat()
    }
    with open("user_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data, ensure_ascii=False) + "\n")
