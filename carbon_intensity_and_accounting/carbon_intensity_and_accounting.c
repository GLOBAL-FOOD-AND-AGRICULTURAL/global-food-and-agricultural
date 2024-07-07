// carbon_intensity_and_accounting.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PI 3.14159

int main() {
  // Load emission data from CSV file
  FILE *file = fopen("emission_data.csv", "r");
  char line[1024];
  while (fgets(line, 1024, file) != NULL) {
    // Process emission data
    char *token = strtok(line, ",");
    double carbonIntensity = atof(token);
    token = strtok(NULL, ",");
    double emissionAmount = atof(token);

    // Calculate carbon footprint
    double carbonFootprint = carbonIntensity * emissionAmount;

    // Print results
    printf("Carbon footprint: %f\n", carbonFootprint);
  }

  fclose(file);
  return 0;
}
