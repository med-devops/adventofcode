package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// Read the input file
	file, err := os.Open("input")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Pre-allocate slices with initial capacity
	l1 := make([]int, 0, 1000)
	l2 := make([]int, 0, 1000)
	
	scanner := bufio.NewScanner(file)
	
	// Read and parse the input
	for scanner.Scan() {
		numbers := strings.Fields(scanner.Text())
		if len(numbers) >= 2 {
			num1, _ := strconv.Atoi(numbers[0])
			num2, _ := strconv.Atoi(numbers[1])
			l1 = append(l1, num1)
			l2 = append(l2, num2)
		}
	}

	// Calculate sum2 using a map for counting
	sum2 := 0
	countMap := make(map[int]int)
	for _, v2 := range l2 {
		countMap[v2]++
	}
	for _, v1 := range l1 {
		if count, exists := countMap[v1]; exists {
			sum2 += count * v1
		}
	}

	// Calculate sum using sorting instead of finding min each time
	
	sort.Ints(l1)
	sort.Ints(l2)

	sum := 0
	for i := 0; i < len(l1); i++ {
		sum += abs(l1[i] - l2[i])
	}

	fmt.Println(sum)
	fmt.Println(sum2)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
