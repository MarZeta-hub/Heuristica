/* Fusion de ambos modelos de GLPK para la obtencion de los beneficios netos */

# Modelo final en MathProg-GLPK que fusiona el modelo basico y el modelo avanzado 

/* Conjuntos de datos */
set AVIONES;
set BILLETES;
set BILLETES_MIN within BILLETES;
set PISTAS;
set SLOTS;


/* Parametros */
param asientos {i in AVIONES};
param carga_aviones {i in AVIONES};
param precio_billetes {i in BILLETES};
param carga_billetes {i in BILLETES};
param min_billetes {i in BILLETES_MIN};
param porcentaje_estandar;

param inicioSlot {i in SLOTS};
param horaEsperada {i in AVIONES};
param horaLimite {i in AVIONES};
param costeMinuto {i in AVIONES};
param slotsDisponibles {i in PISTAS, j in SLOTS};

/* Parametro correspondiente a la matriz C que representa el coste por slot de tiempo de cada avión */
param costesSlot {i in AVIONES, j in SLOTS} :=  costeMinuto[i]*(inicioSlot[j]-horaEsperada[i]);


/* Variables de decision, Unidades de asientos y asignacion de slots de tiempo a aviones en cada pista */
var units {i in BILLETES,j in AVIONES} integer, >=  0;
var asignacionSlot {k in AVIONES, i in PISTAS, j in SLOTS} binary, >= 0;


/* Funcion objetivo: Maximizar los beneficios netos de la compañia sacando el opmimo numero de billetes a vender de cada tipo menos la configuracion de asignacion de slots que tenga menos gastos */
maximize beneficioNeto : sum{i in AVIONES} ( sum{j in BILLETES}(units[j,i] * precio_billetes[j]) - sum{k in PISTAS, l in SLOTS} (asignacionSlot[i,k,l] * costesSlot[i,l]) );

/******** Restricciones ********/

/* Al menos el 60% de todos los billetes vendidos debe ser estandar */
s.t. pbilletes_estandar : sum{i in BILLETES,j in AVIONES} units[i,j]*porcentaje_estandar <= sum{k in AVIONES} units['estandar',k];

/* Numeros minimo billetes leisure plus en total */
s.t. min_leisure { j in AVIONES} : units['leisure_plus',j] >= min_billetes['leisure_plus'];

/* Numero minimo billetes business plus en total */
s.t. min_business {j in AVIONES} : units['business_plus',j] >= min_billetes['business_plus'];

/* Numero maximo de asientos por avion */
s.t. max_asientos {j in AVIONES} : sum{ i in BILLETES} units[i,j] <= asientos[j];

/* Numero maximo de carga por avion */
s.t. max_carga {j in AVIONES} : sum{i in BILLETES} units[i,j]*carga_billetes[i]<= carga_aviones[j];

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