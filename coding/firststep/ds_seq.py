shoplist = ['apple','mango','carrot','banana']

name = 'swaroop'

# indexing or 'subscription' operation
print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is',shoplist[-1]) # banana
print('Item -2 is',shoplist[-2]) # carrot
print('Character 0 is',name[0])

# slicing on a list
print('Item 1 to 3 is',shoplist[1:3]) # [1,3)
print('Item 2 to end is',shoplist[2:]) # from index 2 to the end
print('Item 1 to -1 is',shoplist[1:-1]) # not included the last one ,because -1 equals 3(last one)
print('Item start to end is',shoplist[:]) #all

# slicing on characters
print('characters 1 to 3 is',name[1:3]) #[1,3)
print('characters 2 to end is',name[2:]) # from index 2 to the end
print('characters 1 to -1 is',name[1:-1]) # from index 1 to the last one(not included)
print('characters start to end is',name[:]) # all