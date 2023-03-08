file = open("SMSSpamCollection.txt","r")
smsList = file.readlines()

averageHamWords = 0
numOfHamLines = 0
averageSpamWords = 0
numOfSpamLines = 0
numOfSpamSmsExclamation = 0
for line in smsList:
    if line.startswith('ham'):
        averageHamWords += len(line.split())
        numOfHamLines += 1
    if line.startswith('spam'):
        averageSpamWords += len(line.split())
        numOfSpamLines += 1
        if line[-2].endswith('!'):
            numOfSpamSmsExclamation += 1


print(f"Average num of words in ham: {averageHamWords/numOfHamLines}")
print(f"Average num of words in spam: {averageSpamWords/numOfSpamLines}")
print(f"Number of spam sms that end with exclamation mark: {numOfSpamSmsExclamation}")


file.close()