from dwave.system import DWaveSampler as __DWSampler__
from dwave.system import DWaveCliqueSampler as __DWCSampler__
from dwave.system import LeapHybridSampler as __LHSampler__
from dwave.system import LeapHybridDQMSampler as __LHDQMSampler__


class Annealing:
    def get_sampler(self=str('DWaveSampler'),
                    retry_interval=int(-1)):
        """Create a new D-Wave Sampler based on a specified sampler type.

        Args:
            self(str): D-Wave Sampler as a string. Can be 'DWaveSampler', 'DWaveCliqueSampler', 'LeapHybridSampler', or 'LeapHybridDQMSampler.' (default str('DWaveSampler'))
            retry_interval(int): Interval in seconds to retry, or -1 to propogate SolverNotFound error to user (default int(-1))
        Returns:
            dimod.meta.SamplerABCMeta: A D-Wave Ocean SDK Plugin Sampler"""

        # Initialize variable 'new_sampler'
        new_sampler = None
        # Check if requested sampler is DWaveSampler
        if self == 'DWaveSampler':
            # Create a DWaveSampler
            new_sampler = __DWSampler__(retry_interval=retry_interval)
        # Check if requested samlper is DWaveCliqueSampler
        elif self == 'DWaveCliqueSampler':
            # Create a DWaveCliqueSampler
            new_sampler = __DWCSampler__(retry_interval=retry_interval)
        # Check if requested sampler is LeapHybridSampler
        elif self == 'LeapHybridSampler':
            # Create a LeapHybridSampler
            new_sampler = __LHSampler__(retry_interval=retry_interval)
        elif self == 'LeapHybridDQMSampler':
            # Create a LeapHybridDQMSampler
            new_sampler == __LHDQMSampler__(retry_interval=retry_interval)
        # Check if sampler does not meet any of the above conditions
        else:
            # Set sampler to return as None
            new_sampler = None
        # Return the sampler we just created
        return new_sampler
