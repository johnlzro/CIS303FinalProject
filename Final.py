print('Welcome to the Professional Athlete Championship Quiz!!!\n')

print('Just a reminder the letter can either be upper/lower case. Goodluck:)\n')
# Define Scores
x = 0
score = x

# Questions 1-10
# *Answers will be located at the bottom of the code*
# Number 1
print('1. How many championships does LeBron James have?')
answer1 = input('A)4\nB)5\nC)3\nD)6\n:')
if answer1.upper() == 'C' or answer1 == '3':
	print('You got it')
	x = x + 1
else:
	print('Wrong, LeBron has 3 championships')

# Number 2
print('2. How many championships does Tom Brady have?')
answer2 = input('A)1\nB)9\nC)4\nD)6\n:')
if answer2.upper() == 'D' or answer2 == '6':
	print('You got it')
	x = x + 1
else:
	print('Wrong, Tom has 6 championships')

# Number 3
print('3. How many championships does Steph Curry have?')
answer3 = input('A)3\nB)2\nC)6\nD)7\n:')
if answer3.upper() == 'A' or answer3 == '3':
	print('You got it')
	x = x + 1
else:
	print('Wrong, Steph has 3 championships')

# Number 4
print('4. How many championships does Derek Jeter have?')
answer4 = input('A)1\nB)4\nC)9\nD)2\n:')
if answer4.upper() == 'B' or answer4 == '4':
	print('You got it')
	x = x + 1
else:
	print('Wrong, Derek has 4 championships')

# Number 5
print('5. How many championships does Michael Jordan have?')
answer5 = input('A)6\nB)7\nC)8\nD)11\n:')
if answer5.upper() == 'A' or answer5 == '6':
	print('You got it')
	x = x + 1
else:
	print('Wrong, MJ has 6 championships')

# Number 6
print('6. How many championships does Buster Posey have?')
answer6 = input('A)3\nB)2\nC)1\nD)0\n:')
if answer6.upper() == 'A' or answer6 == '3':
	print('You got it')
	x = x + 1
else:
	print('Wrong, Buster has 3 championships')

# Number 7
print('7. How many championships does Jerry Rice have?')
answer7 = input('A)8\nB)2\nC)3\nD)5\n:')
if answer7.upper() == 'A' or answer7 == '3':
	print('You got it')
	x = x + 1
else:
	print('Wrong, Jerry has 3 championships')

# Number 8
print('8. How many championships does Kawhi Leonard have?')
answer8 = input('A)10\nB)1\nC)5\nD)2\n:')
if answer8.upper() == 'D' or answer8 == '2':
	print('You got it')
	x = x + 1
else:
	print('Wrong, Kawhi has 2 championships')

# Number 9
print('9. How many championships does Kobe Bryant have?')
answer9 = input('A)6\nB)5\nC)4\nD)7\n:')
if answer9.upper() == 'B' or answer9 == '5':
	print('You got it')
	x = x + 1
else:
	print('Wrong, The Black Mamba has 6 championships')

# Number 10
print('10. How many championships does Babe Ruth have?')
answer10 = input('A)9\nB)2\nC)7\nD)3\n:')
if answer10.upper() == 'C' or answer10 == '7':
	print('You got it')
	x = x + 1
else:
	print('Wrong, Babe has 7 championships :(\n')

# Final Score
score = float(x/10) * 100
print("You got", x,"out of 10 correct that is",score,'%\n')

print("Thank you for completing the quiz!\n")


# Question Answers
# 1 Lebron James: 3 
# 2 Tom Brady: 6
# 3 Steph Curry: 3
# 4 Derek Jeter: 4
# 5 Michael Jordan: 6
# 6 Buster Posey: 3
# 7 Jerry Rice: 3
# 8 Kawhi Leonard: 2
# 9 Kobe Bryant: 5
# 10 Babe Ruth: 7