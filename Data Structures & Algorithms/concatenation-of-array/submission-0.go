func getConcatenation(nums []int) []int {
    var arrSize = len(nums)
	arr:= make([]int, arrSize*2)

	for i:=0; i<arrSize;i++ {
		arr[i] = nums[i]
		arr[i+arrSize] = nums[i]
	}

	return arr
}
