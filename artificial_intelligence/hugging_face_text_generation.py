#Hugging Face demo
from transformers import pipeline
def generate_text(prompt):
    # Load the text generation pipeline
    generator = pipeline('text-generation', model='gpt2')

    # Generate text based on the prompt
    generated_text = generator(prompt, max_length=50, num_return_sequences=1)

    # Return the generated text
    return generated_text[0]['generated_text']
if __name__ == "__main__":
    prompt = "Once upon a time in a land far, far away,"
    generated_text = generate_text(prompt)
    print("Generated Text:")
    print(generated_text)
