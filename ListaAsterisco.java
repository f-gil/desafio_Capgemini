import java.util.*;

public class ListaAsterisco {
    public static void main(String[] args) {
        Scanner ïnput = new Scanner(System.in);
        int nEspacos = ïnput.nextInt();
        List<String> listaEspaco = new ArrayList<>(Collections.nCopies(nEspacos, " "));

        for (int i = nEspacos - 1; i >= 0; i--) {
            listaEspaco.set(i, "*");
            String stringEspacoAsterisco = String.join("", listaEspaco);
            System.out.println(stringEspacoAsterisco);
        }

    }

}
