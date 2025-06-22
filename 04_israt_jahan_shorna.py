import matplotlib.pyplot as plt

def compute_total_marks(data):
    for student in data:
        student['Total Marks'] = student['CT(20)'] + student['Final(72)'] + student['Att(8)']

def compute_grade_point(marks):
    if marks >= 80:
        return 4.0
    elif marks >= 70:
        return 3.5
    elif marks >= 60:
        return 3.0
    elif marks >= 50:
        return 2.5
    elif marks >= 40:
        return 2.0
    else:
        return 0.0

def add_grade_points(data):
    for student in data:
        student['Grade Point'] = compute_grade_point(student['Total Marks'])

def save_to_csv(data, filename='GP.csv'):
    with open(filename, 'w') as file:
        file.write("Roll no,Name,Total Marks,Grade Point\n")
        for student in data:
            file.write(f"{student['Roll no']},{student['Name']},{student['Total Marks']},{student['Grade Point']}\n")

def print_student_data(data):
    print("Roll no | Name           |Total Marks      |Grade Point")
    print("--------------------------------------------------")
    for student in data:
        print(f"{student['Roll no']:7} | {student['Name']:13} | {student['Total Marks']:11} | {student['Grade Point']:.1f}")

def plot_total_marks_distribution(data):
    roll_nos = [student['Roll no'] for student in data]
    total_marks = [student['Total Marks'] for student in data]
    plt.scatter(roll_nos, total_marks, color='blue', alpha=0.5)
    plt.xlabel('Student Roll No')
    plt.ylabel('Total Marks')
    plt.title('Total Marks Distribution')
    plt.xticks(rotation=90)
    plt.grid()
    plt.show()

data = [
    {'Roll no': 200501, 'Name': 'Mariaa', 'CT(20)': 15, 'Final(72)': 60, 'Att(8)': 6},
    {'Roll no': 200502, 'Name': 'Taniya', 'CT(20)': 8, 'Final(72)': 62, 'Att(8)': 0},
    {'Roll no': 200504, 'Name': 'Juli', 'CT(20)': 17, 'Final(72)': 55, 'Att(8)': 8},
    {'Roll no': 200505, 'Name': 'Arif', 'CT(20)': 13, 'Final(72)': 54, 'Att(8)': 1},
    {'Roll no': 200506, 'Name': 'Mahfuza', 'CT(20)': 19, 'Final(72)': 42, 'Att(8)': 8},
    {'Roll no': 200508, 'Name': 'meriyem', 'CT(20)': 10, 'Final(72)': 41, 'Att(8)': 0},
    {'Roll no': 200510, 'Name': 'Akash', 'CT(20)': 18, 'Final(72)': 42, 'Att(8)': 7},
    {'Roll no': 200511, 'Name': 'Raiyan', 'CT(20)': 13, 'Final(72)': 65, 'Att(8)': 2},
    {'Roll no': 200512, 'Name': 'Araaf', 'CT(20)': 13, 'Final(72)': 18, 'Att(8)': 3},
    {'Roll no': 200513, 'Name': 'Sreya', 'CT(20)': 12, 'Final(72)': 57, 'Att(8)': 3},
    {'Roll no': 200514, 'Name': 'Ikram', 'CT(20)': 18, 'Final(72)': 46, 'Att(8)': 8},
    {'Roll no': 200515, 'Name': 'Hasib', 'CT(20)': 17, 'Final(72)': 48, 'Att(8)': 6},
    {'Roll no': 200516, 'Name': 'Sojol', 'CT(20)': 13, 'Final(72)': 40, 'Att(8)': 3},
    {'Roll no': 200517, 'Name': 'Jafrin', 'CT(20)': 17, 'Final(72)': 54, 'Att(8)': 6},
    {'Roll no': 200518, 'Name': 'Tafsiya', 'CT(20)': 17, 'Final(72)': 30, 'Att(8)': 8},
    {'Roll no': 200520, 'Name': 'Abdur-Rahman', 'CT(20)': 16, 'Final(72)': 48, 'Att(8)': 7},
    {'Roll no': 200521, 'Name': 'Nahiyan', 'CT(20)': 14, 'Final(72)': 30, 'Att(8)': 5},
    {'Roll no': 200522, 'Name': 'Orhan', 'CT(20)': 18, 'Final(72)': 37, 'Att(8)': 8},
    {'Roll no': 200523, 'Name': 'Rubi', 'CT(20)': 15, 'Final(72)': 56, 'Att(8)': 4},
    {'Roll no': 200524, 'Name': 'Fariya', 'CT(20)': 19, 'Final(72)': 43, 'Att(8)': 8},
    {'Roll no': 200525, 'Name': 'Sheli', 'CT(20)': 12, 'Final(72)': 33, 'Att(8)': 0},
    {'Roll no': 192215, 'Name': 'Abdullah', 'CT(20)': 18, 'Final(72)': 59, 'Att(8)': 8}
]

compute_total_marks(data)
add_grade_points(data)
save_to_csv(data)
print_student_data(data)
plot_total_marks_distribution(data)
