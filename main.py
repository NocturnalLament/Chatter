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
    # Main loop
    while True:
        # Get user input
        prompt = input("Enter a prompt: ")
    
        if prompt.lower() == "exit":
            print("Exiting...")
            break
        
        # Generate response
        response = generate_response(prompt)
        
        # Print the response
        print("\n"*2)
        print(f"Prompt: {prompt}")
        print(f"Response: {response}")

if __name__ == "__main__":
    main()
