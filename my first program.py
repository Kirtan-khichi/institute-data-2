
print("Hello Dear Student Form For STARE Scholarship Program Enrollment ")
def repeat():
	institute=input('enter your institute name :-')
	name=input('enter your name :- ')
	branch=input('enter your branch name :-')
	mobileno=int(input('enter your mobile number :-'))
	emailid=input('enter your email id :-')
	birth=input('enter your birth of date :-')
	age=int(input('enter your age :- '))
	passoutclass=input('enter your 12th pasout school name :-')
	percentage=int(input('enter your percentage :-'))
	if percentage>80:
		print('you are qualified')
		if percentage>95:
			print('you got 100% scholarship')
		elif percentage>85:
			print('you got 50% scholarship')
		else:
			print('you does not qualify for   ourscholarship program')
	else:
		print('you are not qualified , Sorry again for next year')
	print([institute,name,branch,mobileno,emailid,birth,age,passoutclass,percentage])
	question=input('Please check above information is write or wrong,if right tap yes or wrong tap no')
	if question=='yes' or ' YES':
	    print('Thank You')
	else:
	    print('Again fill the data')
	    repeat()
repeat()
			

'''if percentage>95:
	print('you got 100% scholarship')
elif percentage>85:
	print('you got 50% scholarship')
else:
	print('you does not qualify for our scholarship program')'''
