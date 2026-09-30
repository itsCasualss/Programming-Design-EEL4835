from random import randint

def monster_battle(studorah,jeongilla):
    for i in range(3):
        studorah = studorah*randint(1,100)
        jeongilla = jeongilla*randint(1,100)
        print("Evolution", i,)
        print("Studorah HP:", studorah)
        print("Jeongilla HP:", jeongilla)
        
        
    if jeongilla > studorah:
        print("Jeongilla Wins!")
    elif studorah > jeongilla:
        print("Studorah Wins!")
    else:
        print("It's a Tie!")
    
    
    #studorah = int(input("What is studorah's starting HP value?"))
    #jeongilla = int(input("What is jeongilla's starting HP value?"))
    #return evolve_s, evolve_j

def main():
    
    studorah,jeongilla = int(input("What is studorah's starting HP value?")),int(input("What is jeongilla's starting HP value?"))
    
    monster_battle(studorah,jeongilla)
    
    for i in range(1,4):
        studorah = studorah*randint(1,100)
        jeongilla = jeongilla*randint(1,100)
        print("Evolution", i,)
        print("Studorah HP:", studorah)
        print("Jeongilla HP:", jeongilla)

main()
