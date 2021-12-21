import React, { useEffect, useRef } from 'react';
import { DataSet, Network } from 'vis-network/standalone/esm/vis-network';



const VisNetwork = () => {
  // A reference to the div rendered by this component
  const domNode = useRef(null);

  // A reference to the vis network instance
  const network = useRef(null);

  // An array of nodes
  const nodes = new DataSet([
    { id: 1, label: 'Node 1' },
    { id: 2, label: 'Node 2' },
    { id: 3, label: 'Node 3' },
    { id: 4, label: 'Node 4' },
    { id: 5, label: 'Node 5' }
  ]);

  // An array of edges
  const edges = new DataSet([
    { from: 1, to: 3 },
    { from: 1, to: 2 },
    { from: 2, to: 4 },
    { from: 2, to: 5 }
  ]);

  const data = {
    nodes,
    edges
  };

  const options = {
    manipulation: {
      enabled: false,
      // addEdge: function(edgeData,callback) {
      //   console.log(edgeData)
      //   callback(edgeData);
      //   this.testfunc(edgeData);
      // }

      // addEdge: this.testfunc,

      // addNode: function(nodeData,callback) {
      //   console.log(nodeData)
      //   console.log(callback)
      // },
      // addEdge: function(edgeData,callback) {
      //   console.log(edgeData)
      //   console.log(callback)
      // }
    },
    // interaction:{
    //   dragNodes:true,
    //   dragView: true,
    //   hideEdgesOnDrag: false,
    //   hideEdgesOnZoom: false,
    //   hideNodesOnDrag: false,
    //   hover: false,
    //   hoverConnectedEdges: true,
    //   keyboard: {
    //     enabled: false,
    //     speed: {x: 10, y: 10, zoom: 0.02},
    //     bindToWindow: true
    //   },
    //   multiselect: false,
    //   navigationButtons: false,
    //   selectable: true,
    //   selectConnectedEdges: true,
    //   tooltipDelay: 300,
    //   zoomView: true
    // },
    layout: {
      hierarchical: false
    },
    // edges: {
    //   color: "#000000"
    // },
    height: "100%",
    // nodes: {
    //   shape: "circularImage"
    // }
    // manipulation: {
    //   addNode: function(nodeData,callback) {
    //     nodeData.id = 6;
    //     nodeData.label = 'hello world';
    //     nodeData.title = 'dsadasdsad sadsa';
    //     callback(nodeData);
    //   }
    // }
    autoResize: true,
    locale: 'en',

    nodes: {
      scaling: {
        min: 25,
        max: 32
      },
      shadow: true,
    },

    edges: {
      arrows: {
        to: {
          enabled: false
        }
      },
      color: "#444",
      smooth: false,
      shadow: true,
    },

    physics: {
      forceAtlas2Based: {
        springLength: 100,
        damping: 1,
        gravitationalConstant: -130
      },
      minVelocity: 0.75,
      solver: "forceAtlas2Based"

    },

    interaction: {
      navigationButtons: false,
      keyboard: false,
      hover: true,
      dragNodes: true,
      selectConnectedEdges: false
    },

    groups: {
      // OAI needed for nodes without principle
      'Outcome': {
        shape: 'dot',
        color: '#bbb',
        value: 2,
        icon: {
          code: 'O',
          face: 'OpenSans',
          color: '#fff'
        }
      },
      'Action': {
        shape: 'hexagon',
        color: '#bbb',
        value: 1,
        icon: {
          code: 'A',
          face: 'OpenSans',
          color: '#fff'
        }
      },
      'Indicator': {
        shape: 'square',
        color: '#bbb',
        value: 1,
        icon: {
          code: 'I',
          face: 'OpenSans',
          color: '#fff'
        }
      },

    }
  };

  useEffect(
    () => {
      network.current = new Network(domNode.current, data, options);
    },
    [domNode, network, data, options]
  );

  function VisNetwork() {
    <div ref={domNode} />
  }
};

export default VisNetwork;