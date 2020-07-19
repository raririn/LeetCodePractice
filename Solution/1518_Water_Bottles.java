class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ret = 0;
        int emptyBottles = 0;
        while (numBottles > 0) {
            ret += numBottles;
            emptyBottles += numBottles;
            numBottles = emptyBottles / numExchange;
            emptyBottles = emptyBottles % numExchange;
        }
        return ret;
    }
}

/*
Runtime: 2 ms, faster than 100.00% of Java online submissions for Water Bottles.
Memory Usage: 38.4 MB, less than 100.00% of Java online submissions for Water Bottles.
*/