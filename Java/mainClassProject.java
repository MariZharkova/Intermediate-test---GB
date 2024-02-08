import java.io.IOException;
import java.util.Arrays;
import java.io.FileWriter;
import java.io.BufferedWriter;

public class mainClassProject {
    public static void main(String[] args) throws IOException {
        System.out.println("Welcome to the Toy Shop.");
        ToyStore store = new ToyStore(Arrays.asList("1 Ball 6", "2 Chess 2"));
        store.put("3 BabyDoll 4");
        store.put("4 Plane 5");
        store.put("5 Puzzles 7");
        store.put("6 Cubes 3");
        store.put("7 TeddyBear 4");
        store.put("8 Robot 2");
        BufferedWriter writer = new BufferedWriter(new FileWriter("store_out.txt", false));
        for (Integer i=0; i < 10; i++) {
            writer.write(Integer.toString(i + 1) + " : " + store.get() + "\n");
        }
        writer.close();
    }
}

