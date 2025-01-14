import React from 'react';

function ResearchDetail({ research }) {
  return (
    <div>
      <h2>{research.title}</h2>
      <p>{research.description}</p>
    </div>
  );
}

export default ResearchDetail;
