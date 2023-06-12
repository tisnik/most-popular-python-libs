class Ovoce {
}

class Hruska extends Ovoce {
    public String toString() {
        return "Hruska";
    }
}

class Jablko extends Ovoce {
    public String toString() {
        return "Jablko";
    }
}

public class Variance2 {
    public static void smichej(Ovoce[] kosik) {
        kosik[0] = new Hruska();
        kosik[1] = new Jablko();
    }

    public static void main(String[] args) {
        Ovoce[] kosik = new Hruska[2];
        smichej(kosik);

        for (Ovoce ovoce:kosik) {
            System.out.println(ovoce);
        }
    }
}
