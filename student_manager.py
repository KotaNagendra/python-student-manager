def manage_students(scores_dict):
  passing_records=[]
  for name,score in scores_dict.items():
    if score >= 50:
      passing_records.append(name +" - "+str(score)+" [PASS]")
    else:
      passing_records.append(name +" - "+str(score)+" [FAIL]")
  return passing_records

student_scores = {
    "Rahul": 45,
    "Ananya": 78,
    "Kiran": 92,
    "Vikram": 35,
    "Priya": 60
}

saved_records=manage_students(student_scores)
print(saved_records)
