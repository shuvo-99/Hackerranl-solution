def print_formatted(number):
    length = len(str(bin(number))) - 2
    for i in range(1,number+1):
        a = str(i)
        b = str(oct(i))
        c = str(hex(i).upper())
        d = str(bin(i))
            
        print(a.rjust(length, " "),b[2:].rjust(length, " "),c[2:].rjust(length, " "),d[2:].rjust(length," "))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
