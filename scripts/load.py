import os
import table.models as TM

path = os.path.curdir
def writeDataFromCSV(model,filepath, header = False):
    file = open(filepath)
    model.objects.all().delete()
    for line in file.readlines():
        if(header):
            header = False
        else:
            model.objects.create(name = line[:-1])
    
models_files = {TM.WagonType: 'WagonType.txt', 
                TM.CargoType: 'CargoType.txt',
                TM.WagonAssembly: "WagonAssembly.txt",
                TM.WagonComponent: "WagonComponent.txt",
                TM.WagonDefect: "WagonDefect.txt",
                TM.EmployeeName: "EmployeeName.txt"}

def run():
    for model in models_files:
        writeDataFromCSV(model, path + "/scripts/" + models_files[model])
    TM.WagonStatus.objects.all().delete()
    TM.WagonStatus.objects.create(name = True)
    TM.WagonStatus.objects.create(name = False)