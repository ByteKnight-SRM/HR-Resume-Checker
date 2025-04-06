import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [candidates, setCandidates] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/candidates')
      .then(response => setCandidates(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Candidate Profiles</h1>
      <ul>
        {candidates.map(candidate => (
          <li key={candidate.id} className="mb-2 p-4 border rounded">
            <p><strong>Name:</strong> {candidate.name}</p>
            <p><strong>Email:</strong> {candidate.email}</p>
            <p><strong>Skills:</strong> {candidate.skills?.join(', ')}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
