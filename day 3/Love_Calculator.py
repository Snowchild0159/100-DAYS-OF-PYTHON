name1 = input("Enter your name: \n")
name2 = input("Enter your partner's name: \n")

LOVE_NAME = name1 + name2
your_love_score = 0
love_name = LOVE_NAME.lower()
your_love_score = int(str(love_name.count("t") + love_name.count("r")+ love_name.count("u") + love_name.count("e"))+ str(love_name.count("l") + love_name.count("o") + love_name.count("v") + love_name.count("e")))
if your_love_score < 10 or your_love_score > 90:
    print(f"your love score is {your_love_score}, you go together like coke and mentos.")
elif your_love_score >= 40 and your_love_score <= 50:
    print(f"your love score is {your_love_score}, you are alright together.")
else:
    print(f"your love score is {your_love_score}.")
