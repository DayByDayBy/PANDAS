package main

import "fmt"

func main() {
	pairs := 690
	childrenPerPair := 5
	infantMortalityRate := 0.4999
	generations := 0
	population := pairs * childrenPerPair

	for population < 7000000000 {
		newBirths := pairs * childrenPerPair
		population += newBirths
		deathsDueToMortality := int(float64(population) * infantMortalityRate)
		population -= deathsDueToMortality
		pairs = population / childrenPerPair
		generations++
	}

	fmt.Printf("Population reached 7 billion in approximately %d generations.\n", generations)
}
