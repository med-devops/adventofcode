package main

import (
    "fmt"
    "os"
    "log"
    "io/ioutil"
)

func main() {
    file, err := os.Open("input")
    defer file.Close()
    if err != nil {
        log.Fatal(err)
    }
    b, err := io.ReadAll(file)
    
}