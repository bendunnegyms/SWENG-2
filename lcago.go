package main

import "fmt"

type bin_node struct{
	key int
	left, right *bin_node
}

func findPath(root *bin_node, path []int, key int) bool {
	
	if root == nil {
		return false
	}

	path = append(path, root.key)

	if root.key == key{
		return true
	}

	if (root.left != nil && findPath(root.left, path, key)) || (root.right!= nil && findPath(root.right, path, key)){
		return true
	}
	return false
}


func findLCA(root *bin_node, k1, k2 int) (node_num int) {
	path_1 := make([]int, 1)
	path_2 := make([]int, 1)


	// if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
    //     return -1 
    
    // print(path1)
    // # Compare the paths to get the first different value 
    // i = 0 
    // while(i < len(path1) and i < len(path2)): 
    //     if path1[i] != path2[i]: 
    //         break
    //     i += 1
	// return path1[i-1]
	
	if !findPath(root, path_1, k1) || !findPath(root, path_2, k2){
		return -1
	}

	i := 0 
	for i < len(path_1) && i < len(path_2); {
		if path_1[i] != path_2[i] {
			break
		}

	}
	node_num = path_1[i-1]
	return
}

func main(){
	root := &bin_node{1}
	root.left = &bin_node{2}
	root.right = &bin_node{3}
	root.left.left = &bin_node{4}
	root.left.right = &bin_node{5}
	root.right.left = &bin_node{6}
	root.right.right = &bin_node{7}
	
	print("LCA(4, 5) = %d" %(findLCA(root, 4, 5,))) 
	print("LCA(4, 6) = %d" %(findLCA(root, 4, 6))) 
	print("LCA(3, 4) = %d" %(findLCA(root,3,4))) 
	print("LCA(2, 4) = %d" %(findLCA(root,2, 4))) 
}