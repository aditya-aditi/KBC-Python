questions = ["What is the capital of Arunachal Pradesh?", "What is the capital city of France?", "Who wrote the play \"Romeo and Juliet\"?", "How many continents are there in the world?", "What is the largest planet in our solar system?", "Who is known as the inventor of the telephone?", "What is the tallest mountain in the world?"]

answers = ["itanagar", "paris", "william shakespeare", "7", "jupitar", "alexander graham bell", "mount everest"]

print("Welcome to KBC \nYou will get questions and you have to give the correct answers. For every correct answer you will get +20 points and for a wrong answer you will get -10 point. At the end of the game you will be told the amount of money you will get. The amount of money will be based on the points you have scored. \n")

score = 0

for i in range(len(questions)+1):
    # print(i)
    while i != 7 :
        print(questions[i])
        answer = input("Write the answer: ")
        answer = answer.lower()
        if(answer == answers[i]):
            print("correct answer.")
            score = score + 20
        else:
            print("Wrong Answer")
            score = score - 10

        break
    if i >= 6:
        break

print("Your score is ", score)

if score >= 0:
    print("Money Earned -> ", score*1000)
else:
    print("Get some knowledge. You earned nothing ;)")
