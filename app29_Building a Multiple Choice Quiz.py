from Questions import Questions

question_prompts = [
    "\nWhat color are Apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "\nWhat color are Bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "\nWhat color are Strawberries? \n(a) Yellow\n(b) Red\n(c) Blue\n",
]

# setting Question class attributes for 3 objects
questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")
]

# create function
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        if answer != "a" or answer != "b" or answer != "c":
            print("Invalid answer\n")
    print("You got " + str(score) + "/" + str(len(questions)) + " of the answers correctly.")

run_test(questions)


