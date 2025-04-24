students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([score, name])


students.sort()

min_score = students[0][0]


student_list = [i for i in students if i[0] > min_score]

if student_list:
    sec_min_score = student_list[0][0]
    
    names_ordered = sorted([s[1] for s in student_list if s[0] == sec_min_score])
    

    for name in names_ordered:
        print(name)