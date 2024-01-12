package testegitvscode;

public class JavaHelloWorld {

    static Integer numero = 2;
    private static int numero2;

    public static void main(String args[]) {
        System.out.println("Hello World " + numero);

        numero = 1;
        numero2 = 2;
        Long numero3 = 1l;

        if (numero <= numero2) {
            System.out.println(numero + " <= " + numero2);
        }
        System.out.println("Hello World " + numero2 + numero3);

        System.out.println("Finalizado.");
    }
}