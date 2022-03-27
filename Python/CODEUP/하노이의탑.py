# que 클래스 안쓰고

que_list = []

# 큐의 push
que_list.append(1)
que_list.append(2)
print(que_list)

# 비어있는지 확인하는 함수
def is_empty(arr):
    if len(arr) == 0:
        return True
    else:
        return False

def peek(arr):
    return arr[0]

# 비어있다면 비어있습니다 출력
# 안비어있다면 스택 최상단을 출력하고 스택 최상단값을 팝
if is_empty(que_list):
    print('비어있습니다')
else:
    print('안비어있습니다')
    print(peek(que_list))
    que_list.pop()
    if is_empty(que_list):
        print(peek(que_list))

# 클래스를 활용해서

class que:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        return not self.items

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

qque = que()  # stack 객체 생성
print(qque)  # stack object 생성 확인
print(qque.isEmpty())  # 처음에는 아무것도 들어있지 않으므로 True 출력
qque.push(1)  # stk 에 1을 넣음
qque.push(2)  # stk 에 2를 넣음
print(qque.pop())  # stk 에 1가 꺼내지면서 출력 됨
print(qque.pop())  # stk 에 2가 꺼내지면서 출력 됨
print(qque.isEmpty())  # 객체에 아무것도 들어있지 않으므로 True 출력