Providers Supported by qbitkit
==============================
Currently, qbitkit supports the folowing
quantum service vendors:

* Amazon Web Services Braket
    * US Pricing Formula: :math:`p=.3t(sv)`
        * Where :math:`p` is the total cost, :math:`t` is the number of quantum tasks successfully submitted to an AWS braket hardware device, :math:`s` is the number of shots or 'reads' for a given quantum circuit or annealing problem, and :math:`v` is the vendor-specific cost per-shot or per-'read'.
    * Supports ``qbitkit.anneal`` for D-Wave 2000Q as well as the brand-new Advantage System v1 with over 5000 qubits and 35,000 Josephson Junction couplers, cooled to an insanely cold :math:`.01mK`.
    * Supports ``qbitkit.circuit`` for AWS simulators, as well as industry-leading hardware from Rigetti and IonQ