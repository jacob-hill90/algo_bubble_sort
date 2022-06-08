#Create method bubble_sort that takes in sequence as argument 
#Create while loop for when greater than zero
#Create a for loop and loop through the input array
    #If current index > current index + 1 ---> swap the numbers
        #Create a temp variable and assign it to the current index + 1
        #Assign array at current index + 1 to equal current index
        #Assign arrat at current index to equal temp
        #Increment swap by 1 
    #Decrement counter for while loop by 1

sequence = [4, 3, 5, 0, 1]
swaps = 0

def bubble_sort(arr):
    counter = len(arr)
    global swaps

    while counter > 0:
        
        for i in range(len(arr) - 1):
            first_elem = arr[i]
            second_elem = arr[i + 1]

            if first_elem > second_elem:
                temp = second_elem
                arr[i + 1] = first_elem
                arr[i] = temp 
                swaps += 1
        
        counter -= 1
    print(arr)


bubble_sort(sequence)


