class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        left_val = preorder[1]
        left_index = postorder.index(left_val)

        root.left = self.constructFromPrePost(preorder[1:left_index+2], postorder[:left_index+1])
        root.right = self.constructFromPrePost(preorder[left_index+2:], postorder[left_index+1:-1])

        return root