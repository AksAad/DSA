class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        long long windowSum = accumulate(nums.begin(), nums.begin() + k, 0LL);
        long long maxSum = windowSum;
        for (int i = k; i < nums.size(); i++) {
            windowSum += nums[i] - nums[i - k]; 
            maxSum = max(maxSum, windowSum);
        }  
        return (double)maxSum / k;
    }
};