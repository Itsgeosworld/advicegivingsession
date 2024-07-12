print('Welcome to the Advice Giving Session!')
first_name = input('What is your first name? ')
last_name_initial = input('What is the initial for your last name? ')
age = int(input('What is your age? '))

# The user starts with 0 points when entering the session
points = 0

print(f'Hello {first_name} {last_name_initial}, you are {age} years old.')

if age >= 18:
    print(f'{first_name}, you are old enough to start this session!')
else:
    print(f'{first_name}, you are not old enough to start this session.')
    quit()

response_to_join_session = input('Are you ready to begin this session? ').lower()
if response_to_join_session == 'y':
    print(f'Lets begin this session! You currently have {points} points.')
    print('Firstly, you will be asked questions on types of fears you are familiar with or experienced.')
    print('Each fear you are familiar with you will earn 5 points. If not, you will lose 5 points!')


    first_question = input('Are you aware of what fear of rejection is? (y/n) ')
    if first_question == 'n':
        print('Fear of rejection can stem from not being accepted. Getting turned down for a romantic date is an example.')
        points -= 5
        print(f'You now have {points} points...')
    elif first_question == 'y':
        print('Great! You are aware of what fear of rejection is.')
        points += 5
        print(f'You now have earned {points} points!')


    second_question = input('Are you aware of what fear of failure is? (y/n) ')
    if second_question == 'n':
        print('Fear of failure stems from not wanting to do poorly in aspects of your life.')
        points -= 5
        print(f'You now have {points} points...')
    elif second_question == 'y':
        print('Great! You are aware of what fear of failure is.')
        points += 5
        print(f'You now have earned {points} points!')


    third_question = input('Are you aware of what fear of judgement is? (y/n) ')
    if third_question == 'n':
        print('Fear of judgement stems from how others or yourself view you.')
        points -= 5
        print(f'You now have {points} points...')
    elif third_question == 'y':
        print('Great! You are aware of what fear of judgement is.')
        points += 5
        print(f'You have earned {points} points!')


    fourth_question = input('Are you aware of what fear of success is? (y/n) ')
    if fourth_question == 'n':
        print('Fear of success can stem from obstacles you might have to endure to receive success.')
        points -= 5
        print(f'You now have {points} points...')
    elif fourth_question == 'y':
        print('Great! You are aware of what fear of success is.')
        points += 5
        print(f'You now have earned {points} points!')


    fifth_question = input('Are you aware of what fear of change is? (y/n) ')
    if fifth_question == 'n':
        print('Fear of change can stem from not wanting to adapt to new things.')
        points -= 5
        print(f'You now have {points} points...')
    elif fifth_question == 'y':
        print('Great! You are aware of what fear of change is.')
        points += 5
        print(f'You now have earned {points} points!')


    sixth_question = input('Are you aware of what fear of loss is? (y/n) ')
    if sixth_question == 'n':
        print('Fear of loss stems from not wanting to lose the people who are close to you.')
        points -= 5
        print(f'You now have {points} points...')
    elif sixth_question == 'y':
        print('Great! You are aware of what fear of loss is.')
        points += 5
        print(f'You have earned {points} points!')

    print(f'You have answered the questions related to fears! You now have {points} points in total.')


    if points >= 5:
        print('A. Fear of Rejection ')
        print('B. Fear of Failure ')
        print('C. Fear of Judgement ')
        print('D. Fear of Success ')
        print('E. Fear of Change ')
        print('F. Fear of Loss')
        print('G. None')
        response = input('Based on the previous questions, which fear do you believe that you have? ').upper()
        if response == 'A':
            print('One common solution for fear of rejection is face it head on instead of avoiding it.')
        elif response == 'B':
            print('Fear of failure can be combated by swindling out your negative thoughts with positive ones.')
        elif response == 'C':
            print('A solution for fear of judgement is not to think harshly of oneself and not let others influence your feelings.')
        elif response == 'D':
            print('Fear of success could be solved by thinking of positive outcomes that can take place when enduring obstacles.')
        elif response == 'E':
            print('One can overcome fear of change by changing the perspective to being able to sustain more with change.')
        elif response == 'F':
            print('One with fear of loss will have to come to acceptance of loved ones fate and their own. Spend time with loved ones. ')
        elif response == 'G':
            print('No fears? Hmm...interesting.')
        else:
            print(f'You have {points} points. You are not able to continue the session...')
            quit()


print('Now you have been given advice on how to combat your fears!')

