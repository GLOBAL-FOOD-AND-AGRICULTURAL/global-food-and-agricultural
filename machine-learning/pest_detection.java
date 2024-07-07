// pest_detection.java
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.nn.weights.WeightInit;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.dataset.api.iterator.DataSetIterator;
import org.nd4j.linalg.factory.Nd4j;
import org.nd4j.linalg.lossfunctions.LossFunctions;

public class PestDetection {
  public static void main(String[] args) throws IOException {
    // Load dataset
    File file = new File("pest_data.csv");
    List<String> lines = Files.readAllLines(Paths.get(file.getAbsolutePath()));

    // Preprocess data
    List<double[]> features = new ArrayList<>();
    List<Integer> labels = new ArrayList<>();

    for (String line : lines) {
      String[] values = line.split(",");
      double[] featureValues = new double[values.length - 1];
      for (int i = 0; i < values.length - 1; i++) {
        featureValues[i] = Double.parseDouble(values[i]);
      }
      features.add(featureValues);
      labels.add(Integer.parseInt(values[values.length - 1]));
    }

    // Create neural network
    NeuralNetConfiguration config = new NeuralNetConfiguration.Builder()
       .seed(42)
       .weightInit(WeightInit.XAVIER)
       .updater(new Nesterovs(0.01))
       .list()
       .layer(new DenseLayer.Builder()
           .nIn(features.get(0).length)
           .nOut(10)
           .activation(Activation.RELU)
           .build())
       .layer(new DenseLayer.Builder()
           .nIn(10)
           .nOut(2)
           .activation(Activation.SOFTMAX)
           .build())
       .pretrain(false)
       .backprop(true)
       .build();

    MultiLayerNetwork model = new MultiLayerNetwork(config);
    model.init();

    // Train model
    DataSetIterator iterator = new DataSetIterator(features, labels, 10);
    model.fit(iterator);

    // Evaluate model
    System.out.println("Model evaluation:");
    System.out.println(model.evaluate(iterator));
  }
}
