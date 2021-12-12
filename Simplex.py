# Linear optimization example for the following
# optimization problem
#
# maximize:     z = x + 2y
# subject to:   2x + y <= 20
#               -4x + 5y <= 10
#               -x + 2y >= -2
#               -x + 5y = 15
#               x, y >= 0
#
# Modify problem to:
# minimize:     -z = -x - 2y
# subject to:   2x + y <= 20    (1)
#               -4x + 5y <= 10  (2)
#               x - 2y <= 2     (3)
#               -x + 5y = 15    (4)
#               x, y >= 0       (5)



from scipy.optimize import linprog

obj = [-3, -1, -2]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x


lhs_ineq = [[1, 1, 3],         # constraint (1), left
            [2, 2, 5],        # constraint (2), left
            [4, 1, 2],
            ]        # constraint (2), left

rhs_ineq = [30,             # constraint (1), right
            24,             # constraint (2), right
            36
            ]              # constraint (3), right

lhs_eq = [[]]          # constraint (4), left
rhs_eq = []               # constraint (4), right

bnd = [(0, float("inf")),  # Bounds of x
       (0, float("inf")),
       (0, float("inf"))]  # Bounds of y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
                  method="simplex")

print(opt)