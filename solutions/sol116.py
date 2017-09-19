#Himanshu Nachane (@Himanshu1495)
'''input: [1, 2, [2, [5, 3, 4]] ]
output: [1,2, 3, 5, 3, 4]

the output order does not matter, just so long as the array is flattened
'''

def flatten_array(arr):
    for i in arr:
        if len(str(i)) == 1:
            store.append(i)
        else:
            flatten_array(i)
    return store
store = []
