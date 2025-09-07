class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> sol;
        int temp = -(n/2);
        int curr_sum;
        if(n%2 == 0){
            for(int j = 0; j < n; j++){
                sol.push_back(temp);
                curr_sum += temp;
                temp++; 
                if(temp == 0){
                    temp++;
                }
                if(curr_sum == 0){
                    break;
                }
                
            }

        }else{
            for(int j = 0; j < n; j++){
                sol.push_back(temp);
                curr_sum += temp;
                temp++;
                if(curr_sum == 0){
                    break;
                }
            }

        }
        return sol;
    }
};