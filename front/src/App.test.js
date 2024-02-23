import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import NewCard from './components/NewCard'; // Ajustez le chemin d'importation selon votre structure de dossier



// Mock de useNavigate pour éviter les erreurs liées au routing
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => jest.fn(),
}));

describe('NewCard', () => {
  test('affiche le formulaire de création de carte', () => {
    render(<NewCard />);
    expect(screen.getByLabelText(/question/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/answer/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/tag/i)).toBeInTheDocument();
  });

  test('permet aux utilisateurs de saisir des informations', () => {
    render(<NewCard />);
    const questionInput = screen.getByLabelText(/question/i);
    fireEvent.change(questionInput, { target: { value: 'Quelle est la capitale de la France ?' } });
    expect(questionInput.value).toBe('Quelle est la capitale de la France ?');
  });

  // Ajoutez plus de tests ici pour couvrir d'autres aspects comme le comportement du formulaire lors de la soumission, la gestion des erreurs, etc.
});
