# Define a dictionary of symptoms and corresponding illnesses illnesses = { 
    "fever": "You may have a viral or bacterial infection.", 
    "cough": "You might be suffering from a respiratory infection or allergies.", 
    "headache": "There are various causes for a headache, such as stress, tension, or migraines.",     # Add more symptoms and illnesses as needed 
} 
 
# Function to process user input and provide an appropriate response def process_input(symptoms):     response = ""     for symptom in symptoms:         if symptom in illnesses: 
            response += f"{symptom}: {illnesses[symptom]}\n"         else: 
            response += f"{symptom}: Unknown illness\n"     return response 
 
# Main program loop while True: 
user_input = input("Please enter your symptoms (separated by commas): ")     
user_symptoms = [symptom.strip().lower() for symptom in user_input.split(",")]     
bot_response = process_input(user_symptoms)     
print(bot_response) 
