import random;
rn = [1,2,3,4,5,6,7,8,9,10];
rnc = random.choice(rn);
print(rnc);
print("Number Guessing Game!");
print("Instructions:");
print("Guess a number between one to ten");
gn = input("Guess a number --> ");
while gn>rn:
    print("YOU'RE WRONG. GUESS A NUMBER LESS THAN "+str(gn));
    gn = input("Guess a number --> ");

while gn<rn:
    print("YOU'RE WRONG. GUESS A NUMBER MORE THAN "+str(gn));
    gn = input("Guess a number --> ");

if gn==rn:
    print("YOU WIN!");