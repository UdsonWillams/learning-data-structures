public class IdadeEmDias {

    private int idadeDias;

    int calcIdadeEmDias;
    int diasAMais;

    public IdadeEmDias(){}

    public IdadeEmDias(int idadeDias){
        this.idadeDias = idadeDias;
    }

    public int calculaIdadeEmDias(int calcIdadeEmDias){
        calcIdadeEmDias = calcIdadeEmDias * 365;
        return calcIdadeEmDias;
    }

    public int getIdadeDias(){
        return idadeDias;
    }
    public void setIdadeDias(){
        this.setIdadeDias();
    }
}
