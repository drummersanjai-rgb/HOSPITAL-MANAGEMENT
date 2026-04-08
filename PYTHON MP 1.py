# File name
FILE_NAME = "patients.txt"

# Load existing patients from file
patients = {}

try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            pid, name = line.strip().split(",")
            patients[pid] = name
except FileNotFoundError:
    pass  # File doesn't exist yet

# Function to save patients to file
def save_to_file():
    with open(FILE_NAME, "w") as file:
        for pid in patients:
            file.write(pid + "," + patients[pid] + "\n")


while True:
    print("\n1. Add Patient")
    print("2. Show Patients")
    print("3. Appointment")
    print("4. Billing")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pid = input("Enter ID: ")
        name = input("Enter Name: ")
        patients[pid] = name
        save_to_file()   # Save immediately
        print("Patient added and saved!")

    elif choice == "2":
        if not patients:
            print("No patients found")
        else:
            for pid in patients:
                print(pid, "-", patients[pid])

    elif choice == "3":
        pid = input("Enter Patient ID: ")
        if pid in patients:
            doctor = input("Enter Doctor Name: ")
            print("Appointment fixed with", doctor)
        else:
            print("Patient not found")

    elif choice == "4":
        pid = input("Enter Patient ID: ")
        if pid in patients:
            fee = int(input("Enter consultation fee: "))
            med = int(input("Enter medicine cost: "))
            total = fee + med

            print("\n------ HOSPITAL BILL ------")
            print("Patient ID   :", pid)
            print("Patient Name :", patients[pid])
            print("----------------------------")
            print("Consultation :", fee)
            print("Medicine     :", med)
            print("----------------------------")
            print("Total Amount :", total)
            print("----------------------------")
        else:
            print("Patient not found")

    elif choice == "5":
        print("Data saved. Exiting...")
        break

    else:
        print("Invalid choice")
