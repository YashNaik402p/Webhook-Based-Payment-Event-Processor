import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "payment_logs.txt")
# Setup logger
logging.basicConfig(
    filename=LOG_PATH,    
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_event(user_id, event):
    if event == "payment_success":
        logging.info(f"SUCCESS - User {user_id} payment successful")
        print(f"LOG: SUCCESS - User {user_id} payment successful")
    else:
        logging.warning(f"FAILED - User {user_id} payment failed")
        print(f"LOG: FAILED - User {user_id} payment failed")