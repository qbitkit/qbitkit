import itertools
from itertools import combinations
from dwave.system.composites import EmbeddingComposite
from braket.ocean_plugin import BraketDWaveSampler
import time
from datetime import datetime as dt
import pandas as pd
import dimod
from math import log2, floor