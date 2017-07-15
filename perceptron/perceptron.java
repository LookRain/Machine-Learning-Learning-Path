import java.util.*;
import java.io.*;
import java.text.*;
import java.math.*;

Class Perception {

	int MAX_ITER = 100;
	int NUM_INSTANCES = 100;
	int theta = 0;
	double LEARNING_RATE = 0.1;

	static void main(String args[]) {
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

	}

	public static double genRandom(int min, int max) {
		DecimalFormat df = new DecimalFormat("#.####");
		double d = min + Math.random() * (max - min);
		String s = df.format(d);
		double x = Double.parseDouble(s);
		return x;
	}
}