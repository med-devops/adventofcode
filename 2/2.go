package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func isAscending(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		diff := nums[i+1] - nums[i]
		if diff <= 0 || diff > 3 {
			return false
		}
	}
	return true
}

func isDescending(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		diff := nums[i] - nums[i+1]
		if diff <= 0 || diff > 3 {
			return false
		}
	}
	return true
}

func main() {
	sum := 0
	sum2 := 0
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	defer file.Close()
	secondaryRun := [][]int{}
	for scanner.Scan() {
		strNumbers := strings.Fields(scanner.Text())
		numbers := make([]int, len(strNumbers))

		for i, str := range strNumbers {
			num, err := strconv.Atoi(str)
			if err != nil {
				log.Fatal(err)
			}
			numbers[i] = num
		}

		if isAscending(numbers) || isDescending(numbers) {
			sum++
		} else {
			secondaryRun = append(secondaryRun, numbers)
		}

		for _, nums := range secondaryRun {
			for i := range nums {
				// Create a new slice without element at index i
				withoutI := make([]int, 0, len(nums)-1)
				withoutI = append(withoutI, nums[:i]...)
				withoutI = append(withoutI, nums[i+1:]...)

				if isAscending(withoutI) || isDescending(withoutI) {
					sum2++
					break
				}
			}
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(sum)
	fmt.Println(sum + sum2)
}
