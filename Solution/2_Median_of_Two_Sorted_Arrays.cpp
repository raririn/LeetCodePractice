class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size_1 = nums1.size();
        int size_2 = nums2.size();
        int arr[size_1 + size_2];
        int i = 0;
        int j = 0;
        int n = 0;
        double ret;
        while (i < size_1 && j < size_2){
            if (nums1[i] <= nums2[j]){
                arr[n] = nums1[i];
                i++;
            }
            else {
                arr[n] = nums2[j];
                j++;
            }
            n++;
        }
        while (i < size_1){
            arr[n] = nums1[i];
            i++;
            n++;
        }
        while (j < size_2){
            arr[n] = nums2[j];
            j++;
            n++;
        }
        if ((size_1 + size_2) % 2 == 0){
            ret = (arr[(size_1 + size_2)/2-1] + arr[(size_1 + size_2)/2]) / 2.0;
        }
        else{
            ret = arr[(size_1 + size_2 - 1)/2];
        }
        return ret;
    }
};