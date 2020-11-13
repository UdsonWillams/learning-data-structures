import java.util.Scanner;

public class Num1 {

    public static void main(String[] args) {
        IdadeEmDias idadeDias = new IdadeEmDias();
        int idade;
        int idadeEmDias;
        Scanner sc = new Scanner(System.in);

        System.out.println("Qual a sua idade? ");
        idade = sc.nextInt();
        idadeEmDias = idadeDias.calculaIdadeEmDias(idade);
        System.out.println("Sua idade é " + idade + "E em dias é: " + idadeEmDias);
    }
}
