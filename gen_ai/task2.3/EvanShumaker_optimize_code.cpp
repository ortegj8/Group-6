class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return n;  // Already valid if 2 or fewer elements
        
        int index = 2;  // Start from the third element
        for (int i = 2; i < n; ++i) {
            // If current element is not equal to the element two positions before,
            // it means it's allowed (either a new number or the second occurrence).
            if (nums[i] != nums[index - 2]) {
                nums[index++] = nums[i];
            }
        }
        return index;
    }
};
