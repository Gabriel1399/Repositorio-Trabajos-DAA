/**
 *
 * @author gabri
 */
public class Palíndromos {
    
    public static boolean esPalindromo(String cadena) {
		
    // Invertir la cadena, y si es igual que la original entonces
    // son palíndromos
    String invertida = new StringBuilder(cadena).reverse().toString();	
    return invertida.equals(cadena);
	}
    public static void main(String[] args) {
        String horas[] = {"00:", "01:", "02:", "03:", "04:", "05:", "06:", "07:", "08:", "09:", "10:",
                                "11:", "12:", "13:", "14:", "15:", "16:", "17:", "18:", "19:", "20:",
                                "21:", "22:", "23:"};
        String minutos[] = {"00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                  "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", 
                                  "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                                  "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                                  "51", "52", "53", "54", "55", "56", "57", "58", "59"};
        String horaMinuto;
        int numPalindromos = 0;
        for(int i = 0; i < horas.length; i++){
            for(int j = 0; j < minutos.length; j++){
                horaMinuto = horas[i].concat(minutos[j]);
                if(esPalindromo(horaMinuto)){
                    System.out.println(horaMinuto);
                    numPalindromos++;
                }
            }
        }
        System.out.println("Numero de palindromos encontrados: " + numPalindromos);
        
    }
}
