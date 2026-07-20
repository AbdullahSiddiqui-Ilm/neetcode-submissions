class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int wanted = target - nums[i];
            if(hashmap.containsKey(wanted)){
                return new int[]{hashmap.get(wanted), i};
            }
            hashmap.put(nums[i], i);
        }
        return new int[]{};
    }
}
