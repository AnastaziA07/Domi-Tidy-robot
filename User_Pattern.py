from collections import defaultdict
import re

def detect_recurring_patterns(log_path="user_log.json"):
    pattern_counts = defaultdict(int)
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            log = json.loads(line)
            text = log["message"]
            # ตรวจหาคำที่พบบ่อย เช่น ประชุม, ไปหาหมอ, ฯลฯ
            if re.search(r"(ประชุม|หาหมอ|เรียนพิเศษ)", text):
                pattern_counts[text] += 1
    # แสดงพฤติกรรมที่เกิดซ้ำ
    return {k: v for k, v in pattern_counts.items() if v > 1}
