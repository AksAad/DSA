class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        //write a binary search progam which returns index if target == found else returns where it shoulf be
        int i = 0;
        int l = 0;
        int r = nums.size() - 1;
        int curr_ind = (r-l) / 2;
        int position = 0;
        if (target > nums.back()){
            return nums.size();
        }
        for(i = 0; i < nums.size() ; i++){
            if (target > nums[curr_ind]){
                l = curr_ind;
                curr_ind += (int)(r-l) / 2;
                position = curr_ind + 1;
            }
            else if (target < nums[curr_ind]){
                r = curr_ind;
                curr_ind = (int)(r-l)/2;
                position = curr_ind;
            }
            else if (target == nums[curr_ind]){
                return curr_ind;
            }
        }
        return position;
    }
};