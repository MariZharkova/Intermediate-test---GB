import java.util.*;

class Toy {
    String name;
    Integer weight;

    public Toy(String n, Integer w) {
        name = n;
        weight = w;
    }
}

class ParsingResult {
    Integer id;
    String name;
    Integer weight;
}

public class ToyStore {
    // ID -> Toy mapping
    private HashMap<Integer, Toy> toys;
    public ToyStore (List<String> toysList) {
        toys = new HashMap<Integer, Toy>();
        for (String toy: toysList) {
            ParsingResult parsed = parseToyString(toy);
            toys.put(parsed.id, new Toy(parsed.name, parsed.weight));
        }
    }

    public void put(String toy) {
        ParsingResult parsed = parseToyString(toy);
        toys.put(parsed.id, new Toy(parsed.name, parsed.weight));
    }

    public String get() {
        ArrayList<Integer> toys_queue = new ArrayList<>();
        for (Map.Entry<Integer, Toy> entry: toys.entrySet()) {
            toys_queue.addAll(Collections.nCopies(entry.getValue().weight, entry.getKey()));
        }
        Random rand = new Random();
        return toys.get(toys_queue.get(rand.nextInt(toys_queue.size()))).name;
    }

    private ParsingResult parseToyString (String str) {
        String[] split = str.split("\\s+");
        if (split.length != 3) {
            throw new RuntimeException("Wrong number of arguments.");
        }
        ParsingResult result = new ParsingResult();
        try {
            result.id = Integer.parseInt(split[0]);
        } catch (NumberFormatException e) {
            throw new RuntimeException("Failed to parse ID '" + split[0] + "'. Error: " + e.toString());
        }
        result.name = split[1];
        try {
            Integer weight = Integer.parseInt(split[2]);
            if (weight < 0 || weight > 100) {
                throw new RuntimeException("Weight should be a number from interval 1 .. 100");
            }
            result.weight = weight;
        } catch (NumberFormatException e) {
            String err = "Failed to parse ID '" + split[0] + "'. Error: " + e.toString();
            throw new RuntimeException(err);
        }

        return result;
    }
}
