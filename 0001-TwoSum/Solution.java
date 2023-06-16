import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remaining = target - nums[i];
            if (seen.containsKey(remaining)) {
                return new int[]{seen.get(remaining), i};
            }   
            seen.put(nums[i], i);
        }
        return new int[0];
    }
}

/*
 * Space Complexity: O(n)
 * Time Complexity: O(n)
 */