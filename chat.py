import openai

# Initialize OpenAI API client
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the engine (e.g., text-davinci-003)
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def chat():
    print("Welcome to the OpenAI Chat Interface!")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        response = generate_response(prompt)
        print(f"OpenAI: {response}")

if __name__ == "__main__":
    chat()
