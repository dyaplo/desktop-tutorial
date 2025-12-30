secert_answer="cairo"
answer=""
count = 0
limit = 3
lose = False
while secert_answer != answer and not lose:
    if count < limit :
        answer = input("what is capital of egypt? ")
        count += 1
    else:
        lose =True
        
if lose:
    print("you lose")
else:
    print("you win")
