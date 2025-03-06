# ---------------------------------------------------
# AI-Generated Patent Analysis Using OpenAI
# ---------------------------------------------------
# This script applies OpenAI's language model to analyze and extract insights from patent documents.
# It is designed for use in patent analysis workflows, specifically assisting patent attorneys in evaluating AI-generated inventions.
#
# The analysis leverages machine learning to identify relevant legal considerations, such as novelty, inventive step, and prior art, 
# aligning with IP law's requirements for patentability.
#
# Steps:
# 1. Retrieve OpenAI API key securely.
# 2. Initialize OpenAI client to interact with GPT models.
# 3. Define the model and function to analyze a sample patent document.
# 4. Execute the analysis, save it to a file, and print results for review.
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
client = openai.OpenAI(api_key=api_key)

# ---------------------------------------------------
# 3️⃣ Define Model and Patent Analysis Function
# ---------------------------------------------------
def analyze_patent(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Model chosen based on compatibility with OpenAI access.
            messages=[
                {"role": "system", "content": "You are a legal AI expert specializing in patent analysis."},
                {"role": "user", "content": f"Analyze this patent document:\n{text}"}
            ]
        )
        return response.choices[0].message.content

    except openai.OpenAIError as e:
        print(f"❌ OpenAI API Error: {e}")
        return None

# ---------------------------------------------------
# 4️⃣ Run the Script
# ---------------------------------------------------
if __name__ == "__main__":
    # Sample patent text (replace with actual patent data for legal use)
    sample_patent = """
    A method for enhancing AI-generated text by employing reinforcement learning. The system includes a neural network trained on legal datasets, improving its ability to generate structured patent claims.
    """
    
    # Perform the analysis
    patent_analysis = analyze_patent(sample_patent)

    # Check if analysis was successful
    if patent_analysis:
        # Define the folder and file name to save results
        folder_path = os.path.dirname(os.path.abspath(__file__))  # Gets the folder where the script is located
        output_file_path = os.path.join(folder_path, "ai_patent_analysis_output.txt")

        # Save the analysis to a file
        with open(output_file_path, "w") as file:
            file.write(patent_analysis)

        # Print confirmation and file location
        print(f"✅ AI-Generated Patent Analysis saved to: {output_file_path}")

    else:
        print("❌ Failed to analyze patent.")
