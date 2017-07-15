import java.util.*;
import java.io.*;
import java.text.*;
import java.math.*;

class Perception {

	static int MAX_ITER = 100;
	static int NUM_INSTANCES = 100;
	static int theta = 0;
	static double LEARNING_RATE = 0.1;

	public static void main(String args[]) {
		double[] x = new double [NUM_INSTANCES];
		double[] y = new double [NUM_INSTANCES];

		int[] outputs = new int [NUM_INSTANCES];

		for (int i = 0; i < NUM_INSTANCES / 2; i++) {
			x[i] = genRandom(0, 10);
			y[i] = genRandom(10, 20);

			outputs[i] = 0;
		}

		for (int i = 50; i < NUM_INSTANCES; i++) {
			x[i] = genRandom(10, 20);
			y[i] = genRandom(0, 10);

			outputs[i] = 1;
		}

		double[] weights = new double[4];
		double localError, globalError;
		int i, p, iteration, output;

		weights[0] = genRandom(0, 1);
	  weights[1] = genRandom(0, 1);	
	  weights[2] = genRandom(0, 1); //bias

	  iteration = 0;
	  do {
	  	iteration ++;
	  	globalError = 0;

	  	for (p = 0; p < NUM_INSTANCES; p++) {
	  		output = calOutput(theta, weights, x[p], y[p]);
	  		localError = outputs[p] - output;

	  		weights[0] += LEARNING_RATE * localError * x[p];
	  		weights[1] += LEARNING_RATE * localError * y[p];
	  		weights[2] += LEARNING_RATE * localError;
	  		globalError += (localError=localError);
	  	}
	  	System.out.println("Iteration "+iteration+" : RMSE = "+Math.sqrt(globalError/NUM_INSTANCES));

	  } while (globalError != 0 && iteration<=MAX_ITER);

	  System.out.println("\n=======\nDecision boundary equation:");
		System.out.println(weights[0] +"*x + "+weights[1]+"*y +  " + weights[3]+" = 0");


	}

	public static double genRandom(int min, int max) {
		DecimalFormat df = new DecimalFormat("#.####");
		double d = min + Math.random() * (max - min);
		String s = df.format(d);
		double x = Double.parseDouble(s);
		return x;
	}
	static int calOutput(int theta, double weights[], double x, double y) {
		double sum = x * weights[0] + y * weights[1] + weights[2];
		return (sum >= theta) ? 1 : 0;
	}
}