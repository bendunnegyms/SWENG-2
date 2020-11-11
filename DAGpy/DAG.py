import copy

class DAG:
    DAG = {}
    reversed_dag = {}
    def __init__(self):
        self.DAG.clear()
    
    def add_edge(self, k1,k2):

        if k1 == k2:
            print("Edge not valid - loops on itself.")
            return False
        if k1 not in self.DAG and k2 not in self.DAG:
            if self.__disjoint_check(k1, k2):
                print("Disjointed.")
                return False
            
            self.DAG[k1] = [k2]
            self.DAG[k2] = []
            if not self.validate():
                del self.DAG[k1]
                del self.DAG[k2]
                print("Edge not valid. Loop created")
                return False
            else:
                # print(self.DAG)
                return True
        elif k1 in self.DAG and k2 not in self.DAG:
            
            self.DAG[k1].append(k2)
            self.DAG[k2] = []
            if not self.validate():
                self.DAG[k1].remove(k2)
                del self.DAG[k2]
                print("Edge not valid. Loop created")
                return False
            else:
                # print(self.DAG)
                return True
        elif k1 in self.DAG and k2 in self.DAG:
            
            self.DAG[k1].append(k2)
            if not self.validate():
                self.DAG[k1].remove(k2)
                print("Edge not valid. Loop created")
                return False
            else:
                # print(self.DAG)
                return True
        else:
            
            self.DAG[k1] = [k2]
            if not self.validate():
                del self.DAG[k1]
                print("Edge not valid. Loop created")
                return False
            else:
                # print(self.DAG)
                return True
                
        
    def __disjoint_check(self, k1, k2):
        # tests for if k1 or k2 arent in the DAG already, if DAG is not empty
        if k1 not in self.DAG and k2 not in self.DAG and len(self.DAG) > 0:
            return True
        else:
            return False


    def validate(self):
        vol_dag = copy.deepcopy(self.DAG)
        if len(self.DAG) == 0:
            return True
        else:
            while self.__check_for_empty(vol_dag):
                key = self.__get_empty_node(vol_dag)
                del vol_dag[key]
                for remaining_node in vol_dag:
                    if key in vol_dag[remaining_node]:
                        vol_dag[remaining_node].remove(key)

            if len(vol_dag) == 0:
                return True
            else: 
                return False


    def reverse_graph(self):
        reverse = {}
        dag2reverse = copy.deepcopy(self.DAG)

        for key in dag2reverse:
            reverse[key] = []

        for key in dag2reverse:
            for elem in dag2reverse[key]:
                reverse[elem].append(key)

        self.reversed_dag = copy.deepcopy(reverse)

    def LCA(self, k1, k2):   
        ancestors_k1 = self.get_all_ancestors(k1)
        ancestors_k2 = self.get_all_ancestors(k2)
        common_nodes = {}
        ancestors = []

        for k1 in ancestors_k1:
            if k1 in ancestors_k2:
                total_dist = ancestors_k1[k1] + ancestors_k2[k2]
                common_nodes[k1] = total_dist
    #  change to allow multiple lcas
        min_value = min(common_nodes.values())
        ancestors = [key for key, value in common_nodes.items() if value == min_value]

        return ancestors

                

    def get_all_ancestors(self, k):
        self.reverse_graph()
        print(self.reversed_dag)
        return self.__ancestors_recursive(k, {}, -1)  # key = distance, where key is the target and distance is distance from initial node to target


    def __ancestors_recursive(self, k, distances, distance):
        distance += 1
        if len(self.reversed_dag[k]) > 0:
            if k in distances and distance < distances[k]:
                distances[k] = distance
            elif k not in distances:
                distances[k] = distance
            for node in self.reversed_dag[k]:
                distances = self.__ancestors_recursive(node, distances, distance)
        else:
            if k in distances and distance < distances[k]:
                distances[k] = distance
            elif k not in distances:
                distances[k] = distance

        return distances



    def __check_for_empty(self, dag):
        for key in dag:
            if len(dag[key]) == 0:
                return True
        return False

    def __get_empty_node(self,dag):
        for key in dag:
            if len(dag[key])==0:
                return key


class TestDAGLCA:
    dag_main = DAG()

    def test_add_edge(self):
        assert self.dag_main.add_edge(0,0) == False # loop at 0-0
        assert self.dag_main.add_edge(0,1) == True # dag 0-1
        assert self.dag_main.add_edge(1,0) == False # loop at 0-1-0
        assert self.dag_main.add_edge(0,2) == True # fine
        assert self.dag_main.add_edge(0,10) == True # fine
        assert self.dag_main.add_edge(10,11) == True # fine
        assert self.dag_main.add_edge(1,3) == True # fine
        assert self.dag_main.add_edge(4,0) == True #
        assert self.dag_main.add_edge(2,4) == False # loop at 0-2-4-0

    def test_LCA(self):
        # single source
        lca_dag = DAG()
        lca_dag.add_edge("A", "E")
        lca_dag.add_edge("A", "B")
        lca_dag.add_edge("A", "C")
        lca_dag.add_edge("B", "D")
        lca_dag.add_edge("C", "D")
        lca_dag.add_edge("C", "E")
        assert lca_dag.LCA("D", "E") == ["C"]
        
        # double source, mutliple ancestors
        lca_dag_2 = DAG()
        lca_dag_2.add_edge("A", "C")
        lca_dag_2.add_edge("A", "D")
        lca_dag_2.add_edge("B", "C")
        lca_dag_2.add_edge("B", "D")
        assert lca_dag_2.LCA("C", "D") == ["A", "B"]
        
