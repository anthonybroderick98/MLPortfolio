# -------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# -------------------------------------------------------

import os
import openai

# -------------------------------------------------------
# API CONFIGURATION
# -------------------------------------------------------

# Retrieve API key securely
api_key = os.getenv("OPENAI_API_KEY")

# Handle missing API key
if api_key is None:
    raise ValueError("ERROR: OpenAI API key not found. Set the environment variable OPENAI_API_KEY.")

# Create OpenAI client
client = openai.OpenAI()

# Define model
model_name = "gpt-4o"  # Using GPT-4 Omni

# Define output file path
output_directory = r"C:\Users\antho\Documents\AI and ML Internship Projects\Generative_AI_Patent_Drafting\02_Patent_Drafting"
output_file_path = os.path.join(output_directory, "generated_patent_abstract.txt")

# -------------------------------------------------------
# FUNCTION DEFINITIONS
# -------------------------------------------------------

def generate_structured_patent_abstract():
    """
    Generates a structured patent abstract following a predefined format.
    """
    try:
        # Request GPT-4o to generate a structured patent abstract
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are an expert patent attorney. Follow this format: [Title], [Technical Field], [Background], [Summary], [Advantages]."},
                {"role": "user", "content": "Generate a structured patent abstract for a self-driving car AI."}
            ],
            max_tokens=300
        )

        # Extract and validate response
        if response and response.choices:
            return response.choices[0].message.content.strip()
        else:
            print("ERROR: Received empty response from OpenAI.")
            return None

    except openai.OpenAIError as e:
        print(f"ERROR: OpenAI API Error: {e}")
        return None

def save_to_file(content, file_path):
    """
    Saves the AI-generated patent abstract to a text file in the specified directory.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"\n✅ Patent abstract saved to: {file_path}\n")
    except Exception as e:
        print(f"ERROR: Could not save file - {e}")

# -------------------------------------------------------
# EXECUTION PIPELINE
# -------------------------------------------------------

if __name__ == "__main__":
    print("\nGenerating Structured Patent Abstract...\n")

    structured_abstract = generate_structured_patent_abstract()

    if structured_abstract:
        print("\nAI-Generated Structured Patent Abstract:\n")
        print(structured_abstract)

        # Save to file in specified directory
        save_to_file(structured_abstract, output_file_path)

    else:
        print("ERROR: Failed to generate structured patent abstract.")
