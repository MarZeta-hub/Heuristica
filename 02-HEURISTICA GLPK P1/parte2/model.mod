/* Modelo parte 2 modelo avanzado */

/* Cargamos los sets */
set AVIONES;
set PISTAS;
set SLOTS;

#set SUBSLOTS within SLOTS;

/* Cargamos los parametros */
param inicioSlot {i in SLOTS};
param horaEsperada {i in AVIONES};
param horaLimite {i in AVIONES};
param costeMinuto {i in AVIONES};
param slotsDisponibles {i in PISTAS, j in SLOTS};

/* Parametro correspondiente a la matriz C que representa el coste por slot de tiempo de cada avión*/
param costesSlot {i in AVIONES, j in SLOTS} :=  costeMinuto[i]*(inicioSlot[j]-horaEsperada[i]) ;

/*Variable de decision*/
var asignacionSlot {k in AVIONES, i in PISTAS, j in SLOTS} binary;

/* Funcion objetivo */
minimize Gastos: sum{k in AVIONES, i in PISTAS, j in SLOTS} asignacionSlot[k,i,j]*costesSlot[k,j];

/*Restricciones */

/* Restriccion dedicada a que la suma de puertos-slots debe ser 1*/
s.t. llegadaAvion {k in AVIONES}: sum{i in PISTAS,j in SLOTS} asignacionSlot[k,i,j] ==1;

/* Restriccion dedicada a que los costes sean positivos y que los aviones lleguen igual o despues a de la hora programada */
s.t. costePositivo {k in AVIONES, i in PISTAS, j in SLOTS }: asignacionSlot[k,i,j]*costesSlot[k,j]>=0;

/* Restriccion un slot solo puede tener un avion asignado */
s.t. unAvionSlot {k in AVIONES, i in PISTAS, j in SLOTS}: asignacionSlot[k,i,j]+slotsDisponibles[i,j]<=1;

/* Restriccion limite de hora de llegada para los aviones */
s.t. limiteHorario {k in AVIONES, i in PISTAS, j in SLOTS}: asignacionSlot[k,i,j]*inicioSlot[j]<=horaLimite[k];

/* Restriccion de no puede haber slots asignados que sean contiguos */
s.t. slotsContiguos  { (k,l) in AVIONES, (i,m) in PISTAS, (j,n) in SLOTS:j<=5}:   asignacionSlot[k,i,j] + asignacionSlot[l,m,n+1] <=1;

end;