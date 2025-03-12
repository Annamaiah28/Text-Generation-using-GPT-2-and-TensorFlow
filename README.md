# Text Generation using GPT-2 and TensorFlow

This project demonstrates how to generate text using the GPT-2 model with TensorFlow and the Hugging Face Transformers library.

## Requirements
- Python 3.x
- TensorFlow
- Hugging Face Transformers library

## Installation
To install the required libraries, run:
```bash
pip install tensorflow transformers

## Usage
Run the text_generation_using_gpt_2_and_tensorflow.py script to generate text based on a given prompt.

python text_generation_using_gpt_2_and_tensorflow.py

## Requirements

prompt = "Once upon a time"
generated_text = generate_text(prompt, max_length=50)
print("Generated Text:", generated_text)
Saving the Model and Tokenizer
The model and tokenizer are saved in the gpt2_model and gpt2_tokenizer directories, respectively.
