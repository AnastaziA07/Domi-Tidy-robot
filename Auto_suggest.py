def suggest_event():
    patterns = detect_recurring_patterns()
    for p in patterns:
        print(f"คุณต้องการเพิ่มนัดซ้ำ: \"{p}\" ไหม?")
