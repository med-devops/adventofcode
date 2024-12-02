package main

import (
    "fmt"
    "os"
    "log"
)

func main() {
    file, err := os.Open("input")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Print(file)
}