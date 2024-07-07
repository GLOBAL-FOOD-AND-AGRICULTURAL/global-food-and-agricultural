import { SensorData } from './SensorData';

const farmSensorData = new SensorData();

farmSensorData.on('data', (data) => {
  console.log(`Received sensor data: ${data}`);
  // Send data to cloud or database for analysis
});

farmSensorData.start();
