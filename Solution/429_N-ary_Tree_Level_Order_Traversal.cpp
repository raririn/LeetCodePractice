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
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ret;
        if (!root){
            return ret;
        }
        queue<Node*> q;
        q.push(root);
        while (!q.empty()){
            vector<int> cur;
            int size = q.size();
            for (int i = 0; i < size; i++){
                Node* tmp = q.front();
                q.pop();
                cur.push_back(tmp->val);
                for (auto j: tmp->children){
                    q.push(j);
                }
            }
            ret.push_back(cur);
        }
        return ret;
    }
};

/*
Runtime: 152 ms, faster than 65.44% of C++ online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 33.8 MB, less than 77.78% of C++ online submissions for N-ary Tree Level Order Traversal.
*/