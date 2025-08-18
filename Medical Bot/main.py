welcome_prompt = "Welcome Doctor! How can I assist you today?\n - To list all patients, press 1 \n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "Please enter patients name:\n"
appearance_prompt = "Please describe the patient's appearance:\n - 1: Normal\n - 2: Irritable or lethargic\n"
eye_prompt = "Please describe the patient's eye appearance:\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
skin_prompt = "Please perform a skin pinch and describe the patient's skin condition:\n - 1: Normal\n - 2: Skin very dry or tenting\n"
severe_dehydration_prompt = "Severe dehydration detected. Immediate medical attention required!\n"
some_dehydration_prompt = "Some dehydration detected. Further assessment needed.\n"
no_dehydration_prompt = "No dehydration detected. Patient appears to be in good health.\n"

patients_and_diagnosis = [
    "Mike, No dehydration detected. Patient appears to be in good health.",
    "Sarah, Some dehydration detected. Further assessment needed.",
    "Tom, Severe dehydration detected. Immediate medical attention required!"
]

# Function to list all patients
def get_patient_data():
     # This function would typically fetch patient data from a database or an API
     for patient in patients_and_diagnosis:
         print(patient)

def save_new_diagnosis(name, diagnosis):
    # This function would typically save the new diagnosis to a database or an API
    final_diagnosis = name + ", " + diagnosis
    patients_and_diagnosis.append(final_diagnosis)
    print(final_diagnosis + " has been added to the patient list.\n") 


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
    else:
        print("Invalid input for appearance.")
        return

def starting_new_diagnosis():
     # This function would typically initiate a new diagnosis process
     name = input(name_prompt)
     diagnosis = assess_appearance()
     if diagnosis is not None:
         save_new_diagnosis(name, diagnosis)
     else:
         print("Diagnosis could not be completed due to invalid input.\n")
         return
    
def main():
    selection = input(welcome_prompt)
    if selection == '1':
        get_patient_data()
    elif selection == '2':
        starting_new_diagnosis()
    elif selection.lower() == 'q':
        print("Goodbye!")
        return
    else:
        print("Invalid selection, please try again.")
        return

main()
