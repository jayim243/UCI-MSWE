import re
import mysql.connector
import sys

# connecting to database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="", #enter your password
    database="studentDB" #comment out until you've created database in line 15
    )
mycursor = cnx.cursor()

# creating new database named studentDB (only need to run this once)
# mycursor.execute("CREATE DATABASE studentDB") 

# creating dictionary to store all the tables as strings to later use to create the actual table
TABLES = {}
TABLES["student"] = (
    "CREATE TABLE `student` ("
    "`student_id` int NOT NULL AUTO_INCREMENT,"
    "`student_first_name` VARCHAR(50) NOT NULL,"
    "`student_last_name` VARCHAR(50) NOT NULL,"
    "PRIMARY KEY (`student_id`)"
    ") ENGINE=InnoDB"
)

TABLES["course"] = (
    "CREATE TABLE `course` ("
    "`course_id` int NOT NULL AUTO_INCREMENT,"
    "`course_name` VARCHAR(50) NOT NULL,"
    "`day` VARCHAR(9) NOT NULL,"
    "`start_time` time NOT NULL,"
    "PRIMARY KEY (`course_id`)"
    ") ENGINE=InnoDB"
)

TABLES["schedule"] = (
    "CREATE TABLE `schedule` ("
    "`schedule_id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "`student_id` int NOT NULL,"
    "`course_id` int NOT NULL,"
    "FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),"
    "FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`)"
    ") ENGINE=InnoDB"
)


# delete db if needed
# mycursor.execute("DROP DATABASE studentDB")
# cnx.commit()

# # dropping tables if needed
# mycursor.execute("DROP TABLE student, course, schedule")

# # creating tables in database if needed
# for table_name in TABLES:
#     table_description = TABLES[table_name]
#     mycursor.execute(table_description)


# checking to see the if tables were created
# mycursor.execute("DESCRIBE schedule")
# for x in mycursor:
#     print(x)



# allow new students to enroll into the program
def enroll_student(first_name, last_name):
    mycursor.execute("INSERT INTO student (student_first_name, student_last_name) VALUES (%s,%s)", (first_name, last_name))
    cnx.commit()
    print(f"\n{first_name} {last_name} successfully enrolled\n")


# new courses to be introduced
def add_course(course_name, day, start_time):
    mycursor.execute("INSERT INTO course (course_name, day, start_time) VALUES (%s,%s,%s)", (course_name, day, start_time))
    cnx.commit()
    print(f"\n{course_name} on {day} starting at {start_time} successfully added\n")


# students to enroll in courses
# uses course_id because there could be multiple classes of the same subject or name
def enroll_student_course(student_id, course_id):
    mycursor.execute("INSERT INTO schedule (student_id, course_id) VALUES (%s,%s)", (student_id, course_id))
    cnx.commit()
    course = student = "" #empty strings to hold tuple values for print statement
    #selectors to get course and student names to add to empty strings created in previous line
    mycursor.execute(f"SELECT course_name FROM course WHERE course_id = {course_id}")
    for x in mycursor:
        course = x
    mycursor.execute(f"SELECT CONCAT(student_first_name, ' ', student_last_name) FROM student WHERE student_id = {student_id}")
    for x in mycursor:
        student = x
    # print statement to indicate correct enrollment of courses and students
    print(f"\n{course[0]} with course ID {course_id} successfully enrolled to student {student[0]} with student ID {student_id}\n")


# querying to see which students are in each course
def query_course(course_id):
    mycursor.execute(f"SELECT student.student_id, CONCAT(student_first_name, ' ', student_last_name), course.course_id, course.course_name FROM student JOIN schedule ON student.student_id = schedule.student_id JOIN course ON schedule.course_id = course.course_id WHERE {course_id} = course.course_id")
    print(f"\nStudents in course {course_id}:")
    for x in mycursor:
        print(f'course_id: {x[2]}, course_name: {x[3]}, student_id: {x[0]}, student_full_name: {x[1]}')
    print("\n")


# querying to see which courses each student is in
def query_student(student_id):
    mycursor.execute(f"SELECT student.student_id, CONCAT(student_first_name, ' ', student_last_name), course.course_id, course.course_name FROM student JOIN schedule ON student.student_id = schedule.student_id JOIN course ON schedule.course_id = course.course_id WHERE {student_id} = student.student_id")
    print(f"\nStudent {student_id} taking these courses:")
    for x in mycursor:
        print(f'student_id: {x[0]}, student_full_name: {x[1]}, course_id: {x[2]}, course_name: {x[3]}')
    print("\n")


# querying to see which courses and what times each course is for a given student on a given day of the week.
def query_schedule(student_id, weekday):
    mycursor.execute(f"SELECT student.student_id, CONCAT(student_first_name, ' ', student_last_name), course.course_id, course.course_name, course.start_time FROM student JOIN schedule ON student.student_id = schedule.student_id JOIN course ON schedule.course_id = course.course_id WHERE {student_id} = student.student_id AND course.day = '{weekday}'")
    for x in mycursor:
        print(f'For student, {x[1]} with student ID {x[0]}:')
        print(f'  course: \'{x[3]}\' with course ID {x[2]} starts at {x[4]}')
    print("\n")



# additional functions to help see all students or all courses
def all_students(): #prints all students
    mycursor.execute("SELECT * FROM student")
    for x in mycursor:
        print(f'student_id {x[0]}, first_name: {x[1]}, last_name: {x[2]}')
    print("\n")

def student_ids(): #returns a list of student ids
    mycursor.execute("SELECT student_id FROM student")
    ids = []
    for x in mycursor:
        ids.append(x[0])
    return ids

def all_courses(): #prints all courses
    mycursor.execute("SELECT * FROM course")
    for x in mycursor:
        print(f'course_id: {x[0]}, course_name: {x[1]}, day: {x[2]}, start_time: {x[3]}')
    print("\n")

def course_ids(): #returns a list of course ids
    mycursor.execute("SELECT course_id FROM course")
    ids = []
    for x in mycursor:
        ids.append(x[0])
    return ids

def all_schedules(): #prints all schedules
    mycursor.execute("SELECT * FROM schedule")
    for x in mycursor:
        print(f'schedule_id: {x[0]}, course_id: {x[1]}, student_id: {x[2]}')
    print("\n")


def validateStudentID(student_id): #helper function to validate an existing student ID and keeps prompting until one is received
    while not student_id.isnumeric() or int(student_id) not in student_ids():
        if not student_id.isnumeric():
            student_id = input("Please provide a valid course ID (numeric input only)\n")
        else:
            student_id = input("Course ID does not exist. Please enter a valid course ID\n")

    return int(student_id)  # Convert to int before returning


def validateCourseID(course_id): #helper function to validate an existing course ID and keeps prompting until one is received
    while not course_id.isnumeric() or int(course_id) not in course_ids():
        if not course_id.isnumeric():
            course_id = input("Please provide a valid course ID (numeric input only)\n")
        else:
            course_id = input("Course ID does not exist. Please enter a valid course ID\n")

    return int(course_id)  # Convert to int before returning


#reset tables to empty tables
def resetTables():
    mycursor.execute("DROP TABLE student, course, schedule") #clear tables
    for table_name in TABLES: #recreate tables
        table_description = TABLES[table_name]
        mycursor.execute(table_description)


# source: ChatGPT
# validating time input 
def is_valid_time(time_str):
    time_pattern = r'^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'

    # Use re.match to check if the time_str matches the pattern
    if re.match(time_pattern, time_str):
        return True
    else:
        return False



if __name__ == "__main__":
    print("Command Line Interface\n")
    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'] #to validate weekdays input
    while True: #keep running CLI
        print("Type the corresponding number to continue\n")
        print("1: enroll student\n2: add course\n3: enroll_student_course\n4: query courses\n5: query student\n6: query schedule\n7: all students\n8: all courses\n9: all schedules\n0: reset tables\n")
        print("Enter \"q\" to quit program\n")

        user = input() #user input to call proper function for database manipulation
        while not user.isnumeric():
            if user == "q":
                sys.exit()
            user = input("Must be an integer\n")
            if user.isnumeric(): #if input isn't an int, continue prompting user
                while int(user) < 1 or int(user) > 6: #if input isnt within options, keep prompting user
                    user = input("Must be between 1 and 6\n")
                    if not user.isnumeric():
                        break
        user = int(user)

        
        if user == 1: #allow new students to enroll into the program
            first_name = input("Please provide the student's first name: \n")
            while not first_name.isalpha():
                first_name = input("First name must be a string\n")
            last_name = input("Please provide ths student's last name: \n")
            while not last_name.isalpha():
                last_name = input("Last name must be a string\n")
            confirm = input(f"Enroll {first_name} {last_name}? enter: y / n\n") #confirm enrollment
            if confirm == "y": #if "y" enroll, else continue loop
                enroll_student(first_name, last_name)
            continue


        elif user == 2: #new courses to be introduced
            course_name = input("Please provide the course name: \n")
            course_day = input("Please provide the day of the week for the course: \n")
            while course_day.lower() not in weekdays: #checks input for day, must be a valid weekday. if not valid, keep prompting user
                course_day = input(f"Please provide a valid day in {weekdays}: \n")
            course_start_time = input("Please provide a start time for the course (format example: 17:00:00 -> 5PM): \n")
            time_format_pattern = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$') #regex to validate time input
            while not time_format_pattern.match(course_start_time):
                course_start_time = input("Please provide a valid start time (format example: 17:00:00 -> 5PM): \n")
            confirm = input(f"Add {course_name} on {course_day} at {course_start_time}? enter: y / n\n") #confirm add course
            if confirm == "y": #if "y" add, else continue loop
                add_course(course_name, course_day, course_start_time)
            continue
            
        
        elif user == 3: #students to enroll in courses
            student_id = input("Please provide student ID\n")
            student_id = validateStudentID(student_id)

            course_id = input("Please provide course ID\n")
            course_id = validateCourseID(course_id)
            confirm = input(f"Enroll student ID: {student_id} to course ID {course_id}? enter: y / n\n") #confirm add course
            if confirm == "y": #if "y" add, else continue loop
                enroll_student_course(student_id, course_id)
            continue


        elif user == 4: #querying to see which students are in each course
            course_id = input("Please enter course ID\n")
            course_id = validateCourseID(course_id)
            query_course(course_id)

        
        elif user == 5: #querying to see which courses each student is in
            student_id = input("Please enter student ID\n")
            student_id = validateStudentID(student_id)
            query_student(student_id)

        
        elif user == 6: #querying to see which courses and what times each course is for a given student on a given day of the week
            student_id = input("Please enter student ID\n")
            student_id = validateStudentID(student_id)
            course_day = input("Please provide the day of the week for the course: \n")
            while course_day.lower() not in weekdays: #checks input for day, must be a valid weekday. if not valid, keep prompting user
                course_day = input(f"Please provide a valid day in {weekdays}: \n")
            query_schedule(student_id, course_day)


        #additional useful functions
        elif user == 7: #see all students
            all_students()


        elif user == 8: #see all courses
            all_courses()


        elif user == 9: #see schedules
            all_schedules()
        
        elif user == 0:
            resetTables()
        
        else: #if user enters int thats not between 0-9
            print("\nPLEASE SELECT ONE OF THE VALID COMMAND OPTIONS\n")