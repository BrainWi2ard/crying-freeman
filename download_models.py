from transformers import AutoModel, AutoTokenizer
import os

# List of models to download
models = [
    "bert-base-uncased",
    "gpt2",
    "roberta-base",
    "distilbert-base-uncased",
    "t5-base",
    "xlnet-base-cased",
    "facebook/bart-large",
    "albert-base-v2"
]

# Directory to store the models
model_dir = "models"

# Create the directory if it doesn't exist
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Download and save each model
for model_name in models:
    print(f"Downloading {model_name}...")
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.save_pretrained(os.path.join(model_dir, model_name))
    tokenizer.save_pretrained(os.path.join(model_dir, model_name))

print("All models downloaded and saved successfully.")
