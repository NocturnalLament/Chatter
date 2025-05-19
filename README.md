# Chatter - Gemini AI Chat Application

A simple command-line chat application powered by Google's Gemini AI model that allows users to interact with the Gemini-2.0-flash model.

## Features

- Interactive command-line interface
- Real-time responses from Gemini AI
- Easy-to-use prompt system
- Graceful exit functionality

## Prerequisites

- Python 3.x
- Google Cloud API key with Gemini AI access

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Chatter.git
cd Chatter
```

2. Install the required dependencies:
```bash
pip install google-generativeai python-dotenv
```

3. Create a `.env` file in the root directory and add your Google API key:
```bash
GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Enter your prompts when prompted. The application will generate responses using the Gemini AI model.

3. To exit the application, simply type "exit" when prompted for input.

## Example

```
Enter a prompt: What is artificial intelligence?
Prompt: What is artificial intelligence?
Response: [Gemini's response will appear here]

Enter a prompt: exit
Exiting...
```

## Security Note

- Never commit your `.env` file to version control
- Keep your API key secure and private
- Regularly rotate your API keys as per Google Cloud best practices

## License

[Add your chosen license here]

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.
