from skin import Skin
from skin_analyst import SkinAnalyst
from momentum_indicators import *

if __name__ == '__main__':
    test_skin = Skin(name='Gamma 2 Case', app_id=730)
    analyst = SkinAnalyst(test_skin)
    analyst.get_graphs([RSI, ROC, STOCH])

