import pprint



BAL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

BALLANCED_LIST = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '{})())()()}}(){[][][][]}'
]
UNBALLANCED_LIST = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
    '{)(}({()(}{)(}{})})}))',
    '{[{[{{[{[{[{{[{{}}]}}]}]}]}}]}]}'
]


class Stack(list):

    def is_empty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)
    
    def pop(self):
        if not self.is_empty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.is_empty():
            return self[-1]

    def size(self):
        return len(self)


def check_ballance(seq_):
    stack = Stack()
    for item_ in seq_:
        if item_ in BAL_DICT:
            stack.push(item_)
        elif item_ == BAL_DICT.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':
    for seq in BALLANCED_LIST + UNBALLANCED_LIST:
        print(f'{seq} == {check_ballance(seq)}')



