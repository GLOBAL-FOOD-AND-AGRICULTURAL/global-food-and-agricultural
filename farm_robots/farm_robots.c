// farm_robots.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define PI 3.14159

int main() {
  // Initialize robot coordinates
  double lat = 37.7749;
  double lon = -122.4194;
  double alt = 100;

  // Initialize crop monitoring data
  double crop_health[100][100];
  for (int i = 0; i < 100; i++) {
    for (int j = 0; j < 100; j++) {
      crop_health[i][j] = (double)rand() / RAND_MAX;
    }
  }

  // Fly robot over crop field
  for (int i = 0; i < 100; i++) {
    for (int j = 0; j < 100; j++) {
      // Calculate robot coordinates
      double robot_lat = lat + (i * 0.01);
      double robot_lon = lon + (j * 0.01);

      // Calculate crop health index
      double health_index = 0;
      for (int k = 0; k < 10; k++) {
        health_index += crop_health[i + k][j + k];
      }
      health_index /= 10;

      // Print crop health data
      printf("Robot coordinates: (%f, %f, %f)\n", robot_lat, robot_lon, alt);
      printf("Crop health index: %f\n", health_index);
    }
  }

  return 0;
}
