import time
import os
import random
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
phrase = input("Enter your Phrase:")
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
def slot_machine_effect(phrase, lines=10, speed=0.01):
    for _ in range(20):  
        clear_console()
        for _ in range(lines): 
            current_phrase = ''.join(random.choice(letters) if random.random() > 0.2 else ch for ch in phrase)
            print(current_phrase)
        time.sleep(speed)
    for reveal_position in range(len(phrase) + 1):
        clear_console()
        for _ in range(lines):
            current_phrase = phrase[:reveal_position] + ''.join(random.choice(letters) for _ in range(len(phrase) - reveal_position))
            print(current_phrase)
        time.sleep(speed)
    clear_console()
    print("\n".join([phrase] * lines))
slot_machine_effect(phrase, lines=15, speed=0.09)