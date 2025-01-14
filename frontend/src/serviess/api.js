const API_URL = 'http://localhost:5000';

export const getResearches = async () => {
  const response = await fetch(`${API_URL}/researches`);
  const data = await response.json();
  return data;
};
