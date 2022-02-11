from resources import Character, Goblin
import random

def fight(fighter : Character, enemies : list):
    
    while not len(enemies) == 0:
        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.get_health() == 0:
            print("Maxi has died")
            enemies.remove(fighter_target)
            if len(enemies) == 0: break
        
    print(f"Fight is over! {fighter.name} won!")



def main():
    enemies = []
    maxi = Character("Maxi", 1, 0.0000001, -5)
    emy = Character("Emy", 20, 6, 5)


    print(maxi)
    print()
    print(emy)
    
    enemies.append(Goblin(1))
    print("\nGoblin")
    print(enemies[0])

    fight(emy, enemies)

if __name__=="__main__":
    main()