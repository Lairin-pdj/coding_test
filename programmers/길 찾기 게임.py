from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

# 정보를 담는 Node 클래스 생성
class Node:
    def __init__(self, data):
        # 좌표 비교용 x
        self.x = data[0]
        # 순서 값 저장용 num
        self.num = data[2]
        # 좌우 자식 포인터
        self.left = None
        self.right = None
        
class BinaryTree:
    # 생성자
    def __init__(self):
        self.root = None
    
    # 삽입 함수
    def insert(self, data):
        # 루트가 빈 경우 루트에 대입 
        if self.root == None:
            self.root = Node(data)
        else:
            # 루트가 비어있지 않으면 값을 계속적으로 비교하며
            # 빈 공간을 찾을 때까지 들어감
            self.temp = self.root
            while True:
                # 값이 작은 경우 좌측 검색
                if self.temp.x > data[0]:
                    # 비어있는 여부에 따라 진행
                    if self.temp.left != None:
                        self.temp = self.temp.left
                    else:
                        self.temp.left = Node(data)
                        break
                # 값이 큰 경우 우측 검색
                else:
                    # 비어있는 여부에 따라 진행
                    if self.temp.right != None:
                        self.temp = self.temp.right
                    else:
                        self.temp.right = Node(data)
                        break
    
    # 전위 순회
    def preorder(self):
        # 재귀를 통해 결론 도출
        def _preorder(node):
            # 정해진 위치에 따라 temp에 순서대로 데이터 삽입
            temp.append(node.num)
            if node.left != None:
                _preorder(node.left)
            if node.right != None:
                _preorder(node.right)
        
        # 반환할 리스트 생성
        temp = []
        # 재귀 호출
        _preorder(self.root)
        
        # 결과값 반환
        return temp
    
    # 후위 순회
    def postorder(self):
        # 재귀를 통해 결론 도출
        def _postorder(node):
            # 정해진 위치에 따라 temp에 순서대로 데이터 삽입
            if node.left != None:
                _postorder(node.left)
            if node.right != None:
                _postorder(node.right) 
            temp.append(node.num)
            
        # 반환할 리스트 생성
        temp = []
        # 재귀 호출
        _postorder(self.root)
        
        # 결과값 반환
        return temp
    
def solution(nodeinfo):
    
    # 데이터 전처리
    # 순서 정보를 데이터에 추가 시킨 뒤
    # 깊이 정보를 통해 삽입될 순서를 조절
    nodechange = []
    for i, node in enumerate(nodeinfo):
        nodechange.append(node + [i + 1])
    nodechange.sort(key = lambda x : (-x[1], x[0]))
    
    # 이진트리에 삽입
    tree = BinaryTree()
    for node in nodechange:
        tree.insert(node)
    
    # 결과 반환
    return [tree.preorder(), tree.postorder()]
