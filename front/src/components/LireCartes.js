import React, { useState, useEffect } from 'react';
//import { lireCartes } from '../api/api';


function CardList() {
    const [cartes, setCartes] = useState([]);

    useEffect(() => {
    const fetchCartes = async () => {
        try {
            const cardsList = [];
            const url = `http://localhost:8000/cards/`;
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            if (response.ok) {
                const data = await response.json();
                console.log(data)
            } else {
                console.error('Failed to fetch employees for establishment:');
            }
            console.log(cardsList);
            setCartes(cardsList);
        } catch (error) {
            console.error('Error fetching employees:', error);
        }
    };

    fetchCartes();
  }, []);
  
    return (
      <div className="flex-center flex-column">
        test
      </div>
    );
  
};
  
export default CardList;


/*
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
*/
/*
import React, { useEffect, useState } from 'react';

const CardList = () => {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    // Define a function to fetch cards from the backend
    const fetchCards = async () => {
      try {
        const response = await fetch('http://localhost:8000/cards/');
        if (!response.ok) {
          throw new Error('Failed to fetch cards');
        }
        const data = await response.json();
        setCards(data);
      } catch (error) {
        console.error('Error fetching cards:', error);
      }
    };

    // Call the fetchCards function when the component mounts
    fetchCards();
  }, []); // Empty dependency array ensures this effect runs only once, when the component mounts*/