from glob import glob
from PIL import Image, ExifTags
import logging

def jpg_rotate():
	jpglist = glob("./*)t*.[jJ][pP][gG]")
	for jpg in jpglist:
		im = Image.open(jpg)
		if(im.size[0] > im.size[1]):
			im.rotate(270,expand=True).save(jpg,quality=100)
			logging.info("---- {0} ----" .format(jpg))
			logging.info("{0} , {1} \n" .format(im.size[0] , im.size[0]))
		else:
			logging.warning("{0} is already correct." .format(jpg))
			#logging.warning("{0} , {1} \n" .format(im.size[0] , im.size[1]))
	return
	
def back_rorate():
	backlist = glob("./*)back*.[jJ][pP][gG]")
	for back in backlist:
		im = Image.open(back)
		if(im.size[0] > im.size[1]):
			im.rotate(270,expand=True).save(back,quality=100)
			logging.info("---- {0} ----" .format(back))
			logging.info("{0} , {1} \n" .format(im.size[0] , im.size[0]))
		else:
			logging.warning("{0} is already correct." .format(back))
			#logging.warning("{0} , {1} \n" .format(im.size[0] , im.size[1]))
	return
	
def main():
	logging.basicConfig(filename='1.log', level=logging.INFO, format='%(asctime)s [ %(levelname)s ] \n    %(message)s \n')
	logging.info('Start JPG rotation.')
	jpg_rotate()
	logging.info('JPG rotation is done.\n now will start BACK rotation.')
	back_rorate()
	logging.info('BACK rotation is done. this software will exit.')
	
if __name__ == '__main__':
	main()
