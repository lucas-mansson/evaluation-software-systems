import java.io.*;
import java.util.*;

public class Measure {
    public static void main(String args[]) {
        String inputFile = args[0];
        String outputFile = args[1];
        int n = Integer.parseInt(args[2]);

        LinkedList<Integer> numbers = read(inputFile);
        try (PrintWriter writer = new PrintWriter(new FileWriter(outputFile))) {

            writer.println("index,time");

            for (int i = 0; i < n; i++) {
                LinkedList<Integer> temp1 = new LinkedList<>(numbers);
                long start = System.nanoTime();

                sortC(temp1);

                long end = System.nanoTime();
                temp1 = new LinkedList<>(numbers);

                long timeForNoimp = end - start;
                writer.println(i + "," + timeForNoimp);
            }

        } catch (IOException e) {
            System.out.println("Error writing file: " + e.getMessage());
        }
    }

    public static LinkedList<Integer> read(String inputFile) {
        LinkedList<Integer> numbers = new LinkedList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
            String line;
            while ((line = br.readLine()) != null) {
                numbers.add(Integer.parseInt(line.trim()));
            }
        } catch (IOException e) {
            System.out.println("Fel vid läsning av fil: " + e.getMessage());
            return null;
        }
        return numbers;
    }

    public static LinkedList<Integer> sortC(LinkedList<Integer> list) {
        Collections.sort(list);
        return list;
    }

    public static LinkedList<Integer> sortOwn(LinkedList<Integer> list) {
        ListSorter.sort(list);
        return list;
    }

    public class ListSorter {

        public static LinkedList<Integer> sort(LinkedList<Integer> list) {

            LinkedList<Integer> sorted = new LinkedList<>();

            for (Integer value : list) {

                if (sorted.isEmpty()) {
                    sorted.add(value);
                    continue;
                }

                int index = 0;
                while (index < sorted.size() && sorted.get(index) <= value) {
                    index++;
                }

                sorted.add(index, value);
            }
            return sorted;
        }
    }
}
