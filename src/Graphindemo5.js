import React from 'react';
import Graphin, { Behaviors, Utils } from '@antv/graphin';
import { Row, Col, Card } from 'antd';

import 'antd/dist/antd.css';

const { ZoomCanvas, FitView } = Behaviors;
const data1 = Utils.mock(8).circle().graphin();
const data2 = Utils.mock(8).tree().graphin();

const Graphindemo5 = () => {
    return (
        <div>
            <Row gutter={16}>
                <Col span={12}>
                    <Card title="Concentric" bodyStyle={{ height: '554px', overflow: 'scroll' }}>
                        <Graphin data={data1} layout={{ type: 'concentric' }}>
                            <ZoomCanvas enabled />
                        </Graphin>
                    </Card>
                </Col>
                <Col span={12}>
                    <Card title="Dagre">
                        <Graphin data={data2} layout={{ type: 'dagre' }}>
                            <ZoomCanvas enabled />
                            {/** 树图的FitView 有BUG，网图的可以 */}
                            <FitView />
                        </Graphin>
                    </Card>
                </Col>
            </Row>
        </div>
    );
};

export default Graphindemo5;