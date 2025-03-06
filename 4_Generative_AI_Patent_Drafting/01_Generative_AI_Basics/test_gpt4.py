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
output_directory = r"C:\Users\antho\Documents\AI and ML Internship Projects\Generative_AI_Patent_Drafting\01_Generative_AI_Basics"
output_file_path = os.path.join(output_directory, "generated_ai_basics_output.txt")

# -------------------------------------------------------
# FUNCTION DEFINITIONS
# -------------------------------------------------------

def generate_ai_basics_summary():
    """
    Generates a structured summary of AI basics using GPT-4o.
    """
    try:
        # Request GPT-4o to generate a summary
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are an expert in AI, providing clear, structured explanations."},
                {"role": "user", "content": "Generate a structured summary explaining Generative AI, its capabilities, and practical applications."}
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
    Saves the AI-generated summary to a text file in the specified directory.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"\n✅ AI summary saved to: {file_path}\n")
    except Exception as e:
        print(f"ERROR: Could not save file - {e}")

# -------------------------------------------------------
# EXECUTION PIPELINE
# -------------------------------------------------------

if __name__ == "__main__":
    print("\nGenerating AI Basics Summary...\n")

    ai_basics_summary = generate_ai_basics_summary()

    if ai_basics_summary:
        print("\nAI-Generated Summary:\n")
        print(ai_basics_summary)

        # Save to file in specified directory
        save_to_file(ai_basics_summary, output_file_path)

    else:
        print("ERROR: Failed to generate AI summary.")
