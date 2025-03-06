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

# Initialize OpenAI client
client = openai.OpenAI()

# Define GPT-4o model
model_name = "gpt-4o"

# Define output file path (UPDATED LOCATION)
output_directory = r"C:\Users\antho\Documents\AI and ML Internship Projects\Generative_AI_Patent_Drafting\04_Practical_Use_Cases"
output_file_path = os.path.join(output_directory, "generated_contract_summary.txt")

# -------------------------------------------------------
# FUNCTION DEFINITIONS
# -------------------------------------------------------

def summarize_contract(text):
    """
    Summarizes a given legal contract, identifying key obligations and terms.
    """
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a legal expert specializing in contract law. Summarize the key terms of this contract."},
                {"role": "user", "content": f"Summarize this contract:\n{text}"}
            ],
            max_tokens=500
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
    Saves the AI-generated contract summary to a text file in the specified directory.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"\n✅ Contract summary saved to: {file_path}\n")
    except Exception as e:
        print(f"ERROR: Could not save file - {e}")

# -------------------------------------------------------
# EXECUTION PIPELINE
# -------------------------------------------------------

if __name__ == "__main__":
    print("\nGenerating Contract Summary...\n")

    # Example contract text
    contract_text = """
    This agreement outlines the terms for the licensing of AI software. The licensee agrees to use the software 
    only for non-commercial research purposes. The licensor retains full ownership of intellectual property, 
    while the licensee must adhere to strict confidentiality agreements regarding proprietary code and methodologies.
    """

    summary = summarize_contract(contract_text)

    if summary:
        print("\n✅ AI-Generated Contract Summary:\n")
        print(summary)

        # Save to file in specified directory (UPDATED LOCATION)
        save_to_file(summary, output_file_path)

    else:
        print("ERROR: Failed to generate contract summary.")
