print("=== Which TV Detective Are YOU???===")
print()
print("In this game of skill, ingenuity and, let's be frank, dears,","\033[031m","FANTASTIC FUN","\033[0m""...")
print("you will be asked a serious of questions to find out which TV detective you really, REALLY, are!")
print()
gotViolin = input("Do you have a violin? > ")
if gotViolin == "Yes" or "Y":
    print("You are Sherlock Holmes!")
print()
gotNephew = input("Do you have a nephew called 'Grady'? > ")
if gotNephew == "Yes" or "Y":
    print("You are Jessica Fletcher!")
print()
gotWife = input("Do you have a nameless wife? > ")
if gotWife == "Yes" or "Y":
    print("You are Lieutenant Columbo!")
print()
gotJag = input("Do you drive a red Jaguar? > ")
if gotJag == "Yes" or "Y":
    print("You are Inspector Morse!")
print()
gotRow = input("Were you once DCI at Southampton Row nick? > ")
if gotRow == "Yes" or "Y":
    print("You are Jane Tennison!")
else: 
  print("I guess you're not into police procedurals very much, are you?" )
