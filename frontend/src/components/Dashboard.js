import React, { useEffect, useState } from 'react';
import { getResearches } from '../services/api';

function Dashboard() {
  const [researches, setResearches] = useState([]);

  useEffect(() => {
    fetchResearches();
  }, []);

  const fetchResearches = async () => {
    const data = await getResearches();
    setResearches(data);
  };

  return (
    <div>
      <h1>Research Dashboard</h1>
      <ul>
        {researches.map(research => (
          <li key={research.id}>{research.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
