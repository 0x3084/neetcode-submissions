
#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {

        for (int i = 0; i < nums.size(); i++) {


            for (int m = i + 1; m < nums.size(); m++) {

                if (nums[i] + nums[m] == target) {
                    return { i, m };
                  
                } 
            }

        }
        return {};

    
    }
    



};
