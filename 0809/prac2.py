from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="天空為何是藍色的"
)

print(interaction.output_text)