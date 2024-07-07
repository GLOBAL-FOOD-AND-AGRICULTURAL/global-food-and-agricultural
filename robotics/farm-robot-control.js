import { Robot } from './Robot';

const farmRobot = new Robot();

farmRobot.moveTo(5, 10);

farmRobot.on('sensor', (sensor) => {
  console.log(`Robot sensor: ${sensor}`);
  // Use sensor data for analysis or decision-making
});

farmRobot.harvest();
