Providers Supported by qbitkit
==============================
Currently, qbitkit supports the folowing
quantum service vendors:

* Amazon Web Services Braket
    * US Pricing Formula: :math:`p=.3t(sv)`
        * Where :math:`p` is the total cost, :math:`t` is the number of quantum tasks successfully submitted to an AWS braket hardware device, :math:`s` is the number of shots or 'reads' for a given quantum circuit or annealing problem, and :math:`v` is the vendor-specific cost per-shot or per-'read'.
    * Supports ``qbitkit.anneal`` for D-Wave 2000Q as well as the brand-new Advantage System v1 with over 5000 qubits and 35,000 Josephson Junction couplers, cooled to an insanely cold :math:`.01mK`.
    * Supports ``qbitkit.circuit`` for AWS simulators, as well as industry-leading hardware from Rigetti and IonQ

* IBM Quantum Experience
    * US Pricing Formula:
        * Free for public machines
        * IBM does not publicly list the pricing of priority access to public systems or access to systems not available to the public.
    * Supports ``qbitkit.circuit`` for IBMQ Cloud simulators, as well as whatever IBM Q hardware your account has access to.

* D-Wave Leap
    * US Pricing Formula:
        * :math:`p=s+2000h`
            * Where :math:`p` is total cost, :math:`s` is any applicable taxes, and :math:`h` is the amount of time spent actively using any quantum annealing hardware.
            * Customers with a Canada-based billing address don't seem to be subject to tax, so if you live in Canada make sure to use :math:`s=0` in the above pricing formula.
            * *psst* AWS Braket is cheaper for small experiments and doesn't require a monthly plan
    * Supports ``qbitkit.anneal`` for D-Wave 2000Q as well as the brand-new Advantage System v1 with over 5000 qubits