import subprocess, time, os, sys


#hci0
#90:CF:15:BB:70:E2
try:
	len1 = len(sys.argv[1])
	len2 = len(sys.argv[2])
except:
	print "Format:"
	print "	... Bluetooth_Adapter Target_Address"
	sys.exit()
if  len1 > 0 and  len2 == 17:
	adapter = sys.argv[1]
	address = sys.argv[2]
	info = subprocess.check_output("hcitool -i"+ adapter +" info " + address + " | sed -n '/Device Name:/p;/BD Address:/p;/OUI Company:/p;/Manufacturer:/p;/LMP Version:/p' | sed -n 'h;n;H;n;G;h;n;x;N;G;p'",shell=True)
	while True:

		try:

		
			command = "l2ping -i "+ adapter + " -c 1 "+ address +" | grep NULL; hcitool -i "+ adapter +" lq " + address + " | grep Link | awk '{print $3}'"
			out1 = subprocess.check_output(command,shell=True)

			Sout = int(out1)

			if (Sout > 254):
				dist = 0
			else:
				dist = (Sout - 255) / -3
			os.system('clear')
			print "------BlueTrack---------------------\n"

			print "Info:"
			print info
			print "Distance:"
			print "	" + str(Sout) + "/255"
			print "	" + "Approximate Distance:" + str(dist) + " meters"
			print "	-------------------------------------"

			if Sout == 255: 
				print "	|#                                  | Found" 
			elif Sout > 249  and Sout < 255: 
				print "	|    #                              | Hot"
		        elif Sout > 239  and Sout < 250:
		       	        print "	|        #                          | Warm"
		        elif Sout > 229  and Sout < 240:
		       	        print "	|            #                      | Warm"
		        elif Sout > 219  and Sout < 230:
		       	        print "	|                #                  | Warm"
		        elif Sout > 209  and Sout < 220:
		       	        print "	|                    #              | Cold"
		        elif Sout > 199  and Sout < 210:
		       	        print "	|                        #          | Cold"
		        elif Sout > 189  and Sout < 200:
		       	        print "	|                            #      | Cold"
		        elif Sout > 179  and Sout < 190:
		       	        print "	|                               #   | Cold"
			else:
				print "	|                                  #| Cold"
		
			print "	-------------------------------------"
		
		
		except:

			pass

else:
	print "Format:"
	print "	... Bluetooth_Adapter Target_Address"
	sys.exit()

