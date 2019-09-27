/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ret;
        if (!root){
            return ret;
        }
        stack<Node*> stk;
        Node* cur;
        stk.push(root);
        while(!stk.empty()){
            cur = stk.top();
            stk.pop();
            ret.push_back(cur->val);
            for (int i = cur->chilren.size()-1; i>=0; i--){
                if (cur->children[i]){
                    stk.push(cur->chilren[i])
                }
            }
        }
        return ret;
    }
};


/*
Runtime: 168 ms, faster than 13.78% of C++ online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 33 MB, less than 36.84% of C++ online submissions for N-ary Tree Preorder Traversal.
*/