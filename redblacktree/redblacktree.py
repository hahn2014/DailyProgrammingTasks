import sys, os

class Node(object):
    def __init__(self, key):
        self._key = key
        self._parent = None
        self._left = None
        self._right = None
        self._color = 1

    key     = property(fget=lambda self: self._key, doc="The Node's Key/Value")
    parent  = property(fget=lambda self: self._parent, doc="The Node's Parent")
    left    = property(fget=lambda self: self._left, doc="The Node's Left Child")
    right   = property(fget=lambda self: self._right, doc="The Node's Right Child")
    color   = property(fget=lambda self: self._color, doc="1 for black, 0 for red")

    def __str__(self):
        return str(self.key) # string representation of the key/value



                        # Red Black Tree Guide
# 1) Every Node has a color, either Red or Black
# 2) The root of the tree is always black
# 3) There are no two adjacent red nodes (A red node can not have a red parent or a red child)
# 4) Every path from a node (including root) to any of its descendants NULL nodes has the same
#       number of black nodes
# 5) All leaf nodes are black nodes

class RedBlackTree(object):
    def __init__(self, create_node=Node):
        self._nil = create_node(key=None)
        self._root = self.nil
        self._create_node = create_node

    root = property(fget=lambda self: self._root, doc="The Tree's Root Node")
    nil  = property(fget=lambda self: self._nil, doc="The Tree's nil Node")

    

                                # Insertion Psuedocode

# 1) Perform standard BST insertion and make the color of the newly inserted node
#       be red. Let x be the newly inserted node.
#
# 2) If x is the root, change x's color to black.
#
# 3) Do the following if the color of x's parent 'p' is NOT black and x is NOT the root:
#   a) If x's uncle 'u' is red (grandparent 'g' must be black from property 4):
#     i)   Change the p and u node's colors to black
#     ii)  Change the g node's color to red
#     iii) Let x = x's g, and repeat steps 2 and 3 for the new x.
#   b) If x's uncle 'u' is black, then there can be 4 configurations for x, x's parent
#         'p', and x's grandparent 'g'.
#     i)   Left Left Case: p is left child of g and x is left child of p
#     ii)  Left Right Case: p is left child of g and x is right child of p
#     iii) Right Right Case: p is the right child of g and x is the right child of p
#     iv)  Right Left Case: p is the right child of g and x is the left child of p
#
# 4) Re-Coloring after rotation:
#   a) For Left Left Case (3-b-i) and for Right Right Case (3-b-iii), swap colors of
#         grandparent and parent after rotations
#   b) For Left Right Case (3-b-ii) and for Right Left Case (3-b-iv), swap colors of
#         grandparent and inserted node after rotations

    def insert(self, key):
        self.insertNode(self._create_node(key=key))
        print("{} has been inserted into the tree.".format(key))

    def insertNode(self, n):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if (n.key < x.key).any():
                x = x.left
            else:
                x = x.right
        n._parent = y
        if y == self.nil:
            self._root = n
        elif (n.key < y.key).any():
            y._left = n
        else:
            y._right = n
        n._left = self.nil
        n._right = self.nil
        n._color = 0
        self._insert_fix(n)

    # restore red black properties after insertion
    def _insert_fix(self, n):
        while n.parent.color == 0: # continue loop until node's parent's color is no longer red
            if n.parent == n.parent.parent.left:
                y = n.parent.parent.right
                if y.color == 0: # if uncle color is red
                    n.parent._color = 1 # parent is black
                    y._color = 1 # uncle is black
                    n.parent.parent._color = 0 # grandparent is red
                    n = n.parent.parent # make grandparent the current node
                else: # if uncle color is black
                    if n == n.parent.right:
                        n = n.parent
                        self._left_rotate(n)
                    n.parent._color = 1 # parent is black
                    n.parent.parent._color = 0 # grandparent is red
                    self._right_rotate(n.parent.parent)
            else:
                y = n.parent.parent.left
                if y.color == 0:
                    n.parent._color = 1
                    y._color = 1
                    n.parent.parent._color = 0
                    n = n.parent.parent
                else:
                    if n == n.parent.left:
                        n = n.parent
                        self._right_rotate(n)
                    n.parent._color = 1
                    n.parent.parent._color = 0
                    self._left_rotate(n.parent.parent)
        self._root._color = 1


    def _left_rotate(self, x):
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._parent = x
        y._parent = x.parent
        if x.parent == self.nil:
            self._root = y
        elif x == x.parent.left:
            x.parent._left = y
        else:
            x.parent._right = y
        y._left = x
        x._parent = y

    def _right_rotate(self, y):
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._parent = y
        x._parent = y.parent
        if y.parent == self.nil:
            self._root = x
        elif y == y.parent.right:
            y.parent._right = x
        else:
            y.parent._left = x
        x._right = y
        y._parent = x

                                # Deletion Psuedocode

# 1) Perform standard BST deletion. When we perform a standard delete operation in BST,
#       we always end up deleting a node that is either a leaf, or only has one child
#       (For an internal node, we copy the successor and then recursively call delete for
#       successor, successor is always a leaf node or a node with one child). So we only
#       need to handle cases where a node is a leaf or has one child. Let v be the node to
#       be deleted, and u be the child node that replaces v (Note that u is NULL when v is
#       a leaf, and NULL is considered black).
#
# 2) Simple Case (Either u or v are red): If either u or v is red, we mark the replaced
#       child as black (No change in black height). Note that both u and v cannot be red
#       as v is a parent of u and two consecutive reds are not allowed in a red black tree.
#
# 3) Hard Case (Both u and v are black):
#   a) Color u as double black. Now our task reduces to convert this double black to single
#         black. Note that if v is a leaf, then u is NULL and NULL is considered black. So
#         the deletion of a black lead also causes a double black
#   b) Do the following while the current node u is double black, and u is not the root. Let
#         sibling of u be s
#     i)   If s is black and at least one of s's children is red, perform rotations. Let the
#             red child of s be r. This can be divided into four subcases depending upon the
#             positions of s and r.
#       A) Left Left Case: s is the left child of its parent and r is the left child of s, or
#             both children of s are red.
#       B) Left Right Case: s is the left child of its parent and r is the right child of s.
#       C) Right Right Case: s is the right child of its parent and r is the right child of
#             s, or both children of s are red.
#       D) Right Left Case: s is the right child of its parent and r is the left child of s.
#     ii)  If s is black and both children of s are also black, perform recoloring, and recur
#             for the parent if parent is black. If parent was red, then skip the recur for
#             parent, we can simply make it black (red + double black = single black)
#     iii) If s is red, perform a rotation to move old sibling up, then recolor the old
#             sibling and parent. The new sibling is always black. This mainly converts the
#             tree to black sibling case (by rotation) and leads to case (i) or (ii). This
#             case can be divided into two subcases:
#       A) Left Case: s is the left child of its parent. This is a mirror of the Right Right
#             Case (3-b-i-C). We right rotate the parent p.
#       B) Right Case: s is the right child of its parent. We left rotate the parent p.
#   c) If u is root, make it a single black and return (black height of complete tree reduces
#         by 1)

    def delete(self, val):
        print("nothing to see here.")

    def printTree(self):
        print("--- Printing Tree ---")
        self._print_tree(self.root, "", True)

    def _print_tree(self, node, indent, last):
        if node != self.nil:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "    "
            else:
                sys.stdout.write("L----")
                indent += "    "
            s_color = "RED" if node.color == 0 else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self._print_tree(node.left, indent, False)
            self._print_tree(node.right, indent, True)


if __name__ == '__main__':
    import numpy.random as R
    R.seed(2)
    size = 50
    keys = R.randint(-50, 50, size=size)
    tree = RedBlackTree()

    for i in range(1,5):
        tree.insert(R.randint(-50, 50, size=size))



    tree.printTree()
    # tree.insert(10)
    # test_tree(tree)
    # write_tree(t, 'tree')
