class DAG:
    DAG = {}
    source = None
    reversed_dag = {}
    def __init__(self):
        self.DAG.clear()
    
    def add_edge(self, k1,k2):
        if len(self.DAG) == 0:
            self.source = k1

        if k1 == k2:
            print("Edge not valid - loops on itself.")
            return False
        if k1 not in self.DAG:
            if self.__disjoint_check(k1, k2):
                print("Disjointed.")
                return False
            
            self.DAG[k1] = [k2]
            self.DAG[k2] = []
            if not self.__validate:
                del self.DAG[k1]
                del self.DAG[k2]
                print("Edge not valid. Loop created")
                return False
            else:
                return True
        else:
            if self.__disjoint_check(k1, k2):
                print("Disjointed.")
                return False
            
            self.DAG[k1].append(k2)
            self.DAG[k2] = []
            if not self.__validate:
                self.DAG[k1].remove(k2)
                del self.DAG[k2]
                print("Edge not valid. Loop created")
                return False
            else:
                return True
        
    def __disjoint_check(self, k1, k2):
        # tests for if k1 or k2 arent in the DAG already, if DAG is not empty
        if k1 not in self.DAG and k2 not in self.DAG and len(self.DAG) > 0:
            return True
        else:
            return False


    def __validate(self, key):
        vol_dag = self.DAG.copy()

        if len(self.DAG[key]) == 0:
            return True
        else:
            while self.__check_for_empty(vol_dag):
                key = self.__get_empty_node
                del vol_dag[key]
                for remaining_node in vol_dag:
                    if key in vol_dag[remaining_node]:
                        del vol_dag[key]

            if len(vol_dag) == 0:
                return True
            else: 
                return False


    def reverse_graph(self):
        reverse = {}
        dag2reverse = self.DAG.copy()

        while self.__check_for_empty(dag2reverse):
            key = self.__get_empty_node
            del dag2reverse[key]
            reverse[key] = []
            for remaining_node in dag2reverse:
                if key in dag2reverse[remaining_node]:
                    reverse[key].append(remaining_node)
        self.reversed_dag = reverse

    def LCA(self, k1, k2):   
        ancestors_k1 = self.get_all_ancestors(k1)
        ancestors_k2 = self.get_all_ancestors(k2)
        common_nodes = {}

        for k1 in ancestors_k1:
            if k1 in ancestors_k2:
                total_dist = ancestors_k1[k1] + ancestors_k2[k2]
                common_nodes[k1] = total_dist

        return min(common_nodes, key=common_nodes.get)

                

    def get_all_ancestors(self, k):
        self.reverse_graph()
        return self.__ancestors_recursive(k, {}, -1)  # key = distance, where key is the target and distance is distance from initial node to target


    def __ancestors_recursive(self, k, distances, distance):
        distance += 1
        if len(self.reversed_dag[k]) > 0:
            if k in distances and distance < distances[k]:
                distances[k] = distance
            elif k not in distances:
                distances[k] = distance
            for node in self.reversed_dag[k]:
                distances = self.__ancestors_recursive(self, node, distances)
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
        assert self.dag_main.add_edge(0,0) == False
        assert self.dag_main.add_edge(0,1) == True
        assert self.dag_main.add_edge(1,0) == False
        