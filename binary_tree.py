def binary_tree(r):
   return [r, [], []]
def insert_left(root, new_branch):
   t = root.pop(1)
   if len(t) > 1:
      root.insert(1, [new_branch, t, []])
   else:
      root.insert(1, [new_branch, [], []])
   return root
def insert_right(root, new_branch):
   t = root.pop(2)
   if len(t) > 1:
      root.insert(2, [new_branch, [], t])
   else:
      root.insert(2, [new_branch, [], []])
   return root
def get_root_val(root):
   return root[0]

def get_root_val(root):
   return root[0]
def set_root_val(root, new_val):
   root[0] = new_val
def get_left_child(root):
   return root[1]
def get_right_child(root):
   return root[2]
r = binary_tree(3)
print(r)
insert_left(r, 4)
print(r)
insert_left(r, 5)
print(r)
insert_right(r, 6)
insert_right(r, 7)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)

class BinaryTree:
    def __init__(self,root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left(self,obj):
        if self.left_child == None:
            self.left_child = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self,obj):
        if self.right_child == None:
            self.right_child = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.right_child = self.right_child
            self.right_child = t
    def set_root_val(self, obj):
        self.root = obj
    def get_root_val(self):
        return self.root
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
#print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
#print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_left_child().insert_right('d')
print(r.get_left_child().get_right_child().get_root_val())
r.get_right_child().insert_right('f')
print(r.get_right_child().get_right_child().get_root_val())
r.get_right_child().insert_left('e')
r.right_child.left_child=BinaryTree('1')
print(r.right_child.left_child.get_root_val())
