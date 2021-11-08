from collections import defaultdict
import sys
input = sys.stdin.readline

def preorder(a):
    temp = dic[a]
    left = temp[0]
    right = temp[1]
    
    # root -> left -> right
    print(a, end = "")
    if left != ".":
        preorder(left)
    if right != ".":
        preorder(right)
    
def inorder(a):
    temp = dic[a]
    left = temp[0]
    right = temp[1]
    
    # left -> root -> right
    if left != ".":
        inorder(left)
    print(a, end = "")
    if right != ".":
        inorder(right)
    
def postorder(a):
    temp = dic[a]
    left = temp[0]
    right = temp[1]
    
    # left -> right -> root
    if left != ".":
        postorder(left)
    if right != ".":
        postorder(right)
    print(a, end = "")

# 파싱
n = int(input())
dic = defaultdict(list)
for _ in range(n):
    a, b, c = input().rstrip().split()
    dic[a].append(b)
    dic[a].append(c)

# 결과 출력
preorder("A")
print()
inorder("A")
print()
postorder("A")
