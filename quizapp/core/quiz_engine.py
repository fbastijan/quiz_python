import random

class QuizEngine:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        random.shuffle(self.questions)
        for q in self.questions:
            print("\nPitanje:", q["question"])
            for i, opt in enumerate(q["options"], 1):
                print(f"{i}. {opt}")

            answer = input("Tvoj odgovor (broj): ")

            if q["options"][int(answer) - 1] == q["answer"]:
                print("✔️ Točno!")
                self.score += 1
            else:
                print("❌ Netočno.")

        print(f"\nUkupno bodova: {self.score}/{len(self.questions)}")