import turtle
import pandas


class States:

    def __init__(self):
        self.completed = []
        self.completed_states = []
        self.content = pandas.read_csv("50_states.csv")
        self.states = self.content['state'].tolist()

    def create_lack(self):
        states_lacking = [state for state in self.states if state not in self.completed_states]
        file = pandas.DataFrame(states_lacking)
        file.to_csv("Forgotten_states.csv")

    def check_guess(self, guess):
        guess = guess[0].upper() + guess[1:]

        if guess in self.states:
            self.locate_st(guess)
            self.completed_states.append(guess)
            return True
        else:
            return False

    def locate_st(self, guess):
        st = turtle.Turtle()
        st.penup()
        st.hideturtle()
        single_line = self.content[self.content['state'] == guess]
        x = int(single_line.iloc[0,1])
        y = int(single_line.iloc[0,2])
        st.goto(x, y)
        st.write(arg=guess, font=("Courier", 8, "bold"))
        self.completed.append(st)

    @staticmethod
    def you_won():
        win = turtle.Turtle()
        win.penup()
        win.hideturtle()
        win.write(arg="Congrats, you won the game!", align='center', font=("Courier", 22, "bold"))
