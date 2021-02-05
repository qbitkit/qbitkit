from dwave.plugins.qiskit import DWaveMinimumEigensolver as __dwmes__
from qiskit.aqua.algorithms import NumPyMinimumEigensolver as __npmes__
from qbitkit.anneal.embed import composite as __ec__


class Solve:
    def get_solver(self='DWaveMinimumEigensolver'):
        """Get a D-Wave MinimumEigensolver, or NumPyMinimumEigensolver.
        Args:
            self(str): Solver Type to use. Can be DWaveMinimumEigensolver, or NumPyMinimumEigensolver. (default 'DWaveMinimumEigensolver')
        Returns:
            qiskit.aqua.algorithms.minimum_eigen_solvers: A MinimumEigensolver"""
        # Check if specified Solver Type is DWaveMinimumEigensolver.
        if self == 'DWaveMinimumEigensolver':
            # Use DWaveMinimumEigensolver() as solver.
            solver = __dwmes__
        # Check if specified Solver Type is NumPyMinimumEigensolver.
        elif self == 'NumPyMinimumEigensolver':
            # Use NumPyMinimumEigensolver as solver.
            solver = __npmes__
        else:
            # Give error if invalid Solver Type specified.
            print(f"[Error] Invalid Solver Type: {str(self)}.")
        return solver
    def sampler(self=None,
                sampler=None,
                shots=int(1000)):
        """Solve a weighted Pauli operator.

        Args:
            self(qiskit.aqua.operators.legacy.weighted_pauli_operator.WeightedPauliOperator): Weighted Pauli Operator to solve. (default None)
            sampler(dimod.meta.SamplerABCMeta): D-Wave Sampler to sample Weighted Pauli Operator. (default None)
            shots(int): Number of shots (reads) to take when solving. Larger problems need larger numbers of shots. (default 1000)
        Returns:
            qiskit.aqua.algorithms.minimum_eigen_solvers.minimum_eigen_solver.MinimumEigensolverResult: Sampled Eigenstates and Eigenvalues."""
        # Create an EmbeddedSampler based on the specified D-Wave Sampler.
        emb_samp = __ec__(sampler)
        # Sample the Weighted Pauli Operator.
        sample = __dwmes__(self,
                           sampler=emb_samp,
                           num_reads=shots)
        # Return the data read from the QPU.
        return sample

    def numpy(self=None):
        """Solve a Weighted Pauli Operator using Numpy.
        Args:
            self(qiskit.aqua.operators.legacy.weighted_pauli_operator.WeightedPauliOperator): Weighted Pauli Operator to attempt to solve. (default None)
        Returns:
            qiskit.aqua.operators.legacy.weighted_pauli_operator.WeightedPauliOperator: Exact solution to specified Weighted Pauli Operator."""
        # Try Solving Weighted Pauli Operator
        # This will not work for large-scale problems and may produce interesting/funny error messages from Numpy.
        attempt_that_likely_will_fail = __npmes__(self)
        # In case we actually are able to solve the Weighted Pauli Operator, return the exact solution.
        return attempt_that_likely_will_fail
