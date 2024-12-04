package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// extractAndMultiply finds all matches of mul(x,y) pattern and returns their products
func extractAndMultiply(text string, pattern *regexp.Regexp) []int {
	matches := pattern.FindAllStringSubmatch(text, -1)
	results := make([]int, 0, len(matches))

	for _, match := range matches {
		num1, err := strconv.Atoi(match[1])
		if err != nil {
			continue
		}
		num2, err := strconv.Atoi(match[2])
		if err != nil {
			continue
		}
		results = append(results, num1*num2)
	}
	return results
}

func main() {
	// Read input file
	content, err := os.ReadFile("input")
	if err != nil {
		log.Fatal(err)
	}
	text := string(content)

	// Compile regex pattern
	pattern := regexp.MustCompile(`mul\((\d+),(\d+)\)`)

	// Part 1: Find all matches and sum their products
	products := extractAndMultiply(text, pattern)
	sum1 := 0
	for _, p := range products {
		sum1 += p
	}
	fmt.Println("Sum of all multiplications:", sum1)

	// Part 2: Process sections between do() and don
	sum2 := 0
	sections := strings.Split(text, "do()")

	// Skip first section (before first do())
	for _, section := range sections {
		// Split on 'don' and take everything before it
		parts := strings.Split(section, "don")
		if len(parts) > 0 {
			section = parts[0]
			products := extractAndMultiply(section, pattern)
			for _, p := range products {
				sum2 += p
			}
		}
	}

	fmt.Println("Sum of multiplications after do():", sum2)
}
