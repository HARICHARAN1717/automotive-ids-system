blocked_ids = set()

def block_id(can_id):
    blocked_ids.add(can_id)
    print(f"[🛡️ DEFENSE] Blocking CAN ID: {can_id}")

def is_blocked(can_id):
    return can_id in blocked_ids

