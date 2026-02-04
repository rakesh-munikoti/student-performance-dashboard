import mysql.connector
import math

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Munikotirakesh@04",
        database = "student_dashboard"
        )
conn = get_connection()
cursor = conn.cursor()


students = """ CREATE TABLE IF NOT EXISTS students(
          student_id INT PRIMARY KEY,
          name VARCHAR(50),
          class VARCHAR(50)
        ) """
cursor.execute(students)
conn.commit()
student_ins = "INSERT IGNORE INTO students VALUES (%s,%s,%s)"
students_values = (101,"Rahul Sharma","CSE-A"),(102,"Ananya Gupta","CSE-A"),(103,"Rohan Verma","CSE-B"),(104,"Priya Singh","CSE-A"),(105,"Aman Patel","ECE-A"),(106,"Neha Mehta","ECE-A"),(107,"Kunal Joshi","ECE-B"),(108,"Sneha Iyer","MECH-A"),(109,"Arjun Rao","MECH-A"),(110,"Pooja Nair","MECH-B")
cursor.executemany(student_ins, students_values)
conn.commit()


subject = """ CREATE TABLE IF NOT EXISTS subjects(
              subject_id INT PRIMARY KEY,
              subject_name VARCHAR(50)
          ) """
cursor.execute(subject)
conn.commit()
subject_ins = "INSERT IGNORE INTO subjects VALUES(%s,%s)"
subject_values = (1,"Mathematics"),(2,"Physics"),(3,"Chemistry"),(4,"Computer Science"),(5,"Electronics"),(6,"Mechanics")
cursor.executemany(subject_ins, subject_values)
conn.commit()


mark = """ CREATE TABLE IF NOT EXISTS marks(
           mark_id INT PRIMARY KEY,
           student_id INT,
           subject_id INT,
           marks INT,
           FOREIGN KEY(student_id) REFERENCES students(student_id),
           FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
        ) """
cursor.execute(mark)
conn.commit()
mark_ins = "INSERT IGNORE INTO marks VALUES(%s,%s,%s,%s)"
mark_values = (1, 101, 1, 85),(2, 101, 2, 78),(3, 101, 4, 90),(4, 102, 1, 88),(5, 102, 2, 82),(6, 102, 4, 92),(7, 103, 1, 70),(8, 103, 3, 75),(9, 103, 4, 80),(10, 104, 1, 65),(11, 104, 2, 72),(12, 104, 4, 68),(13, 105, 1, 80),(14, 105, 5, 85),(15, 105, 6, 78),(16, 106, 1, 75),(17, 106, 5, 82),(18, 106, 6, 80),(19, 107, 1, 68),(20, 107, 5, 70),(21, 107, 6, 65),(22, 108, 1, 78),(23, 108, 2, 75),(24, 108, 6, 82),(25, 109, 1, 72),(26, 109, 2, 70),(27, 109, 6, 74),(28, 110, 1, 85),(29, 110, 2, 88),(30, 110, 6, 90)
cursor.executemany(mark_ins, mark_values)
conn.commit()


attendance = """ CREATE TABLE IF NOT EXISTS attendance(
                attendance_id INT PRIMARY KEY,
                student_id INT,
                total_classes INT,
                attended_classes INT,
                FOREIGN KEY(student_id) REFERENCES students(student_id)
            )"""
cursor.execute(attendance)
attendance_ins = "INSERT IGNORE INTO attendance VALUES(%s,%s,%s,%s)"
attendance_values = (1, 101, 100, 92),(2, 102, 100, 95),(3, 103, 100, 85),(4, 104, 100, 70),(5, 105, 100, 88),(6, 106, 100, 90),(7, 107, 100, 65),(8, 108, 100, 80),(9, 109, 100, 75),(10,110, 100, 93)
cursor.executemany(attendance_ins, attendance_values)
conn.commit()

def show_menu():
    print("\n1. Add Student")
    print("2. Add Marks")
    print("3. Add Attendance")
    print("4. View Student Report")
    print("5. View Top Performers")
    print("6. Exit")

while True:
    show_menu()
    select = int(input("Enter your choice :"))
    if(select == 1):
        def addstudent():
            stu_id = int(input("\n Enter student id :"))
            stu_name = input("\n Enter student name :")
            stu_class = input("\n Enter student class :")
            stu_ins = "INSERT IGNORE INTO students VALUES (%s,%s,%s)"
            addstudent_values = (stu_id,stu_name,stu_class)
            cursor.execute(stu_ins, addstudent_values)
            conn.commit()
            print("STUDENR DETAILS ADDED")
            another_student_detail = input("Enter 'yes' to add another student detail/ 'No' to end")
            if(another_student_detail == "yes"):
                addstudent()
            else:
                print("Thank YOU")
        addstudent()
    elif(select == 2):
        def addmarks():
            m_marks_id = int(input("Enter marks ID :"))
            m_student_id = int(input("Enter student ID :"))
            m_subject_id = int(input("Enter subject ID :"))
            m_marks = int(input("Enter marks :"))
            mrks_ins = "INSERT IGNORE INTO marks VALUES(%s,%s,%s,%s)"
            addmarks_values = (m_marks_id,m_student_id,m_subject_id,m_marks)
            cursor.execute(mrks_ins, addmarks_values)
            conn.commit()
            print("MARKS DETAILS ADDED")
            another_mark_detail = input("Enter 'yes' to add another mark detail/ 'no' to end :")
            if(another_mark_detail == "yes"):
                addmarks()
            else:
                print("THANK YOU")
        addmarks()
    elif(select == 3):
        def addattendance():
            a_attendance_id = int(input("Enter attendance ID :"))
            a_student_id = int(input("Enter student_id :"))
            a_total_classes = int(input("Enter total classes :"))
            a_attended_class = int(input("Enter the attended classes :"))
            atnd_ins = "INSERT IGNORE INTO attendance VALUES(%s,%s,%s,%s)"
            atnd_values = (a_attendance_id,a_student_id,a_total_classes,a_attended_class)
            cursor.execute(atnd_ins,atnd_values)
            conn.commit()
            print("ATTENDANCE DETAILS ADDED")
            ano_attendance_details = input("Enter 'yes' to add another attendance detail/ 'no' to end :")
            if(ano_attendance_details == "yes"):
                addattendance()
            else:
                print("THANK YOU")
        addattendance()
    elif(select == 4):
        def studentdetails():
            sd_id = int(input("Enter student ID :"))
            s_name = "SELECT name,class FROM students WHERE student_id = %s"
            cursor.execute(s_name,(sd_id,))
            student_info = cursor.fetchone()

            if student_info is None:
                print("Student Not Found")
                return
            name,student_class = student_info
            print("Student name        :",name)
            print("Student class       :",student_class)

            s_marks = "SELECT subject_name,marks FROM marks INNER JOIN subjects ON marks.subject_id = subjects.subject_id WHERE student_id = %s;"
            cursor.execute(s_marks,(sd_id,))
            marks_row = cursor.fetchall()
            for subject,marks in marks_row:
                print(subject,": ", marks)

            s_avgmarkss = """SELECT AVG(marks) as "avg_marks" FROM subjects INNER JOIN marks ON subjects.subject_id = marks.subject_id GROUP BY student_id HAVING student_id = %s"""
            cursor.execute(s_avgmarkss,(sd_id,))
            averg_marks = cursor.fetchone()[0]
            print("Average marks :", round(averg_marks,2))


            s_attendance = """SELECT attended_classes,total_classes FROM attendance WHERE student_id = %s"""
            cursor.execute(s_attendance,(sd_id,))
            stu_att = cursor.fetchone()
            attended,total = stu_att
            attendance = (attended / total) * 100
            print("Attendance :", round(attendance,2), "%")


            ano_stu = input("Enter 'yes' for another student report, 'no' to end :")
            if(ano_stu == "yes"):
                studentdetails()
            else:
                print("THANK YOU")
        studentdetails()
    elif(select == 5):
        def topperformance():
            toppers = """SELECT name, AVG(marks) AS "avg_marks" FROM marks INNER JOIN students ON marks.student_id = students.student_id GROUP by name ORDER BY avg_marks DESC LIMIT 10;"""
            cursor.execute(toppers)
            stu_top = cursor.fetchall()
            for top_name,top_avg in stu_top:
                print(top_name," ",top_avg)
            print("THANK YOU")
        topperformance()
    elif(select == 6):
        print("EXITED")
        break
    

