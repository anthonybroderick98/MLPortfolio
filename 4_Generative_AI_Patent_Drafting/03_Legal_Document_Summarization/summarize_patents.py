import os
import openai

# Retrieve API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key is set
if api_key is None:
    raise ValueError("OpenAI API key not found. Set the environment variable OPENAI_API_KEY.")

# Initialize OpenAI client
client = openai.OpenAI()

# Define GPT-4o model
model_name = "gpt-4o"

def summarize_patent(text):
    """
    Summarizes a given patent document, extracting key technical claims and novelty.
    """
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a legal expert specializing in patent summarization. Extract key claims and technical details."},
                {"role": "user", "content": f"Summarize this patent document:\n{text}"}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

    except openai.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return None

if __name__ == "__main__":
    # Example patent document input
    patent_text = """
    This patent describes a new method for optimizing AI-generated text by using reinforcement learning. 
    The system consists of a neural network model trained on a dataset of legal documents and fine-tuned 
    through iterative self-improvement cycles. The invention aims to improve the consistency and accuracy 
    of AI-generated patent claims.
    """

    print("\nGenerating Patent Summary...\n")
    summary = summarize_patent(patent_text)

    if summary:
        print("AI-Generated Patent Summary:\n")
        print(summary)
    else:
        print("Failed to generate summary.")
