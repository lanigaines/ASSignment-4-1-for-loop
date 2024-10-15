def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the ending letter: ')

        if not start.isalpha() or not end.isalpha():
           print("Error: Input must be a letter. Please try again.")
           continue
    
        if start > end:
           print("Error: The starting letter must come before ending letter. Please try again.")
           continue
    
        for char in range(ord(start), ord(end) + 1):
            result.append(chr(char))
    
        print(''.join(result))
        break

if __name__ == '__main__':
    main()
