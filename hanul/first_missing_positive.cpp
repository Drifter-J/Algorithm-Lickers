class Solution {
public:
	int firstMissingPositive(vector<int>& nums) {
		int positiveIdx = 0;

		int length = nums.size();
		for (int i = 0; i < length; ++i)
		{
			if (nums[i] > 0)
			{
				nums[positiveIdx++] = nums[i];
			}
		}

		int max = positiveIdx;
		for (int i = 0; i < positiveIdx; ++i)
		{
			if (abs(nums[i]) - 1 < positiveIdx && nums[abs(nums[i]) - 1] > 0)
			{
				nums[abs(nums[i]) - 1] *= -1;
			}
		}

		for (int i = 0; i < positiveIdx; ++i)
		{
			if (nums[i] > 0)
			{
				return i + 1;
			}
		}

		return positiveIdx + 1;
	}
};