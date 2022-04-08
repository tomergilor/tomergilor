#########   Dictionary    ############
#_______________________________________#


######  To set new Dictionary  ########
priceOfCameras = {'sony': 500,'nikon': 600, 'Canon': 700}

###### To show the dictionary   ######
print priceOfCameras

##### To show the value of Sony key
print priceOfCameras["sony"]

#####  To change the value of Sony
priceOfCameras["sony"] = 800

##### Show the new dictionary  #######
print priceOfCameras

###### To show the Dictionary keys  #######
print priceOfCameras.keys()

###### To show the Dictionary values  #######
print priceOfCameras.values()

##### To copy the dictionary to another dictionary: #####
copyOFPriceOFCameras = priceOfCameras.copy()

##### To show the new Dictionary  ########
print copyOFPriceOFCameras

##### To delete the Sony key/Value from the Dictionary  ########
del priceOfCameras["sony"]
print priceOfCameras

###### To Clear a Dictionary  #######
priceOfCameras.clear()
print priceOfCameras


