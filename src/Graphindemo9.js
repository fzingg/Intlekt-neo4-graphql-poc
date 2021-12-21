import React, { useEffect } from 'react';

import Graphin, { Utils, Behaviors, GraphinContext, NodeStyle } from '@antv/graphin';
import { ContextMenu, Toolbar } from '@antv/graphin-components';
import { Switch } from 'antd';

import iconLoader from '@antv/graphin-icons';

const { Menu } = ContextMenu;
const { DragNodeWithForce } = Behaviors;


const icons = Graphin.registerFontFamily(iconLoader);
const Color = {
    user: '#FF6A00',
    company: '#46a7a6',
};

const container = document.getElementById('graphin-container');
const width = 1600;
const height = 800;



const Graphindemo9 = () => {
    const [state, setState] = React.useState({
        data: null,
    });
    useEffect(() => {
        // eslint-disable-next-line no-undef
        fetch('https://gw.alipayobjects.com/os/antvdemo/assets/data/relations.json')
            .then(res => res.json())
            .then(res => {
                console.log('data', res);
                res.nodes.map((node, i) => {
                    node.style = {
                        label: {
                            value: node.id, // add label
                        },
                        keyshape: {
                            size: Math.random() * 60 + 5,
                            stroke: Color.company,
                            fill: Color.user,
                            fillOpacity: 0.2,
                            strokeOpacity: 1,
                        },
                        icon: {
                            type: 'font',
                            value: icons['tag-fill'],
                            size: 15,
                            fill: Color.user,
                            fontFamily: 'graphin',
                        },
                        badges: [{
                            position: 'RT',
                            type: 'text',
                            value: 8,
                            size: [20, 20],
                            color: '#fff',
                            fill: 'gray',
                        }],
                        status: {
                            hover: {
                                halo: {
                                    visible: true,
                                },
                            },
                            selected: {
                                halo: {
                                    visible: true,
                                },
                                keyshape: {
                                    lineWidth: 10,
                                },
                            },
                        },
                    };
                });
                res.edges.map((edge, i) => {
                    edge.id = 'edge' + i;
                    edge.style = {
                        keyshape: {
                            lineDash: [4, 4],

                        },
                    }

                });
                setState({
                    data: res,
                });
            });
    }, []);

    const { data } = state;

    return (
        <div id="main-container">
            {data && (
                <Graphin
                    data={data}

                    width={width}
                    height={height}
                    layout={{
                        type: 'graphin-force',
                        nodeSize: 30,
                        preventOverlap: true,
                        linkDistance: 400,
                        nodeStrength: 30,
                        edgeStrength: 0.1
                    }}
                >
                    <DragNodeWithForce autoPin={true} />
                </Graphin>
            )}
        </div>
    );
};

export default Graphindemo9;