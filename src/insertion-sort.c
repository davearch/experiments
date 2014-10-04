#include <stdio.h>
#include <string.h> /* duh! */
#include <stdlib.h> /* malloc */


typedef struct myar {
  int len;
  int arr[];
} myar;

myar *buildMyar(int leng, int *vec);
void insertionsort(myar* myartosort);
int printmyar(const myar* myartoprint);

int main() {
  int i;
  int A[6] = {5, 2, 4, 6, 1, 3};
  myar *mainar = buildMyar(6, A);
  printf("UNSORTED:\n");
  if((i = printmyar(mainar)) != 0){
    printf("error on print");
  }
  insertionsort(mainar);
  return 0;
}

myar *buildMyar(int leng, int *vec) {
  myar *newMyar;
  if((newMyar = (myar *)malloc(sizeof(struct myar) + leng * sizeof(int))) == NULL)
    exit(0);
  newMyar->len = leng;
  int i;
  for (i = 0; i < leng; ++i)
    newMyar->arr[i] = *(vec + i);
  return newMyar;
}

void insertionsort(myar* myartosort) {
  /* j    -> length of array;
     i    -> loop counter;
     A[j] -> Initialized array with length j; */
  int *pj = &myartosort->len;
  int i = 0, b, rc;
  int A[*pj];

  if (*pj == 0) exit(1);

  while (i < *pj) {
    A[i] = myartosort->arr[i];
    ++i;
  }
  for (i = 1; i < *pj; ++i) {
    int key = A[i];
    /* Insert A[i] into the sorted sequence A[0..j-1]. */
    b = i - 1;
    while (b >= 0 && A[b] > key) {
      A[b + 1] = A[b];
      b = b - 1;
    }
    A[b + 1] = key;
  }
  myar *sorted = buildMyar(*pj, A);
  printf("SORTED:\n");
  if ((rc = printmyar(sorted)) != 0){
    printf("error on printmyar");
  }
}

int printmyar(const myar* artoprint) {
  if (artoprint == NULL){
    return 1;
  }
  for (int i = 0; i < artoprint->len; ++i)
    printf("array[%d] = %d\n",i,artoprint->arr[i]);
  printf("\n\n");
  return 0;
}
