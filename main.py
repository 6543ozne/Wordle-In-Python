from colorama import Fore, Style, Back
from random import choice

def get_5_letter_word():
    with open("Wordle/5-letter-words.txt") as file:
        return choice(file.read().splitlines())
        
def check_word(word):
    with open("Wordle/5-letter-words.txt") as file:
        words = file.read().splitlines()
        return word in words

def color_word(input_word, real_word):
    colored_word = ""
    letters_used = []
    
    for i in range(5):
        if input_word[i] == real_word[i]:
            colored_word += Back.GREEN + input_word[i] + Style.RESET_ALL
        elif input_word[i] in real_word and input_word[i] not in letters_used:
            colored_word += Back.YELLOW + input_word[i] + Style.RESET_ALL
            letters_used.append(input_word[i])
            
        else:
            colored_word += Back.WHITE + input_word[i] + Style.RESET_ALL
            
    return colored_word

def main():
    answer = get_5_letter_word()
    word = ""
    for i in range(6):
            word = input("Enter the word: ")
            if len(word) != 5 or not check_word(word):
                print("Please enter a 5-letter word.")
                continue
            else:
                result  = color_word(word, answer)
                print(result)
                if word == answer:
                    print("Congratulations! You've guessed the word!")
                    break
    print (f"The correct word was: {answer}")
    
            

print('''                                                                                                                             ┌───┐
                                                        ┌──┐                                                                 │   │
                                                        │  │               ┌──┐                                              │   │
                                                        │  │               │  │                                              │   │
                                                        │  │               │  │                                              │   │
                                                        │  │               │  │                                              │   │
                                                        │  │       ┌─┐     │  │                                              │   │
                                                        │  │       │ │     │  │     ┌───────────┐    ┌──────────┐            │   │
                                                        │  │       │ │     │  │     │           │   ┌│┐         │     ┌─────────┐│
                                                        │  │       │ │     │  │     │  ┌──────┐ │   │└──────────┘     │      │  ││
                                                        │  │       │ │     │  │     │  │      │ │   │ │               │┌─────┐  ││
                                                        │ ┌────────│┐│     │  │     │  └──────┘ │   │ │               ││     │  ││
                                                        │ ││       ││┌─────│  │     │           │   │ │               │└─────┘  ││
                                                        └─└────────└─└─────└──┘     └───────────┘   └─┘               │      └──│┘
                                                                                                                      └─────────┘ 
                                                           ┌─┐                      ┌───────────────────────┐                     
                                                           │ │                      │                       │                     
                                                           │ │                     ┌│┐                      │                     
                                                           │ │                     │└───────────────────────┘                     
                                                           │ │                     │ │                                            
                                                           │ │                     │ │                                            
                                                           │ │                     │┌───────────────────┐                         
                                                           │┌──────────────┐       │└───────────────────┘                         
                                                           │││             │       │ │                                            
                                                           │││             │       ┌──────────────────────┐                       
                                                           │││             │       │                      │                       
                                                           └└──────────────┘       └──────────────────────┘                       
                                                                                                                                  
─                                                                                                                                 ''')
main()