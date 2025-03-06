### GENERATIVE AI BASICS: TESTING GPT-4o CAPABILITIES  

## OBJECTIVE  
This section tests GPT-4o for structured legal text generation, ensuring the API is set up correctly and can produce useful results for patent drafting.  

---  

## WHAT THIS SCRIPT DOES (`test_gpt4.py`)  
✔ Connects to GPT-4o using the OpenAI API.  
✔ Generates a structured patent abstract based on a legal prompt.  
✔ Confirms that the API key is properly configured and functional.  

---  

## SETUP INSTRUCTIONS  

### 1️⃣ INSTALL DEPENDENCIES  
First, check if Python is installed:  
```powershell
python --version
```  
Then install the OpenAI library:  
```powershell
pip install openai
```  

### 2️⃣ SET UP API KEY  
The OpenAI API key is not stored in this repository for security reasons.  
You must set it manually before running the script:  

```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```  
Check if the key is set correctly:  
```powershell
echo $env:OPENAI_API_KEY
```  

⚠️ DO NOT hardcode the API key inside the script. Always store it securely in environment variables.  

---  

## RUNNING THE SCRIPT  
Run the script from the command line:  
```powershell
python test_gpt4.py
```  
If everything is set up correctly, the script will:  
✔ Generate an AI-created patent abstract.  
✔ Confirm that the API key is working properly.  
✔ Save the generated results to a text file.  

---  

## EXPECTED OUTPUT  
The AI will generate an overview of Generative AI, including:  

```
Title: Autonomous Vehicle Control System with Advanced AI

Technical Field: This invention relates to autonomous vehicles and their AI-based control mechanisms...

Background: Traditional self-driving systems lack adaptability in complex urban settings...

Summary: The system processes sensor data in real-time using deep learning algorithms...

Advantages:
1. Enhanced safety through predictive hazard detection.
2. Optimized route efficiency to reduce energy consumption.
3. Continuous self-improvement via adaptive learning models.
```
This confirms GPT-4o is functioning correctly and generating structured legal text as expected.  

---  

## WHERE RESULTS ARE STORED  
The generated output is saved as a text file:  
📂 Location:  
```
C:\Users\antho\Documents\AI and ML Internship Projects\Generative_AI_Patent_Drafting\01_Generative_AI_Basics\generated_ai_summary.txt
```  

---  

## WHY THIS MATTERS  
✔ Legal Accuracy → Ensures structured and compliant patent abstracts.  
✔ Time Efficiency → Reduces manual drafting time.  
✔ Innovation → Automates complex text generation for legal professionals.  

---  

## QUESTIONS & COLLABORATION  
👤 Anthony Broderick  
📩 Open to feedback, improvements, and discussions. Reach out.