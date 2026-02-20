import subprocess
import sys
import os
import random

MP3_FILES = ["celebration.mp3", "celebration2.mp3", "celebration3.mp3"]

def play_sound():
    available_files = [f for f in MP3_FILES if os.path.exists(f)]
    if not available_files:
        print(f"Could not find any MP3 files. Make sure they exist.")
        return
    chosen = random.choice(available_files)
    try:
        subprocess.Popen(['start', '', chosen], shell=True)
    except Exception as e:
        print(f"Could not play sound: {e}")

def calculator():
    print("=== Calculator (type 'exit' to quit) ===")
    print("Enter calculations like: 5 + 3, 10 * 6, 100 / 2")
    
    while True:
        try:
            user_input = input("\n> ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            result = eval(user_input)
            
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            print(f"Result: {result}")
            
            if result == 67:
                print("\n🎉 67 slyvia ai activated larp larp larp sahur 🎉")
                play_sound()
                
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except Exception as e:
            print(f"Error: Invalid expression")

if __name__ == "__main__":
    calculator()
