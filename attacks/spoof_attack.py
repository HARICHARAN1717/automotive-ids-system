import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import time
from ids.ids import process_message

def spoof_attack():
    print("[⚔️] Starting Spoof Attack...")
    
    while True:
        process_message("0xABC")  # fake identity
        time.sleep(1)

if __name__ == "__main__":
    spoof_attack()
