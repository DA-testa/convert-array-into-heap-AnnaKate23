# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        min = i
        #set i as min_index
        left_child = 2*i + 1
        right_child = 2*i + 2

        if left_child < n and data[left_child] < data[min]:
            min = left_child
        if right_child < n and data[right_child] < data[min]:
            min = right_child
        if i != min:
            swaps.append([i, min])
            data[i], data[min] = data[min], data[i]

            j = min
            while j <= n//2 - 1:
                k = 2*j + 1
                if k+1 < n and data[k+1] < data[k]:
                    k = k+1
                if data[j] > data[k]:
                    swaps.append((j, k))
                    data[j], data[k] = data[k], data[j]
                    j=k
                else:
                    break
                
        

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():

    print("Input 'I' or 'F': ")
    text = input()
    if "F" in text:
        file = input()
        if 'a' not in file:
            with open("./tests/"+file, mode='r') as filee:
                n = int(filee.readline())
                data = list(map(int, filee.readline().split()))
        else:
            print("error")
    elif "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        # assert len(data) == n, "length of data should be the same as n"
        #skaitlu ievade
        
      
            
            #skaitlu ievade
    else:
        print("invalid input")
        return
    
    assert len(data) == n, "length of data should be the same as n"
    
    swaps = build_heap(data)

    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    
    

    # checks if lenght of data is the same as the said lenght
    # assert len(data) == n, "length of data should be the same as n"

    # calls function to assess the data 
    # and give back all swaps
    

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    
        
    #print(len(swaps))
    #for i, j in swaps:
     #   print(i, j)


if __name__ == "__main__":
    main() 
