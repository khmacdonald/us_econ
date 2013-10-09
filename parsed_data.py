i = open("US_GDP.txt","r")
i_l = i.readlines()
i.close()

title = i_l[0]
strd = i_l[2:]

# Parse out data into different arrays
year = [] # The year 
nGDP = [] # Nominal GDP
rGDP = [] # Real GDP
GDPd = [] # GDP deflator
pop = [] # Population
nGDPpc = [] # Nominal GDP per capita
rGDPpc = [] # Real GDP per capita
for line in strd:
    data = line.split()
    for k in range(len(data)):
        data[k] = data[k].replace(",","")
    # The data is importd as numeric data
    year.append(int(data[0]))
    nGDP.append(int(data[1]))
    rGDP.append(int(data[2]))
    GDPd.append(float(data[3]))
    pop.append(int(data[4]))
    nGDPpc.append(float(data[5]))
    rGDPpc.append(float(data[6]))
