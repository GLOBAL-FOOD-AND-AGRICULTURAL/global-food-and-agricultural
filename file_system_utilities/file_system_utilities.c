// file_system_utilities.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

int main() {
  // Create a new file
  FILE *fp = fopen("example.txt", "w");
  if (fp == NULL) {
    printf("Error creating file\n");
    return 1;
  }
  fclose(fp);

  // Read file contents
  fp = fopen("example.txt", "r");
  if (fp == NULL) {
    printf("Error reading file\n");
    return 1;
  }
  char buffer[1024];
  while (fgets(buffer, 1024, fp) != NULL) {
    printf("%s", buffer);
  }
  fclose(fp);

  // Delete file
  if (remove("example.txt") != 0) {
    printf("Error deleting file\n");
    return 1;
  }

  return 0;
}
