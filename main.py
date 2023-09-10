def main():
    adj: str = input('Adjevtive: ')
    verb: str = input('Verb: ')
    verb2: str = input('Verb: ')
    famous_person: str = input('Famous Person: ')

    madlib = f'Computer programming is {adj}, it makes me wanna {verb}, so much that I {verb2}. Even {famous_person} has same point of view as me'

    print(madlib)


if __name__ == '__main__':
    main()
