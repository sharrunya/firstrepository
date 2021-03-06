
import decimal as d


studdict = {}
admission_count = 15
gpa = 5

def get_student_info():
    studentname = input("Please provide Student name: ")
    studdict.update({"Student Name" : studentname})
    quest = ["Is student EU citizen", 
             "Is resume submitted", 
             "Is Internship attened", 
             "Mandatory subjects studied"]             
    for x in quest:
        qvalue = input(f'{x} (Y/N):')
        qvalue = qvalue.upper()
        qvalue = data_val_yn(qvalue, x)
        studdict.update({x : qvalue})
        if qvalue == 'N' and x != "Is student EU citizen":
          print("Candidate is not qualified.")
          studdict.update({"Status" : "FAIL"})
          break
        
def data_val_yn(qvalue, x):
    while qvalue!= "Y" and qvalue != "N":
        qvalue = input(f'Please enter proper value - {x} (Y/N):')
        qvalue = qvalue.upper()
        if qvalue == 'Y' or qvalue == 'N':
            break
    return qvalue
    
    
def gpa_conversion(nObtained):
    nMax = 10
    nMin = 0
    GPAconversion = int(((nMax - nObtained) / (nMax - nMin) * 3) + 1)
    studdict.update({"GPA (converted)" : GPAconversion})
    print(f'GPA Converted to EU Standards: {GPAconversion}')
    return GPAconversion
    
def apps_evaluation():
  gpa = int(input("Enter your GPA : "))
  if studdict["Is student EU citizen"] == "N":
    gpa = int(gpa_conversion(gpa))

  if gpa >= 3:
    print("Candidate's GPA is less for qualification.")
    studdict.update({"Status" : "FAIL"})
  elif 2 <= gpa <= 3:
    aptresult = input("Is aptitude exam cleared (Y/N):")
    aptresult = aptresult.upper()
    aptresult = data_val_yn(aptresult, "Is aptitude exam cleared")
    if aptresult == 'N':
      print("Candidate's aptitude result is not sufficient.")
      studdict.update({"Status" : "FAIL"})
    else:
      print("Candidate qualified for the final interview.")
      interview_evaluation()
  else:
    print("Candidate qualified for the final interview.")
    interview_evaluation()

def interview_evaluation():
    finalinterview = input("Is candidate cleared final interview (Y/N):")
    finalinterview = finalinterview.upper()
    finalinterview = data_val_yn(finalinterview, "Is candidate cleared final interview")
    if finalinterview == 'Y':
        print("Candidate is selected. Please proceed with enrollment.")
        studdict.update({"Status" : "Candidate is selected"})
    else:
        print("Candidate is not selected. Thank you for considering our University.")

    
print("Welcome to University Admission")
for x in range (1, admission_count + 1):
    studdict.update({"Status" : ""})
    print(f'Starting evalution for University Admision {x}')
    get_student_info()
    #status = studdict["Status"]
    if studdict["Status"] != "FAIL":
        apps_evaluation() 
        print(studdict)
   