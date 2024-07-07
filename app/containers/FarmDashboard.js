import React from 'react';
import { FarmDetails } from '../components/FarmDetails';
import { FarmList } from '../components/FarmList';
import { FarmMap } from '../components/FarmMap';

const FarmDashboard = () => {
  return (
    <div>
      <FarmDetails />
      <FarmList />
      <FarmMap />
    </div>
  );
};

export default FarmDashboard;
