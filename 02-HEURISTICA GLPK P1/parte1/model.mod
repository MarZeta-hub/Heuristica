# Modelo parte1 practica 1

/*Sets, se cargan*/
set AVIONES;
set BILLETES;
set BILLETES_MIN within BILLETES;

/*parameters */
param asientos {i in AVIONES};
param carga_aviones {i in AVIONES};
param precio_billetes {i in BILLETES};
param carga_billetes {i in BILLETES};

/*aqui las variables no estan a i */
param min_billetes {i in BILLETES_MIN};
param porcentaje_estandar;

/* variables de decision, en nuestro caso el numero de billetes */
var units {i in BILLETES,j in AVIONES} integer, >=0;

/*Funcion objetivo */
maximize beneficio: sum{i in BILLETES,j in AVIONES} units[i,j]*precio_billetes[i];

/*Restricciones*/

/*Al menos el 60% de todos los billetes vendidos debe ser estandar*/
s.t. pbilletes_estandar: sum{i in BILLETES,j in AVIONES} units[i,j]*porcentaje_estandar <= sum{k in AVIONES} units['estandar',k];

/*BORRAR LO DE ABAJO*/
#s.t. total : sum{i in BILLETES, j in AVIONES} units[i,j]<=600;

/*minimo billetes leisure plus */
s.t. min_leisure { j in AVIONES}: units['leisure_plus',j] >= 20;

s.t. min_business {j in AVIONES}: units['business_plus',j] >= 10;

/* restriccion maximo de asientos*/
s.t. max_asientosa1 : sum{ i in BILLETES} units[i,'a1'] <=90;
s.t. max_asientosa2 : sum{ i in BILLETES} units[i,'a2'] <=120;
s.t. max_asientosa3 : sum{ i in BILLETES} units[i,'a3'] <=200;
s.t. max_asientosa4 : sum{ i in BILLETES} units[i,'a4'] <=150;
s.t. max_asientosa5 : sum{ i in BILLETES} units[i,'a5'] <=190;


/* restriccion maximo de carga por avion*/
s.t. max_cargaa1 : sum{i in BILLETES} units[i,'a1']*carga_billetes[i]<=1700;
s.t. max_cargaa2 : sum{i in BILLETES} units[i,'a2']*carga_billetes[i]<=2700;
s.t. max_cargaa3 : sum{i in BILLETES} units[i,'a3']*carga_billetes[i]<=1300;
s.t. max_cargaa4 : sum{i in BILLETES} units[i,'a4']*carga_billetes[i]<=1700;
s.t. max_cargaa5 : sum{i in BILLETES} units[i,'a5']*carga_billetes[i]<=2000;


/*TODO CAMBIAR LOS NUMEROS DE LAS RESTRICCIONES PARA QUE SEA GENERALIZABLE DESDE EL .DAT*/
end;

