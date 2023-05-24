'''
Reconstruct BST
	The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root 
        node and visits nodes in the following order:
		Current Node
		Left Subtree
		Right Subtree
  	Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree 
        (BST), write a function that creates the relevant BST and returns its root node.
        The input array will contain the values of BST nodes in the order in which these nodes would be 
        visited with a pre-order traversal.
	Sample Input: [10, 4, 2, 1, 5, 17, 19, 18]
	Sample Output:
	10
      /    \
     4      17
   /   \      \
  2     5     19
 /           /
1           18

EXPLANATION:

1. We start by defining a `TreeNode` class to represent each node of the Binary Search Tree (BST). Each node has a value (`val`), as well as references to its left and right child nodes (`left` and `right`).
2. The `constructBST` function takes the pre-order traversal array (`preorder`) as input and returns the root node of the reconstructed BST.
3. The first base case of the recursive function is when the `preorder` array is empty, indicating that there are no more nodes to construct. In this case, we return `None`.
4. Otherwise, we create the root node using the first element of the `preorder` array (`preorder[0]`).
5. We initialize `i` to 1, as we've already used the first element as the root. Then, we iterate through the remaining elements of the `preorder` array until we find an element greater than or equal to the root's value. This marks the partition point between the left and right subtrees.
6. We recursively call `constructBST` with the subarray of elements from index 1 to `i` (exclusive) to construct the left subtree. This recursive call handles all the elements that are less than the root's value.
7. Similarly, we recursively call `constructBST` with the subarray of elements from index `i` to the end of the array to construct the right subtree. This recursive call handles all the elements that are greater than the root's value.
8. We assign the left and right subtrees to the `left` and `right` attributes of the root node, respectively.
9. Finally, we return the root node, completing the construction of the BST.
10. The `inorderTraversal` function performs an inorder traversal of the reconstructed BST to verify its correctness. It returns a list of node values in the order they would be visited in an inorder traversal.
11. In the main part of the code, we define the sample input `preorder` array as `[10, 4, 2, 1, 5, 17, 19, 18]`.
12. We call the `constructBST` function with the `preorder` array to reconstruct the BST and obtain the root node.
13. We then call `inorderTraversal` with the root node to obtain the inorder traversal of the BST as a list.
14. Finally, we print the inorder traversal, which should match the expected output `[1, 2, 4, 5, 10, 17, 18, 19]

TIME AND SPACE COMPLEXITY:

Time complexity of construct BST function is O(n) and space complexity of the function is O(log(n))
In worst case scenario if the input pre-order traversal is already sorted (resulting in an unbalanced BST), the height of the BST becomes n-1 and thus the space complexity becomes O(n)

Therefore;
Time Complexity: O(n)
Space Complexity: O(log(n)) in average case and O(n) in worst case

'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructBST(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])

    i = 1
    while i < len(preorder) and preorder[i] < root.val:
        i += 1

    root.left = constructBST(preorder[1:i])
    root.right = constructBST(preorder[i:])

    return root

def inorderTraversal(root):
    if root is None:
        return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

# Sample Input
preorder = [10, 4, 2, 1, 5, 17, 19, 18]

# Construct the BST
root = constructBST(preorder)

# Print the inorder traversal of the reconstructed BST
inorder = inorderTraversal(root)
print(inorder)
