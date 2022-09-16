if __name__ == '__main__':
    N = int(input())
    input_list=[]
    inp=[]
    output_list = []
    for i in range(N):
        n=input()
        input_list = n.split( )
        inp += input_list 
    for i in range(len(inp)):
        if inp[i] == 'insert':
            # print(output_list[int(inp[i+1])])
            # print(int(inp[i+2]))
            output_list.insert(int(inp[i+1]),int(inp[i+2]))
        elif inp[i] == 'print':
            print(output_list)
        elif inp[i] == 'remove':
            output_list.remove(int(inp[i+1]))
        elif inp[i] == 'append':
            output_list.append(int(inp[i+1]))
        elif inp[i] == 'sort':
            output_list.sort()
        elif inp[i] == 'pop':
            a = inp[i+1]
            if a.isdigit():
                output_list.pop(i+1)
            else:
                output_list.pop()
        elif inp[i] == 'reverse':
            output_list.reverse()
