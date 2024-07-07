// buildings_and_heating.java
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class BuildingsAndHeating {
  public static void main(String[] args) throws IOException {
    // Load building data from CSV file
    File file = new File("building_data.csv");
    List<String> lines = Files.readAllLines(Paths.get(file.getAbsolutePath()));

    // Process building data
    List<Building> buildings = new ArrayList<>();
    for (String line : lines) {
      String[] values = line.split(",");
      Building building = new Building(values[0], Double.parseDouble(values[1]));
      buildings.add(building);
    }

    // Calculate heating energy consumption
    double totalHeatingEnergy = 0;
    for (Building building : buildings) {
      totalHeatingEnergy += building.getHeatingEnergyConsumption();
    }

    // Print results
    System.out.println("Total heating energy consumption: " + totalHeatingEnergy);
  }
}

class Building {
  private String name;
  private double heatingEnergyConsumption;

  public Building(String name, double heatingEnergyConsumption) {
    this.name = name;
    this.heatingEnergyConsumption = heatingEnergyConsumption;
  }

  public double getHeatingEnergyConsumption() {
    return heatingEnergyConsumption;
  }
}
