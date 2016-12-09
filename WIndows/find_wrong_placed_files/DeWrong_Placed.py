from glob import glob
import logging, time, os

def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(d)]

def find_pics():
	folders = listdirs(".")
	for dir in folders:
		time.sleep(0.3) #Delay is for NAS or cloud drive to avoid choke.
		print("Current DIR : {0}".format(dir))
		pics = os.listdir(dir)
		for pic in pics:
			if pic.endswith(".jpg"): #Change it to any kind of ext you want.
				if dir not in pic:
					print(dir + ' / ' + pic)
					logging.warning(dir + ' / ' + pic)
				else:
					pass
			else:
				pass
	return

def main():
	logging.basicConfig(filename='wrong_placed.log', filemode='w', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s ')
	find_pics() 
	return

if __name__ == '__main__':
	main()
