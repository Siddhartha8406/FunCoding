package main
import "fmt"


func mapTo(vari, in1, in2, out1, out2 int)int{
	minIn := 0.9
	fmt.Println(minIn)
	minOut := (out2-out1)/100
	fmt.Println(minOut)

	mapped := vari/minIn
	mapped = mapped * minOut
	fmt.Println(mapped)
	return 0
}

func main()  {
	fmt.Println("This is a test")
	mapTo(30, 10, 100, 100, 1000)
}