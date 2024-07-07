import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { fetchFarmDetails } from '../api/farmAPI';

const FarmDetails = () => {
  const { farmId } = useParams();
  const [farm, setFarm] = useState({});

  useEffect(() => {
    fetchFarmDetails(farmId).then((response) => {
      setFarm(response.data);
    });
  }, [farmId]);

  return (
    <div>
      <h1>{farm.name}</h1>
      <p>{farm.description}</p>
      <img src={farm.image} alt={farm.name} />
    </div>
  );
};

export default FarmDetails;
