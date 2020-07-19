class Solution {
    private final int[] months = new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public int daysBetweenDates(String date1, String date2) {
        return Math.abs(from1971(date1) - from1971(date2));
    }

    // As in the hint
    private int from1971(String date) {
        String[] date_splitted = date.split("-");
        int year = Integer.parseInt(date_splitted[0]);
        int month = Integer.parseInt(date_splitted[1]);
        int day = Integer.parseInt(date_splitted[2]);

        int ret = day;

        for (int i = 1971; i < year; i++) {
            if (leapyear(i)) {
                ret += 366;
            }
            else {
                ret += 365;
            }
        }

        for (int i = 0; i < month-1; i++) {
            ret += months[i];
        }

        if (month > 2 && leapyear(year)) {
            ret += 1;
        }

        return ret;
    }

    private boolean leapyear(int year) {
        if (year % 400 == 0) {
            return true;
        }
        if (year % 4 == 0 && year % 100 != 0) {
            return true;
        }
        return false;
    }
} 

/*
Runtime: 2 ms, faster than 42.97% of Java online submissions for Number of Days Between Two Dates.
Memory Usage: 37.4 MB, less than 84.09% of Java online submissions for Number of Days Between Two Dates.
*/