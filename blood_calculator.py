def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options: ")
        print("1-HDL")
        print("2-LDL")
        print("3-Total Cholesterol")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_Driver()
        elif choice == "2":
            LDL_Driver()
        elif choice == "3"
            totCholesterol_Diver()
        return

def accept_input(test_name):
    entry = input("Enter the {} result: ".format(test_name))
    return int(entry)

def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60 > HDL_value >= 40:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer

def HDL_Driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classification)

def check_LDL(LDL_value):
    if LDL_value >= 190:
        answer = "Very High"
    elif 189 > LDL_value >= 160:
        answer = "High"
    elif 160 > LDL_value >= 130:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer

def LDL_Driver():
    LDL_value = accept_input("LDL")
    classification = check_LDL(LDL_value)
    print_result("LDL", LDL_value, classification)

interface()

