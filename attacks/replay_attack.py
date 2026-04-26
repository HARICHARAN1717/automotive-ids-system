import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import time
from ids.ids import process_message

captured_data = ["0x100", "0x200", "0x999"]

def replay_attack():
    print("[⚔️] Starting Replay Attack...")
    
    while True:
        for can_id in captured_data:
            process_message(can_id)
            time.sleep(1)

if __name__ == "__main__":
    replay_attack()
