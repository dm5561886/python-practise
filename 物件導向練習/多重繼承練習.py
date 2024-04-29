class E:
    pass


class F:
    def do_stuff(self):
        print("do stff from F")


class G:
    def do_stuff(self):
        print("do stff from G")


class B(E, F):
    pass


class C:
    def do_stuff(self):
        print("do stff from C")


class D(G):
    pass


class A(B, C, D):
    pass


a = A()
# 結果為do stff from F
# 使用(Depth-First Search，DFS)
# 順序為B,E,F,C,D,G
a.do_stuff()
# classname.mro()  <--list
# classname.__mro__  <--tuple
print(A.mro())
print(A.__mro__)
