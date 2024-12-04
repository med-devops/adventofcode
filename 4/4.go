package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

const (
	word1 = "XMAS"
	word2 = "SAMX"
)

// checkWord checks for progressive character matches in the string
func checkWord(str string) int {
	count := 0
	i1, i2 := 0, 0

	for _, ch := range str {
		// Check for word1
		if byte(ch) == word1[i1] {
			i1++
			if i1 == len(word1) {
				count++
				i1 = 0
			}
		}
		// Check for word2
		if byte(ch) == word2[i2] {
			i2++
			if i2 == len(word2) {
				count++
				i2 = 0
			}
		}
	}
	return count
}

// checkLines checks all strings in the slice
func checkLines(lines []string) int {
	count := 0
	for _, line := range lines {
		count += checkWord(line)
	}
	return count
}

// getVerticalLines extracts vertical lines from the input
func getVerticalLines(lines []string) []string {
	if len(lines) == 0 {
		return nil
	}

	width := len(lines[0])
	verticals := make([]string, width)

	for i := 0; i < width; i++ {
		var vertical strings.Builder
		for _, line := range lines {
			if i < len(line) {
				vertical.WriteByte(line[i])
			}
		}
		verticals[i] = vertical.String()
	}

	return verticals
}

// getDiagonals extracts diagonal lines from the input
func getDiagonals(lines []string) []string {
	if len(lines) == 0 {
		return nil
	}

	height := len(lines)
	width := len(lines[0])
	diagonals := make([]string, 0)

	// Main diagonal and parallels above
	for startCol := 0; startCol < width; startCol++ {
		var diagonal strings.Builder
		row, col := 0, startCol
		for row < height && col < width {
			diagonal.WriteByte(lines[row][col])
			row++
			col++
		}
		if diagonal.Len() > 0 {
			diagonals = append(diagonals, diagonal.String())
		}
	}

	// Main diagonal and parallels below
	for startRow := 1; startRow < height; startRow++ {
		var diagonal strings.Builder
		row, col := startRow, 0
		for row < height && col < width {
			diagonal.WriteByte(lines[row][col])
			row++
			col++
		}
		if diagonal.Len() > 0 {
			diagonals = append(diagonals, diagonal.String())
		}
	}

	// Anti-diagonal and parallels above
	for startCol := 0; startCol < width; startCol++ {
		var diagonal strings.Builder
		row, col := 0, startCol
		for row < height && col >= 0 {
			diagonal.WriteByte(lines[row][col])
			row++
			col--
		}
		if diagonal.Len() > 0 {
			diagonals = append(diagonals, diagonal.String())
		}
	}

	// Anti-diagonal and parallels below
	for startRow := 1; startRow < height; startRow++ {
		var diagonal strings.Builder
		row, col := startRow, width-1
		for row < height && col >= 0 {
			diagonal.WriteByte(lines[row][col])
			row++
			col--
		}
		if diagonal.Len() > 0 {
			diagonals = append(diagonals, diagonal.String())
		}
	}

	return diagonals
}

func main() {
	// Read input file
	content, err := os.ReadFile("input")
	if err != nil {
		log.Fatal(err)
	}

	// Split into lines and remove any empty lines
	lines := make([]string, 0)
	for _, line := range strings.Split(string(content), "\n") {
		line = strings.TrimSpace(line)
		if line != "" {
			lines = append(lines, line)
		}
	}

	total := 0

	// Check horizontal lines
	total += checkLines(lines)

	// Check vertical lines
	verticals := getVerticalLines(lines)
	total += checkLines(verticals)

	// Check diagonal lines
	diagonals := getDiagonals(lines)
	total += checkLines(diagonals)

	fmt.Println(total)
}
