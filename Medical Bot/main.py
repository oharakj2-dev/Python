welcome_prompt = "Welcome Doctor! How can I assist you today?\n - To list all patients, press 1 \n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "Please enter patients name:\n"
appearance_prompt = "Please describe the patient's appearance:\n - 1: Normal\n - 2: Irritable or lethargic\n - 3: Unresponsive\n"
eye_prompt = "Please describe the patient's eye appearance:\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
skin_prompt = "Please perform a skin pinch and describe the patient's skin condition:\n - 1: Normal\n - 2: Skin very dry or tenting\n"
severe_dehydration_prompt = "Severe dehydration detected. Immediate medical attention required!\n"
some_dehydration_prompt = "Some dehydration detected. Further assessment needed.\n"
no_dehydration_prompt = "No dehydration detected. Patient appears to be in good health.\n"

# Function to list all patients
def get_patient_data():
     print("Listing all patients...")
     # This function would typically fetch patient data from a database or an API
     return [
        {"name": "John Doe", "age": 30, "condition": "Flu"},
        {"name": "Jane Smith", "age": 25, "condition": "Cold"},
        {"name": "Alice Johnson", "age": 40, "condition": "Headache"}
     ] 

def assess_skin(skin):
    if skin == '1':
        return no_dehydration_prompt
    elif skin == '2':
        return severe_dehydration_prompt
    else:
        print("Invalid input for skin condition.")
        return

def assess_eyes(eyes):
    if eyes == '1':
        return some_dehydration_prompt
    elif eyes == '2':
        return severe_dehydration_prompt
    else:
        print("Invalid input for eyes.")
        return

# Function to diagnose based on appearance
def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == '1':
        skin = input(skin_prompt)
        return assess_skin(skin)
    elif appearance == '2':
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == '3':
        return "Immediate medical attention required!"
    else:
        print("Invalid input for appearance.")
        return

def starting_new_diagnosis():
     # This function would typically initiate a new diagnosis process
     name = input(name_prompt)
     diagnosis = assess_appearance()
     print(name + ", " + diagnosis)

def main():
    selection = input(welcome_prompt)
    if selection == '1':
        patients = get_patient_data()
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Condition: {patient['condition']}")
    elif selection == '2':
        starting_new_diagnosis()
    elif selection.lower() == 'q':
        print("Goodbye!")
        return
    else:
        print("Invalid selection, please try again.")
        main()

main()