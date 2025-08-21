import os

# Set file_path to point to 'patients.txt' 
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patients.txt")

welcome_prompt = "Welcome Doctor! How can I assist you today?\n - To list all patients, press 1 \n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "Please enter patients name:\n"
appearance_prompt = "Please describe the patient's appearance:\n - 1: Normal\n - 2: Irritable or lethargic\n"
eye_prompt = "Please describe the patient's eye appearance:\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
skin_prompt = "Please perform a skin pinch and describe the patient's skin condition:\n - 1: Normal\n - 2: Skin very dry or tenting\n"
severe_dehydration_prompt = "Severe dehydration detected. Immediate medical attention required!\n"
some_dehydration_prompt = "Some dehydration detected. Further assessment needed.\n"
no_dehydration_prompt = "No dehydration detected. Patient appears to be in good health.\n"
error_prompt = "Could not save patient and diagnosis due to invalid input.\n"


patients_and_diagnosis = [
    "Mike, No dehydration detected. Patient appears to be in good health.",
    "Sarah, Some dehydration detected. Further assessment needed.",
    "Tom, Severe dehydration detected. Immediate medical attention required!"
]

# Function to list all patients from patients.txt
def get_patient_data():
    #for patient in patients_and_diagnosis:
    #    print(patient)
    if not os.path.exists(file_path):
        print("No patient data found.\n")
        return
    with open(file_path, "r") as patients:
        print(patients.read())

# Function to save a new diagnosis to patients.txt
def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_prompt)
        return
    final_diagnosis = name + ", " + diagnosis
    #patients_and_diagnosis.append(final_diagnosis)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(final_diagnosis + "\n")
            f.close()
    else: 
        with open(file_path, "a") as f:
            f.write(final_diagnosis + "\n")
            f.close()
    print(final_diagnosis + " has been added to the patient list.\n") 


def assess_skin(skin):
    if skin == '1':
        return no_dehydration_prompt
    elif skin == '2':
        return severe_dehydration_prompt
    else:
        return ""

def assess_eyes(eyes):
    if eyes == '1':
        return some_dehydration_prompt
    elif eyes == '2':
        return severe_dehydration_prompt
    else:
        return ""

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
        return ""

def starting_new_diagnosis():
     # Collects patient name, assesses appearance, and saves the new diagnosis
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
main()

# def test_assess_skin():
#     assert assess_skin('1') == no_dehydration_prompt
#     assert assess_skin('2') == severe_dehydration_prompt
#     assert assess_skin('3') == ""
#
# test_assess_skin()
# def test_assess_eyes():
#     assert assess_eyes('1') == some_dehydration_prompt
#     assert assess_eyes('2') == severe_dehydration_prompt
#     assert assess_eyes('3') == ""
#
# def test_assess_appearance():
#     assert assess_appearance() == no_dehydration_prompt
#     assert assess_appearance() == severe_dehydration_prompt
#     assert assess_appearance() == some_dehydration_prompt
