def removeElement (mylist, target):
    if target in mylist:
        for element in mylist:
            if element == target:
                mylist.remove (element)
        print(len(mylist))
        print(mylist)
    else:
        print (f'Element {target} is not in the list')
    return mylist

llista = [1,5,3,4,5]
aBuscar = 6

llista = removeElement (llista, aBuscar)