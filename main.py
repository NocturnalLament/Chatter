import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_response(prompt):
    """
    Generate a response using the Gemini model
    Args:
        prompt (str): The input prompt
    Returns:
        str: The generated response
    """
    response = model.generate_content(prompt)
    return response.text

def main():
    # Example usage
    while True:
        prompt = input("Enter a prompt: ")
        if prompt.lower() == "exit":
            print("Exiting...")
            break
        response = generate_response(prompt)
        print(f"Prompt: {prompt}")
        print(f"Response: {response}")

if __name__ == "__main__":
    main()
