# life_cycle_assessment.R
library(readr)
library(ggplot2)

# Load life cycle assessment data from CSV file
data <- read_csv("lca_data.csv")

# Process life cycle assessment data
data <- data %>%
  group_by(product) %>%
  summarise(total_impact = sum(impact))

# Visualize life cycle assessment data
ggplot(data, aes(x = product, y = total_impact)) +
  geom_bar(stat = "identity") +
  labs(x = "Product", y = "Total Impact") +
  theme_classic()
