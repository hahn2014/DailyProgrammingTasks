import random
import sys

class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

                        # Red Black Tree Guide
# 1) Every Node has a color, either Red or Black
# 2) The root of the tree is always black
# 3) There are no two adjacent red nodes (A red node can not have a red parent or a red child)
# 4) Every path from a node (including root) to any of its descendants NULL nodes has the same
#       number of black nodes
# 5) All leaf nodes are black nodes

class RedBlackTree():
    def __init__(self, item):
        self.head = Node(0)
        self.head.color = 0
        self.head.left = None
        self.head.right = None
        self.root = self.head


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

    def insert(self, val):
        print("hi")



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



def test():
    print("Hello World")


if __name__ == '__main__':
    test()
