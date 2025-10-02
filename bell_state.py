# This sample creates a Bell state with 2 qubits

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate to the first qubit
qc.h(0)

# Apply CNOT gate with first qubit as control and second as target
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1000).result()
counts = result.get_counts(qc)

# Plot the results
plot_histogram(counts)