import csv
import os
import pandas as pd

#############################################################################################
header = ['name', 'phone_no', 'email']
#############################################################################################


#############################################################################################
def searchbyname(file_name):
    name = input("Enter the name of contact for info: ")
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                if row[0].strip().lower() == name.strip().lower():
                    print(f"Contact found:\n Name :{row[0]}\t PhoneNo :{row[1]} Email: {row[2]}")
                    
                    break
                else:
                    continue
    except Exception as e:
        print(f"No file found of the name {file_name}",e)
#############################################################################################



#############################################################################################
def Choice_file():
    while True:
        c = int(input("Enter choice 1.CreateFile 2.DeleteFile (or any other key to exit): "))
        if c == 1:
            try:
                file_name = input("Enter file name: ")
                with open(file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                print(f"File '{file_name}' created successfully.")
            except Exception as e:
                print("Trouble creating file:", e)
        elif c == 2:
            try:
                filename = input("Enter file you want to delete: ")
                if os.path.exists(filename):
                    os.remove(filename)
                    print(f"File '{filename}' deleted successfully.")
                else:
                    print(f"No such file: '{filename}'")
            except Exception as e:
                print("Error while deleting file:", e)
        else:
            break
#############################################################################################


#############################################################################################
def Choice_Contact():
    file_name = input("Enter file name: ")
    while True:
        c = int(input("Enter choice 1.CreateContact 2.DeleteContact 3.ReadContact 4.SearchContact (or any other key to exit): "))
        if c == 1:
            try:
                with open(file_name, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    if file.tell() == 0:
                        writer.writerow(header)
                    name = input("Enter name: ")
                    phone_no = input("Enter phone number: ")
                    email = input("Enter email: ")
                    writer.writerow([name, phone_no, email])
                    print("Contact added successfully.")
            except FileNotFoundError:
                print(f"File '{file_name}' does not exist. Please create it first.")
            except Exception as e:
                print("Error while adding contact:", e)
        elif c == 2:
            try:
                rows = []
                name = input("Enter the name of the contact you want to delete: ")
                with open(file_name, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    rows = [row for row in reader]
                header, data = rows[0], rows[1:]
                updated_data = [row for row in data if row[0].strip().lower() != name.strip().lower()]
                if len(data) == len(updated_data):
                    print("Contact not found.")
                else:
                    with open(file_name, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(header)
                        writer.writerows(updated_data)
                    print("Contact deleted successfully.")
            except FileNotFoundError:
                print(f"File '{file_name}' does not exist.")
            except Exception as e:
                print("Error while deleting contact:", e)
        elif c == 3:
            try:
                df = pd.read_csv(file_name)
                print(df)
            except FileNotFoundError:
                print(f"File '{file_name}' does not exist.")
            except Exception as e:
                print("Error while reading the file:", e)
        elif c == 4:
            searchbyname(file_name)
        else:
            break
#############################################################################################


#############################################################################################
def program():
    while True:
        i = int(input("Enter choice 1.Choice_File 2.Contact_File (or any other key to exit): "))
        if i == 1:
            Choice_file()
        elif i == 2:
            Choice_Contact()
        else:
            print("Exiting program.")
            break

if __name__ == "__main__":
    program()
#############################################################################################