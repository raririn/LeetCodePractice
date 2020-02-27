/*
Consider the following shape:
++++++
++++--
++++--
+++---
+-----
+-----
↑start from here (m-1, 0)
*/

class Solution {
    public int countNegatives(int[][] grid) {
        int ret = 0;
        int m = grid.length, n = grid[0].length;
        int row = m-1, col = 0;
        while (row >= 0 && col < n){
            if (grid[row][col] < 0){
                row--;
                ret += (n - col);
                // System.out.println(n-col);
            }
            else{
                col++;
            }
        }
        return ret;
    }
}

/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 41.5 MB, less than 100.00% of Java online submissions for Count Negative Numbers in a Sorted Matrix.
*/