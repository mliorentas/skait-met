package com.company;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

/**
 * Created by Matas on 2017-10-29.
 */
public class Tridiagonal {
    List<Double> matrixColumn1 = new ArrayList<>();
    List<Double> matrixColumn2 = new ArrayList<>();
    List<Double> matrixColumn3 = new ArrayList<>();

    List<Double> matrixValues = new ArrayList<>();

    List<Double> solverC = new ArrayList<>();
    List<Double> solverD = new ArrayList<>();

    Map<Integer, Double> solutions = new HashMap<>();
    Integer lastIndex;

    public void calc(String path ) {
        readFile(path);
        calculateForward();
        System.out.println("c" + solverC.toString());
        System.out.println("d" + solverD.toString());
        calculateBackward();
        for (int iterator = 0; iterator <= lastIndex; iterator++) {
            System.out.println(solutions.get(iterator).toString());
        }
    }

    private void calculateBackward() {
        solutions.put(lastIndex, solverD.get(lastIndex));
        for (int iterator = lastIndex - 1; iterator >= 0; iterator--) {
            solutions.put(iterator, solverD.get(iterator) + solverC.get(iterator) * solutions.get(iterator + 1));
        }
    }

    private void calculateForward () {
        solverC.add(-1 * (matrixColumn3.get(0) / matrixColumn2.get(0)));
        solverD.add(matrixValues.get(0) / matrixColumn2.get(0));

        for (int iterator = 1; iterator <=  lastIndex - 1; iterator++) {
            double division = matrixColumn1.get(iterator) * solverC.get(iterator - 1) + matrixColumn2.get(iterator);
            solverC.add(-1 * matrixColumn3.get(iterator) / division);
            solverD.add((matrixValues.get(iterator) - matrixColumn1.get(iterator) * solverD.get(iterator-1)) / division);
        }
        int last = lastIndex;
        double division = matrixColumn1.get(last) * solverC.get(last - 1) + matrixColumn2.get(last);
        solverD.add((matrixValues.get(last) - matrixColumn1.get(last) * solverD.get(last-1)) / division);
    }

    private void readFile(String fileName)
    {
        // This will reference one line at a time
        String line = null;

        try {
            // FileReader reads text files in the default encoding.
            FileReader fileReader =
                    new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader =
                    new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                String[] values = line.split(" ");
                matrixColumn1.add(Double.parseDouble(values[0]));
                matrixColumn2.add(Double.parseDouble(values[1]));
                matrixColumn3.add(Double.parseDouble(values[2]));
                matrixValues.add(Double.parseDouble(values[3]));
                System.out.println(line);
            }
            lastIndex = new Integer(matrixColumn1.size() - 1);
            // Always close files.
            bufferedReader.close();
        }
        catch(FileNotFoundException ex) {
            System.out.println(
                    "Unable to open file '" +
                            fileName + "'");
        }
        catch(IOException ex) {
            System.out.println(
                    "Error reading file '"
                            + fileName + "'");
            // Or we could just do this:
            // ex.printStackTrace();
        }


    }


}
