from flask import render_template, Blueprint, request
from pyvis.network import Network

coverage_route = Blueprint('coverage',__name__, url_prefix='/public/coverage')

MAX_NODES = 40
MAX_EDGES = 400

@coverage_route.route('/')
def coverage():
    nodes = '[{"id": 0, "label": "0", "shape": "dot", "title": "0"}, {"id": 1, "label": 1, "shape": "dot", "title": "1"}, {"id": 2, "label": 2, "shape": "dot", "title": "2"}, {"id": 3, "label": 3, "shape": "dot", "title": "3"}, {"id": 4, "label": 4, "shape": "dot", "title": "4"}, {"id": 5, "label": 5, "shape": "dot", "title": "5"}, {"id": 6, "label": 6, "shape": "dot", "title": "6"}, {"id": 7, "label": 7, "shape": "dot", "title": "7"}]'
    edges = '[{"from": 0, "to": 1}, {"from": 0, "to": 2}, {"from": 0, "to": 3}, {"from": 0, "to": 4}, {"from": 0, "to": 5}, {"from": 0, "to": 6}, {"from": 0, "to": 7}, {"from": 1, "to": 2}, {"from": 1, "to": 3}, {"from": 1, "to": 4}, {"from": 1, "to": 5}, {"from": 1, "to": 6}, {"from": 1, "to": 7}, {"from": 2, "to": 3}, {"from": 2, "to": 4}, {"from": 2, "to": 5}, {"from": 2, "to": 6}, {"from": 2, "to": 7}, {"from": 3, "to": 4}, {"from": 3, "to": 5}, {"from": 3, "to": 6}, {"from": 3, "to": 7}, {"from": 4, "to": 5}, {"from": 4, "to": 6}, {"from": 4, "to": 7}, {"from": 5, "to": 6}, {"from": 5, "to": 7}, {"from": 6, "to": 7}]'
    return render_template('public/graph-coverage-card.html', nodes=nodes, edges=edges)


@coverage_route.route('/random/')
def random_coverage():
    from  app.models.graph import Node, Edge
    import networkx as nx
    nxg = nx.complete_graph(10)
    nodes = [ Node(n) for n in nxg.nodes ]
    edges = [ Edge(e[0], e[1]) for e in nxg.edges ]

    #nodes = '[{"id": 0, "label": 0, "shape": "dot", "title": "0"}, {"id": 1, "label": 1, "shape": "dot", "title": "1"}, {"id": 2, "label": 2, "shape": "dot", "title": "2"}, {"id": 3, "label": 3, "shape": "dot", "title": "3"}, {"id": 4, "label": 4, "shape": "dot", "title": "4"}, {"id": 5, "label": 5, "shape": "dot", "title": "5"}, {"id": 6, "label": 6, "shape": "dot", "title": "6"}, {"id": 7, "label": 7, "shape": "dot", "title": "7"}]'
    #edges = '[{"from": 0, "to": 1}, {"from": 0, "to": 2}, {"from": 0, "to": 3}, {"from": 0, "to": 4}, {"from": 0, "to": 5}, {"from": 0, "to": 6}, {"from": 0, "to": 7}, {"from": 1, "to": 2}, {"from": 1, "to": 3}, {"from": 1, "to": 4}, {"from": 1, "to": 5}, {"from": 1, "to": 6}, {"from": 1, "to": 7}, {"from": 2, "to": 3}, {"from": 2, "to": 4}, {"from": 2, "to": 5}, {"from": 2, "to": 6}, {"from": 2, "to": 7}, {"from": 3, "to": 4}, {"from": 3, "to": 5}, {"from": 3, "to": 6}, {"from": 3, "to": 7}, {"from": 4, "to": 5}, {"from": 4, "to": 6}, {"from": 4, "to": 7}, {"from": 5, "to": 6}, {"from": 5, "to": 7}, {"from": 6, "to": 7}]'
    return render_template('public/graph-coverage-card.html', nodes=nodes, edges=edges)


