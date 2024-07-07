import { Drone } from './Drone';

const farmDrone = new Drone();

farmDrone.takeoff();

farmDrone.on('location', (location) => {
  console.log(`Drone location: ${location}`);
  // Uselocation for mapping or analysis
});

farmDrone.land();
