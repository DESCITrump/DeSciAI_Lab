import React, { useState } from 'react';

function Evaluation({ researchId, onEvaluate }) {
  const [score, setScore] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    onEvaluate(researchId, score);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Score:
        <input type="number" value={score} onChange={(e) => setScore(e.target.value)} />
      </label>
      <button type="submit">Submit Evaluation</button>
    </form>
  );
}

export default Evaluation;
