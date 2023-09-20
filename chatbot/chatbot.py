from bard import call_bard
from gpt3 import call_gpt3

def main():
    banner = """
     |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  AICat

    """
    print(banner)

    print("Hello! I'm AiCat,  What is your name?")
    name = input("Username: ")

    print(f"\nAiCat: Hello {name}! Ask me anything.\n")


    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"\nAiCat: Goodbye, {name}!\n")
            break

        bard_response = call_bard(user_input)
        gpt3_response = call_gpt3(user_input)

        print(f"\nAiCat (from Bard): {bard_response}")
        print(f"AiCat (from GPT-3): {gpt3_response}\n")

if __name__ == '__main__':
    main()
