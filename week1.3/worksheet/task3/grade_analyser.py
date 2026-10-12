import csv

# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

path = input("Please enter the filename of the student file: ")

# open the file

out = []

with open(path) as file:
    data = csv.reader(file)
    data.__next__()
    for row in data:
        id = row.pop(0)
        row = [int(s) for s in row if (s != '')]
        avg = sum(row) / len(row)
        
        if (avg < 40):
            grade = "F"
        elif (avg < 50):
            grade = "3"
        elif (avg < 60):
            grade = "2:2"
        elif (avg < 70):
            grade = "2:1"
        else:
            grade = "1"

        out.append([id,f"{avg:.2f}",grade])

with open(path.replace(".csv","") + "_out.csv", "x") as output:
    csv.writer(output).writerows(out)
        

    
# read in the data, and for each student calculate their average grade and classification




# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder