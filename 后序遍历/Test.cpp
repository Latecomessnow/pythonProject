#define _CRT_SECURE_NO_WARNINGS 1

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> v;
        stack<TreeNode*> st;
        TreeNode* cur = root;
        TreeNode* prev = nullptr;
        while (cur || !st.empty())
        {
            while (cur)
            {
                st.push(cur);
                cur = cur->left;
            }
            // ����·�ڵ��ջ�г�������ʾ��·�ڵ��Ѿ���������
            TreeNode* top = st.top();
            // ջ���ڵ��������Ϊ�ջ�����һ�η��ʵ���top�������ĸ��ڵ㣬�Ϳ���ֱ�ӷ���
            // �������������top������
            if (top->right == nullptr || top->right == prev)
            {
                v.push_back(top->val);
                // ��¼��һ���Ѿ����ʵĽڵ�
                prev = top;
                st.pop();
            }
            // ���������������
            else
                cur = top->right;
        }
        return v;
    }
};
