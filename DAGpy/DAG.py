class DAG:
    DAG = {}

    def __init__(self):
        self.DAG.clear()
    
    def add_node(self, key):
        if key in self.DAG:
            print("Fail. Key in DAG.")
            return

        self.DAG[key] = []
        if not self.validate:
            del self.DAG[key]
    

    def validate(self, key, path = None):
        vol_dag = self.DAG.copy()
        if not path:
            path = []

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
                

    # def reverse_graph(self):
    #     reverse = {}
    #     dag2reverse = self.DAG.copy()

    #     while self.__check_for_empty(dag2reverse):
    #         key = self.__get_empty_node
    #         del dag2reverse[key]
    #         reverse[key] = []
    #         for remaining_node in dag2reverse:
    #             if key in dag2reverse[remaining_node]:
    #                 reverse[key].append(remaining_node)

    #     return reverse
    
    def __check_for_empty(self, dag):
        for key in dag:
            if len(dag[key]) == 0:
                return True
        return False

    def __get_empty_node(self,dag):
        for key in dag:
            if len(dag[key])==0:
                return key

    def add_edge(self):
        return