from binarytree import build

#data structure list
nodes =[8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15] 

#insert the node values
b_tree = build(nodes)

#print statement
print("Binary tree from list :\n", b_tree)

#print statement
print("\nList from binary tree: ", b_tree.values)