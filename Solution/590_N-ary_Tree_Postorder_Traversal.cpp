/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
private:
    vector<int> ret;

public:
    vector<int> postorder(Node* root) {
        postorder_helper(root);
        return ret;
    }

    void postorder_helper(Node* cur) {
        if (!cur) {
            return;
        }
        if (!cur->children.empty()) {
            for (auto i: cur->children) {
                postorder_helper(i);
            }
        }
        ret.push_back(cur->val);
    }

};

/*
Runtime: 44 ms, faster than 74.00% of C++ online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 11.2 MB, less than 60.02% of C++ online submissions for N-ary Tree Postorder Traversal.
*/