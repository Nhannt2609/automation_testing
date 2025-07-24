from dotenv import load_dotenv
import os

load_dotenv()

AGENT_EMAIL = os.getenv('AGENT_EMAIL')
AGENT_PASSWORD = os.getenv('AGENT_PASSWORD')
CONSIGNEE_EMAIL = os.getenv('CONSIGNEE_EMAIL')
CONSIGNEE_PASSWORD = os.getenv('CONSIGNEE_PASSWORD')
SIGNIN_URL = os.getenv('SIGNIN_URL')
JOBS_URL = os.getenv('JOBS_URL')
