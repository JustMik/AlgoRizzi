
// This method is responsible for drawing the graph, returns the drawn network

function drawGraph() {
    // initialize global variables.

    // parsing and collecting nodes and edges from the python
        nodes = new vis.DataSet([{"id": 0, "label": 0, "shape": "dot", "title": "0"}, {"id": 1, "label": 1, "shape": "dot", "title": "1"}, {"id": 2, "label": 2, "shape": "dot", "title": "2"}, {"id": 3, "label": 3, "shape": "dot", "title": "3"}, {"id": 4, "label": 4, "shape": "dot", "title": "4"}]);
        edges = new vis.DataSet([{"from": 0, "to": 1}, {"from": 0, "to": 2}, {"from": 0, "to": 3}, {"from": 0, "to": 4}, {"from": 1, "to": 2}, {"from": 1, "to": 3}, {"from": 1, "to": 4}, {"from": 2, "to": 3}, {"from": 2, "to": 4}, {"from": 3, "to": 4}]);

        // adding nodes and edges to the graph
        data = {nodes: nodes, edges: edges};

    var network;
    var container;
    var options;

    var container = document.getElementById('mynetwork');

    // parsing and collecting nodes and edges from the python
    nodes = new vis.DataSet( nodes );
    edges = new vis.DataSet( edges );

    // adding nodes and edges to the graph
    data = {nodes: nodes, edges: edges};

    var options = {
        "configure": {
            "enabled": false
        },
        "edges": {
            "color": {
                "inherit": true
            },
            "smooth": {
                "enabled": false,
                "type": "continuous"
            }
        },
        "interaction": {
            "dragNodes": true,
            "hideEdgesOnDrag": false,
            "hideNodesOnDrag": false
        },
        "physics": {
            "enabled": true,
            "stabilization": {
                "enabled": true,
                "fit": true,
                "iterations": 1000,
                "onlyDynamicEdges": false,
                "updateInterval": 50
            }
        }
    };


    // default to using dot shape for nodes
    options.nodes = {
        shape: "dot"
    }


    network = new vis.Network(container, data, options);

}

drawGraph();
