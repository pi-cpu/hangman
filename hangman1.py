# http://tinyurl.com/jhrvs94
import random

def hangman():
    word_list = ["boke", "piyo", "beetle", "quanon", "hacker"]
    word_n = random.randint(0, 4)
    word = word_list[word_n]
    wrong = 0
    stages = [
              "________        ",
              "|               ",
              "|       |       ",
              "|       O       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to hangman")

    while wrong < len(stages) :
        print("\n")
        msg = "一文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))



hangman()

              
        
