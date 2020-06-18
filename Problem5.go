/*
Problem 5: Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the number
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

Note: This solution is the Go version of what has already been done in
Python as a way to test language performance differences. The Python
version takes at least 8 seconds to run, whereas the Go version
completes in less than a second.
*/
package main

import (
	"fmt"
	"time"
)

// This simple function returns n!

func factorial(n int) int {
	product := 1
	for i := 1; i < n+1; i++ {
		product *= i
	}
	return product
}

// This function checks if x is divisible by all naturals up to n.

func isDivisible(x int, n int) bool {
	for i := 1; i < n+1; i++ {
		if x%i == 0 {
			// Do nothing.
		} else {
			return false
		}
	}
	return true
}

// This function returns the smallest number divisible by all naturals
// to n, with some steps being saved on by going in steps of n.

func smallestNumberDivisible(n int) int {
	for i := n; i < factorial(n)+1; i += n {
		if isDivisible(i, n) == true {
			return i
		}
	}
	return n
}

// Prints the solution and ensures that it completes within 1 minute.

func main() {
	start := time.Now()
	fmt.Println(smallestNumberDivisible(20))
	stop := time.Now()
	fmt.Println("Time:", stop.Sub(start))
}
