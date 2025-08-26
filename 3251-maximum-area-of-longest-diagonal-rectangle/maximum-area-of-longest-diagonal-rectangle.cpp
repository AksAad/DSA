class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        int curr_max =0;
        int curr_diag = 0;
        int max_diag = 0;
        int tot_max= 0; 
        for(int i = 0; i< dimensions.size(); i++){
            curr_diag = dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1];
            if (curr_diag > max_diag){
                curr_max = dimensions[i][0] * dimensions[i][1];
                max_diag = curr_diag;
                tot_max = curr_max;
            } else if (curr_diag == max_diag){
                curr_max = dimensions[i][0] * dimensions[i][1];
                if (curr_max > tot_max){
                    tot_max = curr_max;
                }else{
                    continue;
                }
            }
        }
        return tot_max;
    }
};