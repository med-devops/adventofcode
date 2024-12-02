package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func ascend(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		diff := nums[i+1] - nums[i]
		if nums[i] >= nums[i+1] || diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func descend(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		diff := nums[i] - nums[i+1]
		if nums[i] <= nums[i+1] || diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	
	sum := 0
	sum2 := 0
	secondrun := make([][]int, 0)

	// First pass - check original sequences
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		nums := make([]int, len(fields))
		
		for i, field := range fields {
			num, err := strconv.Atoi(field)
			if err != nil {
				log.Fatal(err)
			}
			nums[i] = num
		}

		if ascend(nums) || descend(nums) {
			sum++
		} else {
			secondrun = append(secondrun, nums)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// Second pass - try removing one number
	for _, seq := range secondrun {
		for i := range seq {
			// Create new sequence without element at index i
			withoutI := make([]int, len(seq)-1)
			copy(withoutI, seq[:i])
			copy(withoutI[i:], seq[i+1:])

			if ascend(withoutI) || descend(withoutI) {
				sum2++
				break
			}
		}
	}

	fmt.Println(sum)
	fmt.Println(sum + sum2)
}
