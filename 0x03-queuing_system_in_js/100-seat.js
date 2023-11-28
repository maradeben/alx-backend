import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const client = createClient({ name: 'reserve_seat' });
const queue = createQueue();
const INITIAL_SEATS_COUNT = 50;
let reservationEnabled = false;
const PORT = 1245;

// Modifies the number of available seats.
const reserveSeat = async (number) => {
  return promisify(client.SET).bind(client)('available_seats', number);
};

// Retrieves the number of available seats.
const getCurrentAvailableSeats = async () => {
  return promisify(client.GET).bind(client)('available_seats');
};

app.get('/available_seats', (_, res) => {
  getCurrentAvailableSeats()
    .then((numberOfAvailableSeats) => {
      res.json({ numberOfAvailableSeats })
    });
});
