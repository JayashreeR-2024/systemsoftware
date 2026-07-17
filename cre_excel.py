file_name = "demo_student_validation.csv"

file = open(file_name, "w")

# ---------------- HEADER ----------------
file.write("TestCaseID,Scenario,USN,Student Name,Expected Result,Actual Result,Status\n")

# ---------------- DATA ----------------
file.write("TC01,Add new student,1BM22CS101,Student One,Student should be added successfully,Student added successfully,PASS\n")

file.write("TC02,Add duplicate student,1BM22CS101,Student Duplicate,Duplicate entry should be rejected,Error: USN already exists,PASS\n")

file.write("TC03,Validate duplicate prevention,1BM22CS101,Fake Student,System should block duplicate USN,Duplicate not allowed,PASS\n")

file.write("TC04,Empty USN validation,,No USN Student,Validation error should appear,USN required,PASS\n")

file.close()

print("CSV Excel file created successfully:", file_name)