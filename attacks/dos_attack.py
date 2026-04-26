import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




import time
from ids.ids import process_message

def dos_attack():
    print("[⚔️] Starting DoS Attack...")
    
    while True:
        process_message("0x999")  # malicious CAN ID
        time.sleep(0.1)  # very fast = flood

if __name__ == "__main__":
    dos_attack()
