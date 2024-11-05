import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = map(str,input().split())
    tree[root] = [left, right]

def inorder(root):
    if root != '.':
        print(root, end = '')
        inorder(tree[root][0])
        inorder(tree[root][1])

def preorder(root):
    if root != '.':
        preorder(tree[root][0])
        preorder(tree[root][1])
        print(root, end ='')

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        print(root, end ='')
        postorder(tree[root][1])

inorder('A')
print()
postorder('A')
print()
preorder('A')