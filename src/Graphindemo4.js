import React from 'react';
import Graphin, { Behaviors, GraphinData } from '@antv/graphin';
import { Row, Col, Card } from 'antd';
import iconLoader from '@antv/graphin-icons';

const icons = Graphin.registerFontFamily(iconLoader);
const Color = {
    user: '#FF6A00',
    company: '#46a7a6',
};
const data: GraphinData = {
    nodes: [
        {
            id: 'node-0',
            label: "\"EN\": \"is the mode of the attribute of\" \n\"FR\": \"est le mode de l attribut de\"",
            x: 100,
            y: 100,
            data: {
                type: 'user',
                iconref: 'share',
                icontext: 71,
                count: 300,
                badgenumber: 3,
                badgesize: [20, 20]
            },
        },
        {
            id: 'node-1',
            label: "\"EN\": \"is a grammatical mode of\" \n\"FR\": \"mode grammatical\"",
            x: 200,
            y: 100,
            data: {
                type: 'user',
                iconref: 'share',
                icontext: 64,
                count: 300,
                badgesize: [0, 0]
            },
        },
        {
            id: 'node-2',
            label: "\"EN\": \"seme\" \n\"FR\": \"sème\"",
            x: 200,
            y: 300,
            data: {
                type: 'user',
                iconref: 'share',
                icontext: 18,
                count: 300,
                badgesize: [0, 0]
            },
        },
        {
            id: 'node-3',
            label: "\"EN\": \"is a grammatical attribute of\" \n\"FR\": \"est un attribut grammatical de\"",
            x: 200,
            y: 400,
            data: {
                type: 'user',
                iconref: 'share',
                icontext: 62,
                count: 300,
                badgesize: [0, 0]
            },
        },
    ],
    edges: [
        {
            source: 'node-0',
            target: 'node-1',
            style: {
                keyshape: {
                    lineDash: [2, 2],
                    stroke: Color.user,
                },
                label: {
                    value: '/#/0',
                    fill: Color.user,
                },
            },
        },
        {
            source: 'node-0',
            target: 'node-2',
            style: {
                keyshape: {
                    lineDash: [2, 2],
                    stroke: Color.user,
                },
                label: {
                    value: '/#/1',
                    fill: Color.user,
                },
            },
        },
        {
            source: 'node-0',
            target: 'node-3',
            style: {
                keyshape: {
                    lineDash: [2, 2],
                    stroke: Color.user,
                },
                label: {
                    value: "/#/4/*'E:S:.x.-'",
                    fill: Color.user,
                },
            },
        },
    ],
};

data.nodes.forEach(node => {
    const { id, label } = node;
    const { type, count, iconref, icontext, badgenumber, badgesize } = node.data;
    node.style = {
        label: {
            value: label,
        },
        keyshape: {
            size: count ? (count / 10) * 2 : 30,
            stroke: Color[type],
            fill: Color[type],
            fillOpacity: 0.2,
            strokeOpacity: 1,
        },
        icon: {
            type: 'text',
            value: icontext,
            /** 图标大小 */
            size: count ? count / 10 : 15,
            fill: Color[type],
            fontFamily: 'graphin',
        },
        badges: [{
            position: 'RT',
            type: 'text',
            value: badgenumber,
            size: badgesize,
            color: '#fff',
            fill: 'gray',
        }]
    };
});

const { ZoomCanvas } = Behaviors;
const Graphindemo4 = () => {
    return (
        <div>
            <Row gutter={16}>
                {/* <Col span={12}>
          <Card title="关系数据" bodyStyle={{ height: '554px', overflow: 'scroll' }}>
            <pre>{JSON.stringify(data, null, 2)}</pre>
          </Card>
        </Col> */}
                <Col span={12}>
                    <Card title="Graphin">
                        <Graphin data={data} layout={{ type: 'preset' }}>
                            <ZoomCanvas enabled />
                        </Graphin>
                    </Card>
                </Col>
            </Row>
        </div>
    );
};

export default Graphindemo4;