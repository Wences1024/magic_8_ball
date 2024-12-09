import random
import os

class MagicBall:
    def __init__(self):
        self.answ = {
			0:[
				"It is certain",
				"It is decidedly so",
				"Without a doubt",
				"Yes definitely",
				"You may rely on it",
				"As I see it, yes",
				"Most likely",
				"Outlook good",
				"Yes",
				"Signs point to yes"
			],
			1:[
				"Reply hazy, try again",
				"Ask again later",
				"Better not tell you now",
				"Cannot predict now",
				"Concentrate and ask again"
			],
			2:[
				"Don't count on it",
				"My reply is no",
				"My sources say no",
				"Outlook not so good",
				"Very doubtful"
			]
		}
    def Answer(self):
        type_0 = random.randint(0,2)
        type_1 =  random.randint(0,9) if (type_0 == 0) else random.randint(0,4) 
        return self.answ[type_0][type_1]


if __name__ == "__main__":
    Ball = MagicBall()
    os.system("cls")
    print("Welcome to magic 8 Ball!")
    print("Ask any question, and I'll answer it for you!")
    print("Type exit when you are done")
    print("")
    
    while True:
        x = input("Ask your question: ")
        if not x == "exit":
            print(Ball.Answer())
            print("")
        else:
            break
        
        
        