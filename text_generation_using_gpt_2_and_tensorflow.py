# -*- coding: utf-8 -*-
"""Text Generation using GPT-2 and TensorFlow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zpZnCdLUq7ygDIK0noT9gF3nAzre6aOp
"""

!pip install tensorflow transformers

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Specify the model name (GPT-2)
model_name = "gpt2"

# Load the pre-trained GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Load the pre-trained GPT-2 model
model = GPT2LMHeadModel.from_pretrained(model_name)

# Example text
text = "Hello, how are you?"

# Tokenize the text
input_ids = tokenizer.encode(text, return_tensors="pt")  # "pt" for PyTorch tensor

# Print the tokenized output
print("Tokenized Input:", input_ids)

def generate_text(prompt, max_length=100):
    """
    Generate text using the GPT-2 model.

    Parameters:
        prompt (str): The input text prompt.
        max_length (int): Maximum length of the generated text.

    Returns:
        generated_text (str): The generated text.
    """
    # Encode the input prompt into token IDs
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text using the GPT-2 model
    output = model.generate(
        input_ids,
        max_length=max_length,  # Maximum length of the generated text
        num_return_sequences=1,  # Number of sequences to generate
        no_repeat_ngram_size=2,  # Prevent repetition of n-grams
        top_k=50,  # Top-k sampling
        top_p=0.95,  # Top-p (nucleus) sampling
        temperature=0.7  # Controls randomness (lower = more deterministic)
    )

    # Decode the generated token IDs into text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Example prompt
prompt = "Once Up on a time"

# Generate text
generated_text = generate_text(prompt, max_length=50)
print("Generated Text:", generated_text)

# Save the model
model.save_pretrained("gpt2_model")

# Save the tokenizer
tokenizer.save_pretrained("gpt2_tokenizer")