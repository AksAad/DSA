class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int checker = s1.size();
        int i = 0;
        int j;
        sort(s1.begin(),s1.end());
        while (i + checker <= s2.size()){
            string temp = s2.substr(i,checker);
            sort(temp.begin(), temp.end());
            if(s1 == temp){
                return true;
            } 
            else{
                i++;
            }
        }
        return false;
    }
};