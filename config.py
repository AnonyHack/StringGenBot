from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("8321864901:AAEQeg7Ct9JyGDc8RDMA736rGESs886lck0")
MONGO_URL = getenv("mongodb+srv://anonymousguywas:12345Trials@cluster0.t4nmrtp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 5962658076))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Megahubbots")

