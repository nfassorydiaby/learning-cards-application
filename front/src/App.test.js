// Import the necessary functions and components for testing
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';
import ReadCards from './components/ReadCards';
import { BrowserRouter as Router } from 'react-router-dom';

// Mock the fetch API to simulate fetching cards
jest.mock('node-fetch', () => ({
  fetch: jest.fn(() =>
    Promise.resolve({
      ok: true,
      json: () => Promise.resolve([{ 
        id: '3fa85f64-5717-4562-b3fc-2c963f66afa6', 
        question: 'Question 1',
        answer: 'Answer 1',
        tag: 'Tag 1'
      }]), // Mocked response data
    })
  ),
}));

describe('App', () => {
  test('renders App component', async () => {
    render(
      <Router>
        <App />
      </Router>
    );
    // Verify that the component renders without crashing
    expect(screen.getByText('My cards')).toBeInTheDocument();
    // Verify that the "Add a new card" button is rendered
    expect(screen.getByText('Add a new card')).toBeInTheDocument();
    // Verify that the "Start the quiz" button is rendered
    expect(screen.getByText('Start the quiz')).toBeInTheDocument();
  });

  test('renders Cards array when cards is displayed', async () => {
    render(
      <Router>
        <App />
      </Router>
    );

    // Wait for the asynchronous data fetching to complete
    await waitFor(() => {
      // Verify that the CardList component is rendered
      expect(screen.getByText('Question 1')).toBeInTheDocument();
      expect(screen.getByText('Answer 1')).toBeInTheDocument();
      expect(screen.getByText('Tag 1')).toBeInTheDocument();
    });
  });
});

// describe('CardList', () => {
//   test('renders CardList component', async () => {
//     render(<ReadCards />);
//     // Verify that the component renders without crashing
//     expect(screen.getByText('Mes fiches')).toBeInTheDocument();
//     // Verify that the "Add a new card" button is rendered
//     expect(screen.getByText('Add a new card')).toBeInTheDocument();
//     // Verify that the "Start the quiz" button is rendered
//     expect(screen.getByText('Start the quiz')).toBeInTheDocument();
//   });

//   test('fetches and displays cards', async () => {
//     render(<ReadCards />);
//     // Wait for the component to fetch cards
//     await screen.findByText('Question 1');
//     // Verify that the fetched card is displayed
//     expect(screen.getByText('Question 1')).toBeInTheDocument();
//   });

// });
