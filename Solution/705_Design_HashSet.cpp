class MyHashSet {

private:
    int arr[1000001];

public:
    /** Initialize your data structure here. */
    MyHashSet() {
        
    }
    
    void add(int key) {
        this->arr[key] = 1;
    }
    
    void remove(int key) {
        this->arr[key] = 0;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return this->arr[key] == 1;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */

/*
Runtime: 176 ms, faster than 63.48% of C++ online submissions for Design HashSet.
Memory Usage: 54.9 MB, less than 37.53% of C++ online submissions for Design HashSet.
*/