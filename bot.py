from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained model and tokenizer
model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()

# Main interaction loop
print("Chatbot: Hello! I am a Substation Asset Maintenance bot. How can I assist you today? Type 'quit' to exit.")
while True:
    user_input = input("User: ")

    # Check if user wants to quit
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Modify user input to include the specific prompt
    user_input_with_prompt = f"Pretend as if you are a Substation Asset Maintenance bot and {user_input}"

    # Tokenize the modified user input
    input_ids = tokenizer.encode(user_input_with_prompt, return_tensors="pt")

    # Generate a response from the model
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100)[0]

    # Decode and print the model's response
    chatbot_response = tokenizer.decode(output, skip_special_tokens=True)
    print("Chatbot:", chatbot_response)
