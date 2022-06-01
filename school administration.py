import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age" , "Phone" , "Email-id"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        print("")
        print("DISCLAIMER: ","MAKE SURE TO USE 'SPACE' WHILE ENTERING THE INFO")
        print("")
        student_info= input("Enter student information for student #{} in the following format(Name Age Phone Email-ID):".format(student_num))
        print("")
        student_info_list = student_info.split(" ")
        print("\nThe entered information is \nName: {}\nAge: {}\nPhone: {}\nEmail-id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        print("")
        choice_check =input("is the entered info correct? (yes/no):")

        if choice_check== "yes":
            write_into_csv(student_info_list)
    
            condition_check = input("Enter (yes/no) if you want to enter information for another student:")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False

        elif choice_check == "no":print("\nPlease re-enter the values")
