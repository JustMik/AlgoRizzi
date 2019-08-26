
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
            "zoomView": false,
            "selectConnectedEdges": false,
            "multiselect": true,
            "dragNodes": true,
            "hideEdgesOnDrag": false,
            "hideNodesOnDrag": false,
            "multiselect": true
        },
        "physics": {
            "enabled": false,
            "stabilization": {
                "enabled": false,
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

    network.on( 'click', function(properties) {
            var nodeIds = properties.nodes;
            var clickedNode = nodes.get(nodeIds);
            console.log(clickedNode)
            if (clickedNode !== "null" && clickedNode !== "undefined" && Object.keys(clickedNode).length != 0) {
                console.log("Hai clikato il nodo ", clickedNode[0].label)
            }

            var edgeIds = properties.edges;
            var clickedEdge = edges.get(edgeIds);
            if (clickedEdge !== "null" &&
                clickedEdge !== "undefined" &&
                Object.keys(clickedEdge).length != 0 &&
                Object.keys(clickedNode).length == 0) {
                    console.log("Hai clikato l'arco ", clickedEdge[0].from, " -> ", clickedEdge[0].to )
            }
        });

    return network;

}

