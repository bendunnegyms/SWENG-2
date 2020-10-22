package main

import "testing"

func TestFindLCA(t *testing.T){
	root := &bin_node{key:1}
	root.left = &bin_node{key:2}
	root.right = &bin_node{key:3}
	root.right.left = &bin_node{key:4}
	root.right.right = &bin_node{key:5}
	root.right.left.right = &bin_node{key:6}
	root.left.left = &bin_node{key:7}
	root.left.left.left = &bin_node{key:8}
	root.right.right.right = &bin_node{key:9}
	root.right.left.left = &bin_node{key:10}
	root.left.left.left.left = &bin_node{key:11}
		

	lca_4_5 := findLCA(root, 4, 5)
	lca_4_6 := findLCA(root, 4, 6)
	lca_3_4 := findLCA(root, 3, 4)
	lca_2_2 := findLCA(root, 2, 2)
	lca_6_5 := findLCA(root, 6, 5)

	lca_12_10 := findLCA(root, 12, 10)

	lca_0_0 := findLCA(root, 0, 0)

	t.Log("LCA(4,5): ", lca_4_5)
	if lca_4_5 != 3 {
		t.Errorf("LCA(4,5) should be 3, got %d", lca_4_5)
	}
	t.Log("LCA(4,6): ", lca_4_6)
	if lca_4_6 != 4 {
		t.Errorf("LCA(4,6) should be 4, got %d", lca_4_6)
	}
	t.Log("LCA(3,4): ", lca_3_4)
	if lca_3_4 != 3 {
		t.Errorf("LCA(3,4) should be 3, got %d", lca_3_4)
	}
	t.Log("LCA(2,2): ", lca_2_2)
	if lca_2_2 != 2 {
		t.Errorf("LCA(2,4) should be 2, got %d", lca_2_2)
	}
	t.Log("LCA(6,5): ", lca_6_5)
	if lca_6_5 != 3 {
		t.Errorf("LCA(2,4) should be 3, got %d", lca_6_5)
	}
	t.Log("LCA(12,10): ", lca_12_10)
	if lca_12_10 != -1 {
		t.Errorf("LCA(12,10) should be -1, got %d", lca_12_10)
	}
	t.Log("LCA(0,0): ", lca_0_0)
	if lca_0_0 != -1 {
		t.Errorf("LCA(0,0) should be 0, got %d", lca_0_0)
	}
	
}

