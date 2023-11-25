// 以下是将给定的 Python 代码转换为对应的 Go 代码：
package main

import (
	"math/rand"
	"sort"
)

type Solution struct {
	prefixSum []int
} //定义结构体

// partition 选取最左边为 pivot
func checkSubarraySum(nums []int, k int) bool { // 
	n := len(nums) // @ := 自动类型
	sum := make([]int, n+1) // list
	for i := 1; i <= n; i++ {
		sum[i] = sum[i-1] + nums[i-1]
	}
	s := make((map[int]int)) // empty dict
	for i := 2; i <= n; i++ {
		s[sum[i-2]%k]++
		if s[sum[i]%k] > 0 {
			return true
		}
	return false
	}
}


func Constructor(w []int) Solution {
	n := len(w)
	prefixSum := make([]int, n)
	prefixSum[0] = w[0]

	// 前缀和
	for i := 1; i < n; i++ {
		prefixSum[i] = prefixSum[i-1] + w[i]
	}
	return Solution{prefixSum: prefixSum}
}

func (s *Solution) PickIndex() int {
	seed := rand.Intn(s.prefixSum[len(s.prefixSum)-1]) + 1
	index := sort.Search(len(s.prefixSum), func(i int) bool {
		return s.prefixSum[i] >= seed
	})
	return index
}
