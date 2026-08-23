print('''
__________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/

''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('you are have been thrown into an empty room with two doors, what do you choose? Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('now you are infront of a lake with an ilsand over the horizon, do you want to "wait" for a boat or "swim" across?\n').lower()
    if choice2 == "wait":
        choice3 = input('you have arrived at the island!!! now there are three shuffles in front of you, red, yellow and blue, choose wisely :/ \n').lower()
        if choice3 == "red":
            print("you have been set on fire, HAHAHAA BUUUURNNN GAME OVER")
        elif choice3 == "yellow":
            print("now you are poisoned and coughing blood sadly you have died, GAME OVER!!!")
        elif choice3 == "blue":
            print("is that a shiny chest? you are soooo lucky CONGRATULATIONS YOU HAVE WON THE GAME!!!")
        else:
            print("you have chosen a door that doesn't exist and the Island punished you by death, GAME OVER!!!")
    else:
        print("you are attacked by a sea monsters and you have been eaten alive :( SAD!)")
else:
    print("you have fallen into darkness and slowly swolled by the emptyness of the room, sorry you are crazy now, GAME OVER!!!")

