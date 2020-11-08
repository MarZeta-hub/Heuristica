# Modelo parte2 (Modelo Avanzado) practica 1 en MathProg-GLPK 

/* Conjuntos de datos */
set AVIONES;
set PISTAS;
set SLOTS;

/* Cargamos los parametros */
param inicioSlot {i in SLOTS};
param horaEsperada {i in AVIONES};
param horaLimite {i in AVIONES};
param costeMinuto {i in AVIONES};
param slotsDisponibles {i in PISTAS, j in SLOTS};

/* Parametro correspondiente a la matriz C que representa el coste por slot de tiempo de cada avión */
param costesSlot {i in AVIONES, j in SLOTS} :=  costeMinuto[i]*(inicioSlot[j]-horaEsperada[i]);

/*Variable de decision binaria, saber si a un avion se le asgina un slot */
var asignacionSlot {k in AVIONES, i in PISTAS, j in SLOTS} binary, >= 0;

/* Funcion objetivo: Minimizar los gastos de la compañia con la asignacion correcta de slots a los aviones -> pagar el minimo de coste */
minimize Gastos : sum{k in AVIONES, i in PISTAS, j in SLOTS} asignacionSlot[k,i,j]*costesSlot[k,j];

/******** Restricciones ********/

/* Restriccion: La suma de puertos-slots debe ser 1, cada avion debe tener una pista asignada */
s.t. llegadaAvion {k in AVIONES} : sum{i in PISTAS,j in SLOTS} asignacionSlot[k,i,j] == 1;

/* Restriccion:  Costes positivos y que los aviones lleguen igual o despues a de la hora programada */
s.t. costePositivo {k in AVIONES, i in PISTAS, j in SLOTS } : asignacionSlot[k,i,j]*costesSlot[k,j] >= 0;

/* Restriccion: Un slot solo puede tener un avion asignado */
s.t. unAvionSlot {k in AVIONES, i in PISTAS, j in SLOTS} : asignacionSlot[k,i,j]+slotsDisponibles[i,j] <= 1;

/* Restriccion: Limite de hora de llegada para los aviones */
s.t. limiteHorario {k in AVIONES, i in PISTAS, j in SLOTS} : asignacionSlot[k,i,j]*inicioSlot[j] <= horaLimite[k];

/* Restriccion: No puede haber slots asignados que sean contiguos */
s.t. slotsContiguos  { i in PISTAS, j in SLOTS: j>=2} : sum{k in AVIONES} (asignacionSlot[k,i,j-1] + asignacionSlot[k,i,j]) <= 1;

end;