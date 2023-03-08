numList = []
while True:
    userInput = input("Unesi broj:")
    print(type(userInput))
    if "Done" in userInput:
        break
    try:
        userInput = int(userInput)
    except:
        print("Potrebno je unijeti broj.")
        pass
#    if type(userInput) != int:
#        print("Potrebno je unijeti broj.")
    if type(userInput) != str:
        numList.append(userInput)

print(len(numList))
print(sum(numList)/len(numList))
print(min(numList))
print(max(numList))
numList.sort()
print(numList)