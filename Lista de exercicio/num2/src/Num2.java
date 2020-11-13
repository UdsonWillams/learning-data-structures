import java.util.Scanner;

public class Num2 {

    public static void main(String[] args) {

        int base, altura;
        Scanner sc = new Scanner(System.in);
        CalculaBaseRetangulo calcular = new CalculaBaseRetangulo();

        System.out.println("Diga a base do Retângulo: ");
        base = sc.nextInt();
        System.out.println("Diga a altura do Retângulo: ");
        altura = sc.nextInt();
        int resultado = calcular.calculaBaseRetangulo(base, altura);

        System.out.println("A area desse Retângulo é: " + resultado);
    }
}
