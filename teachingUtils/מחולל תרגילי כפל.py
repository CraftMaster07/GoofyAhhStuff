import random
import re
import os

LINE = "----"

def printExcercise(num1: int, num2: int):
	print(f" {num1}\n*{num2}\n{LINE}")


def calculateExerciseWay(num1: int, num2: int):
	wayNumbers = []
	matansWayNumbers = []
	for x in str(num1):
		for y in str(num2):
			wayNumbers.append(int(x)*int(y))
			try:
				matansWayNumbers.append(int(input()))
			except ValueError:
				matansWayNumbers.append(0)
	
	wayNumbers[0] *= 100
	wayNumbers[1] *= 10
	wayNumbers[2] *= 10
	
	print()
	for i in range(len(wayNumbers)):
		if matansWayNumbers[i] in wayNumbers:
			print(str(matansWayNumbers[i]).rjust(4, " "), " -> V")
		else:
			print(str(matansWayNumbers[i]).rjust(4, " "), " -> X")
	print(LINE)


def main():
	if not os.path.exists(r"C:\Users\אורטל\Desktop\excersises.txt"):
		with open(r"C:\Users\אורטל\Desktop\excersises.txt", "w") as f:
			f.write("0;0")
	while True:
		num1 = random.randint(10,99)
		num2 = random.randint(10,99)
		printExcercise(num1, num2)
		calculateExerciseWay(num1, num2)
		answer = input()
		if answer == "ביי":
			exit()
		if re.match(str(num1*num2), answer):
			validation = "V"
		else:
			validation = "X"
		print(num1*num2, validation)
		print()
		with open(r"C:\Users\אורטל\Desktop\excersises.txt", "r") as f:
			fileText = f.read()
		fileText = fileText.split(";")
		try:
			fileText[0] = str(int(fileText[0])+1)
			fileText[1] = str(int(fileText[1])+1 if validation == "V" else int(fileText[1]))
		except ValueError:
			fileText = ["0", "0"]
		with open(r"C:\Users\אורטל\Desktop\excersises.txt", "w") as f:
			f.write(";".join(fileText))


if __name__ == "__main__":
	main()
