
# Import the OpenAI library
import openai

# Set your OpenAI API key here
openai.api_key = "<YOUR_API_KEY>"  # Replace with your OpenAI API key

# This code is for a simple chat application using OpenAI's GPT-3.5 Turbo model.

# Function to send a prompt to the GPT model and get a response
def chat_with_gpt(prompt):
    # Create an OpenAI client with the API key
    client = openai.OpenAI(api_key=openai.api_key)
    # Send the prompt to the chat completion endpoint
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[
            {"role": "user", "content": prompt}  # User's message
        ]
    )
    # Extract and return the assistant's reply
    return response.choices[0].message.content.strip()


# Main loop for the chat application
if __name__ == "__main__":
    while True:
        # Get user input
        user_input = input("You: ")
        # Exit the chat if the user types 'exit' or 'quit'
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break
        # Get the response from the GPT model
        response = chat_with_gpt(user_input)
        # Print the model's response
        print(f"GPT-4: {response}")