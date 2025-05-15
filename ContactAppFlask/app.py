import csv
import os
import pandas as pd
from flask import Flask,request,render_template

fileName='contacts.csv'

app=Flask(__name__)

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


@app.route('/update', methods=['GET', 'POST'])
def updateContact():
    fileName = 'contacts.csv'   

    if request.method == 'POST':
        
        with open(fileName, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            rows = list(reader)

        contactName = request.form['Search']
        for row in rows:
            if row[0].strip().lower() == contactName.strip().lower():
           
                newName = request.form.get('name')
                newPhone = request.form.get('number')
                newEmail = request.form.get('email')

                if newName:
                    row[0] = newName
            
                if newPhone:
                    row[1] = newPhone

                if newEmail:
                    row[2] = newEmail
                break  

        with open(fileName, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)

    return render_template("update.html")


#############################################################################################

@app.route('/add',methods=['GET','POST'])
def addContact():
   
   
    if request.method=='POST':

        with open(fileName, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    if file.tell() == 0:
                        writer.writerow(header)
                    name = request.form['name']
                    phone_no = request.form['phone']
                    email = request.form['email']
                    writer.writerow([name, phone_no, email])
  
    return render_template("addcontact.html")
                    
                
    
       

#############################################################################################
@app.route('/delete', methods=['GET', 'POST'])
def deleteContact():
    fileName = 'contacts.csv'  
    message = ''
    
    if request.method == 'POST':
        name = request.form['name']
        rows = []

        with open(fileName, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]


        header, data = rows[0], rows[1:]

        updated_data = [row for row in data if row[0].strip().lower() != name.strip().lower()]

        if len(data) == len(updated_data):
            message = "Contact not found."
        else:
            
            with open(fileName, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(updated_data)
            message = "Contact deleted successfully."

    return render_template("delete.html", message=message)
        
    
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
@app.route('/')
def program():
     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
#############################################################################################
