import numpy as np
import scipy.datasets as datasets

# načtení signálu
ekg = datasets.electrocardiogram()

# zobrazení základních informací o signálu
np.info(ekg)
