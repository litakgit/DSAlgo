import collections

class StackWithMax(object):
    def __init__(self):
        self.stack = []

    def insert(self, val):
        self.stack.append((val, max(self.stack[-1][1] if self.stack else val, val)))

    def pop(self):
        return self.stack.pop() if self.stack else None

    def get_max(self):
        return self.stack[-1][1] if self.stack else None

if __name__ == "__main__":
    st = StackWithMax()
    st.insert(12)
    st.insert(21)
    st.insert(1)
    st.insert(15)
    print (st.get_max())
    st.pop()
    print (st.get_max())
    st.pop()
    print (st.get_max())
    st.pop()
    print (st.get_max())
    st.pop()
    print (st.get_max())
    st.pop()
