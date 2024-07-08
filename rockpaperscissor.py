import random
print('winning rules of the game are:\n')
print('rock vs paper -> paper wins\n')
print('rock vs scissor -> rock wins\n')
print('paper vs scissor -> scissor wins')
while True:
    print('enter your choice\n 1 - Rock \n 2 - Paper \n 3- Scissor\n')
    choice=int(input('Enter your choice'))
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('User choice is \n', choice_name)
    print('now its computer turn')
    computer_choice = random.randint(1,3)
    print('compuyer choice is \n',computer_choice)
    print(choice_name ,'vs', computer_choice)
    if choice == computer_choice:
            print('Its a Tie',end='')
            result = 'Tie'
    if (choice ==1 and computer_choice ==2):
            print('Paper wins =>',end='')
            result ='Paper'
    elif(choice ==2 and computer_choice ==1):
            print('Paper wins =>',end='')
            result ='Paper'
    if (choice ==1 and computer_choice ==3):
            print('Rock wins =>',end='')
            result ='Rock'
    elif(choice ==3 and computer_choice ==1):
            print('Rock wins =>',end='')
            result ='Rock'
    if (choice ==2 and computer_choice ==3):
            print('Scissor wins =>',end='')
            result ='Scissor'
    elif(choice ==3 and computer_choice ==2):
            print('Scissor wins =>',end='')
            result ='Scissor'
    if result == 'Tie':
            print('<== Draw')
    if result == choice_name:
            print('# player wins')
    else:
            print('#computer wins')
    print('Do you want to play again?(Y/N)')
    ans = input()    
    if ans == 'N':
            break
    print('Thanks for playing')

        