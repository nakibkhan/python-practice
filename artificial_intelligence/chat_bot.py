#Creating sample chat bot using Hugging Face's Transformers library
from transformers import AutoModelForCausalLM, AutoTokenizer
def generate_response(prompt):
    # Load pre-trained model and tokenizer
    model_name = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Encode the input prompt
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Generate a response
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)

    # Decode the generated response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response

if __name__ == "__main__":

    while(True):
        try:
            # Ask the user for a prompt
            prompt = input("Enter your prompt: ")
            if prompt.lower() == 'exit':
                print("Exiting the chat bot.")
                break
            response = generate_response(prompt)
            print("Chat Bot Response:")
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")
            continue