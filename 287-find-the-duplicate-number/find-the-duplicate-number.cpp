class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        vector<int> numidx(nums.size() + 1, 0);
        int i = 0;
        for (i = 0 ; i < nums.size(); i++){
            if (numidx[nums[i]] == 0){
                numidx[nums[i]] = 1;
            }else{
                return nums[i];
            }
        }
        return -1;
    }
};