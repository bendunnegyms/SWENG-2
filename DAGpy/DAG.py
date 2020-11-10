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
        if not path:
            path = []

        if len(self.DAG[key]) == 0:
            return True
        else:
            return False
        # test for loop

    def reverse_graph(self):
        # reverse graph to facilitate 
        return
    
    def add_edge(self):
        return