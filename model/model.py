import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.listaPaesi = DAO.getAllCountries()
        self.idMap = {}
        for v in self.listaPaesi:
            self.idMap[v.cCode] = v

    def creaGrafo(self, anno):
        self.paesiAnno =DAO.getCountriesAnno(anno)
        self.grafo = nx.Graph()
        self.grafo.add_nodes_from(self.paesiAnno)
        self.aggiungiArchi(anno)
    def aggiungiArchi(self,anno):
        self.grafo.clear_edges()
        archi = DAO.getEdges(anno)
        for a in archi:
            self.grafo.add_edge(self.idMap[a.stato1],self.idMap[a.stato2])

    def getConnessa(self):
        n = nx.number_connected_components(self.grafo)
        return n
    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def connessi(self, nodoInt):
        # modo 3: conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self.grafo, self.idMap[int(nodoInt)])
        print(f'connessi: {len(tree.nodes)}')
        return tree.nodes


