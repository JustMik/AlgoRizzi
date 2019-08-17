
// This method is responsible for drawing the graph, returns the drawn network

function drawGraph(nodes, edges) {
    // initialize global variables.
    var edges;
    var nodes;
    var network; 
    var container;
    var options, data;
    
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

    return network;

}

