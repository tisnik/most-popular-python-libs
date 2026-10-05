import scipy.datasets as datasets

import numpy as np

# načtení signálu
ekg = datasets.electrocardiogram()

# zobrazení základních informací o signálu
np.info(ekg)
