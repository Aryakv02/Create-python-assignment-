def calculate_grade(score):

  if score >= 90:
    return 'A'
  elif score >= 80:
    return 'B'
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return 'D'
  else:
    return 'F'

def main():

  name = input("Enter student's name: ")
  num_subjects = int(input("Enter the number of subjects: "))

  total_score = 0
  for i in range(num_subjects):
    score = float(input(f"Enter score for subject {i+1}: "))
    total_score += score

  average_score = total_score / num_subjects
  grade = calculate_grade(average_score)

  print(f"\nStudent Name: {name}")
  print(f"Average Score: {average_score:.2f}")
  print(f"Grade: {grade}")

if __name__ == "__main__":
  main()