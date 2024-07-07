// farm_monitoring.js
import express from 'express';
import socketIO from 'ocket.io';
import { FarmSensor } from './farm_sensor';

const app = express();
const io = socketIO();

app.use(express.json());

const farmSensor = new FarmSensor();

io.on('connection', (socket) => {
  console.log('New client connected');

  farmSensor.on('data', (data) => {
    socket.emit('farm_data', data);
  });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
