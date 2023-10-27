from data import patterns, responses
import spacy
nlp = spacy.load("en_core_web_sm")
def chatbot_response(input_text):
    nlp(input_text.lower())
    for category, patterns_list in patterns.items():
        for pattern in patterns_list:
            if pattern in input_text.lower():
                return responses[category]
    return "I'm sorry, I don't understand that. Please ask about test procedures, acceptable limits, issue resolution, safety guidelines, or equipment recommendations."
print("nlpbot: Hello! How can I assist you with Substation Asset Maintenance today? Type 'quit' to exit.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        print("nlpbot: Goodbye! Have a great day!")
        break
    else:
        response = chatbot_response(user_input)
        print("nlpbot:", response)
