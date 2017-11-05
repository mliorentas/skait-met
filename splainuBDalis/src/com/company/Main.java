package com.company;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static List<Double> xList = new ArrayList<>();
    static List<Double> yList = new ArrayList<>();

    public static void main(String[] args) {
        xList.add(0d);
        xList.add(1d);
        xList.add(2d);
        xList.add(3d);
        xList.add(4d);
        xList.add(5d);
        yList.add(0d);
        yList.add(0d);
        yList.add(0d);
        yList.add(209d);
        yList.add(0d);
        yList.add(209d);

        System.out.println("\nInput values.");
        System.out.println("x values: " + xList.toString());
        System.out.println("y values: " + yList.toString());
        // Make h list
        List<Double> hList = new ArrayList<>();
        for(int x = 0; x < xList.size() - 1; x++)
        {
            hList.add(xList.get(x + 1) - xList.get(x));
        }

        //Make f(xi+1, xi) list
        List<Double> fList = new ArrayList<>();
        for(int x = 0; x < xList.size() - 1; x++)
        {
            fList.add((yList.get(x + 1) - yList.get(x))/hList.get(x));
        }

        List<Double> matrixColumn1 = new ArrayList<>();
        List<Double> matrixColumn2 = new ArrayList<>();
        List<Double> matrixColumn3 = new ArrayList<>();

        List<Double> matrixValues = new ArrayList<>();
        matrixColumn1.add(0d);
        matrixColumn2.add(1d);
        matrixColumn3.add(0d);
        matrixValues.add(0d);
        for (int iter = 1; iter <= xList.size() - 2; iter++)
        {
            matrixColumn1.add(hList.get(iter-1));
            matrixColumn2.add(2*(hList.get(iter)+ hList.get(iter-1)));
            matrixColumn3.add(hList.get(iter));
            matrixValues.add(6*(fList.get(iter)-fList.get(iter-1)));
        }
        matrixColumn1.add(0d);
        matrixColumn2.add(1d);
        matrixColumn3.add(0d);
        matrixValues.add(0d);

        Tridiagonal tridiagonalCalculator = new Tridiagonal();
        List<Double> gList = tridiagonalCalculator.calc(matrixColumn1, matrixColumn2, matrixColumn3, matrixValues);
        List<Double> eList = new ArrayList<>();
        List<Double> HList = new ArrayList<>();
        List<Double> GList = new ArrayList<>();

        for (int iterator = 0; iterator < xList.size() - 1; iterator++)
        {
            // fix using map as list
            eList.add(fList.get(iterator) - gList.get(iterator + 1)*hList.get(iterator)/6 - gList.get(iterator)*hList.get(iterator)/3);
            GList.add(gList.get(iterator)/2);
            HList.add((gList.get(iterator+1)-gList.get(iterator))/(6*hList.get(iterator)));
        }

        System.out.println("\nFunction coeficients: ");
        for(int iter = 0; iter < eList.size(); iter++)
        {
            System.out.println(HList.get(iter).toString() + " " + GList.get(iter).toString() + " " + eList.get(iter).toString() + " " + yList.get(iter).toString());
        }

        // Calculate x
        Double xValue = 2.2d;
        Integer intervalNumber = 2;
        Double approx = HList.get(intervalNumber)*Math.pow(xValue - xList.get(intervalNumber), 3)+ GList.get(intervalNumber)*Math.pow(xValue - xList.get(intervalNumber), 2) + eList.get(intervalNumber)*(xValue-xList.get(intervalNumber)) + yList.get(intervalNumber);
        System.out.println("\n x = "+ xValue.toString() + " is " + approx.toString());
    }
}
