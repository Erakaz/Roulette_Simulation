from pulp import *

# Création du problème
prob = LpProblem("Optimisation_Roulette", LpMaximize)

# Variables de décision (mises sur chaque type de pari)
x1 = LpVariable("Rouge", 0, cat="Integer")
x2 = LpVariable("Numero", 0, cat="Integer")
x3 = LpVariable("Pair", 0, cat="Integer")
x4 = LpVariable("Douzaine", 0, cat="Integer")

# Fonction objectif : gain espéré
prob += 0.973 * x1 + 0.946 * x2 + 0.973 * x3 + 0.973 * x4

# Contrainte de budget
prob += x1 + x2 + x3 + x4 <= 100

# Résolution
prob.solve()

# Affichage des résultats
print("Statut:", LpStatus[prob.status])
for v in prob.variables():
    print(f"{v.name} = {v.varValue}")
print("Gain espéré max:", value(prob.objective))
