import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self._view.update_page()
        self._model.creaGrafo(self._view._txtAnno.value)
        self._view._txt_result.controls.append(ft.Text('Grafo correttamente creato'))
        self._view._txt_result.controls.append(ft.Text(f'Il Grafo contiene {self._model.getNumNodes()} nodi'))
        self._view._txt_result.controls.append(ft.Text(f'Il Grafo contiene {self._model.getNumEdges()} archi'))
        self._view._txt_result.controls.append(ft.Text(f'Il Grafo ha  {self._model.getConnessa()} componenti connesse'))
        gradi_nodi = self._model.grafo.degree()
        for nodo, grado in gradi_nodi:
            self._view._txt_result.controls.append(ft.Text(f"Il grado del nodo {nodo} è {grado}"))
        self.fillDD()
        self._view._btnRaggiungibili.disabled= False
        self._view.update_page()


    def fillDD(self):
        for paese in self._model.paesiAnno:
            self._view.dd.options.append(ft.dropdown.Option(key=paese.cCode, text=paese.stateNme))
        self._view.update_page()

    def handleConfinanti(self,e):
        self._view._txt_result.controls.clear()
        for n in self._model.connessi(self._view.dd.value):
            self._view._txt_result.controls.append(ft.Text(f" {n} "))
        self._view.update_page()
