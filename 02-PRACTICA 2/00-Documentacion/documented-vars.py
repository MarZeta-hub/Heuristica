#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# documented-vars.py
# Description: 
# -----------------------------------------------------------------------------
#
# Login   <carlos.linares@uc3m.es>
#

"""

"""

from constraint import *

problem=Problem ()

variables = {'a': 'the value of my first variable is',
             'b': 'and my second variable gets'}
problem.addVariables (variables, range (10))
problem.addConstraint (ExactSumConstraint(10), variables)

solutions = problem.getSolutions ()
for isolution in solutions:
    for ivariable in variables:
        print ("{0} {1}".format (variables[ivariable], isolution[ivariable]))
    print ()



# Local Variables:
# mode:python
# fill-column:80
# End:
