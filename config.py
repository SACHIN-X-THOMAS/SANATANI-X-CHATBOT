from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "5959548791"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
SUPPORT_GRP = getenv("SUPPORT_GRP", "Il_4ST_FIGHTER_lI")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ALL_SANATANI_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "V_VIP_OWNER")

# Random Start Images
IMG = [
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgEAAxkBAAIJomRdLhVJVebkx0JRsp1STwTv3t3eAAJrAgAClpxhRD4z4bgqlIF0LwQ",
    "CAACAgUAAxkBAAIJo2RdLhjLjCpmPipMT8ksrqwUjGAIAAK1BQACLZ8oVFVNmhalU8eOLwQ",
    "CAACAgUAAx0CekRwCQADYWWaUnQ2oJqJLbDTZgZbXRT58wuqAAKECgACkgnhVLC0s4joaxF4HgQ",
]


EMOJIOS = [
    "❤️",
    "🧡",
    "💛",
    "💚",
    "💙",
    "💜",
    "🤎",
    "🖤",
    "🤍",
    "♥️",
]
