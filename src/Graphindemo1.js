import React from 'react';
import Graphin, { Utils } from '@antv/graphin';

const data = Utils.mock(10)
  .circle()
  .graphin();

const Graphindemo1 = () => {
  const graphinRef = React.createRef();

  React.useEffect(() => {
    const {
      graph, // Graph instance of g6
      apis, // API interface provided by Graphin
    } = graphinRef.current;
    console.log('ref', graphinRef, graph, apis);
  }, []);

  return (
    <div className="App">
      <Graphin data={data} ref={graphinRef}></Graphin>
    </div>
  );
};
export default Graphindemo1;