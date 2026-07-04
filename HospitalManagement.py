print("========== HOSPITAL MANAGEMENT ==========")
patients = {}
while True:
    print("1. Add Patient, 2. Display All Patients, 3. Search Patient, 4. Update Patient Details, 5. Discharge Patient, 6. Delete Patient Record, 7. Total Patients, 8. Show Admitted Patients, 9. Exit")
    choice = int(input("enter your choice: "))
    if choice==1:
        patient_id = input("enter patient id: ")
        if patient_id in patients:
            print("patient id already exists")
        else:
            name = input("enter patient name: ")
            age = int(input("enter patient age: "))
            disease = input("enter disease: ")
            doctor = input("enter doctor name: ")
            patients[patient_id] = {"name":name, "age":age, "disease": disease, "doctor": doctor, "admitted": True}
            print("patient data is updated successfully")
    elif choice==2:
        if len(patients)==0:
            print("there is no patient data available")
        else:
                patient_id = input("enter patient id: ")
                if patient_id in patients:
                    for patient_id in patients:
                        print(patients[patient_id])
                else:
                    print("enter correct id")
    elif choice==3:
        patient_id = input("enter patient id: ")
        if patient_id in patients:
            print(patients[patient_id])
        else:
            print("patient id does not exist")
    elif choice==4:
        patient_id = input("enter patient id: ")
        if patient_id in patients:
            print("what do you want to update 1.name 2.age 3.disease 4.doctor")
            choice1 = int(input("select one option: "))
            if choice1==1:
                patients[patient_id]["name"] = input("enter new name: ")
            elif choice1==2:
                patients[patient_id]["age"] = input("enter new age: ")
            elif choice1==3:
                patients[patient_id]["disease"] = input("enter new disease name: ")
            elif choice1==4:
                patients[patient_id]["doctor"] = input("enter new docctor name: ")
        else:
            print("invalid selection")
    elif choice==5:
        #discharge patient
        patient_id = input("enter patient id: ")
        if patient_id in patients:
            patients[patient_id]["admitted"] = False
            print("patient is disadmitted")
        else:
            print("patient id not found")
    elif choice==6:
        #delete patient record
        patient_id = input("enter patient_id: ")
        if patient_id in patients:
            patients.pop(patient_id)
        else:
            print("invalid patient_id")
    elif choice==7:
        #Total Patients
        print("total no.of patients are: ",len(patients))
    elif choice==8:
        #show Admitted Patients
        count = 0
        for patient_id in patients:
            if patients[patient_id]["admitted"] == True :
                print("Patient ID :", patient_id)
                print("Name :", patients[patient_id]["name"])
                count = count+1
                print(count)
            else:
                print("there are no admitted patients")
    elif choice==9:
        print("you have Exited")
        break