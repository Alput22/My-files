#%%
import random


def money(prize, cash):
    if True:
        prize = prize * 2
        cash = prize + prize
        return prize, cash


questions = {
    1:[['What is the tallest mountain? '],['A.everest','B.kilimanjaro','C.fuji','D.rushmore'],['A']],
    2:[['What is the music of life?'],['A.silence','B.innocence','C.song','D.illusion'],['A']],
    3:[['Who is the best girl in BanG Dream!, according to Blanc?'],['A.ako udagawa','B.ran mitake','C.rinko shirokane','D.rimi ushigome'],['C']],
    4:[['What is the scareist game?'],['A.silent hills','B.python','C.scary maze','D.mobile legends'],['A.'d]]}

i = 0
cash = 0
prize = 250
a, b = True, True
while i <= (len(questions) + 1) // 2:
    num = random.choice(list(questions.keys()))

    print(f"{i + 1}. {questions[num][0][0]}\n{questions[num][1]}\n")

    Help = {"1": "50/50", "2": "Ask friend", "": "Press any key to continue"}
    choice = input(f"{Help} \nPlease input help method: ")
    if choice == "1" and a == True:
        List = ["A", "B", "C", "D"]
        List.remove(questions[num][2][0])
        print()
        wrong = random.choices(List)
        print(f"Hint: ({questions[num][2][0]} or {wrong[0]})")
        del Help["1"]
        a = False

    elif choice == "2" and b == True:
        List = ["A", "B", "C", "D"]
        List.extend([questions[num][2][0], questions[num][2][0]])
        random.shuffle(List)
        print(f"'Hey! What's up bro, the answer is {random.choice(List)}")
        del Help["2"]
        b = False
    else:
        print("")

    ans = input("Your answer will be: ")
    ans = ans.upper()
    if ans == questions[num][2][0]:
        prize, cash = money(prize, cash)
        if i < (len(questions) + 1) // 2:
            print(f"Congratulation! You got {prize} and your cash is {cash}.\n>>Next, you will get {money(prize, cash)}")
        print("-"*10, f" End of section {i+1}!", "-"*10, "\n")
        Q = True
        del questions[num]

    elif ans == " ":
        print("You are considered surrender!")
        Q = False
        break

    else:
        print("Wrong answer!\n")
        Q = False
        break
    i += 1

if Q == False:
    print("-" * 10, "This is the end of the game!", "-" * 10)
    print(f"Unfortunately, you finished the game until question {i+1}")

else:
    print("-" * 10, "This is the end of the game!", "-" * 10)
    if Q == True:
        print("Congratulation!")
print(f"You won the game with total money of {cash}")