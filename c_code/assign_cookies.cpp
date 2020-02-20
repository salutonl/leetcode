#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
class Solution
{
public:
    int findContentChildren(vector<int> &g, vector<int> &s)
    {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int res = 0;
        int i, j;
        for(i = 0, j = 0; i < s.size() &&j < g.size();){
            if(s[i] >= g[j]){
                res += 1;
                i++;
                j++;
            }else{
                i++;
            }
        }
        return res;
    }
};

int main(){
    cout << "Hello world";
    return 0;
}