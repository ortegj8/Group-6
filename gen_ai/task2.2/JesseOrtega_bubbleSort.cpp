/**
 * ============================================================
 *                       Bubble Sort 🫧
 * ============================================================
 * Autor: Jesse Ortega
 * Descripción: Implementación del algoritmo de ordenamiento Bubble Sort.
 *              Este algoritmo ordena un arreglo iterativamente comparando
 *              pares de elementos adyacentes y los intercambia si están
 *              en el orden incorrecto. Se repite hasta que el arreglo
 *              esté completamente ordenado.
 *
 * Ventajas:
 * - Fácil de implementar.
 * - Útil para pequeños conjuntos de datos.
 *
 * Desventajas:
 * - Ineficiente para grandes conjuntos de datos (O(n²)).
 * - No es el algoritmo de ordenamiento más óptimo.
 *
 * 🫧 Representación Visual del Bubble Sort 🫧
 *
 * Un ejemplo con el arreglo [5, 3, 8, 4, 2]
 * Iteración 1:
 *      [5, 3, 8, 4, 2] -> [3, 5, 8, 4, 2] (se intercambia 5 y 3)
 *      [3, 5, 8, 4, 2] -> [3, 5, 8, 4, 2] (no se intercambia 8 y 5)
 *      [3, 5, 8, 4, 2] -> [3, 5, 4, 8, 2] (se intercambia 8 y 4)
 *      [3, 5, 4, 8, 2] -> [3, 5, 4, 2, 8] (se intercambia 8 y 2)
 *
 * Iteración 2:
 *      [3, 5, 4, 2, 8] -> [3, 5, 4, 2, 8] (no se intercambia 3 y 5)
 *      [3, 5, 4, 2, 8] -> [3, 4, 5, 2, 8] (se intercambia 5 y 4)
 *      [3, 4, 5, 2, 8] -> [3, 4, 2, 5, 8] (se intercambia 5 y 2)
 *
 * ... y así sucesivamente hasta que el arreglo esté ordenado.
 *
 * ============================================================
 */

 #include <iostream>

 /**
  * Función bubbleSort
  * -------------------
  * Implementa el algoritmo de ordenamiento Bubble Sort.
  *
  * @param arr[] - Arreglo de enteros a ordenar.
  * @param n - Número de elementos en el arreglo.
  */
 void bubbleSort(int arr[], int n) {
     for (int i = 0; i < n - 1; i++) {  // Recorre todo el arreglo n-1 veces
         for (int j = 0; j < n - i - 1; j++) { // Compara elementos adyacentes
             if (arr[j] > arr[j + 1]) { // Si el actual es mayor que el siguiente, se intercambian
                 int temp = arr[j];
                 arr[j] = arr[j + 1];
                 arr[j + 1] = temp;
             }
         }
     }
 }
 
 /**
  * Función printArray
  * -------------------
  * Imprime los elementos de un arreglo en una sola línea.
  *
  * @param arr[] - Arreglo de enteros a imprimir.
  * @param n - Número de elementos en el arreglo.
  */
 void printArray(int arr[], int n) {
     for (int i = 0; i < n; i++) {
         std::cout << arr[i] << " ";
     }
     std::cout << std::endl;
 }
 
 /**
  * Función principal main
  * ----------------------
  * Punto de entrada del programa. Define un arreglo de prueba,
  * lo ordena usando Bubble Sort y muestra el resultado.
  */
 int main() {
     int arr[] = {64, 34, 25, 12, 22, 11, 90};  // Arreglo de prueba
     int n = sizeof(arr) / sizeof(arr[0]);  // Calcula el número de elementos
     
     std::cout << "Arreglo original: \n";
     printArray(arr, n);
     
     bubbleSort(arr, n);  // Ordena el arreglo
     
     std::cout << "Arreglo ordenado: \n";
     printArray(arr, n);
     
     return 0;
 }
 