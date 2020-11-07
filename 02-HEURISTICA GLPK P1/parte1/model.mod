# Modelo parte1 practica 1 en MathProg-GLPK 

/* Conjuntos de datos */
set AVIONES;
set BILLETES;
set BILLETES_MIN within BILLETES;

/* Parametros */
param asientos {i in AVIONES};
param carga_aviones {i in AVIONES};
param precio_billetes {i in BILLETES};
param carga_billetes {i in BILLETES};
param min_billetes {i in BILLETES_MIN};
param porcentaje_estandar;

/* Variables de decision, en nuestro caso el numero de billetes */
var units {i in BILLETES,j in AVIONES} integer, >=0;

/* Funcion objetivo: Maximizar los beneficios de la compañia con los billetes vendidos */
maximize beneficio: sum{i in BILLETES,j in AVIONES} units[i,j]*precio_billetes[i];

/******** Restricciones ********/

/* Al menos el 60% de todos los billetes vendidos debe ser estandar */
s.t. pbilletes_estandar: sum{i in BILLETES,j in AVIONES} units[i,j]*porcentaje_estandar <= sum{k in AVIONES} units['estandar',k];

/* Numeros minimo billetes leisure plus en total */
s.t. min_leisure { j in AVIONES}: units['leisure_plus',j] >= min_billetes['leisure_plus'];

/* Numero minimo billetes business plus en total */
s.t. min_business {j in AVIONES}: units['business_plus',j] >= min_billetes['business_plus'];

/* Numero maximo de asientos por avion */
s.t. max_asientos {j in AVIONES} : sum{ i in BILLETES} units[i,j] <= asientos[j];

/* Numero maximo de carga por avion */
s.t. max_carga {j in AVIONES} : sum{i in BILLETES} units[i,j]*carga_billetes[i]<= carga_aviones[j];

end;