
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:38:53 2023

@author: santi
"""

import pyomo.environ as pyo


#PARAMETERS
N = [1,2,3,4,5,6,7,8,9]
N_2 = [1,2,3]

I = [0,1,2]
J = [0,1,2]
P = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

v = {(1,1):1, (1,2):1, (1,3):8,
     (2,1):2, (2,2):3, (2,3):3,
     (3,1):3, (3,2):2, (3,3):7,
     #Region 2 
     (4,1):2, (4,2):4, (4,3):6,
     (5,1):3, (5,2):5, (5,3):9,
     #Region 3
     (6,1):3, (6,2):7, (6,3):2,
     #Region 4
     (7,1):4, (7,2):2, (7,3):5,
     #Region 5
     (8,1):4, (8,2):6, (8,3):7,
     (9,1):5, (9,2):5, (9,3):4,
     (10,1):5, (10,2):6, (10,3):5,
     (11,1):6, (11,2):4, (11,3):1,
     #Region 6
     (12,1):5, (12,2):7, (12,3):7,
     (13,1):6, (13,2):8, (13,3):3,
     #Region 7
     (14,1):7, (14,2):3, (14,3):1,
     (15,1):8, (15,2):3, (15,3):8,
     (16,1):9, (16,2):2, (16,3):9,
     #Region 8
     (17,1):8, (17,2):4, (17,3):5,
     #Region 9
     (18,1):7, (18,2):8, (18,3):6,
     (19,1):7, (19,2):9, (19,3):8,
     (20,1):8, (20,2):8, (20,3):1,
     (21,1):9, (21,2):7, (21,3):4}

#ADD THE MODEL CODE, TO CREATE MODEL
model = pyo.ConcreteModel()

#This gives Binary and CREATES THE VARIABLES
model.x = pyo.Var(N,N,N, domain = pyo.Binary)

#OBJECTIVE
def obj_rule(model):
    return 0
model.obj = pyo.Objective(rule=obj_rule,sense=pyo.maximize)

#CONSTRAINTS
#CONSTRAINT 1
#xrcn = 1 for r = 1, . . . , N; c = 1, . . . , N
#Only 1 number in each cell
def OneNumInCell_rule(model,r,c):
    return sum(model.x[r,c,n] for n in N) == 1
model.OneNumInCell = pyo.Constraint(N,N,rule=OneNumInCell_rule)

#CONSTRAINT 2
#xrcn = 1 for r = 1, . . . , N; n = 1, . . . , N
#2. Unique values in each row
def UniqueRow_rule(model,r,n):
    return sum(model.x[r,c,n] for c in N) == 1
model.UniqueRow = pyo.Constraint(N,N,rule=UniqueRow_rule)

#CONSTRAINT 3
#xrcn = 1 for c = 1, . . . , N; n = 1, . . . , N
#3. Unique values in each column
def UniqueColumn_rule(model,c,n):
    return sum(model.x[r,c,n] for r in N) == 1
model.UniqueColumn = pyo.Constraint(N,N,rule = UniqueColumn_rule)

#CONSTRAINT 4
#xr+j√N,c+i√N,n
#4. Unique values in each region
def UniqueValuesInEachRegion_rule(model,i,j,n):
    return sum(model.x[r+(j*3),c+(i*3),n] for r in N_2 for c in N_2) == 1
model.UniqueValuesInEachRegion = pyo.Constraint(I,J,N,rule=UniqueValuesInEachRegion_rule)

#CONSTRAINT 5
#xvp1,vp2,vp3 = 1 for p = 1, . . . , P
#5. Setting pre-filled values
def SettingPreField_rule(model,p):
    return model.x[v[p,1],v[p,2],v[p,3]] == 1
model.SettingPreField = pyo.Constraint(P,rule=SettingPreField_rule)

#Now SOLUTION
#Solve for model
result = pyo.SolverFactory("glpk").solve(model)
l = 0
print('In this Optimal Solution the sudoku answer will be read from top to bottom, from left to right')
print('First number inside the x is row,column and the value (answer) for each cell')
print('I left the one on them to verify it is the correct answer for each cell, for ease of mind while I tested it')
print('Happy Easter!')

if result.solver.termination_condition == pyo.TerminationCondition.optimal:
    print(f"Optimal value: {pyo.value(model.obj)}")
    print("Optimal Solution:")
    for r in N:
        for c in N:
            for n in N:
                if pyo.value(model.x[r,c,n]) == 1:
                    print(f"x[{r,c,n}] = {pyo.value(model.x[r,c,n])}")
                    l +=1
    print('Variable l is just to confirm that it prints all correct 81 cells. Test:',l)