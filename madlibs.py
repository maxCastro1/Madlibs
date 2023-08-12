def scifi_madlib():
    adjective = input('enter an adjective: ')
    noun = input('enter a noun: ')
    verb = input ('enter a sci-fi verb: ')
    place = input ('enter a distant place: ')

    madlib = f'In the {adjective} future , humans rely on {noun} technology to {verb} throught time and space. Our journey took us to {place}, where we encounters strange creature and explored new dimensions.'
    print(madlib)

def romance_madlib():
    name1 = input("Enter a name: ")
    name2 = input("Enter another name: ")
    verb = input("Enter a romantic verb: ")
    noun = input("Enter a noun: ")

    madlib = f"{name1} and {name2} decided to {verb} under the moonlight. They held each other close, feeling the warmth of their {noun} and the magic of the moment."
    print(madlib)

    romance_madlib()
def adventure_madlib():
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    madlib = f"One day, I went on an {adjective} adventure to {place}. I brought my trusty {noun} with me and we decided to {verb} together. It was an incredible journey!"
    print(madlib)

    adventure_madlib()

def play_madlib():
    answer = input('which madlib do you want to play \n (a) scif \n (B) romance madlib \n (c) adventure madlib\n\n\n')
    if answer.lower() == 'a':
        scifi_madlib()
    elif answer.lower() == 'b':
        romance_madlib()
    elif answer.lower() == 'c':
        adventure_madlib()
    else:
        print('invalid in put')           


play_madlib()