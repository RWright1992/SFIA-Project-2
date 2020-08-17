import random

ans1 = "It is certain"
ans2 = "It is decidedly so"
ans3 = "Without a doubt"
ans4 = "Yes - Definitely"
ans5 = "You may rely on it"
ans6 = "As I see it yes"
ans7 = "Most Likely"
ans8 = "Outlook Good"
ans9 = "Yes"
ans10 = "Signs point to yes"
ans11 = "Reply hazy, try again"
ans12 = "Ask again later"
ans13 = "Better not tell you now"
ans14 = "Cannot predict now"
ans15 = "Concentrate and ask again"
ans16 = "Don't Count on it"
ans17 = "My reply is no"
ans18 = "My sources say no"
ans19 = "Outlook not so good"
ans20 = "Very doubtful"

input("What is your question?")

output = random.randint(1,20)

if output == 1:
    answer = ans1
elif output == 2:
    answer = ans2
elif output == 3:
    answer = ans3
elif output == 4:
    answer = ans4
elif output == 5:
    answer = ans5
elif output == 6:
    answer = ans6
elif output == 7:
    answer = ans7
elif output == 8:
    answer = ans8
elif output == 9:
    answer = ans9
elif output == 10:
    answer = ans10
elif output == 11:
    answer = ans11
elif output == 12:
    answer = ans12
elif output == 13:
    answer = ans13
elif output == 14:
    answer = ans14
elif output == 15:
    answer = ans15
elif output == 16:
    answer = ans16
elif output == 17:
    answer = ans17
elif output == 18:
    answer = ans18
elif output == 19:
    answer = ans19
else:
    answer = ans20

print(answer)