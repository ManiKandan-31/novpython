q = ['1.What is the capital of India?',
     '2.What is the national animal?',
     '3.What is the national flower?',
     '4.How many states are present in India?',
     '5.How many union territories are in India?']
ans = ['delhi','tiger','lotus','28','8']
for x in q:
    print(x)
    user_ans = input('enter the answer:').lower()
    if user_ans in ans:
        print('correct answer')
    else:
        print('wrong answer')