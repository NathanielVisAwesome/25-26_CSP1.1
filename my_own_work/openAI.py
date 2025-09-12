import os
import openai
from dotenv import load_dotenv

load_dotenv()

username = "User"

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

print("Your OPENAI key is..", os.getenv("OPENAI_API_KEY"))
print("Hello", username, "Welcome to D.A.V.I.S.")