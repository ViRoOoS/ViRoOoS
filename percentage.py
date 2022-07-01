subjects = int(input('How many subjects do you have? '))
max_score = int(input('Enter the maximum score : '))
sub_list = [
     '\nEnter 1st subject\'s marks : ',
     'Enter 2nd subject\'s marks : ',
     'Enter 3rd subject\'s marks : ',
     'Enter 4th subject\'s marks : ',
     'Enter 5th subject\'s marks : ',
     'Enter 6th subject\'s marks : ',
     'Enter 7th subject\'s marks : ',
     'Enter 8th subject\'s marks : ',
     'Enter 9th subject\'s marks : ',
     'Enter 10th subject\'s marks : ',
     'Enter 11th subject\'s marks : ',
     'Enter 12th subject\'s marks : '
 ]
total = 0
for i in range(subjects):
    x = float(input(sub_list[i]))
    total += x
print(f'\nThe percentage of your marks is:',str(total/(max_score*subjects)*100).split(".0")[0]+"%")
