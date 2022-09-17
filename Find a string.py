def count_substring(string, sub_string):
    count = 0
    size = len(string) - len(sub_string)+1
    for i in range(size):
        text=''
        for j in range(len(sub_string)):
            text += string[i+j]
        if text == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDCD'
    
    count = count_substring(string, sub_string)
    print(count)
