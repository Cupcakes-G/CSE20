'''
12.11 LAB: Course Grade
Write a program that reads the student information from a tab separated values (tsv) file. The program then creates a text file that records the course grades of the students. Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, and the Final score of a student. A sample of the student information is provided in StudentInfo.tsv. Assume the number of students is at least 1 and at most 20.

The program performs the following tasks:

Read the file name of the tsv file from the user.
Open the tsv file and read the student information.
Compute the average exam score of each student.
Assign a letter grade to each student based on the average exam score in the following scale:
A: 90 =< x
B: 80 =< x < 90
C: 70 =< x < 80
D: 60 =< x < 70
F: x < 60
Compute the average of each exam.
Output the last names, first names, exam scores, and letter grades of the students into a text file named report.txt. Output one student per row and separate the values with a tab character.
Output the average of each exam, with two digits after the decimal point, at the end of report.txt. Hint: Use the format specification to set the precision of the output.
'''

# TODO: Declare any necessary variables here.
grades_dict = {}
student_name = ""

# TODO: Read a file name from the user and read the tsv file here.
file_name = input()  # this will be StudentInfo.tsv
with open(file_name) as fh:
    for each_line in fh:
        line = each_line.split('\t')  # line is a list of each value in one line
        student_name = str(line[0]) + "\t" + str(line[1])  # combines student first name and last name
        line[4] = line[4][:-1]  # takes out the \n at the end of line[4]
        student_scores = [line[2], line[3], line[4]]
        grades_dict[student_name] = student_scores

# TODO: Compute student grades and exam averages, then output results to a text file here.
avg_midterm1 = 0
avg_midterm2 = 0
avg_final = 0
for key in grades_dict:
    avg_midterm1 += int(grades_dict[key][0])
    avg_midterm2 += int(grades_dict[key][1])
    avg_final += int(grades_dict[key][2])
    average_score = 0
    for score in grades_dict[key]:
        average_score += int(score)
    average_score = average_score / 3

    if average_score >= 90:
        average_score = "A"
    elif average_score >= 80:
        average_score = "B"
    elif average_score >= 70:
        average_score = "C"
    elif average_score >= 60:
        average_score = "D"
    else:
        average_score = "F"
    grades_dict[key].append(average_score)

avg_midterm1 = avg_midterm1 / len(grades_dict)
avg_midterm2 = avg_midterm2 / len(grades_dict)
avg_final = avg_final / len(grades_dict)
print(avg_midterm1)
print(avg_midterm2)
print(avg_final)

with open('report.txt', 'w') as fh:
    for key in grades_dict:
        fh.write(key)
        for x in grades_dict[key]:
            fh.write("\t" + str(x))
        fh.write("\n")
    fh.write("\n")
    fh.write(f'Averages: midterm1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}\n')