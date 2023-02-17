from glob import glob
from tkinter import *
import random


def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            # نضع في مربع الضغط عليه اسم اللاعب
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                # switch player تغير اللاعب
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[0] + " !wins! Winner"))

            elif check_winner() == 'tie':
                label.config(text=("Tie, No Winner!"))

        elif player == players[1]:
            # نضع في مربع الضغط عليه اسم اللاعب
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                # switch player
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[1] + " !wins! Winner"))

            elif check_winner() == 'tie':
                label.config(text=("Tie, No Winner!"))


def check_winner():
    # في حاله الفوز الافقي
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg='#00c853')
            game_btns[row][1].config(bg='#00c853')
            game_btns[row][2].config(bg='#00c853')
            return True

    # في حاله الفوز الراسي
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg='#00c853')
            game_btns[1][col].config(bg='#00c853')
            game_btns[2][col].config(bg='#00c853')
            return True

    # في حاله فوز السمبوكس
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg='#00c853')
        game_btns[1][1].config(bg='#00c853')
        game_btns[2][2].config(bg='#00c853')
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg='#00c853')
        game_btns[1][1].config(bg='#00c853')
        game_btns[2][0].config(bg='#00c853')
        return True

    # في حاله التعادل
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='orange')
        return 'tie'
    else:
        return False


def check_empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != '':
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def start_new_game():
    global player
    player = random.choice(players)

    label.config(text=(player + ' Turn'))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text='', bg='#f0f0f0')


window = Tk()

# عنوان اللعبه
window.title("X/O")

# لون الخلفيه اللعبه
window.config(bg='#651fff')

# اللاعبين
players = ["X", "O"]
player = random.choice(players)  # اختيار عشوائي لمن يبدء اللعب


# خانات اللعب
game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# خانه الادوار (X Turn or O Turn)
label = Label(text=(player + " Turn"), font=('consolas', 40), width='20')
label.config(bg="#3d5afe")
label.pack(side="top")


# زرار RESTART
restart_btn = Button(text="restart", font=(
    'consolas', 20), command=start_new_game)
restart_btn.config(bg="#c51162")
restart_btn.pack(side="top")


# تهئيه خانات اللعبه
btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()  # عشان اللعبه متقفلش
