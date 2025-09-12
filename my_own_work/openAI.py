import os
import openai
from dotenv import load_dotenv

load_dotenv()

username = "User"

os.environ["OPENAI_API_KEY"] = "your_key_here"
openai.api_key = os.getenv("OPENAI_API_KEY")

print("Your OPENAI key is..", os.getenv("OPENAI_API_KEY"))
print("Hello", username, "Welcome to D.A.V.I.S.")