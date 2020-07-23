/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    if (n % 2 == 0) {
        return "a".repeat(n-1) + "b";
    }
    else {
        return "a".repeat(n);
    }
};

/*
Runtime: 72 ms, faster than 55.77% of JavaScript online submissions for Generate a String With Characters That Have Odd Counts.
Memory Usage: 36.7 MB, less than 14.52% of JavaScript online submissions for Generate a String With Characters That Have Odd Counts.
*/