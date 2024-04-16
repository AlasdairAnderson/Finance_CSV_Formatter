import sys
import csv
from datetime import datetime, date

SUPPORTEDBANKS = ["Monzo", "Barcleys", "AMEX"]
REFERANCEFOLDER = "/home/alasdair/Documents/Denaro/Statements/ReferanceStatement/"
EXPORTFILE = "/home/alasdair/Documents/Denaro/Statements/ConvertedStatement/Denaro.csv"

def main():
    # Get cmdline arguments
    if len(sys.argv) < 3:
        print("[Usage]: python statmentconversion.py statmentCSV relevantBank")
        sys.exit(1)

    # Load csv values from referance statement
    statement = []
    with open(REFERANCEFOLDER+sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter= ",")
        for row in reader:
            statement.append(row)
    bank = str.lower(sys.argv[2])

    # Load csv values from converted statment
    convertedStatementId = 0
    with open(EXPORTFILE, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            if row['id'] == "id":
                return
            elif int(row['id']) > convertedStatementId:
                convertedStatementId = int(row['id'])


    # Format Statements
    if bank == "monzo":
        banoStatement = convertMonzo(statement, convertedStatementId)
    elif bank == "barcleys":
        banoStatement = convertBarcleys(statement, convertedStatementId)
    elif bank == "amex":
        banoStatement = convertAmex(statement, convertedStatementId)
    else:
        print("Supported Banks [{}]".format(SUPPORTEDBANKS))
        sys.exit(1)

    #print(list(banoStatement[0].keys()))

    # Write formated statement to csv file
    
    #Rewrite to append to file
    with open(EXPORTFILE, 'a', newline='') as csvfile:
        fieldnames = list(banoStatement[0].keys())
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        for row in banoStatement:
            writer.writerow(row)

    
    

def convertMonzo(statement, convertedStatementId):
    # Iterate through statement
    banoStatement = []
    id = convertedStatementId
    for row in statement:
        if row['Date'] != None:
            # Convert statement values to make them banoStatment compatable
            id = id + 1
            date = datetime.strptime(row['Date'], '%d/%m/%Y').strftime('%m/%d/%Y')
            description = str(row['Name'])
            type = 0
            rgb = "rgb(53,132,228)"
            repeatInterval = 0
            repeatForm = -1
            repeatEndDate = ""
            amount = str(row['Amount'])
            useColorGoup = 1
            group = 1
            groupName = "Monzo"
            groupDescription = "Tranzactions with Monzo"
            groupRGB = "rgb(255, 79, 64)"
            tags = row['Category']
            if "-" in row['Amount']:
                type = 1
                rgb = "rgb(246,97,81)"
                amount = amount.replace('-', "")


            values = {'id':id, 'date':date, 'description':description, 'type':type,'repeatInsterval':repeatInterval,'repeatForm':repeatForm, 'repeatEndDate':repeatEndDate, 'amount':amount, 'rgb':rgb, 'useColorGroup':useColorGoup, 'group':group, 'groupName':groupName, 'groupDescription':groupDescription, 'groupRGB':groupRGB, 'tags':tags}
            # Append statement to banoStatment
            banoStatement.append(values)

    return banoStatement

def convertBarcleys(statement, convertedStatementId):

    banoStatement = []

    id = convertedStatementId
    for row in statement:
        if row['Date'] != None:
            # Convert statement values to make them banoStatment compatable
            id = id + 1
            date = datetime.strptime(row['Date'], '%d/%m/%Y').strftime('%m/%d/%Y')
            description = str(row['Memo'])
            type = 0
            rgb = "rgb(53,132,228)"
            repeatInterval = 0
            repeatForm = -1
            repeatEndDate = ""
            amount = str(row['Amount'])
            useColorGoup = 1
            group = 2
            groupName = "Barcleys"
            groupDescription = "Tranzactions with Barcleys"
            groupRGB = "rgb(0, 174, 239)"
            tags = row['Subcategory']
            if "-" in row['Amount']:
                type = 1
                rgb = "rgb(246,97,81)"
                amount = amount.replace('-', "")


            values = {'id':id, 'date':date, 'description':description, 'type':type,'repeatInsterval':repeatInterval,'repeatForm':repeatForm, 'repeatEndDate':repeatEndDate, 'amount':amount, 'rgb':rgb, 'useColorGroup':useColorGoup, 'group':group, 'groupName':groupName, 'groupDescription':groupDescription, 'groupRGB':groupRGB, 'tags':tags}

            # Append statement to banoStatment
            banoStatement.append(values)

    return banoStatement

def convertAmex(statement, convertedStatementId):
     
    banoStatement = []
    id = convertedStatementId

    for row in statement:
        if row['Date'] != None:
            # Convert statement values to make them banoStatment compatable
            id = id + 1
            date = datetime.strptime(row['Date'], '%d/%m/%Y').strftime('%m/%d/%Y')
            description = str(row['Description'])
            type = 0
            rgb = "rgb(53,132,228)"
            repeatInterval = 0
            repeatForm = -1
            repeatEndDate = ""
            amount = str(row['Amount'])
            useColorGoup = 1
            group = 3
            groupName = "Amex"
            groupDescription = "Tranzactions with Barcleys"
            groupRGB = "rgb(29, 142, 206)"
            tags = ""
            if "-" in row['Amount']:
                type = 1
                rgb = "rgb(246,97,81)"
                amount = amount.replace('-', "")


            values = {'id':id, 'date':date, 'description':description, 'type':type,'repeatInsterval':repeatInterval,'repeatForm':repeatForm, 'repeatEndDate':repeatEndDate, 'amount':amount, 'rgb':rgb, 'useColorGroup':useColorGoup, 'group':group, 'groupName':groupName, 'groupDescription':groupDescription, 'groupRGB':groupRGB, 'tags':tags}

            # Append statement to banoStatment
            banoStatement.append(values)

    return banoStatement

main()