class Solution {
public:
    bool checkDivisibility(int n) {
        vector<int> arr;
        int number = abs(n);
        while(number>0){
            arr.push_back(number%10);
            number/=10;
        }
        reverse(arr.begin(), arr.end());
        int sum = accumulate(arr.begin(), arr.end(), 0);
        int product = 1;
        for(int i = 0; i < arr.size(); i++){
            product = product * arr[i];
        }
        sum = sum + product;
        if(n % sum == 0 ){
            return true;
        }
        return false;
    }
};