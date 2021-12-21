import React, { useEffect } from 'react';

import Graphin, { Behaviors, GraphinData } from '@antv/graphin';
import iconLoader from '@antv/graphin-icons';

const icons = Graphin.registerFontFamily(iconLoader);
const Color = {
    user: '#FF6A00',
    company: '#46a7a6',
};
const { TreeCollapse } = Behaviors;

const walk = (node, callback) => {
    callback(node);
    if (node.children && node.children.length !== 0) {
        node.children.forEach(n => {
            walk(n, callback);
        });
    }
};
const Graphindemo7 = () => {
    const [state, setState] = React.useState({
        data: null,
    });
    useEffect(() => {
        // eslint-disable-next-line no-undef
        fetch('https://gw.alipayobjects.com/os/antvdemo/assets/data/algorithm-category.json')
            .then(res => res.json())
            .then(res => {
                console.log('data', res);
                walk(res, node => {
                    node.style = {
                        label: {
                            value: node.id, // add label
                        },
                    };
                });
                setState({
                    data: res,
                });
            });
    }, []);

    const { data } = state;

    return (
        <div>
            {data && (
                <Graphin
                    data={data}
                    fitView
                    theme={{
                        mode: 'light',
                        primaryColor: '#D77622',
                        edgeSize: 2,
                        primaryEdgeColor: Color.company
                    }}
                    layout={{
                        type: 'compactBox',
                        direction: 'TB',
                        getId: function getId(d) {
                            return d.id;
                        },
                        getHeight: function getHeight() {
                            return 16;
                        },
                        getWidth: function getWidth() {
                            return 16;
                        },
                        getVGap: function getVGap() {
                            return 80;
                        },
                        getHGap: function getHGap() {
                            return 50;
                        },
                    }}
                >
                    {/* <FitView /> */}
                    <TreeCollapse trigger="click" />
                </Graphin>
            )}
        </div>
    );
};

export default Graphindemo7;