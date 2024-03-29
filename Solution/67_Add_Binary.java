class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder;
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        int sum = 0;
        while (i >= 0 || j >= 0) {
            sum = carry;
            if (i >= 0) {
                sum += (a.charAt(i--) - '0');
            }
            if (j >= 0) {
                sum += (b.charAt(j--) - '0');
            }
            sb.insert(0, sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) {
            sb.insert(0, carry);
        }
        return sb.toString();
    }
}

/*
Runtime: 2 ms, faster than 76.33% of Java online submissions for Add Binary.
Memory Usage: 39.2 MB, less than 48.84% of Java online submissions for Add Binary.
*/