# Finance_CSV_Formatter
A personal finance CSV formatter using python, to convert bank statement CSV files to a CSV format that can be interprated and uploaded to the Denaro finance tracking software.

This project currently supports the CSV formats for Monzon, Barcleys, and Amex.

## Project Use
### Folder Setup
A folder system must be set up to ensure that the program and referance and export the projects CVS's
1. Set up **referance folder** to insert all bank statemnet CSV's into, insert folder route into the `REFERANCEFOLDER` variable.
2. Set up **export folder** to export Denaro formatted CSV, insert folder route into the `EXPORTFILE` variable.
3. Insert the CSV requireing formatting into the **referance folder**.


### Run Program
To run the program open up the computers terminal and execute:
```
<code>python statmentconversion.py statmentCSV relevantBank</code>
```
With the `statementCSV` being the CSV that you would like to format and the `relevantBank` being the bank that provided the CSV.
The program will then take the specified CSV located in the **referance folder** and convert it into a format compatibale with Denaro.
The converted CSV will be written to the **export folder** where it can be exported to Denaro.

