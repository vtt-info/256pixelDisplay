import machine , neopixel, urandom, time

pixel = neopixel.NeoPixel(machine.Pin(0),16*16)

rot = (255,0,0)
braun = (96,57,19)
blau = (0,0,255)
orange = (255,127,0)
grün = (0,255,0)
gelb = (255,255,0)
lila = (255,0,250)
weiss = (255,255,255)
schwarz = (0,0,0)

f01 = (0,0,0) 			#schwarz
f02 = (85,85,85) 		#grau

f03 = (0,0,177)			#blau
f04 = (85,85,255)		#hellblau

f05 = (0,85,0)			#grün
f06 = (85,255,85)		#hellgrün

f07 = (0,177,177)		#türkies
f08 = (85,255,255)		#helltürkies

f09 = (177,0,0)			#rot
f10 = (255,85,85)		#hellrot

f11 = (85,0,85)			#lila
f12 = (255,85,255)		#helllila

f13 = (177,85,0)		#braun
f14 = (255,255,85)		#gelb

f15 = (177,177,177)		#weis low
f16 = (255,255,255)		#weiss hige



"""vorlage = [	[,,,,,,,,,,,,,,,],		#1 
			[,,,,,,,,,,,,,,,],		#2
			[,,,,,,,,,,,,,,,],		#3
			[,,,,,,,,,,,,,,,],		#4
			[,,,,,,,,,,,,,,,],		#5
			[,,,,,,,,,,,,,,,],		#6
			[,,,,,,,,,,,,,,,],		#7
			[,,,,,,,,,,,,,,,],		#8
			[,,,,,,,,,,,,,,,],		#9 
			[,,,,,,,,,,,,,,,],		#10
			[,,,,,,,,,,,,,,,],		#11
			[,,,,,,,,,,,,,,,],		#12
			[,,,,,,,,,,,,,,,],		#13
			[,,,,,,,,,,,,,,,],		#14
			[,,,,,,,,,,,,,,,],		#15
			[,,,,,,,,,,,,,,,]		#16
		]
"""
farbtest = [	[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#1 
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#2
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#3
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#4
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#5
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#6
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#7
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#8
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#9 
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#10
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#11
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#12
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#13
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#14
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16],		#15
			[f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16]		#16
		]

fox = [	[blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau	],
		[blau,	orange,	orange,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	orange,	orange,blau	],
		[blau,	orange,	orange,	orange,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	orange,	orange,	orange,	blau	],
		[blau,	orange,	weiss,	orange,	orange,	blau,	blau,	blau,	blau,	blau,	blau,	orange,	orange,	weiss,	orange,	blau	],
		[blau,	orange,	weiss,	weiss,	orange,	orange,	blau,	blau,	blau,	blau,	orange,	orange,	weiss,	weiss,	orange,	blau	],
		[blau,	orange,	weiss,	weiss,	weiss,	orange,	orange,	orange,	orange,	orange,	orange,	weiss,	weiss,	weiss,	orange,	blau	],
		[blau,	orange,	weiss,	weiss,	weiss,	weiss,	orange,	orange,	orange,	orange,	weiss,	weiss,	weiss,	weiss,	orange,	blau	],
		[blau,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	blau	],
		[blau,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	blau	],
		[blau,	orange,	orange,	orange,	orange,	schwarz,orange,	orange,	orange,	orange,	schwarz,orange,	orange,	orange,	orange,	blau	],
		[blau,	weiss,	orange,	orange,	orange,	schwarz,orange,	orange,	orange,	orange,	schwarz,orange,	orange,	orange,	weiss,	blau	],
		[blau,	weiss,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	weiss,	blau	],
		[blau,	weiss,	weiss,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	orange,	weiss,	weiss,	blau	],
		[blau,	blau,	weiss,	weiss,	weiss,	orange,	orange,	schwarz,schwarz,orange,	orange,	weiss,	weiss,	weiss,	blau,	blau	],
		[blau,	blau,	blau,	weiss,	weiss,	orange,	orange,	schwarz,schwarz,orange,	orange,	weiss,	weiss,	blau,	blau,	blau	],
		[blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau,	blau	]]



def sortieren(bildin):
	for zeile in range(0,16,2):
		zeile2 = bildin[zeile]
		bildin[zeile] = zeile2[::-1]
		
	return bildin

def pixelClear():
	for x in range(0,16*16):
		pixel[x] = (0,0,0)
	pixel.write()

while True:

#zufall für auswahl der programme
	#programm = 6
	programm = urandom.getrandbits(3)
	
#farbtest
	if programm == 6:
		print("farbtest")
		sort = sortieren(farbtest)
		pos = 0
		for inhalt in sort:
			for teil in inhalt:		
				pixel[pos] = teil 	
				pos = pos + 1
		pixel.write()
		time.sleep(5)
		pixelClear()



# Fuchs bild pixelArt
	elif programm == 5:
		print("PixelArt Fox")
		sort = sortieren(fox)
		pos = 0
		for inhalt in sort:
			for teil in inhalt:		
				pixel[pos] = teil 	
				pos = pos + 1
		pixel.write()
		time.sleep(5)
		pixelClear()

# panel strobo
	elif programm == 4:
		print("strobo")
		for p in range(0,3):
			bild = []
			farbe = ((urandom.getrandbits(8),urandom.getrandbits(8),urandom.getrandbits(8)))
			for y in range(0,16*16):	
				bild.append(farbe)			
										
						
			for s in range(0,12):				
				pos = 0			
				for inhalt in bild:
					pixel[pos] = inhalt 	
					pos = pos + 1
				pixel.write()
				time.sleep(0.05)
				pixelClear()
#random 1
	elif programm == 3:
		print("random 1")
		bild = []
		farbe = ((urandom.getrandbits(8),urandom.getrandbits(8),urandom.getrandbits(8)))
		for y in range(0,16):
			zeile = []		
			for x in range(0,16):	
				if y == x:
					zeile.append(farbe)
				else:			
					zeile.append((0,0,0))
			bild.append(zeile)

		pos = 0
		sort = sortieren(bild)
		for inhalt in sort:
			for teil in inhalt:		
				pixel[pos] = teil 	
				pos = pos + 1
		pixel.write()
		time.sleep(3)
		pixelClear()	
#random 2 + sort
	elif programm == 2:
		print("random 2 + sort")			
		bild = []
		for y in range(0,16):
			zeile = []		
			for x in range(0,16):	
				zeile.append((urandom.getrandbits(8),urandom.getrandbits(8),urandom.getrandbits(8)))
			bild.append(zeile)

		pos = 0
		for inhalt in bild:
			for teil in inhalt:
				pixel[pos] = teil 	
				pos = pos + 1
				pixel.write()
			time.sleep(0.1)
		time.sleep(3)
		pixelClear()
		pos = 0
		sort = sortieren(bild)
		for inhalt in sort:
			for teil in inhalt:		
				pixel[pos] = teil 	
				pos = pos + 1
				pixel.write()
			#time.sleep(0.1)
		time.sleep(3)
		pixelClear()
#laufrandom 3
	elif programm == 1:
		print("lauf random")
		for x in range(0, 16):
			row = x * 16
			for y in range(0, 16):
				pixel[row + y] = (urandom.getrandbits(8),urandom.getrandbits(8),urandom.getrandbits(8))
					
				pixel.write()
				time.sleep(0.3)

		for x in range (0,16):
			row = x * 16
			for y in range(0,16):
				pixel[row + y] = (0,0,0)
					
				pixel.write()
				time.sleep(0.2)
#random bits
	elif programm == 0:
		print("random bits")
		w = 0
		for x in range (0,100):
			w = w + 1
			if w > 5:
				w = 0
			else:
				
				for i in range(0,w): 
					pos = urandom.getrandbits(8)
					if pos > 16*16:
						pos = 16*16		
					pixel[pos] = (urandom.getrandbits(8),urandom.getrandbits(8),urandom.getrandbits(8))
				pixel.write()
				time.sleep(0.2)
				
				pixelClear()		
				time.sleep(0.2)
		pixelClear()
	else:
		print("tut nichts")
		pixelClear()
			
