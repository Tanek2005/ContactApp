import csv
import os
import pandas as pd

fileName='fileName.csv'

#############################################################################################
header = ['name', 'phone_no', 'email']
#############################################################################################
    


#############################################################################################
def searchbyName(fileName):
    
    try:
        with open(fileName, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                if row[0].strip().lower() == fileName.strip().lower():
                    print(f"Contact found:\n Name :{row[0]}\t PhoneNo :{row[1]} Email: {row[2]}")
                    
                    break
                else:
                    continue
    except Exception as e:
        print(f"No file found of the name {fileName}",e)
#############################################################################################


def updateContact(contactName, fileName):
    try:
        
        with open(fileName, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            rows = list(reader)  

        
        for row in rows:
            if row[0].strip().lower() == contactName.strip().lower():
                newName = input("Enter new name: ")
                if newName!="":
                     row[0]=newName     
                newPhone = input("Enter new phone number: ")
                if newPhone!="":
                     row[1]=newPhone
                newEmail = input("Enter new email: ")
                if newEmail!="":
                     row[2]=newEmail
                
                break
        else:
            print(f"No contact found with the name '{contactName}'.")
            return

        
        with open(fileName, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)

        print(f"Contact '{contactName}' updated successfully.")
    
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#############################################################################################

def addContact():
 
    c = int(input("Enter choice 1.CreateContact 2. (or any other key to exit): "))
    if c == 1:
            try:
                with open(fileName, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    if file.tell() == 0:
                        writer.writerow(header)
                    name = input("Enter name: ")
                    phone_no = input("Enter phone number: ")
                    email = input("Enter email: ")
                    writer.writerow([name, phone_no, email])
                    print("Contact added successfully.")
            except FileNotFoundError:
                print(f"File '{fileName}' does not exist. Please create it first.")
            except Exception as e:
                print("Error while adding contact:", e)

#############################################################################################
def deleteContact(fileName):
    

    try:
                rows = []
                name = input("Enter the name of the contact you want to delete: ")
                with open(fileName, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    rows = [row for row in reader]
                header, data = rows[0], rows[1:]
                updated_data = [row for row in data if row[0].strip().lower() != name.strip().lower()]
                if len(data) == len(updated_data):
                    print("Contact not found.")
                else:
                    with open(fileName, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(header)
                        writer.writerows(updated_data)
                    print("Contact deleted successfully.")
    except FileNotFoundError:
                print(f"File '{fileName}' does not exist.")
    except Exception as e:
                print("Error while deleting contact:", e)
        
    
#############################################################################################
def readFile():
    try:
        df = pd.read_csv(fileName)
        print(df)
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist.")
    except Exception as e:
                print("Error while reading the file:", e)

#############################################################################################
def program():
    while True:
        i = eval(input("Enter choice 1.AddContact 2.DeleteContact 3.UpdateContact (or any other number to exit) : "))
      
        if i == 1:
            addContact()
        elif i==2:
             
             deleteContact(fileName)
        
        elif i==3:
 
             contactName=input("Enter contact name : ")
             updateContact(contactName,fileName)

        else:
            print("Exiting program.")
            break


if __name__ == "__main__":
    program()
#############################################################################################
