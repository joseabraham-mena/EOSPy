from EOS.vanderWaals import vanderWaals 
from EOS.ReducedVariables import ReducedVariables
from EOS.Virial import Virial


compounds = ['Acetic acid','Acetone','Benzene','Methane']
vdW = vanderWaals('vdW')
RV = ReducedVariables('RV')
Vi = Virial('Vi')

data = Vi.get_data(compounds)










