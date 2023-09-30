import turtle
import pandas

data = pandas.read_csv("50_states.csv")
statesList = data.state.to_list()
xcorList = data.x.to_list()
ycorList = data.y.to_list()
score = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
background = turtle.shape(image)
textWriter = turtle.Turtle()  # Turtle object for writing correct answers
textWriter.penup()
textWriter.hideturtle()
wrongText = turtle.Turtle()  # Turtle object for writing wrong answer text
wrongText.penup()
wrongText.hideturtle()
wrongText.goto(-40, 260)
scoreTurtle = turtle.Turtle()  # Turtle object for writing score and end game text
scoreTurtle.penup()
scoreTurtle.hideturtle()
scoreTurtle.goto(0, 245)

while len(statesList) > 0:

    playerGuess = turtle.textinput(f"Guess the state {score}/50", "What's another state's name?\n"
                                                                  "(Enter 'quit' to exit)").title()

    if playerGuess in statesList:
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(str(score) + "/50")
        wrongText.clear()
        index = statesList.index(playerGuess)
        textWriter.goto(xcorList[index], ycorList[index])
        textWriter.write(statesList[index])
        del statesList[index]
        del xcorList[index]
        del ycorList[index]

    elif playerGuess == "Quit":
        break

    else:
        wrongText.write("WRONG, TRY AGAIN!")
        scoreTurtle.clear()
        scoreTurtle.write(str(score) + "/50")

if len(statesList) == 0:
    scoreTurtle.goto(-40, 260)
    scoreTurtle.write("CONGRATULATIONS!!")
else:
    scoreTurtle.goto(-140, 260)
    scoreTurtle.write("CSV file with missed states has been created in your game folder.")
    missedStates = {
        "Missed States": statesList
    }
    missedStatesFile = pandas.DataFrame(missedStates)
    missedStatesFile.to_csv("Missed states.csv")

turtle.exitonclick()
