import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import random
from ids.ids import process_message

CAN_IDS = ["0x100", "0x200", "0x300", "0x999", "0xABC"]

def simulate():
    while True:
        can_id = random.choice(CAN_IDS)
        process_message(can_id)
        time.sleep(2)

if __name__ == "__main__":
    simulate()
