#!/usr/bin/env python3

import time
import pygame
import sys
pygame.init()
pygame.mixer.init()

def helper():
	print('\nERROR: Incorrect arguemnts!')
	print('\n\tFORMAT:')
	print('\t{} [min] [sec] --set minutes and sec'.format(sys.argv[0]))
	print('\t{} [sec]  --set only sec'.format(sys.argv[0]))
	print('\n\tEXAMPLE:')
	print('\tpython3 {} 15 0  --set 15 minute counter'.format(sys.argv[0]))
	print('\tpython3 {} 15  --set 15 second counter\n'.format(sys.argv[0]))


def format_time(s):
	stringer = ''
	min_ = s / 60
	#hr_ = min_ / 60
	#if hr_ >= 1:
		#stringer += 'hr {} '.format(int(hr_))
	if min_ >= 1:
		stringer += 'min {} '.format(int(min_))
	if s >= 1:
		stringer += 'sec {} '.format(s % 60)
	stringer += ' ' * 10
	return stringer

sound_path = 'attention.wav'
sounder = pygame.mixer.Sound(sound_path)


if len(sys.argv) == 3:
	filename, min, sec = sys.argv
	sec = (int(min) * 60) + int(sec)
elif len(sys.argv) == 2:
	filename, sec = sys.argv
	sec = int(sec)
else:
	helper()
	sys.exit()


	
while True:
	if sec > 0:
		sec -= 1
		sys.stdout.write('\r{}'.format(format_time(sec)))

		time.sleep(1)
	else:
		sys.stdout.write('\rTime Expired!')
		sounder.play()
		time.sleep(1)
