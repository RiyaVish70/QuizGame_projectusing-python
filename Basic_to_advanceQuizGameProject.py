print("************************")
print("Welcome to My Quiz Game!!!")

Question_bank=[
    {"text":"The ability of one class to acquire methods and attributes another class is called.....","answer":"A"},
    {"text":"Which of the following is typrof inheritance?","answer" :"D"},
    {"text":"What typeof inheritance has multiple subclass to asingle superclass?","answer":"C"},
    {"text":"What is the depth of multiple inheritance in python?","answer":"C"},
    {"text":"What does MRO stand for?","answer":"B"}

]
options=[["A.Inheritance","B.Abstraction","C.Polymorphism","D.Object"],
         ["A.Single","B.Double","C.Multiple","D.both A and C"],
         ["A.Multiple Inheritance","B.Multiple Inheritance","C.Hierarchical Inheritance","D.None of these"],
         ["A. Two level","B. Three level","C. Any level","D.None of these"],
         ["A. method Recursive Object","B. Method resolution Order","C. Main Resolution order","D. method Resolution Object"],

]


def check_answer(user_guess,correct_answer):

    if user_guess==correct_answer:
        return True
    else:
        return False
score = 0 # Initialize score outside the loop

for question_num in range(len(Question_bank)):
    print("************************")
    print(Question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess=input("Enter your answer(A/B/C/D):").upper()
    is_correct=check_answer(guess,Question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score +=1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {Question_bank[question_num]['answer']}")

print(f"You have given {score} correct answers")
print(f"your score is {(score/len(Question_bank))*100}%")

