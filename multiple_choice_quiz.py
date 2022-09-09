class Quiz:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are stawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Quiz(question_prompts[0],"a"),
    Quiz(question_prompts[1],"c"),
    Quiz(question_prompts[2],"b")
]

print(questions)
def test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got "+str(score)+ "/" + str(len(questions)))


test(questions)