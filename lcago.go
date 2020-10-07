package main

import "fmt"

type bin_node struct{
	key int
	left, right *bin_node
}

func findPath(root *bin_node, path *[]int, key int) bool {
	if root == nil {
		return false
	}

	*path = append(*path, root.key)

	if root.key == key{
		return true
	}

	if (root.left != nil && findPath(root.left, path, key)) || (root.right!= nil && findPath(root.right, path, key)){
		return true
	}

	if len(*path) > 0 {
		*path = (*path)[:len(*path)-1]
	}

	return false
}


func findLCA(root *bin_node, k1, k2 int) int {
	path_1 := make([]int, 0)
	path_2 := make([]int, 0)

	if !findPath(root, &path_1, k1) || !findPath(root, &path_2, k2){
		fmt.Println("here4")
		return -1
	}

	i := 0 
	for i < len(path_1) && i < len(path_2) {
		if path_1[i] != path_2[i] {
			break
		}
		i += 1
	}
	node_num := path_1[i-1]
	return node_num
}

func main(){
	root := &bin_node{key:1}
	root.left = &bin_node{key:2}
	root.right = &bin_node{key:3}
	root.left.left = &bin_node{key:4}
	root.left.right = &bin_node{key:5}
	root.right.left = &bin_node{key:6}
	root.right.right = &bin_node{key:7}
	lca_4_5 := findLCA(root, 4, 5)
	lca_4_6 := findLCA(root, 4, 6)
	lca_3_4 := findLCA(root, 3, 4)
	lca_2_4 := findLCA(root, 2, 4)
	
	fmt.Println("LCA(4,5) = " + fmt.Sprint(lca_4_5))
	fmt.Println("LCA(4,6) = " + fmt.Sprint(lca_4_6))
	fmt.Println("LCA(3,4) = " + fmt.Sprint(lca_3_4))
	fmt.Println("LCA(2,4) = " + fmt.Sprint(lca_2_4))
	
}