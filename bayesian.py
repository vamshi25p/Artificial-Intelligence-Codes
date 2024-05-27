from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define the network structure
model = BayesianNetwork([('Disease', 'Test'), ('Disease', 'Symptom')])

# Step 2: Define the CPDs
cpd_disease = TabularCPD(variable='Disease', variable_card=2, values=[[0.01], [0.99]])
cpd_test = TabularCPD(variable='Test', variable_card=2,
                      values=[[0.99, 0.05], [0.01, 0.95]],
                      evidence=['Disease'], evidence_card=[2])
cpd_symptom = TabularCPD(variable='Symptom', variable_card=2,
                         values=[[0.8, 0.1], [0.2, 0.9]],
                         evidence=['Disease'], evidence_card=[2])

# Step 3: Add the CPDs to the network
model.add_cpds(cpd_disease, cpd_test, cpd_symptom)

# Step 4: Check if the model is valid
assert model.check_model()

# Step 5: Perform inference
infer = VariableElimination(model)

# Example queries:
prob_disease_given_symptom = infer.query(variables=['Disease'], evidence={'Symptom': 1})
prob_disease_given_test = infer.query(variables=['Disease'], evidence={'Test': 1})

print(prob_disease_given_symptom)
print(prob_disease_given_test)
