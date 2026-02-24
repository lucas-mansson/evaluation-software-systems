import java.io.*;
import java.util.*;

public class Measure {
    public static void main(String args[]) {
        String inputFile = args[0];
        String outputFile = args[1];
        int n = Integer.parseInt(args[2]);
		String algo = args[3];


        LinkedList<Integer> numbers = read(inputFile);
        try (PrintWriter writer = new PrintWriter(new FileWriter(outputFile))) {

            writer.println("index,time");
			if(algo.equals( "own")){
				for (int i = 0; i < n; i++) {
					LinkedList<Integer> temp1 = new LinkedList<>(numbers);
					long start = System.nanoTime();

					sortOwn(temp1);

					long end = System.nanoTime();
					temp1 = new LinkedList<>(numbers);

					long timeForNoimp = end - start;
					writer.println(i + "," + timeForNoimp);
				}
			} else {
				for (int i = 0; i < n; i++) {
					LinkedList<Integer> temp1 = new LinkedList<>(numbers);
					long start = System.nanoTime();

					sortC(temp1);

					long end = System.nanoTime();
					temp1 = new LinkedList<>(numbers);

					long timeForNoimp = end - start;
					writer.println(i + "," + timeForNoimp);
				}	
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
        LinkedList<Integer> temp = ListSorter.mergeSort(list);
        return temp;
    }
    private static boolean isSorted(LinkedList<Integer> list){
        for (int i = 0; i < list.size() - 1; i++) {
            if (list.get(i) > list.get(i + 1)) return false;
        }
        return true;
    }
    public class ListSorter {
        public static LinkedList<Integer> mergeSort(LinkedList<Integer> list) {
            if (list.size() <= 1) return list;
            int mid = list.size() / 2;
            LinkedList<Integer> left  = new LinkedList<>(list.subList(0, mid));
            LinkedList<Integer> right = new LinkedList<>(list.subList(mid, list.size()));
            left  = mergeSort(left);
            right = mergeSort(right);
            return merge(left, right);
        }
        private static LinkedList<Integer> merge(LinkedList<Integer> left, LinkedList<Integer> right) {
            LinkedList<Integer> result = new LinkedList<>();
            while (!left.isEmpty() && !right.isEmpty()) {
                if (left.peek() <= right.peek()) {
                    result.add(left.poll());
                } else {
                    result.add(right.poll());
                }
            }
            result.addAll(left);
            result.addAll(right);
            return result;
        }
    }
}
