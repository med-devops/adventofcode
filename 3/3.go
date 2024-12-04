package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var inputContent string

func main() {
	content, err := os.ReadFile("input")
	if err != nil {
		log.Fatal(err)
	}
	sum := 0
	inputContent = string(content)
	r := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	matches := r.FindAllStringSubmatch(inputContent, -1)
	for _, match := range matches {
		num1, err := strconv.Atoi(match[1])
		if err != nil {
			log.Fatal(err)
		}
		num2, err := strconv.Atoi(match[2])
		if err != nil {
			log.Fatal(err)
		}
		sum += num1 * num2
	}
	fmt.Println(sum)

	sum2 := 0
	sections := strings.Split(inputContent, "do()")
	for _, section := range sections[1:] {
		donParts := strings.Split(section, "don")
		if len(donParts) > 0 {
			matches2 := r.FindAllStringSubmatch(donParts[0], -1)
			for _, match := range matches2 {
				num1, err := strconv.Atoi(match[1])
				if err != nil {
					log.Fatal(err)
				}
				num2, err := strconv.Atoi(match[2])
				if err != nil {
					log.Fatal(err)
				}
				sum2 += num1 * num2
			}
		}
	}
	fmt.Println(sum2)
}
