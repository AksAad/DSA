class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int count = 0;
        int flag = 0;
        int max_count = 0;
        for (int l = 0; l < nums.size(); l++){
            if (nums[l] != 1){
                flag++;
            }
            if (nums[l] == 1){
                count++;
            }
            for (int r = l+1; r< nums.size(); r++ ){
                if (flag < 2 && nums[r] == 1){
                    count ++;
                } 
                else if(nums[r] != 1 && flag < 2){
                    flag++;
                }
                max_count = max(max_count, count);
                if(flag >= 2){
                    break;
                }
            }
            flag = 0;
            count = 0;
        }
        if (max_count == 0){
            return max_count;
        }
        if (max_count == nums.size()){
            return max_count-1;
        }
        return max_count;
    }
};