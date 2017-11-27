def main():
    showItems = []
    with open('ShowList.txt', 'r') as f:
        for line in f:
            line = line.strip()
            showItems.append(line)
    
    while True:
        prompt = input('What shows would you like to watch this weekend? Type show name or "help" for list of commands ')
        if prompt == "help":
            print("\nCOMMANDS\nhelp: display instructions | show: show show list | quit: save and quit | move: move list item to different list index")
            continue
        elif prompt == "quit":
            open('ShowList.txt', 'w').close()
            for i in showItems:
                f = open("ShowList.txt", "a")
                f.write("%s\n" % i)
                f.close()
            print("\nShow list saved. Hope you come back soon!")
            break
        elif prompt == "show":
            for i in showItems:
                print(i)
            print()
            continue
        elif prompt == "clear":
            showItems = []
            open('ShowList.txt', 'w').close()
            continue
        elif prompt == "move":
            move = input("Which show would you like to move? ")
            space = input("Which index would you like to move " + move + " to ")
            space = int(space)
            showItems.remove(move)
            showItems.insert(space, move)
            continue
        elif prompt == "remove":
            remove = input("Which show would you like to remove? ")
            showItems.remove(remove)
            continue
        else:
            showItems.append(prompt)
            continue

main()