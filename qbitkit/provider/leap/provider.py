from dwave.system import DWaveSampler as __DWSampler__
from dwave.system import DWaveCliqueSampler as __DWCSampler__
from dwave.system import LeapHybridSampler as __LHSampler__
from dwave.system import LeapHybridDQMSampler as __LHDQMSampler__


class Annealing:
    def get_sampler(sampler=str('DWaveSampler'),
                    retry_interval=int(-1)):
        """Create a new D-Wave Sampler based on a specified sampler type.

        Args:
            sampler(str): D-Wave Sampler as a string. Can be 'DWaveSampler', 'DWaveCliqueSampler', 'LeapHybridSampler', or 'LeapHybridDQMSampler.' (default str('DWaveSampler'))
            retry_interval(int): Interval in seconds to retry, or -1 to propogate SolverNotFound error to user (default int(-1))
        Returns:
            dimod.meta.SamplerABCMeta: A D-Wave Ocean SDK Plugin Sampler"""

        new_sampler = None
        if sampler == 'DWaveSampler':
            new_sampler = __DWSampler__(retry_interval=retry_interval)
        elif sampler == 'DWaveCliqueSampler':
            new_sampler = __DWCSampler__(retry_interval=retry_interval)
        elif sampler == 'LeapHybridSampler':
            new_sampler = __LHSampler__(retry_interval=retry_interval)
        elif sampler == 'LeapHybridDQMSampler':
            new_sampler == __LHDQMSampler__(retry_interval=retry_interval)
        else:
            new_sampler = None
        return new_sampler
