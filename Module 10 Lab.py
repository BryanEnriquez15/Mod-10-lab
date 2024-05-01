def main():
    amount = get_float('ENTER THE MONEY!: ')
    print(f'{amount:@>10.2f}')

def get_float(message):
    while True:
        try:
            user_input = float(input(message))
            return user_input
        except ValueError:
            print('Wrong, Enter a new one now')

main()
