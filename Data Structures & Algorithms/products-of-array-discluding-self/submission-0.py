class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		size = len(nums)
		currProd = 1
		countZero = 0

		for n in nums:
			if n == 0:
				countZero += 1
			else:
				currProd *= n

		if countZero > 1:
			return size * [0]

		ret = size * [0]
		for idx, num in enumerate(nums):
			print(f"idx: {idx} and num: {num}")
			if countZero:
				ret[idx] = 0 if num else currProd
			else:
				ret[idx] = currProd // nums[idx]
		return ret