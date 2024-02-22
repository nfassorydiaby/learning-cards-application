import React, { useState, useEffect } from 'react';
import { lireCartes } from '../api/api';

const LireCartes = () => {
  const [cartes, setCartes] = useState([]);

  useEffect(() => {
    const fetchCartes = async () => {
      const { data } = await lireCartes();
      setCartes(data);
    };

    fetchCartes();
  }, []);

  return (
    <div className="p-5">
      <h2 className="text-2xl font-bold mb-4">Liste des Cartes</h2>
      {cartes.map((carte, index) => (
        <div key={index} className="mb-3 p-4 shadow rounded bg-white">
          <h3 className="text-xl font-semibold">{carte.titre}</h3>
          <p>{carte.description}</p>
        </div>
      ))}
    </div>
  );
};

export default LireCartes;
