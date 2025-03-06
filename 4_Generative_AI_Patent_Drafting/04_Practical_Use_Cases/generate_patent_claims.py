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
output_file_path = os.path.join(output_directory, "generated_patent_claims.txt")

# -------------------------------------------------------
# FUNCTION DEFINITIONS
# -------------------------------------------------------

def generate_patent_claims(invention_description):
    """
    Generates structured patent claims for an AI-powered invention.
    """
    try:
        # Request GPT-4o to generate structured patent claims
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are an expert patent attorney specializing in drafting structured patent claims."},
                {"role": "user", "content": f"Generate structured patent claims for the following invention:\n{invention_description}"}
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
    Saves the AI-generated patent claims to a text file in the specified directory.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"\n✅ Patent claims saved to: {file_path}\n")
    except Exception as e:
        print(f"ERROR: Could not save file - {e}")

# -------------------------------------------------------
# EXECUTION PIPELINE
# -------------------------------------------------------

if __name__ == "__main__":
    print("\nGenerating Patent Claims...\n")

    # Example invention description input
    invention_text = """
    An AI-powered chatbot that adapts dynamically to user emotions, utilizing sentiment analysis and contextual learning.
    """

    claims = generate_patent_claims(invention_text)

    if claims:
        print("\n✅ AI-Generated Patent Claims:\n")
        print(claims)

        # Save to file in specified directory (UPDATED LOCATION)
        save_to_file(claims, output_file_path)

    else:
        print("ERROR: Failed to generate patent claims.")
