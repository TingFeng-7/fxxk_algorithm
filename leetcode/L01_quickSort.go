// 以下是将给定的 Python 代码转换为对应的 Go 代码：
package main

import (
	"math/rand"
)

// partition 选取最左边为 pivot
func partition(arr []int, low int, high int) int { // 
	pivot, left, right := arr[low], low, high // @ := 自动类型
	for left < right {
		for left < right && arr[right] >= pivot {
			right--
		}
		arr[left] = arr[right]
		for left < right && arr[left] <= pivot {
			left++
		}
		arr[right] = arr[left]
	}
	arr[left] = pivot
	return left
}

// randomPartition 随机选择 pivot
func randomPartition(arr []int, low int, high int) int {
	pivotIdx := rand.Intn(high-low+1) + low
	arr[low], arr[pivotIdx] = arr[pivotIdx], arr[low]
	return partition(arr, low, high)
}

// topKSplit 返回第 K 个元素
func topKSplit(arr []int, low int, high int, k int) int {
	p := randomPartition(arr, low, high)
	if p == k-1 {
		return arr[p]
	} else if p < k-1 {
		return topKSplit(arr, p+1, high, k)
	}
	return topKSplit(arr, low, p-1, k)
}

// randomizedQuicksort 随机快排
func randomizedQuicksort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	pivotIdx := rand.Intn(len(arr))
	pivot := arr[pivotIdx]
	arr[pivotIdx], arr[len(arr)-1] = arr[len(arr)-1], arr[pivotIdx]
	var left, middle, right []int
	for _, x := range arr[:len(arr)-1] {
		switch {
		case x < pivot:
			left = append(left, x)
		case x > pivot:
			right = append(right, x)
		default:
			middle = append(middle, x)
		}
	}
	return append(append(randomizedQuicksort(left), middle...), randomizedQuicksort(right)...)
}

// search 搜索旋转排序数组
func search(nums []int, target int) int {
	if len(nums) < 1 {
		return -1
	}
	l, r := 0, len(nums)-1
	for l <= r {
		mid := (l + r) / 2
		if nums[mid] == target {
			return mid
		}
		if nums[l] <= nums[mid] {
			if nums[l] <= target && target < nums[mid] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		} else {
			if nums[mid] < target && target <= nums[len(nums)-1] {
				l = mid + 1
			} else {
				r = mid - 1
			}
		}
	}
	return -1
}

// findKthLargest 第K大元素
func findKthLargest(nums []int, k int) int {
	n := len(nums)
	return topKSplit(nums, 0, n-1, n-k+1)
}

func main() {
	// 测试代码可以在这里添加
}
