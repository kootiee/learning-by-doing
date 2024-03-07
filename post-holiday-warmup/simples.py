def main():
    name = input('What is your name?: ')
    print(shout(f'Hello, {name}'))

def shout(text):
    return text.upper()

if __name__ == '__main__':
    main()
