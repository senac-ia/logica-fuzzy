# exemplo retirado de
# https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
tip = ctrl.Consequent(np.arange(0, 25, 1), 'gorjeta')

# Auto-membership function population is possible with .automf(3, 5, or 7)
names = ['ruim', "medio", "bom"]
quality.automf(names=names)
service.automf(names=names)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
# https://pythonhosted.org/scikit-fuzzy/api/skfuzzy.membership.html
# trimf => Função triangular
tip['baixa'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['media'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['alta'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Regras de inferências
rule1 = ctrl.Rule(quality['ruim'] | service['ruim'], tip['baixa'])
rule2 = ctrl.Rule(service['medio'], tip['media'])
rule3 = ctrl.Rule(service['bom'] | quality['bom'], tip['alta'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Processamento
tipping.input['qualidade'] = 6.5
tipping.input['servico'] = 9.8

tipping.compute()

"""
Once computed, we can view the result as well as visualize it.
"""

print(tipping.output['gorjeta'])