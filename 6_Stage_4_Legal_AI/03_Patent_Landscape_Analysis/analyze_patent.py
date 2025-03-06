# ---------------------------------------------------
# AI-Generated Patent Landscape Analysis Using OpenAI
# ---------------------------------------------------
# This script applies OpenAI's language model to analyze patent trends and the patent landscape.
# It is designed for use in patent analysis workflows, specifically assisting patent attorneys and researchers
# in evaluating the trends and filing patterns of AI-related patents.
#
# The analysis leverages machine learning to identify major players, technological trends, and potential gaps in the patent landscape.
#
# Steps:
# 1. Retrieve OpenAI API key securely.
# 2. Initialize OpenAI client to interact with GPT models.
# 3. Define the model and function to analyze the patent landscape.
# 4. Execute the analysis, save results to a file, and print output for review.
# ---------------------------------------------------

import os
import openai

# ---------------------------------------------------
# 1️⃣ Retrieve OpenAI API Key Securely
# ---------------------------------------------------
api_key = os.getenv("OPENAI_API_KEY")

# ❌ Handle missing API key
if not api_key:
    raise ValueError("❌ ERROR: OpenAI API key not found. Set the environment variable OPENAI_API_KEY.")

# ---------------------------------------------------
# 2️⃣ Initialize OpenAI Client
# ---------------------------------------------------
openai.api_key = api_key

# ---------------------------------------------------
# 3️⃣ Define Model and Patent Landscape Analysis Function
# ---------------------------------------------------
def analyze_patent_landscape(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the correct model identifier for GPT-4
            messages=[
                {"role": "system", "content": "You are an AI specializing in patent landscape analysis."},
                {"role": "user", "content": f"Analyze the following patent landscape:\n{text}"}
            ]
        )
        return response['choices'][0]['message']['content']

    except openai.OpenAIError as e:
        print(f"❌ OpenAI API Error: {e}")
        return None

# ---------------------------------------------------
# 4️⃣ Run the Script
# ---------------------------------------------------
if __name__ == "__main__":
    # Sample patent landscape text (this should be replaced with actual patent data)
    sample_patent_data = """
    The dataset includes patents related to AI-driven medical diagnosis, neural network optimization, and real-time speech recognition. Companies filing these patents include OpenAI, DeepMind, and IBM.
    """

    # Perform the analysis
    landscape_analysis = analyze_patent_landscape(sample_patent_data)

    # Check if the analysis was successful
    if landscape_analysis:
        folder_path = os.path.dirname(os.path.abspath(__file__))  # Get the script folder
        output_file_path = os.path.join(folder_path, "ai_patent_landscape_analysis_output.txt")

        # Save the analysis to a file
        with open(output_file_path, "w") as file:
            file.write(landscape_analysis)

        # Print confirmation and output file location
        print(f"✅ AI-Generated Patent Landscape Analysis saved to: {output_file_path}")

    else:
        print("❌ Failed to analyze patent landscape.")
