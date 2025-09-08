class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        vector<int> sol;
        vector <int> th;
        for (int i = 1; i <= n; i++) {
            int a = i;
            bool ok = true;
            while (a > 0) {
                if (a % 10 == 0) {  
                    ok = false;
                    break;
                }
                a /= 10;
            }
            if (ok) sol.push_back(i);
        }
        int target;
        for(int i = 0; i <= sol.size(); i++){
            target = n - sol[i];
            if(find(sol.begin(),sol.end(),target) != sol.end()){
                th.push_back(target);
                th.push_back(sol[i]);
                break;
            }
        }
        return th;
    }
};