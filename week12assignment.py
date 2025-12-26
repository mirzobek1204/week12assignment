data = """John,Math,55,60
Sarah,Science,40,45
Mike,Math,30,40
Emma,History,80,90
David,Science,95,90
BadLine,Data,Missing
Chris,History,20,30"""

with open("exam_scores.txt", "w") as f:
    f.write(data)
def process_exam_scores(filename):
    subject_totals={}
    failing_students=[]
    with open(filename, "r") as file:
        for line in file:
            items=line.strip().split(",")
            if len(items)!=4:
                continue
            name, subject, part1, part2 = items
            try:
                part1=int(part1)
                part2=int(part2)
            except ValueError:
                continue
            total=part1+part2
            subject_totals[subject]=subject_totals.get(subject,0)+total
            if total<100:
                failing_students.append((name,total))
    return subject_totals,failing_students

def save_grade_report(subject_totals,failing_students):
    with open("grade_report.txt","w") as file:
        file.write("SUBJECT TOTAL POINTS\n")
        file.write("--------------------\n")
        for subject,total in subject_totals.items():
            file.write(f"{subject}: {total}\n")
        file.write("\nAT RISK STUDENTS (< 100 pts)\n")
        file.write("----------------------------\n")
        for name,score in failing_students:
            file.write(f"{name} ({score} pts)\n")

subject_totals,failing_students=process_exam_scores("exam_scores.txt")
save_grade_report(subject_totals,failing_students)






