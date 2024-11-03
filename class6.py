print("Problems");

#........1..........
# strVar = "Hello, world! Hello everyone. Welcome to the world of Python. Enjoy coding in Python.";
# findStr = input("Enter Word To Find: ");

# if findStr in strVar:
#     print(f"The word '{findStr}' is in the string.")
# else:
#     print(f"The word '{findStr}' is not in the string.")





#.............2...............
# inputGradeStr =input("Enter grade: ");
# inputGrade = int(inputGradeStr);

# if(inputGrade>=90):
#     print("A+");
# elif(inputGrade>=70 and inputGrade<90):
#     print("B+");
# elif(inputGrade>=50 and inputGrade<=70):
#     print("B");  
# elif(inputGrade<=50):
#     print("Failed");


#...............3.................
# numberStr = input("Enter Number: ");
# numberInt = int(numberStr);
# if((numberInt%3==0) and (numberInt%5 == 0)):
#     print("FizzBuzz");
# elif(numberInt%3 == 0):
#     print("Fizz");
# elif(numberInt%5 == 0):
#     print("Buzz");


numStr1 = input("Enter Number-1: ");
numStr2 = input("Enter Number-2: ");

numInt1 = int(numStr1);
numInt2 = int(numStr2);
operation = input("Enter Operands (+,-*,/): ");

if(operation=="+"):
    print(numInt1+numInt2);
elif(operation=="-"):
    print(numInt1-numInt2);
elif(operation=="*"):
    print(numInt1*numInt2);
elif(operation=="/"):
    print(numInt1/numInt2);
elif(operation=="%"):
    print(numInt1%numInt2);
