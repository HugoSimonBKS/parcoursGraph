#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <stdbool.h>

/*
  type permettant de definir un élément de la file
*/

typedef struct Element Element;
struct Element
{
    int nombre;
    Element *suivant;
};

/*
  type permettant de definir le debut de la file
*/

typedef struct File File;
struct File
{
    Element *premier;
};

/*
  type permettant de definir un arbre
*/

typedef struct Arbre Arbre;
struct Arbre{
  Arbre *predecesseur;
  Arbre *successeur;
  int valeur;
};

/*  FONCTIONS */

void enfiler(File *file, int nvNombre)
{
    Element *nouveau = malloc(sizeof(*nouveau));
    if (file == NULL || nouveau == NULL)
    {
        exit(EXIT_FAILURE);
    }

    nouveau->nombre = nvNombre;
    nouveau->suivant = NULL;

    if (file->premier != NULL) /* La file n'est pas vide */
    {
        /* On se positionne à la fin de la file */
        Element *elementActuel = file->premier;
        while (elementActuel->suivant != NULL)
        {
            elementActuel = elementActuel->suivant;
        }
        elementActuel->suivant = nouveau;
    }
    else /* La file est vide, notre élément est le premier */
    {
        file->premier = nouveau;
    }
}

/* fonction pour afficher la file resultante */
void afficherFile(File *file){
  Element *prem = File->premier;
  if(prem != NULL){
    while(prem->suivant != NULL){
      printf("[%d]",prem->nombre );
      prem = prem->suivant;
    }
  }
  else{
    printf("cette file est vide");
  }
}



int main(){
  return 0;
}
