import axios from 'axios';

const API_URL = process.env.API_URL;

export const fetchFarmDetails = (farmId) => {
  return axios.get(`${API_URL}/farms/${farmId}`);
};

export const fetchFarmList = () => {
  return axios.get(`${API_URL}/farms`);
};

export const fetchFarmMapData = () => {
  return axios.get(`${API_URL}/farms/map`);
};
