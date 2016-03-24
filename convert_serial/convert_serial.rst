                              1 ;--------------------------------------------------------
                              2 ; File Created by SDCC : free open source ANSI-C Compiler
                              3 ; Version 3.3.0 #8604 (Dec 30 2013) (Linux)
                              4 ; This file was generated Thu Mar 24 11:52:23 2016
                              5 ;--------------------------------------------------------
                              6 	.module convert_serial
                              7 	.optsdcc -mmcs51 --model-small
                              8 	
                              9 ;--------------------------------------------------------
                             10 ; Public variables in this module
                             11 ;--------------------------------------------------------
                             12 	.globl _EPCS_Offset_Lookup_Table
                             13 	.globl _main
                             14 	.globl _EIP
                             15 	.globl _B
                             16 	.globl _EIE
                             17 	.globl _ACC
                             18 	.globl _EICON
                             19 	.globl _PSW
                             20 	.globl _TH2
                             21 	.globl _TL2
                             22 	.globl _RCAP2H
                             23 	.globl _RCAP2L
                             24 	.globl _T2CON
                             25 	.globl _SBUF1
                             26 	.globl _SCON1
                             27 	.globl _GPIFSGLDATLNOX
                             28 	.globl _GPIFSGLDATLX
                             29 	.globl _GPIFSGLDATH
                             30 	.globl _GPIFTRIG
                             31 	.globl _EP01STAT
                             32 	.globl _IP
                             33 	.globl _OEE
                             34 	.globl _OED
                             35 	.globl _OEC
                             36 	.globl _OEB
                             37 	.globl _OEA
                             38 	.globl _IOE
                             39 	.globl _IOD
                             40 	.globl _AUTOPTRSETUP
                             41 	.globl _EP68FIFOFLGS
                             42 	.globl _EP24FIFOFLGS
                             43 	.globl _EP2468STAT
                             44 	.globl _IE
                             45 	.globl _INT4CLR
                             46 	.globl _INT2CLR
                             47 	.globl _IOC
                             48 	.globl _AUTODAT2
                             49 	.globl _AUTOPTRL2
                             50 	.globl _AUTOPTRH2
                             51 	.globl _AUTODAT1
                             52 	.globl _APTR1L
                             53 	.globl _APTR1H
                             54 	.globl _SBU
                             55 	.globl _SCO
                             56 	.globl _MPA
                             57 	.globl _EXIF
                             58 	.globl _IOB
                             59 	.globl _SPC_
                             60 	.globl _CKCO
                             61 	.globl _TH1
                             62 	.globl _TH0
                             63 	.globl _TL1
                             64 	.globl _TL0
                             65 	.globl _TMOD
                             66 	.globl _TCON
                             67 	.globl _PCON
                             68 	.globl _DPS
                             69 	.globl _DPH1
                             70 	.globl _DPL1
                             71 	.globl _DPH
                             72 	.globl _DPL
                             73 	.globl _SP
                             74 	.globl _IOA
                             75 	.globl _myOutEndpntDscr
                             76 	.globl _myInEndpntDscr
                             77 	.globl _myIntrfcDscr
                             78 	.globl _myConfigDscr
                             79 	.globl _myDeviceQualDscr
                             80 	.globl _myDeviceDscr
                             81 	.globl _EP8FIFOBUF
                             82 	.globl _EP6FIFOBUF
                             83 	.globl _EP4FIFOBUF
                             84 	.globl _EP2FIFOBUF
                             85 	.globl _EP1INBUF
                             86 	.globl _EP1OUTBUF
                             87 	.globl _EP0BUF
                             88 	.globl _CT4
                             89 	.globl _CT3
                             90 	.globl _CT2
                             91 	.globl _CT1
                             92 	.globl _USBTEST
                             93 	.globl _TESTCFG
                             94 	.globl _DBUG
                             95 	.globl _UDMACRCQUAL
                             96 	.globl _UDMACRCL
                             97 	.globl _UDMACRCH
                             98 	.globl _GPIFHOLDAMOUNT
                             99 	.globl _FLOWSTBHPERIOD
                            100 	.globl _FLOWSTBEDGE
                            101 	.globl _FLOWSTB
                            102 	.globl _FLOWHOLDOFF
                            103 	.globl _FLOWEQ1CTL
                            104 	.globl _FLOWEQ0CTL
                            105 	.globl _FLOWLOGIC
                            106 	.globl _FLOWSTATE
                            107 	.globl _GPIFABORT
                            108 	.globl _GPIFREADYSTAT
                            109 	.globl _GPIFREADYCFG
                            110 	.globl _XGPIFSGLDATLNOX
                            111 	.globl _XGPIFSGLDATLX
                            112 	.globl _XGPIFSGLDATH
                            113 	.globl _EP8GPIFTRIG
                            114 	.globl _EP8GPIFPFSTOP
                            115 	.globl _EP8GPIFFLGSEL
                            116 	.globl _EP6GPIFTRIG
                            117 	.globl _EP6GPIFPFSTOP
                            118 	.globl _EP6GPIFFLGSEL
                            119 	.globl _EP4GPIFTRIG
                            120 	.globl _EP4GPIFPFSTOP
                            121 	.globl _EP4GPIFFLGSEL
                            122 	.globl _EP2GPIFTRIG
                            123 	.globl _EP2GPIFPFSTOP
                            124 	.globl _EP2GPIFFLGSEL
                            125 	.globl _GPIFTCB0
                            126 	.globl _GPIFTCB1
                            127 	.globl _GPIFTCB2
                            128 	.globl _GPIFTCB3
                            129 	.globl _GPIFADRL
                            130 	.globl _GPIFADRH
                            131 	.globl _GPIFCTLCFG
                            132 	.globl _GPIFIDLECTL
                            133 	.globl _GPIFIDLECS
                            134 	.globl _GPIFWFSELECT
                            135 	.globl _SETUPDAT
                            136 	.globl _SUDPTRCTL
                            137 	.globl _SUDPTRL
                            138 	.globl _SUDPTRH
                            139 	.globl _EP8FIFOBCL
                            140 	.globl _EP8FIFOBCH
                            141 	.globl _EP6FIFOBCL
                            142 	.globl _EP6FIFOBCH
                            143 	.globl _EP4FIFOBCL
                            144 	.globl _EP4FIFOBCH
                            145 	.globl _EP2FIFOBCL
                            146 	.globl _EP2FIFOBCH
                            147 	.globl _EP8FIFOFLGS
                            148 	.globl _EP6FIFOFLGS
                            149 	.globl _EP4FIFOFLGS
                            150 	.globl _EP2FIFOFLGS
                            151 	.globl _EP8CS
                            152 	.globl _EP6CS
                            153 	.globl _EP4CS
                            154 	.globl _EP2CS
                            155 	.globl _EP1INCS
                            156 	.globl _EP1OUTCS
                            157 	.globl _EP0CS
                            158 	.globl _EP8BCL
                            159 	.globl _EP8BCH
                            160 	.globl _EP6BCL
                            161 	.globl _EP6BCH
                            162 	.globl _EP4BCL
                            163 	.globl _EP4BCH
                            164 	.globl _EP2BCL
                            165 	.globl _EP2BCH
                            166 	.globl _EP1INBC
                            167 	.globl _EP1OUTBC
                            168 	.globl _EP0BCL
                            169 	.globl _EP0BCH
                            170 	.globl _FNADDR
                            171 	.globl _MICROFRAME
                            172 	.globl _USBFRAMEL
                            173 	.globl _USBFRAMEH
                            174 	.globl _TOGCTL
                            175 	.globl _WAKEUPCS
                            176 	.globl _SUSPEND
                            177 	.globl _USBCS
                            178 	.globl _XAUTODAT2
                            179 	.globl _XAUTODAT1
                            180 	.globl _I2CTL
                            181 	.globl _I2DAT
                            182 	.globl _I2CS
                            183 	.globl _PORTECFG
                            184 	.globl _PORTCCFG
                            185 	.globl _PORTACFG
                            186 	.globl _INTSETUP
                            187 	.globl _INT4IVEC
                            188 	.globl _INT2IVEC
                            189 	.globl _CLRERRCNT
                            190 	.globl _ERRCNTLIM
                            191 	.globl _USBERRIRQ
                            192 	.globl _USBERRIE
                            193 	.globl _GPIFIRQ
                            194 	.globl _GPIFIE
                            195 	.globl _EPIRQ
                            196 	.globl _EPIE
                            197 	.globl _USBIRQ
                            198 	.globl _USBIE
                            199 	.globl _NAKIRQ
                            200 	.globl _NAKIE
                            201 	.globl _IBNIRQ
                            202 	.globl _IBNIE
                            203 	.globl _EP8FIFOIRQ
                            204 	.globl _EP8FIFOIE
                            205 	.globl _EP6FIFOIRQ
                            206 	.globl _EP6FIFOIE
                            207 	.globl _EP4FIFOIRQ
                            208 	.globl _EP4FIFOIE
                            209 	.globl _EP2FIFOIRQ
                            210 	.globl _EP2FIFOIE
                            211 	.globl _OUTPKTEND
                            212 	.globl _INPKTEND
                            213 	.globl _EP8ISOINPKTS
                            214 	.globl _EP6ISOINPKTS
                            215 	.globl _EP4ISOINPKTS
                            216 	.globl _EP2ISOINPKTS
                            217 	.globl _EP8FIFOPFL
                            218 	.globl _EP8FIFOPFH
                            219 	.globl _EP6FIFOPFL
                            220 	.globl _EP6FIFOPFH
                            221 	.globl _EP4FIFOPFL
                            222 	.globl _EP4FIFOPFH
                            223 	.globl _EP2FIFOPFL
                            224 	.globl _EP2FIFOPFH
                            225 	.globl _EP8AUTOINLENL
                            226 	.globl _EP8AUTOINLENH
                            227 	.globl _EP6AUTOINLENL
                            228 	.globl _EP6AUTOINLENH
                            229 	.globl _EP4AUTOINLENL
                            230 	.globl _EP4AUTOINLENH
                            231 	.globl _EP2AUTOINLENL
                            232 	.globl _EP2AUTOINLENH
                            233 	.globl _EP8FIFOCFG
                            234 	.globl _EP6FIFOCFG
                            235 	.globl _EP4FIFOCFG
                            236 	.globl _EP2FIFOCFG
                            237 	.globl _EP8CFG
                            238 	.globl _EP6CFG
                            239 	.globl _EP4CFG
                            240 	.globl _EP2CFG
                            241 	.globl _EP1INCFG
                            242 	.globl _EP1OUTCFG
                            243 	.globl _REVCTL
                            244 	.globl _REVID
                            245 	.globl _FIFOPINPOLAR
                            246 	.globl _UART230
                            247 	.globl _BPADDRL
                            248 	.globl _BPADDRH
                            249 	.globl _BREAKPT
                            250 	.globl _FIFORESET
                            251 	.globl _PINFLAGSCD
                            252 	.globl _PINFLAGSAB
                            253 	.globl _IFCONFIG
                            254 	.globl _CPUCS
                            255 	.globl _RES_WAVEDATA_END
                            256 	.globl _GPIF_WAVE_DATA
                            257 	.globl _Selfpwr
                            258 	.globl _Rwuen
                            259 	.globl _Rwuen_allowed
                            260 	.globl _latency_us
                            261 	.globl _bytes_waiting_for_xmit
                            262 	.globl _USB_strings
                            263 	.globl _InterfaceSetting
                            264 	.globl _Configuration
                            265 ;--------------------------------------------------------
                            266 ; special function registers
                            267 ;--------------------------------------------------------
                            268 	.area RSEG    (ABS,DATA)
   0000                     269 	.org 0x0000
                     0080   270 _IOA	=	0x0080
                     0081   271 _SP	=	0x0081
                     0082   272 _DPL	=	0x0082
                     0083   273 _DPH	=	0x0083
                     0084   274 _DPL1	=	0x0084
                     0085   275 _DPH1	=	0x0085
                     0086   276 _DPS	=	0x0086
                     0087   277 _PCON	=	0x0087
                     0088   278 _TCON	=	0x0088
                     0089   279 _TMOD	=	0x0089
                     008A   280 _TL0	=	0x008a
                     008B   281 _TL1	=	0x008b
                     008C   282 _TH0	=	0x008c
                     008D   283 _TH1	=	0x008d
                     008E   284 _CKCO	=	0x008e
                     008F   285 _SPC_	=	0x008f
                     0090   286 _IOB	=	0x0090
                     0091   287 _EXIF	=	0x0091
                     0092   288 _MPA	=	0x0092
                     0098   289 _SCO	=	0x0098
                     0099   290 _SBU	=	0x0099
                     009A   291 _APTR1H	=	0x009a
                     009B   292 _APTR1L	=	0x009b
                     009C   293 _AUTODAT1	=	0x009c
                     009D   294 _AUTOPTRH2	=	0x009d
                     009E   295 _AUTOPTRL2	=	0x009e
                     009F   296 _AUTODAT2	=	0x009f
                     00A0   297 _IOC	=	0x00a0
                     00A1   298 _INT2CLR	=	0x00a1
                     00A2   299 _INT4CLR	=	0x00a2
                     00A8   300 _IE	=	0x00a8
                     00AA   301 _EP2468STAT	=	0x00aa
                     00AB   302 _EP24FIFOFLGS	=	0x00ab
                     00AC   303 _EP68FIFOFLGS	=	0x00ac
                     00AF   304 _AUTOPTRSETUP	=	0x00af
                     00B0   305 _IOD	=	0x00b0
                     00B1   306 _IOE	=	0x00b1
                     00B2   307 _OEA	=	0x00b2
                     00B3   308 _OEB	=	0x00b3
                     00B4   309 _OEC	=	0x00b4
                     00B5   310 _OED	=	0x00b5
                     00B6   311 _OEE	=	0x00b6
                     00B8   312 _IP	=	0x00b8
                     00BA   313 _EP01STAT	=	0x00ba
                     00BB   314 _GPIFTRIG	=	0x00bb
                     00BD   315 _GPIFSGLDATH	=	0x00bd
                     00BE   316 _GPIFSGLDATLX	=	0x00be
                     00BF   317 _GPIFSGLDATLNOX	=	0x00bf
                     00C0   318 _SCON1	=	0x00c0
                     00C1   319 _SBUF1	=	0x00c1
                     00C8   320 _T2CON	=	0x00c8
                     00CA   321 _RCAP2L	=	0x00ca
                     00CB   322 _RCAP2H	=	0x00cb
                     00CC   323 _TL2	=	0x00cc
                     00CD   324 _TH2	=	0x00cd
                     00D0   325 _PSW	=	0x00d0
                     00D8   326 _EICON	=	0x00d8
                     00E0   327 _ACC	=	0x00e0
                     00E8   328 _EIE	=	0x00e8
                     00F0   329 _B	=	0x00f0
                     00F8   330 _EIP	=	0x00f8
                            331 ;--------------------------------------------------------
                            332 ; special function bits
                            333 ;--------------------------------------------------------
                            334 	.area RSEG    (ABS,DATA)
   0000                     335 	.org 0x0000
                            336 ;--------------------------------------------------------
                            337 ; overlayable register banks
                            338 ;--------------------------------------------------------
                            339 	.area REG_BANK_0	(REL,OVR,DATA)
   0000                     340 	.ds 8
                            341 ;--------------------------------------------------------
                            342 ; overlayable bit register bank
                            343 ;--------------------------------------------------------
                            344 	.area BIT_BANK	(REL,OVR,DATA)
   0021                     345 bits:
   0021                     346 	.ds 1
                     8000   347 	b0 = bits[0]
                     8100   348 	b1 = bits[1]
                     8200   349 	b2 = bits[2]
                     8300   350 	b3 = bits[3]
                     8400   351 	b4 = bits[4]
                     8500   352 	b5 = bits[5]
                     8600   353 	b6 = bits[6]
                     8700   354 	b7 = bits[7]
                            355 ;--------------------------------------------------------
                            356 ; internal ram data
                            357 ;--------------------------------------------------------
                            358 	.area DSEG    (DATA)
   0008                     359 _Configuration::
   0008                     360 	.ds 1
   0009                     361 _InterfaceSetting::
   0009                     362 	.ds 1
   000A                     363 _USB_strings::
   000A                     364 	.ds 9
   0013                     365 _SetupCommand_i_1_21:
   0013                     366 	.ds 2
   0015                     367 _bytes_waiting_for_xmit::
   0015                     368 	.ds 2
   0017                     369 _latency_us::
   0017                     370 	.ds 2
                            371 ;--------------------------------------------------------
                            372 ; overlayable items in internal ram 
                            373 ;--------------------------------------------------------
                            374 	.area	OSEG    (OVR,DATA)
                            375 ;--------------------------------------------------------
                            376 ; Stack segment in internal ram 
                            377 ;--------------------------------------------------------
                            378 	.area	SSEG	(DATA)
   0022                     379 __start__stack:
   0022                     380 	.ds	1
                            381 
                            382 ;--------------------------------------------------------
                            383 ; indirectly addressable internal ram data
                            384 ;--------------------------------------------------------
                            385 	.area ISEG    (DATA)
                            386 ;--------------------------------------------------------
                            387 ; absolute internal ram data
                            388 ;--------------------------------------------------------
                            389 	.area IABS    (ABS,DATA)
                            390 	.area IABS    (ABS,DATA)
                            391 ;--------------------------------------------------------
                            392 ; bit data
                            393 ;--------------------------------------------------------
                            394 	.area BSEG    (BIT)
   0000                     395 _Rwuen_allowed::
   0000                     396 	.ds 1
   0001                     397 _Rwuen::
   0001                     398 	.ds 1
   0002                     399 _Selfpwr::
   0002                     400 	.ds 1
                            401 ;--------------------------------------------------------
                            402 ; paged external ram data
                            403 ;--------------------------------------------------------
                            404 	.area PSEG    (PAG,XDATA)
                            405 ;--------------------------------------------------------
                            406 ; external ram data
                            407 ;--------------------------------------------------------
                            408 	.area XSEG    (XDATA)
                     E400   409 _GPIF_WAVE_DATA	=	0xe400
                     E480   410 _RES_WAVEDATA_END	=	0xe480
                     E600   411 _CPUCS	=	0xe600
                     E601   412 _IFCONFIG	=	0xe601
                     E602   413 _PINFLAGSAB	=	0xe602
                     E603   414 _PINFLAGSCD	=	0xe603
                     E604   415 _FIFORESET	=	0xe604
                     E605   416 _BREAKPT	=	0xe605
                     E606   417 _BPADDRH	=	0xe606
                     E607   418 _BPADDRL	=	0xe607
                     E608   419 _UART230	=	0xe608
                     E609   420 _FIFOPINPOLAR	=	0xe609
                     E60A   421 _REVID	=	0xe60a
                     E60B   422 _REVCTL	=	0xe60b
                     E610   423 _EP1OUTCFG	=	0xe610
                     E611   424 _EP1INCFG	=	0xe611
                     E612   425 _EP2CFG	=	0xe612
                     E613   426 _EP4CFG	=	0xe613
                     E614   427 _EP6CFG	=	0xe614
                     E615   428 _EP8CFG	=	0xe615
                     E618   429 _EP2FIFOCFG	=	0xe618
                     E619   430 _EP4FIFOCFG	=	0xe619
                     E61A   431 _EP6FIFOCFG	=	0xe61a
                     E61B   432 _EP8FIFOCFG	=	0xe61b
                     E620   433 _EP2AUTOINLENH	=	0xe620
                     E621   434 _EP2AUTOINLENL	=	0xe621
                     E622   435 _EP4AUTOINLENH	=	0xe622
                     E623   436 _EP4AUTOINLENL	=	0xe623
                     E624   437 _EP6AUTOINLENH	=	0xe624
                     E625   438 _EP6AUTOINLENL	=	0xe625
                     E626   439 _EP8AUTOINLENH	=	0xe626
                     E627   440 _EP8AUTOINLENL	=	0xe627
                     E630   441 _EP2FIFOPFH	=	0xe630
                     E631   442 _EP2FIFOPFL	=	0xe631
                     E632   443 _EP4FIFOPFH	=	0xe632
                     E633   444 _EP4FIFOPFL	=	0xe633
                     E634   445 _EP6FIFOPFH	=	0xe634
                     E635   446 _EP6FIFOPFL	=	0xe635
                     E636   447 _EP8FIFOPFH	=	0xe636
                     E637   448 _EP8FIFOPFL	=	0xe637
                     E640   449 _EP2ISOINPKTS	=	0xe640
                     E641   450 _EP4ISOINPKTS	=	0xe641
                     E642   451 _EP6ISOINPKTS	=	0xe642
                     E643   452 _EP8ISOINPKTS	=	0xe643
                     E648   453 _INPKTEND	=	0xe648
                     E649   454 _OUTPKTEND	=	0xe649
                     E650   455 _EP2FIFOIE	=	0xe650
                     E651   456 _EP2FIFOIRQ	=	0xe651
                     E652   457 _EP4FIFOIE	=	0xe652
                     E653   458 _EP4FIFOIRQ	=	0xe653
                     E654   459 _EP6FIFOIE	=	0xe654
                     E655   460 _EP6FIFOIRQ	=	0xe655
                     E656   461 _EP8FIFOIE	=	0xe656
                     E657   462 _EP8FIFOIRQ	=	0xe657
                     E658   463 _IBNIE	=	0xe658
                     E659   464 _IBNIRQ	=	0xe659
                     E65A   465 _NAKIE	=	0xe65a
                     E65B   466 _NAKIRQ	=	0xe65b
                     E65C   467 _USBIE	=	0xe65c
                     E65D   468 _USBIRQ	=	0xe65d
                     E65E   469 _EPIE	=	0xe65e
                     E65F   470 _EPIRQ	=	0xe65f
                     E660   471 _GPIFIE	=	0xe660
                     E661   472 _GPIFIRQ	=	0xe661
                     E662   473 _USBERRIE	=	0xe662
                     E663   474 _USBERRIRQ	=	0xe663
                     E664   475 _ERRCNTLIM	=	0xe664
                     E665   476 _CLRERRCNT	=	0xe665
                     E666   477 _INT2IVEC	=	0xe666
                     E667   478 _INT4IVEC	=	0xe667
                     E668   479 _INTSETUP	=	0xe668
                     E670   480 _PORTACFG	=	0xe670
                     E671   481 _PORTCCFG	=	0xe671
                     E672   482 _PORTECFG	=	0xe672
                     E678   483 _I2CS	=	0xe678
                     E679   484 _I2DAT	=	0xe679
                     E67A   485 _I2CTL	=	0xe67a
                     E67B   486 _XAUTODAT1	=	0xe67b
                     E67C   487 _XAUTODAT2	=	0xe67c
                     E680   488 _USBCS	=	0xe680
                     E681   489 _SUSPEND	=	0xe681
                     E682   490 _WAKEUPCS	=	0xe682
                     E683   491 _TOGCTL	=	0xe683
                     E684   492 _USBFRAMEH	=	0xe684
                     E685   493 _USBFRAMEL	=	0xe685
                     E686   494 _MICROFRAME	=	0xe686
                     E687   495 _FNADDR	=	0xe687
                     E68A   496 _EP0BCH	=	0xe68a
                     E68B   497 _EP0BCL	=	0xe68b
                     E68D   498 _EP1OUTBC	=	0xe68d
                     E68F   499 _EP1INBC	=	0xe68f
                     E690   500 _EP2BCH	=	0xe690
                     E691   501 _EP2BCL	=	0xe691
                     E694   502 _EP4BCH	=	0xe694
                     E695   503 _EP4BCL	=	0xe695
                     E698   504 _EP6BCH	=	0xe698
                     E699   505 _EP6BCL	=	0xe699
                     E69C   506 _EP8BCH	=	0xe69c
                     E69D   507 _EP8BCL	=	0xe69d
                     E6A0   508 _EP0CS	=	0xe6a0
                     E6A1   509 _EP1OUTCS	=	0xe6a1
                     E6A2   510 _EP1INCS	=	0xe6a2
                     E6A3   511 _EP2CS	=	0xe6a3
                     E6A4   512 _EP4CS	=	0xe6a4
                     E6A5   513 _EP6CS	=	0xe6a5
                     E6A6   514 _EP8CS	=	0xe6a6
                     E6A7   515 _EP2FIFOFLGS	=	0xe6a7
                     E6A8   516 _EP4FIFOFLGS	=	0xe6a8
                     E6A9   517 _EP6FIFOFLGS	=	0xe6a9
                     E6AA   518 _EP8FIFOFLGS	=	0xe6aa
                     E6AB   519 _EP2FIFOBCH	=	0xe6ab
                     E6AC   520 _EP2FIFOBCL	=	0xe6ac
                     E6AD   521 _EP4FIFOBCH	=	0xe6ad
                     E6AE   522 _EP4FIFOBCL	=	0xe6ae
                     E6AF   523 _EP6FIFOBCH	=	0xe6af
                     E6B0   524 _EP6FIFOBCL	=	0xe6b0
                     E6B1   525 _EP8FIFOBCH	=	0xe6b1
                     E6B2   526 _EP8FIFOBCL	=	0xe6b2
                     E6B3   527 _SUDPTRH	=	0xe6b3
                     E6B4   528 _SUDPTRL	=	0xe6b4
                     E6B5   529 _SUDPTRCTL	=	0xe6b5
                     E6B8   530 _SETUPDAT	=	0xe6b8
                     E6C0   531 _GPIFWFSELECT	=	0xe6c0
                     E6C1   532 _GPIFIDLECS	=	0xe6c1
                     E6C2   533 _GPIFIDLECTL	=	0xe6c2
                     E6C3   534 _GPIFCTLCFG	=	0xe6c3
                     E6C4   535 _GPIFADRH	=	0xe6c4
                     E6C5   536 _GPIFADRL	=	0xe6c5
                     E6CE   537 _GPIFTCB3	=	0xe6ce
                     E6CF   538 _GPIFTCB2	=	0xe6cf
                     E6D0   539 _GPIFTCB1	=	0xe6d0
                     E6D1   540 _GPIFTCB0	=	0xe6d1
                     E6D2   541 _EP2GPIFFLGSEL	=	0xe6d2
                     E6D3   542 _EP2GPIFPFSTOP	=	0xe6d3
                     E6D4   543 _EP2GPIFTRIG	=	0xe6d4
                     E6DA   544 _EP4GPIFFLGSEL	=	0xe6da
                     E6DB   545 _EP4GPIFPFSTOP	=	0xe6db
                     E6DC   546 _EP4GPIFTRIG	=	0xe6dc
                     E6E2   547 _EP6GPIFFLGSEL	=	0xe6e2
                     E6E3   548 _EP6GPIFPFSTOP	=	0xe6e3
                     E6E4   549 _EP6GPIFTRIG	=	0xe6e4
                     E6EA   550 _EP8GPIFFLGSEL	=	0xe6ea
                     E6EB   551 _EP8GPIFPFSTOP	=	0xe6eb
                     E6EC   552 _EP8GPIFTRIG	=	0xe6ec
                     E6F0   553 _XGPIFSGLDATH	=	0xe6f0
                     E6F1   554 _XGPIFSGLDATLX	=	0xe6f1
                     E6F2   555 _XGPIFSGLDATLNOX	=	0xe6f2
                     E6F3   556 _GPIFREADYCFG	=	0xe6f3
                     E6F4   557 _GPIFREADYSTAT	=	0xe6f4
                     E6F5   558 _GPIFABORT	=	0xe6f5
                     E6C6   559 _FLOWSTATE	=	0xe6c6
                     E6C7   560 _FLOWLOGIC	=	0xe6c7
                     E6C8   561 _FLOWEQ0CTL	=	0xe6c8
                     E6C9   562 _FLOWEQ1CTL	=	0xe6c9
                     E6CA   563 _FLOWHOLDOFF	=	0xe6ca
                     E6CB   564 _FLOWSTB	=	0xe6cb
                     E6CC   565 _FLOWSTBEDGE	=	0xe6cc
                     E6CD   566 _FLOWSTBHPERIOD	=	0xe6cd
                     E60C   567 _GPIFHOLDAMOUNT	=	0xe60c
                     E67D   568 _UDMACRCH	=	0xe67d
                     E67E   569 _UDMACRCL	=	0xe67e
                     E67F   570 _UDMACRCQUAL	=	0xe67f
                     E6F8   571 _DBUG	=	0xe6f8
                     E6F9   572 _TESTCFG	=	0xe6f9
                     E6FA   573 _USBTEST	=	0xe6fa
                     E6FB   574 _CT1	=	0xe6fb
                     E6FC   575 _CT2	=	0xe6fc
                     E6FD   576 _CT3	=	0xe6fd
                     E6FE   577 _CT4	=	0xe6fe
                     E740   578 _EP0BUF	=	0xe740
                     E780   579 _EP1OUTBUF	=	0xe780
                     E7C0   580 _EP1INBUF	=	0xe7c0
                     F000   581 _EP2FIFOBUF	=	0xf000
                     F400   582 _EP4FIFOBUF	=	0xf400
                     F800   583 _EP6FIFOBUF	=	0xf800
                     FC00   584 _EP8FIFOBUF	=	0xfc00
                            585 ;--------------------------------------------------------
                            586 ; absolute external ram data
                            587 ;--------------------------------------------------------
                            588 	.area XABS    (ABS,XDATA)
   3D00                     589 	.org 0x3D00
   3D00                     590 _myDeviceDscr::
   3D00                     591 	.ds 18
   3D20                     592 	.org 0x3D20
   3D20                     593 _myDeviceQualDscr::
   3D20                     594 	.ds 10
   3D30                     595 	.org 0x3D30
   3D30                     596 _myConfigDscr::
   3D30                     597 	.ds 9
   3D39                     598 	.org 0x3D39
   3D39                     599 _myIntrfcDscr::
   3D39                     600 	.ds 9
   3D42                     601 	.org 0x3D42
   3D42                     602 _myInEndpntDscr::
   3D42                     603 	.ds 7
   3D49                     604 	.org 0x3D49
   3D49                     605 _myOutEndpntDscr::
   3D49                     606 	.ds 7
                            607 ;--------------------------------------------------------
                            608 ; external initialized ram data
                            609 ;--------------------------------------------------------
                            610 	.area XISEG   (XDATA)
                            611 	.area HOME    (CODE)
                            612 	.area GSINIT0 (CODE)
                            613 	.area GSINIT1 (CODE)
                            614 	.area GSINIT2 (CODE)
                            615 	.area GSINIT3 (CODE)
                            616 	.area GSINIT4 (CODE)
                            617 	.area GSINIT5 (CODE)
                            618 	.area GSINIT  (CODE)
                            619 	.area GSFINAL (CODE)
                            620 	.area CSEG    (CODE)
                            621 ;--------------------------------------------------------
                            622 ; interrupt vector 
                            623 ;--------------------------------------------------------
                            624 	.area HOME    (CODE)
   0000                     625 __interrupt_vect:
   0000 02 00 77      [24]  626 	ljmp	__sdcc_gsinit_startup
   0003 32            [24]  627 	reti
   0004                     628 	.ds	7
   000B 32            [24]  629 	reti
   000C                     630 	.ds	7
   0013 32            [24]  631 	reti
   0014                     632 	.ds	7
   001B 32            [24]  633 	reti
   001C                     634 	.ds	7
   0023 32            [24]  635 	reti
   0024                     636 	.ds	7
   002B 32            [24]  637 	reti
   002C                     638 	.ds	7
   0033 32            [24]  639 	reti
   0034                     640 	.ds	7
   003B 32            [24]  641 	reti
   003C                     642 	.ds	7
   0043 02 07 1B      [24]  643 	ljmp	_USB_isr
                            644 ;--------------------------------------------------------
                            645 ; global & static initialisations
                            646 ;--------------------------------------------------------
                            647 	.area HOME    (CODE)
                            648 	.area GSINIT  (CODE)
                            649 	.area GSFINAL (CODE)
                            650 	.area GSINIT  (CODE)
                            651 	.globl __sdcc_gsinit_startup
                            652 	.globl __sdcc_program_startup
                            653 	.globl __start__stack
                            654 	.globl __mcs51_genXINIT
                            655 	.globl __mcs51_genXRAMCLEAR
                            656 	.globl __mcs51_genRAMCLEAR
                            657 ;	convert_serial.c:116: char * USB_strings[] = { "EN", "freesoft.org", "FX2 case converter" };
   00D0 75 0A 13      [24]  658 	mov	(_USB_strings + 0),#__str_0
   00D3 75 0B 09      [24]  659 	mov	(_USB_strings + 1),#(__str_0 >> 8)
   00D6 75 0C 80      [24]  660 	mov	(_USB_strings + 2),#0x80
   00D9 75 0D 16      [24]  661 	mov	((_USB_strings + 0x0003) + 0),#__str_1
   00DC 75 0E 09      [24]  662 	mov	((_USB_strings + 0x0003) + 1),#(__str_1 >> 8)
   00DF 75 0F 80      [24]  663 	mov	((_USB_strings + 0x0003) + 2),#0x80
   00E2 75 10 23      [24]  664 	mov	((_USB_strings + 0x0006) + 0),#__str_2
   00E5 75 11 09      [24]  665 	mov	((_USB_strings + 0x0006) + 1),#(__str_2 >> 8)
   00E8 75 12 80      [24]  666 	mov	((_USB_strings + 0x0006) + 2),#0x80
                            667 ;	convert_serial.c:497: unsigned int bytes_waiting_for_xmit = 0;
   00EB E4            [12]  668 	clr	a
   00EC F5 15         [12]  669 	mov	_bytes_waiting_for_xmit,a
   00EE F5 16         [12]  670 	mov	(_bytes_waiting_for_xmit + 1),a
                            671 ;	convert_serial.c:498: unsigned int latency_us = 40000;
   00F0 75 17 40      [24]  672 	mov	_latency_us,#0x40
   00F3 75 18 9C      [24]  673 	mov	(_latency_us + 1),#0x9C
                            674 ;	convert_serial.c:47: BOOL Rwuen_allowed = FALSE;	// Allow remote wakeup to be enabled
   00F6 C2 00         [12]  675 	clr	_Rwuen_allowed
                            676 ;	convert_serial.c:48: BOOL Rwuen = FALSE;		// Remote wakeup enable
   00F8 C2 01         [12]  677 	clr	_Rwuen
                            678 ;	convert_serial.c:49: BOOL Selfpwr = FALSE;		// Device is (not) self-powered
   00FA C2 02         [12]  679 	clr	_Selfpwr
                            680 ;	convert_serial.c:134: DEVICEDSCR xdata at 0x3d00 myDeviceDscr = {
   00FC 90 3D 00      [24]  681 	mov	dptr,#_myDeviceDscr
   00FF 74 12         [12]  682 	mov	a,#0x12
   0101 F0            [24]  683 	movx	@dptr,a
   0102 90 3D 01      [24]  684 	mov	dptr,#(_myDeviceDscr + 0x0001)
   0105 74 01         [12]  685 	mov	a,#0x01
   0107 F0            [24]  686 	movx	@dptr,a
   0108 90 3D 02      [24]  687 	mov	dptr,#(_myDeviceDscr + 0x0002)
   010B E4            [12]  688 	clr	a
   010C F0            [24]  689 	movx	@dptr,a
   010D 74 02         [12]  690 	mov	a,#0x02
   010F A3            [24]  691 	inc	dptr
   0110 F0            [24]  692 	movx	@dptr,a
   0111 90 3D 04      [24]  693 	mov	dptr,#(_myDeviceDscr + 0x0004)
   0114 E4            [12]  694 	clr	a
   0115 F0            [24]  695 	movx	@dptr,a
   0116 90 3D 05      [24]  696 	mov	dptr,#(_myDeviceDscr + 0x0005)
   0119 F0            [24]  697 	movx	@dptr,a
   011A 90 3D 06      [24]  698 	mov	dptr,#(_myDeviceDscr + 0x0006)
   011D F0            [24]  699 	movx	@dptr,a
   011E 90 3D 07      [24]  700 	mov	dptr,#(_myDeviceDscr + 0x0007)
   0121 74 40         [12]  701 	mov	a,#0x40
   0123 F0            [24]  702 	movx	@dptr,a
   0124 90 3D 08      [24]  703 	mov	dptr,#(_myDeviceDscr + 0x0008)
   0127 74 03         [12]  704 	mov	a,#0x03
   0129 F0            [24]  705 	movx	@dptr,a
   012A 74 04         [12]  706 	mov	a,#0x04
   012C A3            [24]  707 	inc	dptr
   012D F0            [24]  708 	movx	@dptr,a
   012E 90 3D 0A      [24]  709 	mov	dptr,#(_myDeviceDscr + 0x000a)
   0131 74 72         [12]  710 	mov	a,#0x72
   0133 F0            [24]  711 	movx	@dptr,a
   0134 74 83         [12]  712 	mov	a,#0x83
   0136 A3            [24]  713 	inc	dptr
   0137 F0            [24]  714 	movx	@dptr,a
   0138 90 3D 0C      [24]  715 	mov	dptr,#(_myDeviceDscr + 0x000c)
   013B E4            [12]  716 	clr	a
   013C F0            [24]  717 	movx	@dptr,a
   013D 74 01         [12]  718 	mov	a,#0x01
   013F A3            [24]  719 	inc	dptr
   0140 F0            [24]  720 	movx	@dptr,a
   0141 90 3D 0E      [24]  721 	mov	dptr,#(_myDeviceDscr + 0x000e)
   0144 74 01         [12]  722 	mov	a,#0x01
   0146 F0            [24]  723 	movx	@dptr,a
   0147 90 3D 0F      [24]  724 	mov	dptr,#(_myDeviceDscr + 0x000f)
   014A 74 02         [12]  725 	mov	a,#0x02
   014C F0            [24]  726 	movx	@dptr,a
   014D 90 3D 10      [24]  727 	mov	dptr,#(_myDeviceDscr + 0x0010)
   0150 E4            [12]  728 	clr	a
   0151 F0            [24]  729 	movx	@dptr,a
   0152 90 3D 11      [24]  730 	mov	dptr,#(_myDeviceDscr + 0x0011)
   0155 74 01         [12]  731 	mov	a,#0x01
   0157 F0            [24]  732 	movx	@dptr,a
                            733 ;	convert_serial.c:159: DEVICEQUALDSCR xdata at 0x3d20 myDeviceQualDscr = {
   0158 90 3D 20      [24]  734 	mov	dptr,#_myDeviceQualDscr
   015B 74 0A         [12]  735 	mov	a,#0x0A
   015D F0            [24]  736 	movx	@dptr,a
   015E 90 3D 21      [24]  737 	mov	dptr,#(_myDeviceQualDscr + 0x0001)
   0161 74 06         [12]  738 	mov	a,#0x06
   0163 F0            [24]  739 	movx	@dptr,a
   0164 90 3D 22      [24]  740 	mov	dptr,#(_myDeviceQualDscr + 0x0002)
   0167 E4            [12]  741 	clr	a
   0168 F0            [24]  742 	movx	@dptr,a
   0169 74 02         [12]  743 	mov	a,#0x02
   016B A3            [24]  744 	inc	dptr
   016C F0            [24]  745 	movx	@dptr,a
   016D 90 3D 24      [24]  746 	mov	dptr,#(_myDeviceQualDscr + 0x0004)
   0170 E4            [12]  747 	clr	a
   0171 F0            [24]  748 	movx	@dptr,a
   0172 90 3D 25      [24]  749 	mov	dptr,#(_myDeviceQualDscr + 0x0005)
   0175 F0            [24]  750 	movx	@dptr,a
   0176 90 3D 26      [24]  751 	mov	dptr,#(_myDeviceQualDscr + 0x0006)
   0179 F0            [24]  752 	movx	@dptr,a
   017A 90 3D 27      [24]  753 	mov	dptr,#(_myDeviceQualDscr + 0x0007)
   017D 74 40         [12]  754 	mov	a,#0x40
   017F F0            [24]  755 	movx	@dptr,a
   0180 90 3D 28      [24]  756 	mov	dptr,#(_myDeviceQualDscr + 0x0008)
   0183 74 01         [12]  757 	mov	a,#0x01
   0185 F0            [24]  758 	movx	@dptr,a
                            759 ;	convert_serial.c:177: CONFIGDSCR xdata at 0x3d30 myConfigDscr = {
   0186 90 3D 30      [24]  760 	mov	dptr,#_myConfigDscr
   0189 74 09         [12]  761 	mov	a,#0x09
   018B F0            [24]  762 	movx	@dptr,a
   018C 90 3D 31      [24]  763 	mov	dptr,#(_myConfigDscr + 0x0001)
   018F 74 02         [12]  764 	mov	a,#0x02
   0191 F0            [24]  765 	movx	@dptr,a
   0192 90 3D 32      [24]  766 	mov	dptr,#(_myConfigDscr + 0x0002)
   0195 74 20         [12]  767 	mov	a,#0x20
   0197 F0            [24]  768 	movx	@dptr,a
   0198 E4            [12]  769 	clr	a
   0199 A3            [24]  770 	inc	dptr
   019A F0            [24]  771 	movx	@dptr,a
   019B 90 3D 34      [24]  772 	mov	dptr,#(_myConfigDscr + 0x0004)
   019E 74 01         [12]  773 	mov	a,#0x01
   01A0 F0            [24]  774 	movx	@dptr,a
   01A1 90 3D 35      [24]  775 	mov	dptr,#(_myConfigDscr + 0x0005)
   01A4 74 01         [12]  776 	mov	a,#0x01
   01A6 F0            [24]  777 	movx	@dptr,a
   01A7 90 3D 36      [24]  778 	mov	dptr,#(_myConfigDscr + 0x0006)
   01AA E4            [12]  779 	clr	a
   01AB F0            [24]  780 	movx	@dptr,a
   01AC 90 3D 37      [24]  781 	mov	dptr,#(_myConfigDscr + 0x0007)
   01AF 74 A0         [12]  782 	mov	a,#0xA0
   01B1 F0            [24]  783 	movx	@dptr,a
   01B2 90 3D 38      [24]  784 	mov	dptr,#(_myConfigDscr + 0x0008)
   01B5 74 1E         [12]  785 	mov	a,#0x1E
   01B7 F0            [24]  786 	movx	@dptr,a
                            787 ;	convert_serial.c:188: INTRFCDSCR xdata at 0x3d30+DSCR_OFFSET(0,0) myIntrfcDscr = {
   01B8 90 3D 39      [24]  788 	mov	dptr,#_myIntrfcDscr
   01BB 74 09         [12]  789 	mov	a,#0x09
   01BD F0            [24]  790 	movx	@dptr,a
   01BE 90 3D 3A      [24]  791 	mov	dptr,#(_myIntrfcDscr + 0x0001)
   01C1 74 04         [12]  792 	mov	a,#0x04
   01C3 F0            [24]  793 	movx	@dptr,a
   01C4 90 3D 3B      [24]  794 	mov	dptr,#(_myIntrfcDscr + 0x0002)
   01C7 E4            [12]  795 	clr	a
   01C8 F0            [24]  796 	movx	@dptr,a
   01C9 90 3D 3C      [24]  797 	mov	dptr,#(_myIntrfcDscr + 0x0003)
   01CC F0            [24]  798 	movx	@dptr,a
   01CD 90 3D 3D      [24]  799 	mov	dptr,#(_myIntrfcDscr + 0x0004)
   01D0 74 02         [12]  800 	mov	a,#0x02
   01D2 F0            [24]  801 	movx	@dptr,a
   01D3 90 3D 3E      [24]  802 	mov	dptr,#(_myIntrfcDscr + 0x0005)
   01D6 74 FF         [12]  803 	mov	a,#0xFF
   01D8 F0            [24]  804 	movx	@dptr,a
   01D9 90 3D 3F      [24]  805 	mov	dptr,#(_myIntrfcDscr + 0x0006)
   01DC 74 FF         [12]  806 	mov	a,#0xFF
   01DE F0            [24]  807 	movx	@dptr,a
   01DF 90 3D 40      [24]  808 	mov	dptr,#(_myIntrfcDscr + 0x0007)
   01E2 74 FF         [12]  809 	mov	a,#0xFF
   01E4 F0            [24]  810 	movx	@dptr,a
   01E5 90 3D 41      [24]  811 	mov	dptr,#(_myIntrfcDscr + 0x0008)
   01E8 E4            [12]  812 	clr	a
   01E9 F0            [24]  813 	movx	@dptr,a
                            814 ;	convert_serial.c:200: ENDPNTDSCR xdata at 0x3d30+DSCR_OFFSET(1,0) myInEndpntDscr = {
   01EA 90 3D 42      [24]  815 	mov	dptr,#_myInEndpntDscr
   01ED 74 07         [12]  816 	mov	a,#0x07
   01EF F0            [24]  817 	movx	@dptr,a
   01F0 90 3D 43      [24]  818 	mov	dptr,#(_myInEndpntDscr + 0x0001)
   01F3 74 05         [12]  819 	mov	a,#0x05
   01F5 F0            [24]  820 	movx	@dptr,a
   01F6 90 3D 44      [24]  821 	mov	dptr,#(_myInEndpntDscr + 0x0002)
   01F9 74 81         [12]  822 	mov	a,#0x81
   01FB F0            [24]  823 	movx	@dptr,a
   01FC 90 3D 45      [24]  824 	mov	dptr,#(_myInEndpntDscr + 0x0003)
   01FF 74 02         [12]  825 	mov	a,#0x02
   0201 F0            [24]  826 	movx	@dptr,a
   0202 90 3D 46      [24]  827 	mov	dptr,#(_myInEndpntDscr + 0x0004)
   0205 E4            [12]  828 	clr	a
   0206 F0            [24]  829 	movx	@dptr,a
   0207 74 02         [12]  830 	mov	a,#0x02
   0209 A3            [24]  831 	inc	dptr
   020A F0            [24]  832 	movx	@dptr,a
   020B 90 3D 48      [24]  833 	mov	dptr,#(_myInEndpntDscr + 0x0006)
   020E E4            [12]  834 	clr	a
   020F F0            [24]  835 	movx	@dptr,a
                            836 ;	convert_serial.c:210: ENDPNTDSCR xdata at 0x3d30+DSCR_OFFSET(1,1) myOutEndpntDscr = {
   0210 90 3D 49      [24]  837 	mov	dptr,#_myOutEndpntDscr
   0213 74 07         [12]  838 	mov	a,#0x07
   0215 F0            [24]  839 	movx	@dptr,a
   0216 90 3D 4A      [24]  840 	mov	dptr,#(_myOutEndpntDscr + 0x0001)
   0219 74 05         [12]  841 	mov	a,#0x05
   021B F0            [24]  842 	movx	@dptr,a
   021C 90 3D 4B      [24]  843 	mov	dptr,#(_myOutEndpntDscr + 0x0002)
   021F 74 01         [12]  844 	mov	a,#0x01
   0221 F0            [24]  845 	movx	@dptr,a
   0222 90 3D 4C      [24]  846 	mov	dptr,#(_myOutEndpntDscr + 0x0003)
   0225 74 02         [12]  847 	mov	a,#0x02
   0227 F0            [24]  848 	movx	@dptr,a
   0228 90 3D 4D      [24]  849 	mov	dptr,#(_myOutEndpntDscr + 0x0004)
   022B E4            [12]  850 	clr	a
   022C F0            [24]  851 	movx	@dptr,a
   022D 74 02         [12]  852 	mov	a,#0x02
   022F A3            [24]  853 	inc	dptr
   0230 F0            [24]  854 	movx	@dptr,a
   0231 90 3D 4F      [24]  855 	mov	dptr,#(_myOutEndpntDscr + 0x0006)
   0234 E4            [12]  856 	clr	a
   0235 F0            [24]  857 	movx	@dptr,a
                            858 	.area GSFINAL (CODE)
   0236 02 00 46      [24]  859 	ljmp	__sdcc_program_startup
                            860 ;--------------------------------------------------------
                            861 ; Home
                            862 ;--------------------------------------------------------
                            863 	.area HOME    (CODE)
                            864 	.area HOME    (CODE)
   0046                     865 __sdcc_program_startup:
   0046 02 08 AE      [24]  866 	ljmp	_main
                            867 ;	return from main will return to caller
                            868 ;--------------------------------------------------------
                            869 ; code
                            870 ;--------------------------------------------------------
                            871 	.area CSEG    (CODE)
                            872 ;------------------------------------------------------------
                            873 ;Allocation info for local variables in function 'count_array_size'
                            874 ;------------------------------------------------------------
                            875 ;array                     Allocated to registers 
                            876 ;size                      Allocated to registers r3 r4 
                            877 ;------------------------------------------------------------
                            878 ;	convert_serial.c:224: static int count_array_size(void ** array)
                            879 ;	-----------------------------------------
                            880 ;	 function count_array_size
                            881 ;	-----------------------------------------
   0239                     882 _count_array_size:
                     0007   883 	ar7 = 0x07
                     0006   884 	ar6 = 0x06
                     0005   885 	ar5 = 0x05
                     0004   886 	ar4 = 0x04
                     0003   887 	ar3 = 0x03
                     0002   888 	ar2 = 0x02
                     0001   889 	ar1 = 0x01
                     0000   890 	ar0 = 0x00
   0239 AD 82         [24]  891 	mov	r5,dpl
   023B AE 83         [24]  892 	mov	r6,dph
   023D AF F0         [24]  893 	mov	r7,b
                            894 ;	convert_serial.c:227: for (size=0; *array != 0; array++, size++);
   023F 7B 00         [12]  895 	mov	r3,#0x00
   0241 7C 00         [12]  896 	mov	r4,#0x00
   0243                     897 00103$:
   0243 8D 82         [24]  898 	mov	dpl,r5
   0245 8E 83         [24]  899 	mov	dph,r6
   0247 8F F0         [24]  900 	mov	b,r7
   0249 12 08 E9      [24]  901 	lcall	__gptrget
   024C F8            [12]  902 	mov	r0,a
   024D A3            [24]  903 	inc	dptr
   024E 12 08 E9      [24]  904 	lcall	__gptrget
   0251 F9            [12]  905 	mov	r1,a
   0252 A3            [24]  906 	inc	dptr
   0253 12 08 E9      [24]  907 	lcall	__gptrget
   0256 FA            [12]  908 	mov	r2,a
   0257 E4            [12]  909 	clr	a
   0258 C0 E0         [24]  910 	push	acc
   025A E4            [12]  911 	clr	a
   025B C0 E0         [24]  912 	push	acc
   025D E4            [12]  913 	clr	a
   025E C0 E0         [24]  914 	push	acc
   0260 88 82         [24]  915 	mov	dpl,r0
   0262 89 83         [24]  916 	mov	dph,r1
   0264 8A F0         [24]  917 	mov	b,r2
   0266 12 00 49      [24]  918 	lcall	___gptr_cmp
   0269 15 81         [12]  919 	dec	sp
   026B 15 81         [12]  920 	dec	sp
   026D 15 81         [12]  921 	dec	sp
   026F 60 0E         [24]  922 	jz	00101$
   0271 74 03         [12]  923 	mov	a,#0x03
   0273 2D            [12]  924 	add	a,r5
   0274 FD            [12]  925 	mov	r5,a
   0275 E4            [12]  926 	clr	a
   0276 3E            [12]  927 	addc	a,r6
   0277 FE            [12]  928 	mov	r6,a
   0278 0B            [12]  929 	inc	r3
   0279 BB 00 C7      [24]  930 	cjne	r3,#0x00,00103$
   027C 0C            [12]  931 	inc	r4
   027D 80 C4         [24]  932 	sjmp	00103$
   027F                     933 00101$:
                            934 ;	convert_serial.c:228: return size;
   027F 8B 82         [24]  935 	mov	dpl,r3
   0281 8C 83         [24]  936 	mov	dph,r4
   0283 22            [24]  937 	ret
                            938 ;------------------------------------------------------------
                            939 ;Allocation info for local variables in function 'SetupCommand'
                            940 ;------------------------------------------------------------
                            941 ;i                         Allocated with name '_SetupCommand_i_1_21'
                            942 ;interface                 Allocated to registers r6 r7 
                            943 ;------------------------------------------------------------
                            944 ;	convert_serial.c:231: static void SetupCommand(void)
                            945 ;	-----------------------------------------
                            946 ;	 function SetupCommand
                            947 ;	-----------------------------------------
   0284                     948 _SetupCommand:
                            949 ;	convert_serial.c:238: switch(SETUPDAT[0] & SETUP_MASK) {
   0284 90 E6 B8      [24]  950 	mov	dptr,#_SETUPDAT
   0287 E0            [24]  951 	movx	a,@dptr
   0288 FF            [12]  952 	mov	r7,a
   0289 53 07 60      [24]  953 	anl	ar7,#0x60
   028C BF 00 02      [24]  954 	cjne	r7,#0x00,00245$
   028F 80 03         [24]  955 	sjmp	00246$
   0291                     956 00245$:
   0291 02 07 0B      [24]  957 	ljmp	00160$
   0294                     958 00246$:
                            959 ;	convert_serial.c:241: switch(SETUPDAT[1])
   0294 90 E6 B9      [24]  960 	mov	dptr,#(_SETUPDAT + 0x0001)
   0297 E0            [24]  961 	movx	a,@dptr
   0298 FF            [12]  962 	mov  r7,a
   0299 24 F4         [12]  963 	add	a,#0xff - 0x0B
   029B 50 03         [24]  964 	jnc	00247$
   029D 02 07 01      [24]  965 	ljmp	00158$
   02A0                     966 00247$:
   02A0 EF            [12]  967 	mov	a,r7
   02A1 24 0A         [12]  968 	add	a,#(00248$-3-.)
   02A3 83            [24]  969 	movc	a,@a+pc
   02A4 F5 82         [12]  970 	mov	dpl,a
   02A6 EF            [12]  971 	mov	a,r7
   02A7 24 10         [12]  972 	add	a,#(00249$-3-.)
   02A9 83            [24]  973 	movc	a,@a+pc
   02AA F5 83         [12]  974 	mov	dph,a
   02AC E4            [12]  975 	clr	a
   02AD 73            [24]  976 	jmp	@a+dptr
   02AE                     977 00248$:
   02AE 0E                  978 	.db	00130$
   02AF B0                  979 	.db	00136$
   02B0 01                  980 	.db	00158$
   02B1 67                  981 	.db	00146$
   02B2 01                  982 	.db	00158$
   02B3 01                  983 	.db	00158$
   02B4 C6                  984 	.db	00102$
   02B5 01                  985 	.db	00158$
   02B6 FA                  986 	.db	00129$
   02B7 F1                  987 	.db	00128$
   02B8 A0                  988 	.db	00122$
   02B9 CE                  989 	.db	00125$
   02BA                     990 00249$:
   02BA 05                  991 	.db	00130$>>8
   02BB 05                  992 	.db	00136$>>8
   02BC 07                  993 	.db	00158$>>8
   02BD 06                  994 	.db	00146$>>8
   02BE 07                  995 	.db	00158$>>8
   02BF 07                  996 	.db	00158$>>8
   02C0 02                  997 	.db	00102$>>8
   02C1 07                  998 	.db	00158$>>8
   02C2 04                  999 	.db	00129$>>8
   02C3 04                 1000 	.db	00128$>>8
   02C4 04                 1001 	.db	00122$>>8
   02C5 04                 1002 	.db	00125$>>8
                           1003 ;	convert_serial.c:243: case SC_GET_DESCRIPTOR:
   02C6                    1004 00102$:
                           1005 ;	convert_serial.c:244: switch(SETUPDAT[3])
   02C6 90 E6 BB      [24] 1006 	mov	dptr,#(_SETUPDAT + 0x0003)
   02C9 E0            [24] 1007 	movx	a,@dptr
   02CA FF            [12] 1008 	mov	r7,a
   02CB BF 01 02      [24] 1009 	cjne	r7,#0x01,00250$
   02CE 80 19         [24] 1010 	sjmp	00103$
   02D0                    1011 00250$:
   02D0 BF 02 02      [24] 1012 	cjne	r7,#0x02,00251$
   02D3 80 46         [24] 1013 	sjmp	00105$
   02D5                    1014 00251$:
   02D5 BF 03 03      [24] 1015 	cjne	r7,#0x03,00252$
   02D8 02 03 B5      [24] 1016 	ljmp	00113$
   02DB                    1017 00252$:
   02DB BF 06 02      [24] 1018 	cjne	r7,#0x06,00253$
   02DE 80 22         [24] 1019 	sjmp	00104$
   02E0                    1020 00253$:
   02E0 BF 07 03      [24] 1021 	cjne	r7,#0x07,00254$
   02E3 02 03 68      [24] 1022 	ljmp	00109$
   02E6                    1023 00254$:
   02E6 02 04 95      [24] 1024 	ljmp	00120$
                           1025 ;	convert_serial.c:246: case GD_DEVICE:
   02E9                    1026 00103$:
                           1027 ;	convert_serial.c:247: SUDPTRH = MSB(&myDeviceDscr);
   02E9 7E 00         [12] 1028 	mov	r6,#_myDeviceDscr
   02EB 7F 3D         [12] 1029 	mov	r7,#(_myDeviceDscr >> 8)
   02ED 8F 06         [24] 1030 	mov	ar6,r7
   02EF 90 E6 B3      [24] 1031 	mov	dptr,#_SUDPTRH
   02F2 EE            [12] 1032 	mov	a,r6
   02F3 F0            [24] 1033 	movx	@dptr,a
                           1034 ;	convert_serial.c:248: SUDPTRL = LSB(&myDeviceDscr);
   02F4 7E 00         [12] 1035 	mov	r6,#_myDeviceDscr
   02F6 7F 3D         [12] 1036 	mov	r7,#(_myDeviceDscr >> 8)
   02F8 7F 00         [12] 1037 	mov	r7,#0x00
   02FA 90 E6 B4      [24] 1038 	mov	dptr,#_SUDPTRL
   02FD EE            [12] 1039 	mov	a,r6
   02FE F0            [24] 1040 	movx	@dptr,a
                           1041 ;	convert_serial.c:249: break;
   02FF 02 07 13      [24] 1042 	ljmp	00161$
                           1043 ;	convert_serial.c:250: case GD_DEVICE_QUALIFIER:
   0302                    1044 00104$:
                           1045 ;	convert_serial.c:251: SUDPTRH = MSB(&myDeviceQualDscr);
   0302 7E 20         [12] 1046 	mov	r6,#_myDeviceQualDscr
   0304 7F 3D         [12] 1047 	mov	r7,#(_myDeviceQualDscr >> 8)
   0306 8F 06         [24] 1048 	mov	ar6,r7
   0308 90 E6 B3      [24] 1049 	mov	dptr,#_SUDPTRH
   030B EE            [12] 1050 	mov	a,r6
   030C F0            [24] 1051 	movx	@dptr,a
                           1052 ;	convert_serial.c:252: SUDPTRL = LSB(&myDeviceQualDscr);
   030D 7E 20         [12] 1053 	mov	r6,#_myDeviceQualDscr
   030F 7F 3D         [12] 1054 	mov	r7,#(_myDeviceQualDscr >> 8)
   0311 7F 00         [12] 1055 	mov	r7,#0x00
   0313 90 E6 B4      [24] 1056 	mov	dptr,#_SUDPTRL
   0316 EE            [12] 1057 	mov	a,r6
   0317 F0            [24] 1058 	movx	@dptr,a
                           1059 ;	convert_serial.c:253: break;
   0318 02 07 13      [24] 1060 	ljmp	00161$
                           1061 ;	convert_serial.c:254: case GD_CONFIGURATION:
   031B                    1062 00105$:
                           1063 ;	convert_serial.c:255: myConfigDscr.type = CONFIG_DSCR;
   031B 90 3D 31      [24] 1064 	mov	dptr,#(_myConfigDscr + 0x0001)
   031E 74 02         [12] 1065 	mov	a,#0x02
   0320 F0            [24] 1066 	movx	@dptr,a
                           1067 ;	convert_serial.c:256: if (USBCS & bmHSM) {
   0321 90 E6 80      [24] 1068 	mov	dptr,#_USBCS
   0324 E0            [24] 1069 	movx	a,@dptr
   0325 FF            [12] 1070 	mov	r7,a
   0326 30 E7 14      [24] 1071 	jnb	acc.7,00107$
                           1072 ;	convert_serial.c:258: myInEndpntDscr.mp = 64;
   0329 90 3D 46      [24] 1073 	mov	dptr,#(_myInEndpntDscr + 0x0004)
   032C 74 40         [12] 1074 	mov	a,#0x40
   032E F0            [24] 1075 	movx	@dptr,a
   032F E4            [12] 1076 	clr	a
   0330 A3            [24] 1077 	inc	dptr
   0331 F0            [24] 1078 	movx	@dptr,a
                           1079 ;	convert_serial.c:259: myOutEndpntDscr.mp = 64;
   0332 90 3D 4D      [24] 1080 	mov	dptr,#(_myOutEndpntDscr + 0x0004)
   0335 74 40         [12] 1081 	mov	a,#0x40
   0337 F0            [24] 1082 	movx	@dptr,a
   0338 E4            [12] 1083 	clr	a
   0339 A3            [24] 1084 	inc	dptr
   033A F0            [24] 1085 	movx	@dptr,a
   033B 80 12         [24] 1086 	sjmp	00108$
   033D                    1087 00107$:
                           1088 ;	convert_serial.c:262: myInEndpntDscr.mp = 64;
   033D 90 3D 46      [24] 1089 	mov	dptr,#(_myInEndpntDscr + 0x0004)
   0340 74 40         [12] 1090 	mov	a,#0x40
   0342 F0            [24] 1091 	movx	@dptr,a
   0343 E4            [12] 1092 	clr	a
   0344 A3            [24] 1093 	inc	dptr
   0345 F0            [24] 1094 	movx	@dptr,a
                           1095 ;	convert_serial.c:263: myOutEndpntDscr.mp = 64;
   0346 90 3D 4D      [24] 1096 	mov	dptr,#(_myOutEndpntDscr + 0x0004)
   0349 74 40         [12] 1097 	mov	a,#0x40
   034B F0            [24] 1098 	movx	@dptr,a
   034C E4            [12] 1099 	clr	a
   034D A3            [24] 1100 	inc	dptr
   034E F0            [24] 1101 	movx	@dptr,a
   034F                    1102 00108$:
                           1103 ;	convert_serial.c:265: SUDPTRH = MSB(&myConfigDscr);
   034F 7E 30         [12] 1104 	mov	r6,#_myConfigDscr
   0351 7F 3D         [12] 1105 	mov	r7,#(_myConfigDscr >> 8)
   0353 8F 06         [24] 1106 	mov	ar6,r7
   0355 90 E6 B3      [24] 1107 	mov	dptr,#_SUDPTRH
   0358 EE            [12] 1108 	mov	a,r6
   0359 F0            [24] 1109 	movx	@dptr,a
                           1110 ;	convert_serial.c:266: SUDPTRL = LSB(&myConfigDscr);
   035A 7E 30         [12] 1111 	mov	r6,#_myConfigDscr
   035C 7F 3D         [12] 1112 	mov	r7,#(_myConfigDscr >> 8)
   035E 7F 00         [12] 1113 	mov	r7,#0x00
   0360 90 E6 B4      [24] 1114 	mov	dptr,#_SUDPTRL
   0363 EE            [12] 1115 	mov	a,r6
   0364 F0            [24] 1116 	movx	@dptr,a
                           1117 ;	convert_serial.c:267: break;
   0365 02 07 13      [24] 1118 	ljmp	00161$
                           1119 ;	convert_serial.c:268: case GD_OTHER_SPEED_CONFIGURATION:
   0368                    1120 00109$:
                           1121 ;	convert_serial.c:269: myConfigDscr.type = OTHERSPEED_DSCR;
   0368 90 3D 31      [24] 1122 	mov	dptr,#(_myConfigDscr + 0x0001)
   036B 74 07         [12] 1123 	mov	a,#0x07
   036D F0            [24] 1124 	movx	@dptr,a
                           1125 ;	convert_serial.c:270: if (USBCS & bmHSM) {
   036E 90 E6 80      [24] 1126 	mov	dptr,#_USBCS
   0371 E0            [24] 1127 	movx	a,@dptr
   0372 FF            [12] 1128 	mov	r7,a
   0373 30 E7 14      [24] 1129 	jnb	acc.7,00111$
                           1130 ;	convert_serial.c:273: myInEndpntDscr.mp = 64;
   0376 90 3D 46      [24] 1131 	mov	dptr,#(_myInEndpntDscr + 0x0004)
   0379 74 40         [12] 1132 	mov	a,#0x40
   037B F0            [24] 1133 	movx	@dptr,a
   037C E4            [12] 1134 	clr	a
   037D A3            [24] 1135 	inc	dptr
   037E F0            [24] 1136 	movx	@dptr,a
                           1137 ;	convert_serial.c:274: myOutEndpntDscr.mp = 64;
   037F 90 3D 4D      [24] 1138 	mov	dptr,#(_myOutEndpntDscr + 0x0004)
   0382 74 40         [12] 1139 	mov	a,#0x40
   0384 F0            [24] 1140 	movx	@dptr,a
   0385 E4            [12] 1141 	clr	a
   0386 A3            [24] 1142 	inc	dptr
   0387 F0            [24] 1143 	movx	@dptr,a
   0388 80 12         [24] 1144 	sjmp	00112$
   038A                    1145 00111$:
                           1146 ;	convert_serial.c:278: myInEndpntDscr.mp = 64;
   038A 90 3D 46      [24] 1147 	mov	dptr,#(_myInEndpntDscr + 0x0004)
   038D 74 40         [12] 1148 	mov	a,#0x40
   038F F0            [24] 1149 	movx	@dptr,a
   0390 E4            [12] 1150 	clr	a
   0391 A3            [24] 1151 	inc	dptr
   0392 F0            [24] 1152 	movx	@dptr,a
                           1153 ;	convert_serial.c:279: myOutEndpntDscr.mp = 64;
   0393 90 3D 4D      [24] 1154 	mov	dptr,#(_myOutEndpntDscr + 0x0004)
   0396 74 40         [12] 1155 	mov	a,#0x40
   0398 F0            [24] 1156 	movx	@dptr,a
   0399 E4            [12] 1157 	clr	a
   039A A3            [24] 1158 	inc	dptr
   039B F0            [24] 1159 	movx	@dptr,a
   039C                    1160 00112$:
                           1161 ;	convert_serial.c:281: SUDPTRH = MSB(&myConfigDscr);
   039C 7E 30         [12] 1162 	mov	r6,#_myConfigDscr
   039E 7F 3D         [12] 1163 	mov	r7,#(_myConfigDscr >> 8)
   03A0 8F 06         [24] 1164 	mov	ar6,r7
   03A2 90 E6 B3      [24] 1165 	mov	dptr,#_SUDPTRH
   03A5 EE            [12] 1166 	mov	a,r6
   03A6 F0            [24] 1167 	movx	@dptr,a
                           1168 ;	convert_serial.c:282: SUDPTRL = LSB(&myConfigDscr);
   03A7 7E 30         [12] 1169 	mov	r6,#_myConfigDscr
   03A9 7F 3D         [12] 1170 	mov	r7,#(_myConfigDscr >> 8)
   03AB 7F 00         [12] 1171 	mov	r7,#0x00
   03AD 90 E6 B4      [24] 1172 	mov	dptr,#_SUDPTRL
   03B0 EE            [12] 1173 	mov	a,r6
   03B1 F0            [24] 1174 	movx	@dptr,a
                           1175 ;	convert_serial.c:283: break;
   03B2 02 07 13      [24] 1176 	ljmp	00161$
                           1177 ;	convert_serial.c:284: case GD_STRING:
   03B5                    1178 00113$:
                           1179 ;	convert_serial.c:285: if (SETUPDAT[2] >= count_array_size((void **) USB_strings)) {
   03B5 90 E6 BA      [24] 1180 	mov	dptr,#(_SETUPDAT + 0x0002)
   03B8 E0            [24] 1181 	movx	a,@dptr
   03B9 FF            [12] 1182 	mov	r7,a
   03BA 90 00 0A      [24] 1183 	mov	dptr,#_USB_strings
   03BD 75 F0 40      [24] 1184 	mov	b,#0x40
   03C0 C0 07         [24] 1185 	push	ar7
   03C2 12 02 39      [24] 1186 	lcall	_count_array_size
   03C5 AD 82         [24] 1187 	mov	r5,dpl
   03C7 AE 83         [24] 1188 	mov	r6,dph
   03C9 D0 07         [24] 1189 	pop	ar7
   03CB 7C 00         [12] 1190 	mov	r4,#0x00
   03CD C3            [12] 1191 	clr	c
   03CE EF            [12] 1192 	mov	a,r7
   03CF 9D            [12] 1193 	subb	a,r5
   03D0 EC            [12] 1194 	mov	a,r4
   03D1 64 80         [12] 1195 	xrl	a,#0x80
   03D3 8E F0         [24] 1196 	mov	b,r6
   03D5 63 F0 80      [24] 1197 	xrl	b,#0x80
   03D8 95 F0         [12] 1198 	subb	a,b
   03DA 40 0B         [24] 1199 	jc	00177$
                           1200 ;	convert_serial.c:286: EZUSB_STALL_EP0();
   03DC 90 E6 A0      [24] 1201 	mov	dptr,#_EP0CS
   03DF E0            [24] 1202 	movx	a,@dptr
   03E0 FF            [12] 1203 	mov	r7,a
   03E1 44 01         [12] 1204 	orl	a,#0x01
   03E3 F0            [24] 1205 	movx	@dptr,a
   03E4 02 07 13      [24] 1206 	ljmp	00161$
                           1207 ;	convert_serial.c:288: for (i=0; i<31; i++) {
   03E7                    1208 00177$:
   03E7 E4            [12] 1209 	clr	a
   03E8 F5 13         [12] 1210 	mov	_SetupCommand_i_1_21,a
   03EA F5 14         [12] 1211 	mov	(_SetupCommand_i_1_21 + 1),a
   03EC                    1212 00162$:
                           1213 ;	convert_serial.c:289: if (USB_strings[SETUPDAT[2]][i] == '\0') break;
   03EC 90 E6 BA      [24] 1214 	mov	dptr,#(_SETUPDAT + 0x0002)
   03EF E0            [24] 1215 	movx	a,@dptr
   03F0 75 F0 03      [24] 1216 	mov	b,#0x03
   03F3 A4            [48] 1217 	mul	ab
   03F4 24 0A         [12] 1218 	add	a,#_USB_strings
   03F6 F9            [12] 1219 	mov	r1,a
   03F7 87 03         [24] 1220 	mov	ar3,@r1
   03F9 09            [12] 1221 	inc	r1
   03FA 87 04         [24] 1222 	mov	ar4,@r1
   03FC 09            [12] 1223 	inc	r1
   03FD 87 05         [24] 1224 	mov	ar5,@r1
   03FF 19            [12] 1225 	dec	r1
   0400 19            [12] 1226 	dec	r1
   0401 E5 13         [12] 1227 	mov	a,_SetupCommand_i_1_21
   0403 2B            [12] 1228 	add	a,r3
   0404 FB            [12] 1229 	mov	r3,a
   0405 E5 14         [12] 1230 	mov	a,(_SetupCommand_i_1_21 + 1)
   0407 3C            [12] 1231 	addc	a,r4
   0408 FC            [12] 1232 	mov	r4,a
   0409 8B 82         [24] 1233 	mov	dpl,r3
   040B 8C 83         [24] 1234 	mov	dph,r4
   040D 8D F0         [24] 1235 	mov	b,r5
   040F 12 08 E9      [24] 1236 	lcall	__gptrget
   0412 60 60         [24] 1237 	jz	00116$
                           1238 ;	convert_serial.c:290: EP0BUF[2*i+2] = USB_strings[SETUPDAT[2]][i];
   0414 E5 13         [12] 1239 	mov	a,_SetupCommand_i_1_21
   0416 25 E0         [12] 1240 	add	a,acc
   0418 FD            [12] 1241 	mov	r5,a
   0419 24 02         [12] 1242 	add	a,#0x02
   041B 24 40         [12] 1243 	add	a,#_EP0BUF
   041D FB            [12] 1244 	mov	r3,a
   041E E4            [12] 1245 	clr	a
   041F 34 E7         [12] 1246 	addc	a,#(_EP0BUF >> 8)
   0421 FC            [12] 1247 	mov	r4,a
   0422 90 E6 BA      [24] 1248 	mov	dptr,#(_SETUPDAT + 0x0002)
   0425 E0            [24] 1249 	movx	a,@dptr
   0426 75 F0 03      [24] 1250 	mov	b,#0x03
   0429 A4            [48] 1251 	mul	ab
   042A 24 0A         [12] 1252 	add	a,#_USB_strings
   042C F9            [12] 1253 	mov	r1,a
   042D 87 02         [24] 1254 	mov	ar2,@r1
   042F 09            [12] 1255 	inc	r1
   0430 87 06         [24] 1256 	mov	ar6,@r1
   0432 09            [12] 1257 	inc	r1
   0433 87 07         [24] 1258 	mov	ar7,@r1
   0435 19            [12] 1259 	dec	r1
   0436 19            [12] 1260 	dec	r1
   0437 E5 13         [12] 1261 	mov	a,_SetupCommand_i_1_21
   0439 2A            [12] 1262 	add	a,r2
   043A FA            [12] 1263 	mov	r2,a
   043B E5 14         [12] 1264 	mov	a,(_SetupCommand_i_1_21 + 1)
   043D 3E            [12] 1265 	addc	a,r6
   043E FE            [12] 1266 	mov	r6,a
   043F 8A 82         [24] 1267 	mov	dpl,r2
   0441 8E 83         [24] 1268 	mov	dph,r6
   0443 8F F0         [24] 1269 	mov	b,r7
   0445 12 08 E9      [24] 1270 	lcall	__gptrget
   0448 FA            [12] 1271 	mov	r2,a
   0449 8B 82         [24] 1272 	mov	dpl,r3
   044B 8C 83         [24] 1273 	mov	dph,r4
   044D F0            [24] 1274 	movx	@dptr,a
                           1275 ;	convert_serial.c:291: EP0BUF[2*i+3] = '\0';
   044E 74 03         [12] 1276 	mov	a,#0x03
   0450 2D            [12] 1277 	add	a,r5
   0451 24 40         [12] 1278 	add	a,#_EP0BUF
   0453 F5 82         [12] 1279 	mov	dpl,a
   0455 E4            [12] 1280 	clr	a
   0456 34 E7         [12] 1281 	addc	a,#(_EP0BUF >> 8)
   0458 F5 83         [12] 1282 	mov	dph,a
   045A E4            [12] 1283 	clr	a
   045B F0            [24] 1284 	movx	@dptr,a
                           1285 ;	convert_serial.c:288: for (i=0; i<31; i++) {
   045C 05 13         [12] 1286 	inc	_SetupCommand_i_1_21
   045E E4            [12] 1287 	clr	a
   045F B5 13 02      [24] 1288 	cjne	a,_SetupCommand_i_1_21,00259$
   0462 05 14         [12] 1289 	inc	(_SetupCommand_i_1_21 + 1)
   0464                    1290 00259$:
   0464 C3            [12] 1291 	clr	c
   0465 E5 13         [12] 1292 	mov	a,_SetupCommand_i_1_21
   0467 94 1F         [12] 1293 	subb	a,#0x1F
   0469 E5 14         [12] 1294 	mov	a,(_SetupCommand_i_1_21 + 1)
   046B 64 80         [12] 1295 	xrl	a,#0x80
   046D 94 80         [12] 1296 	subb	a,#0x80
   046F 50 03         [24] 1297 	jnc	00260$
   0471 02 03 EC      [24] 1298 	ljmp	00162$
   0474                    1299 00260$:
   0474                    1300 00116$:
                           1301 ;	convert_serial.c:293: EP0BUF[0] = 2*i+2;
   0474 E5 13         [12] 1302 	mov	a,_SetupCommand_i_1_21
   0476 25 E0         [12] 1303 	add	a,acc
   0478 FE            [12] 1304 	mov	r6,a
   0479 0E            [12] 1305 	inc	r6
   047A 0E            [12] 1306 	inc	r6
   047B 90 E7 40      [24] 1307 	mov	dptr,#_EP0BUF
   047E EE            [12] 1308 	mov	a,r6
   047F F0            [24] 1309 	movx	@dptr,a
                           1310 ;	convert_serial.c:294: EP0BUF[1] = STRING_DSCR;
   0480 90 E7 41      [24] 1311 	mov	dptr,#(_EP0BUF + 0x0001)
   0483 74 03         [12] 1312 	mov	a,#0x03
   0485 F0            [24] 1313 	movx	@dptr,a
                           1314 ;	convert_serial.c:295: SYNCDELAY; EP0BCH = 0;
   0486 00            [12] 1315 	nop 
   0487 90 E6 8A      [24] 1316 	mov	dptr,#_EP0BCH
   048A E4            [12] 1317 	clr	a
   048B F0            [24] 1318 	movx	@dptr,a
                           1319 ;	convert_serial.c:296: SYNCDELAY; EP0BCL = 2*i+2;
   048C 00            [12] 1320 	nop 
   048D 90 E6 8B      [24] 1321 	mov	dptr,#_EP0BCL
   0490 EE            [12] 1322 	mov	a,r6
   0491 F0            [24] 1323 	movx	@dptr,a
                           1324 ;	convert_serial.c:298: break;
   0492 02 07 13      [24] 1325 	ljmp	00161$
                           1326 ;	convert_serial.c:299: default:            // Invalid request
   0495                    1327 00120$:
                           1328 ;	convert_serial.c:300: EZUSB_STALL_EP0();
   0495 90 E6 A0      [24] 1329 	mov	dptr,#_EP0CS
   0498 E0            [24] 1330 	movx	a,@dptr
   0499 FF            [12] 1331 	mov	r7,a
   049A 44 01         [12] 1332 	orl	a,#0x01
   049C F0            [24] 1333 	movx	@dptr,a
                           1334 ;	convert_serial.c:302: break;
   049D 02 07 13      [24] 1335 	ljmp	00161$
                           1336 ;	convert_serial.c:303: case SC_GET_INTERFACE:
   04A0                    1337 00122$:
                           1338 ;	convert_serial.c:304: interface = SETUPDAT[4];
   04A0 90 E6 BC      [24] 1339 	mov	dptr,#(_SETUPDAT + 0x0004)
   04A3 E0            [24] 1340 	movx	a,@dptr
   04A4 FE            [12] 1341 	mov	r6,a
   04A5 7F 00         [12] 1342 	mov	r7,#0x00
                           1343 ;	convert_serial.c:305: if (interface < NUM_INTERFACES) {
   04A7 C3            [12] 1344 	clr	c
   04A8 EE            [12] 1345 	mov	a,r6
   04A9 94 01         [12] 1346 	subb	a,#0x01
   04AB EF            [12] 1347 	mov	a,r7
   04AC 64 80         [12] 1348 	xrl	a,#0x80
   04AE 94 80         [12] 1349 	subb	a,#0x80
   04B0 40 03         [24] 1350 	jc	00261$
   04B2 02 07 13      [24] 1351 	ljmp	00161$
   04B5                    1352 00261$:
                           1353 ;	convert_serial.c:306: EP0BUF[0] = InterfaceSetting[interface];
   04B5 EE            [12] 1354 	mov	a,r6
   04B6 24 09         [12] 1355 	add	a,#_InterfaceSetting
   04B8 F9            [12] 1356 	mov	r1,a
   04B9 87 05         [24] 1357 	mov	ar5,@r1
   04BB 90 E7 40      [24] 1358 	mov	dptr,#_EP0BUF
   04BE ED            [12] 1359 	mov	a,r5
   04BF F0            [24] 1360 	movx	@dptr,a
                           1361 ;	convert_serial.c:307: EP0BCH = 0;
   04C0 90 E6 8A      [24] 1362 	mov	dptr,#_EP0BCH
   04C3 E4            [12] 1363 	clr	a
   04C4 F0            [24] 1364 	movx	@dptr,a
                           1365 ;	convert_serial.c:308: EP0BCL = 1;
   04C5 90 E6 8B      [24] 1366 	mov	dptr,#_EP0BCL
   04C8 74 01         [12] 1367 	mov	a,#0x01
   04CA F0            [24] 1368 	movx	@dptr,a
                           1369 ;	convert_serial.c:310: break;
   04CB 02 07 13      [24] 1370 	ljmp	00161$
                           1371 ;	convert_serial.c:311: case SC_SET_INTERFACE:
   04CE                    1372 00125$:
                           1373 ;	convert_serial.c:312: interface = SETUPDAT[4];
   04CE 90 E6 BC      [24] 1374 	mov	dptr,#(_SETUPDAT + 0x0004)
   04D1 E0            [24] 1375 	movx	a,@dptr
   04D2 FD            [12] 1376 	mov	r5,a
   04D3 FE            [12] 1377 	mov	r6,a
   04D4 7F 00         [12] 1378 	mov	r7,#0x00
                           1379 ;	convert_serial.c:313: if (interface < NUM_INTERFACES) {
   04D6 C3            [12] 1380 	clr	c
   04D7 EE            [12] 1381 	mov	a,r6
   04D8 94 01         [12] 1382 	subb	a,#0x01
   04DA EF            [12] 1383 	mov	a,r7
   04DB 64 80         [12] 1384 	xrl	a,#0x80
   04DD 94 80         [12] 1385 	subb	a,#0x80
   04DF 40 03         [24] 1386 	jc	00262$
   04E1 02 07 13      [24] 1387 	ljmp	00161$
   04E4                    1388 00262$:
                           1389 ;	convert_serial.c:314: InterfaceSetting[interface] = SETUPDAT[2];
   04E4 EE            [12] 1390 	mov	a,r6
   04E5 24 09         [12] 1391 	add	a,#_InterfaceSetting
   04E7 F9            [12] 1392 	mov	r1,a
   04E8 90 E6 BA      [24] 1393 	mov	dptr,#(_SETUPDAT + 0x0002)
   04EB E0            [24] 1394 	movx	a,@dptr
   04EC FF            [12] 1395 	mov	r7,a
   04ED F7            [12] 1396 	mov	@r1,a
                           1397 ;	convert_serial.c:316: break;
   04EE 02 07 13      [24] 1398 	ljmp	00161$
                           1399 ;	convert_serial.c:317: case SC_SET_CONFIGURATION:
   04F1                    1400 00128$:
                           1401 ;	convert_serial.c:318: Configuration = SETUPDAT[2];
   04F1 90 E6 BA      [24] 1402 	mov	dptr,#(_SETUPDAT + 0x0002)
   04F4 E0            [24] 1403 	movx	a,@dptr
   04F5 F5 08         [12] 1404 	mov	_Configuration,a
                           1405 ;	convert_serial.c:319: break;
   04F7 02 07 13      [24] 1406 	ljmp	00161$
                           1407 ;	convert_serial.c:320: case SC_GET_CONFIGURATION:
   04FA                    1408 00129$:
                           1409 ;	convert_serial.c:321: EP0BUF[0] = Configuration;
   04FA 90 E7 40      [24] 1410 	mov	dptr,#_EP0BUF
   04FD E5 08         [12] 1411 	mov	a,_Configuration
   04FF F0            [24] 1412 	movx	@dptr,a
                           1413 ;	convert_serial.c:322: EP0BCH = 0;
   0500 90 E6 8A      [24] 1414 	mov	dptr,#_EP0BCH
   0503 E4            [12] 1415 	clr	a
   0504 F0            [24] 1416 	movx	@dptr,a
                           1417 ;	convert_serial.c:323: EP0BCL = 1;
   0505 90 E6 8B      [24] 1418 	mov	dptr,#_EP0BCL
   0508 74 01         [12] 1419 	mov	a,#0x01
   050A F0            [24] 1420 	movx	@dptr,a
                           1421 ;	convert_serial.c:324: break;
   050B 02 07 13      [24] 1422 	ljmp	00161$
                           1423 ;	convert_serial.c:325: case SC_GET_STATUS:
   050E                    1424 00130$:
                           1425 ;	convert_serial.c:326: switch(SETUPDAT[0])
   050E 90 E6 B8      [24] 1426 	mov	dptr,#_SETUPDAT
   0511 E0            [24] 1427 	movx	a,@dptr
   0512 FF            [12] 1428 	mov	r7,a
   0513 BF 80 02      [24] 1429 	cjne	r7,#0x80,00263$
   0516 80 0D         [24] 1430 	sjmp	00131$
   0518                    1431 00263$:
   0518 BF 81 02      [24] 1432 	cjne	r7,#0x81,00264$
   051B 80 2D         [24] 1433 	sjmp	00132$
   051D                    1434 00264$:
   051D BF 82 02      [24] 1435 	cjne	r7,#0x82,00265$
   0520 80 3E         [24] 1436 	sjmp	00133$
   0522                    1437 00265$:
   0522 02 05 A5      [24] 1438 	ljmp	00134$
                           1439 ;	convert_serial.c:328: case GS_DEVICE:
   0525                    1440 00131$:
                           1441 ;	convert_serial.c:329: EP0BUF[0] = ((BYTE)Rwuen << 1) | (BYTE)Selfpwr;
   0525 A2 01         [12] 1442 	mov	c,_Rwuen
   0527 E4            [12] 1443 	clr	a
   0528 33            [12] 1444 	rlc	a
   0529 25 E0         [12] 1445 	add	a,acc
   052B FF            [12] 1446 	mov	r7,a
   052C A2 02         [12] 1447 	mov	c,_Selfpwr
   052E E4            [12] 1448 	clr	a
   052F 33            [12] 1449 	rlc	a
   0530 FE            [12] 1450 	mov	r6,a
   0531 42 07         [12] 1451 	orl	ar7,a
   0533 90 E7 40      [24] 1452 	mov	dptr,#_EP0BUF
   0536 EF            [12] 1453 	mov	a,r7
   0537 F0            [24] 1454 	movx	@dptr,a
                           1455 ;	convert_serial.c:330: EP0BUF[1] = 0;
   0538 90 E7 41      [24] 1456 	mov	dptr,#(_EP0BUF + 0x0001)
                           1457 ;	convert_serial.c:331: EP0BCH = 0;
   053B E4            [12] 1458 	clr	a
   053C F0            [24] 1459 	movx	@dptr,a
   053D 90 E6 8A      [24] 1460 	mov	dptr,#_EP0BCH
   0540 F0            [24] 1461 	movx	@dptr,a
                           1462 ;	convert_serial.c:332: EP0BCL = 2;
   0541 90 E6 8B      [24] 1463 	mov	dptr,#_EP0BCL
   0544 74 02         [12] 1464 	mov	a,#0x02
   0546 F0            [24] 1465 	movx	@dptr,a
                           1466 ;	convert_serial.c:333: break;
   0547 02 07 13      [24] 1467 	ljmp	00161$
                           1468 ;	convert_serial.c:334: case GS_INTERFACE:
   054A                    1469 00132$:
                           1470 ;	convert_serial.c:335: EP0BUF[0] = 0;
   054A 90 E7 40      [24] 1471 	mov	dptr,#_EP0BUF
                           1472 ;	convert_serial.c:336: EP0BUF[1] = 0;
                           1473 ;	convert_serial.c:337: EP0BCH = 0;
   054D E4            [12] 1474 	clr	a
   054E F0            [24] 1475 	movx	@dptr,a
   054F 90 E7 41      [24] 1476 	mov	dptr,#(_EP0BUF + 0x0001)
   0552 F0            [24] 1477 	movx	@dptr,a
   0553 90 E6 8A      [24] 1478 	mov	dptr,#_EP0BCH
   0556 F0            [24] 1479 	movx	@dptr,a
                           1480 ;	convert_serial.c:338: EP0BCL = 2;
   0557 90 E6 8B      [24] 1481 	mov	dptr,#_EP0BCL
   055A 74 02         [12] 1482 	mov	a,#0x02
   055C F0            [24] 1483 	movx	@dptr,a
                           1484 ;	convert_serial.c:339: break;
   055D 02 07 13      [24] 1485 	ljmp	00161$
                           1486 ;	convert_serial.c:340: case GS_ENDPOINT:
   0560                    1487 00133$:
                           1488 ;	convert_serial.c:341: EP0BUF[0] = *(BYTE xdata *) epcs(SETUPDAT[4]) & bmEPSTALL;
   0560 90 E6 BC      [24] 1489 	mov	dptr,#(_SETUPDAT + 0x0004)
   0563 E0            [24] 1490 	movx	a,@dptr
   0564 FF            [12] 1491 	mov	r7,a
   0565 53 07 7E      [24] 1492 	anl	ar7,#0x7E
   0568 90 E6 BC      [24] 1493 	mov	dptr,#(_SETUPDAT + 0x0004)
   056B E0            [24] 1494 	movx	a,@dptr
   056C FE            [12] 1495 	mov	r6,a
   056D C3            [12] 1496 	clr	c
   056E 74 80         [12] 1497 	mov	a,#0x80
   0570 9E            [12] 1498 	subb	a,r6
   0571 E4            [12] 1499 	clr	a
   0572 33            [12] 1500 	rlc	a
   0573 4F            [12] 1501 	orl	a,r7
   0574 90 09 09      [24] 1502 	mov	dptr,#_EPCS_Offset_Lookup_Table
   0577 93            [24] 1503 	movc	a,@a+dptr
   0578 FF            [12] 1504 	mov	r7,a
   0579 33            [12] 1505 	rlc	a
   057A 95 E0         [12] 1506 	subb	a,acc
   057C FE            [12] 1507 	mov	r6,a
   057D 74 A1         [12] 1508 	mov	a,#0xA1
   057F 2F            [12] 1509 	add	a,r7
   0580 FF            [12] 1510 	mov	r7,a
   0581 74 E6         [12] 1511 	mov	a,#0xE6
   0583 3E            [12] 1512 	addc	a,r6
   0584 FE            [12] 1513 	mov	r6,a
   0585 8F 82         [24] 1514 	mov	dpl,r7
   0587 8E 83         [24] 1515 	mov	dph,r6
   0589 E0            [24] 1516 	movx	a,@dptr
   058A FF            [12] 1517 	mov	r7,a
   058B 53 07 01      [24] 1518 	anl	ar7,#0x01
   058E 90 E7 40      [24] 1519 	mov	dptr,#_EP0BUF
   0591 EF            [12] 1520 	mov	a,r7
   0592 F0            [24] 1521 	movx	@dptr,a
                           1522 ;	convert_serial.c:342: EP0BUF[1] = 0;
   0593 90 E7 41      [24] 1523 	mov	dptr,#(_EP0BUF + 0x0001)
                           1524 ;	convert_serial.c:343: EP0BCH = 0;
   0596 E4            [12] 1525 	clr	a
   0597 F0            [24] 1526 	movx	@dptr,a
   0598 90 E6 8A      [24] 1527 	mov	dptr,#_EP0BCH
   059B F0            [24] 1528 	movx	@dptr,a
                           1529 ;	convert_serial.c:344: EP0BCL = 2;
   059C 90 E6 8B      [24] 1530 	mov	dptr,#_EP0BCL
   059F 74 02         [12] 1531 	mov	a,#0x02
   05A1 F0            [24] 1532 	movx	@dptr,a
                           1533 ;	convert_serial.c:345: break;
   05A2 02 07 13      [24] 1534 	ljmp	00161$
                           1535 ;	convert_serial.c:346: default:            // Invalid Command
   05A5                    1536 00134$:
                           1537 ;	convert_serial.c:347: EZUSB_STALL_EP0();
   05A5 90 E6 A0      [24] 1538 	mov	dptr,#_EP0CS
   05A8 E0            [24] 1539 	movx	a,@dptr
   05A9 FF            [12] 1540 	mov	r7,a
   05AA 44 01         [12] 1541 	orl	a,#0x01
   05AC F0            [24] 1542 	movx	@dptr,a
                           1543 ;	convert_serial.c:349: break;
   05AD 02 07 13      [24] 1544 	ljmp	00161$
                           1545 ;	convert_serial.c:350: case SC_CLEAR_FEATURE:
   05B0                    1546 00136$:
                           1547 ;	convert_serial.c:351: switch(SETUPDAT[0])
   05B0 90 E6 B8      [24] 1548 	mov	dptr,#_SETUPDAT
   05B3 E0            [24] 1549 	movx	a,@dptr
   05B4 FF            [12] 1550 	mov	r7,a
   05B5 60 08         [24] 1551 	jz	00137$
   05B7 BF 02 02      [24] 1552 	cjne	r7,#0x02,00267$
   05BA 80 1B         [24] 1553 	sjmp	00141$
   05BC                    1554 00267$:
   05BC 02 07 13      [24] 1555 	ljmp	00161$
                           1556 ;	convert_serial.c:353: case FT_DEVICE:
   05BF                    1557 00137$:
                           1558 ;	convert_serial.c:354: if(SETUPDAT[2] == 1)
   05BF 90 E6 BA      [24] 1559 	mov	dptr,#(_SETUPDAT + 0x0002)
   05C2 E0            [24] 1560 	movx	a,@dptr
   05C3 FF            [12] 1561 	mov	r7,a
   05C4 BF 01 05      [24] 1562 	cjne	r7,#0x01,00139$
                           1563 ;	convert_serial.c:355: Rwuen = FALSE;       // Disable Remote Wakeup
   05C7 C2 01         [12] 1564 	clr	_Rwuen
   05C9 02 07 13      [24] 1565 	ljmp	00161$
   05CC                    1566 00139$:
                           1567 ;	convert_serial.c:357: EZUSB_STALL_EP0();
   05CC 90 E6 A0      [24] 1568 	mov	dptr,#_EP0CS
   05CF E0            [24] 1569 	movx	a,@dptr
   05D0 FF            [12] 1570 	mov	r7,a
   05D1 44 01         [12] 1571 	orl	a,#0x01
   05D3 F0            [24] 1572 	movx	@dptr,a
                           1573 ;	convert_serial.c:358: break;
   05D4 02 07 13      [24] 1574 	ljmp	00161$
                           1575 ;	convert_serial.c:359: case FT_ENDPOINT:
   05D7                    1576 00141$:
                           1577 ;	convert_serial.c:360: if(SETUPDAT[2] == 0)
   05D7 90 E6 BA      [24] 1578 	mov	dptr,#(_SETUPDAT + 0x0002)
   05DA E0            [24] 1579 	movx	a,@dptr
   05DB 60 03         [24] 1580 	jz	00270$
   05DD 02 06 5C      [24] 1581 	ljmp	00143$
   05E0                    1582 00270$:
                           1583 ;	convert_serial.c:362: *(BYTE xdata *) epcs(SETUPDAT[4]) &= ~bmEPSTALL;
   05E0 90 E6 BC      [24] 1584 	mov	dptr,#(_SETUPDAT + 0x0004)
   05E3 E0            [24] 1585 	movx	a,@dptr
   05E4 FF            [12] 1586 	mov	r7,a
   05E5 53 07 7E      [24] 1587 	anl	ar7,#0x7E
   05E8 90 E6 BC      [24] 1588 	mov	dptr,#(_SETUPDAT + 0x0004)
   05EB E0            [24] 1589 	movx	a,@dptr
   05EC FE            [12] 1590 	mov	r6,a
   05ED C3            [12] 1591 	clr	c
   05EE 74 80         [12] 1592 	mov	a,#0x80
   05F0 9E            [12] 1593 	subb	a,r6
   05F1 E4            [12] 1594 	clr	a
   05F2 33            [12] 1595 	rlc	a
   05F3 4F            [12] 1596 	orl	a,r7
   05F4 90 09 09      [24] 1597 	mov	dptr,#_EPCS_Offset_Lookup_Table
   05F7 93            [24] 1598 	movc	a,@a+dptr
   05F8 FF            [12] 1599 	mov	r7,a
   05F9 33            [12] 1600 	rlc	a
   05FA 95 E0         [12] 1601 	subb	a,acc
   05FC FE            [12] 1602 	mov	r6,a
   05FD 74 A1         [12] 1603 	mov	a,#0xA1
   05FF 2F            [12] 1604 	add	a,r7
   0600 FF            [12] 1605 	mov	r7,a
   0601 74 E6         [12] 1606 	mov	a,#0xE6
   0603 3E            [12] 1607 	addc	a,r6
   0604 FE            [12] 1608 	mov	r6,a
   0605 90 E6 BC      [24] 1609 	mov	dptr,#(_SETUPDAT + 0x0004)
   0608 E0            [24] 1610 	movx	a,@dptr
   0609 FD            [12] 1611 	mov	r5,a
   060A 53 05 7E      [24] 1612 	anl	ar5,#0x7E
   060D 90 E6 BC      [24] 1613 	mov	dptr,#(_SETUPDAT + 0x0004)
   0610 E0            [24] 1614 	movx	a,@dptr
   0611 FC            [12] 1615 	mov	r4,a
   0612 C3            [12] 1616 	clr	c
   0613 74 80         [12] 1617 	mov	a,#0x80
   0615 9C            [12] 1618 	subb	a,r4
   0616 E4            [12] 1619 	clr	a
   0617 33            [12] 1620 	rlc	a
   0618 4D            [12] 1621 	orl	a,r5
   0619 90 09 09      [24] 1622 	mov	dptr,#_EPCS_Offset_Lookup_Table
   061C 93            [24] 1623 	movc	a,@a+dptr
   061D FD            [12] 1624 	mov	r5,a
   061E 33            [12] 1625 	rlc	a
   061F 95 E0         [12] 1626 	subb	a,acc
   0621 FC            [12] 1627 	mov	r4,a
   0622 74 A1         [12] 1628 	mov	a,#0xA1
   0624 2D            [12] 1629 	add	a,r5
   0625 FD            [12] 1630 	mov	r5,a
   0626 74 E6         [12] 1631 	mov	a,#0xE6
   0628 3C            [12] 1632 	addc	a,r4
   0629 FC            [12] 1633 	mov	r4,a
   062A 8D 82         [24] 1634 	mov	dpl,r5
   062C 8C 83         [24] 1635 	mov	dph,r4
   062E E0            [24] 1636 	movx	a,@dptr
   062F FD            [12] 1637 	mov	r5,a
   0630 53 05 FE      [24] 1638 	anl	ar5,#0xFE
   0633 8F 82         [24] 1639 	mov	dpl,r7
   0635 8E 83         [24] 1640 	mov	dph,r6
   0637 ED            [12] 1641 	mov	a,r5
   0638 F0            [24] 1642 	movx	@dptr,a
                           1643 ;	convert_serial.c:363: EZUSB_RESET_DATA_TOGGLE( SETUPDAT[4] );
   0639 90 E6 BC      [24] 1644 	mov	dptr,#(_SETUPDAT + 0x0004)
   063C E0            [24] 1645 	movx	a,@dptr
   063D 54 80         [12] 1646 	anl	a,#0x80
   063F C4            [12] 1647 	swap	a
   0640 23            [12] 1648 	rl	a
   0641 54 1F         [12] 1649 	anl	a,#0x1F
   0643 FF            [12] 1650 	mov	r7,a
   0644 90 E6 BC      [24] 1651 	mov	dptr,#(_SETUPDAT + 0x0004)
   0647 E0            [24] 1652 	movx	a,@dptr
   0648 FE            [12] 1653 	mov	r6,a
   0649 74 0F         [12] 1654 	mov	a,#0x0F
   064B 5E            [12] 1655 	anl	a,r6
   064C 90 E6 83      [24] 1656 	mov	dptr,#_TOGCTL
   064F 2F            [12] 1657 	add	a,r7
   0650 F0            [24] 1658 	movx	@dptr,a
   0651 90 E6 83      [24] 1659 	mov	dptr,#_TOGCTL
   0654 E0            [24] 1660 	movx	a,@dptr
   0655 FF            [12] 1661 	mov	r7,a
   0656 44 20         [12] 1662 	orl	a,#0x20
   0658 F0            [24] 1663 	movx	@dptr,a
   0659 02 07 13      [24] 1664 	ljmp	00161$
   065C                    1665 00143$:
                           1666 ;	convert_serial.c:366: EZUSB_STALL_EP0();
   065C 90 E6 A0      [24] 1667 	mov	dptr,#_EP0CS
   065F E0            [24] 1668 	movx	a,@dptr
   0660 FF            [12] 1669 	mov	r7,a
   0661 44 01         [12] 1670 	orl	a,#0x01
   0663 F0            [24] 1671 	movx	@dptr,a
                           1672 ;	convert_serial.c:369: break;
   0664 02 07 13      [24] 1673 	ljmp	00161$
                           1674 ;	convert_serial.c:370: case SC_SET_FEATURE:
   0667                    1675 00146$:
                           1676 ;	convert_serial.c:371: switch(SETUPDAT[0])
   0667 90 E6 B8      [24] 1677 	mov	dptr,#_SETUPDAT
   066A E0            [24] 1678 	movx	a,@dptr
   066B FF            [12] 1679 	mov	r7,a
   066C 60 08         [24] 1680 	jz	00147$
   066E BF 02 02      [24] 1681 	cjne	r7,#0x02,00272$
   0671 80 29         [24] 1682 	sjmp	00155$
   0673                    1683 00272$:
   0673 02 06 F7      [24] 1684 	ljmp	00156$
                           1685 ;	convert_serial.c:373: case FT_DEVICE:
   0676                    1686 00147$:
                           1687 ;	convert_serial.c:374: if((SETUPDAT[2] == 1) && Rwuen_allowed)
   0676 90 E6 BA      [24] 1688 	mov	dptr,#(_SETUPDAT + 0x0002)
   0679 E0            [24] 1689 	movx	a,@dptr
   067A FF            [12] 1690 	mov	r7,a
   067B BF 01 08      [24] 1691 	cjne	r7,#0x01,00152$
   067E 30 00 05      [24] 1692 	jnb	_Rwuen_allowed,00152$
                           1693 ;	convert_serial.c:375: Rwuen = TRUE;      // Enable Remote Wakeup
   0681 D2 01         [12] 1694 	setb	_Rwuen
   0683 02 07 13      [24] 1695 	ljmp	00161$
   0686                    1696 00152$:
                           1697 ;	convert_serial.c:376: else if(SETUPDAT[2] == 2)
   0686 90 E6 BA      [24] 1698 	mov	dptr,#(_SETUPDAT + 0x0002)
   0689 E0            [24] 1699 	movx	a,@dptr
   068A FF            [12] 1700 	mov	r7,a
   068B BF 02 03      [24] 1701 	cjne	r7,#0x02,00276$
   068E 02 07 13      [24] 1702 	ljmp	00161$
   0691                    1703 00276$:
                           1704 ;	convert_serial.c:386: EZUSB_STALL_EP0();
   0691 90 E6 A0      [24] 1705 	mov	dptr,#_EP0CS
   0694 E0            [24] 1706 	movx	a,@dptr
   0695 FF            [12] 1707 	mov	r7,a
   0696 44 01         [12] 1708 	orl	a,#0x01
   0698 F0            [24] 1709 	movx	@dptr,a
                           1710 ;	convert_serial.c:387: break;
   0699 02 07 13      [24] 1711 	ljmp	00161$
                           1712 ;	convert_serial.c:388: case FT_ENDPOINT:
   069C                    1713 00155$:
                           1714 ;	convert_serial.c:389: *(BYTE xdata *) epcs(SETUPDAT[4]) |= bmEPSTALL;
   069C 90 E6 BC      [24] 1715 	mov	dptr,#(_SETUPDAT + 0x0004)
   069F E0            [24] 1716 	movx	a,@dptr
   06A0 FF            [12] 1717 	mov	r7,a
   06A1 53 07 7E      [24] 1718 	anl	ar7,#0x7E
   06A4 90 E6 BC      [24] 1719 	mov	dptr,#(_SETUPDAT + 0x0004)
   06A7 E0            [24] 1720 	movx	a,@dptr
   06A8 FE            [12] 1721 	mov	r6,a
   06A9 C3            [12] 1722 	clr	c
   06AA 74 80         [12] 1723 	mov	a,#0x80
   06AC 9E            [12] 1724 	subb	a,r6
   06AD E4            [12] 1725 	clr	a
   06AE 33            [12] 1726 	rlc	a
   06AF 4F            [12] 1727 	orl	a,r7
   06B0 90 09 09      [24] 1728 	mov	dptr,#_EPCS_Offset_Lookup_Table
   06B3 93            [24] 1729 	movc	a,@a+dptr
   06B4 FF            [12] 1730 	mov	r7,a
   06B5 33            [12] 1731 	rlc	a
   06B6 95 E0         [12] 1732 	subb	a,acc
   06B8 FE            [12] 1733 	mov	r6,a
   06B9 74 A1         [12] 1734 	mov	a,#0xA1
   06BB 2F            [12] 1735 	add	a,r7
   06BC FF            [12] 1736 	mov	r7,a
   06BD 74 E6         [12] 1737 	mov	a,#0xE6
   06BF 3E            [12] 1738 	addc	a,r6
   06C0 FE            [12] 1739 	mov	r6,a
   06C1 90 E6 BC      [24] 1740 	mov	dptr,#(_SETUPDAT + 0x0004)
   06C4 E0            [24] 1741 	movx	a,@dptr
   06C5 FD            [12] 1742 	mov	r5,a
   06C6 53 05 7E      [24] 1743 	anl	ar5,#0x7E
   06C9 90 E6 BC      [24] 1744 	mov	dptr,#(_SETUPDAT + 0x0004)
   06CC E0            [24] 1745 	movx	a,@dptr
   06CD FC            [12] 1746 	mov	r4,a
   06CE C3            [12] 1747 	clr	c
   06CF 74 80         [12] 1748 	mov	a,#0x80
   06D1 9C            [12] 1749 	subb	a,r4
   06D2 E4            [12] 1750 	clr	a
   06D3 33            [12] 1751 	rlc	a
   06D4 4D            [12] 1752 	orl	a,r5
   06D5 90 09 09      [24] 1753 	mov	dptr,#_EPCS_Offset_Lookup_Table
   06D8 93            [24] 1754 	movc	a,@a+dptr
   06D9 FD            [12] 1755 	mov	r5,a
   06DA 33            [12] 1756 	rlc	a
   06DB 95 E0         [12] 1757 	subb	a,acc
   06DD FC            [12] 1758 	mov	r4,a
   06DE 74 A1         [12] 1759 	mov	a,#0xA1
   06E0 2D            [12] 1760 	add	a,r5
   06E1 FD            [12] 1761 	mov	r5,a
   06E2 74 E6         [12] 1762 	mov	a,#0xE6
   06E4 3C            [12] 1763 	addc	a,r4
   06E5 FC            [12] 1764 	mov	r4,a
   06E6 8D 82         [24] 1765 	mov	dpl,r5
   06E8 8C 83         [24] 1766 	mov	dph,r4
   06EA E0            [24] 1767 	movx	a,@dptr
   06EB FD            [12] 1768 	mov	r5,a
   06EC 43 05 01      [24] 1769 	orl	ar5,#0x01
   06EF 8F 82         [24] 1770 	mov	dpl,r7
   06F1 8E 83         [24] 1771 	mov	dph,r6
   06F3 ED            [12] 1772 	mov	a,r5
   06F4 F0            [24] 1773 	movx	@dptr,a
                           1774 ;	convert_serial.c:390: break;
                           1775 ;	convert_serial.c:391: default:
   06F5 80 1C         [24] 1776 	sjmp	00161$
   06F7                    1777 00156$:
                           1778 ;	convert_serial.c:392: EZUSB_STALL_EP0();
   06F7 90 E6 A0      [24] 1779 	mov	dptr,#_EP0CS
   06FA E0            [24] 1780 	movx	a,@dptr
   06FB FF            [12] 1781 	mov	r7,a
   06FC 44 01         [12] 1782 	orl	a,#0x01
   06FE F0            [24] 1783 	movx	@dptr,a
                           1784 ;	convert_serial.c:394: break;
                           1785 ;	convert_serial.c:395: default:                     // *** Invalid Command
   06FF 80 12         [24] 1786 	sjmp	00161$
   0701                    1787 00158$:
                           1788 ;	convert_serial.c:396: EZUSB_STALL_EP0();
   0701 90 E6 A0      [24] 1789 	mov	dptr,#_EP0CS
   0704 E0            [24] 1790 	movx	a,@dptr
   0705 FF            [12] 1791 	mov	r7,a
   0706 44 01         [12] 1792 	orl	a,#0x01
   0708 F0            [24] 1793 	movx	@dptr,a
                           1794 ;	convert_serial.c:399: break;
                           1795 ;	convert_serial.c:401: default:
   0709 80 08         [24] 1796 	sjmp	00161$
   070B                    1797 00160$:
                           1798 ;	convert_serial.c:402: EZUSB_STALL_EP0();
   070B 90 E6 A0      [24] 1799 	mov	dptr,#_EP0CS
   070E E0            [24] 1800 	movx	a,@dptr
   070F FF            [12] 1801 	mov	r7,a
   0710 44 01         [12] 1802 	orl	a,#0x01
   0712 F0            [24] 1803 	movx	@dptr,a
                           1804 ;	convert_serial.c:404: }
   0713                    1805 00161$:
                           1806 ;	convert_serial.c:407: EP0CS |= bmHSNAK;
   0713 90 E6 A0      [24] 1807 	mov	dptr,#_EP0CS
   0716 E0            [24] 1808 	movx	a,@dptr
   0717 44 80         [12] 1809 	orl	a,#0x80
   0719 F0            [24] 1810 	movx	@dptr,a
   071A 22            [24] 1811 	ret
                           1812 ;------------------------------------------------------------
                           1813 ;Allocation info for local variables in function 'USB_isr'
                           1814 ;------------------------------------------------------------
                           1815 ;	convert_serial.c:410: static void USB_isr(void) __interrupt 8
                           1816 ;	-----------------------------------------
                           1817 ;	 function USB_isr
                           1818 ;	-----------------------------------------
   071B                    1819 _USB_isr:
   071B C0 21         [24] 1820 	push	bits
   071D C0 E0         [24] 1821 	push	acc
   071F C0 F0         [24] 1822 	push	b
   0721 C0 82         [24] 1823 	push	dpl
   0723 C0 83         [24] 1824 	push	dph
   0725 C0 07         [24] 1825 	push	(0+7)
   0727 C0 06         [24] 1826 	push	(0+6)
   0729 C0 05         [24] 1827 	push	(0+5)
   072B C0 04         [24] 1828 	push	(0+4)
   072D C0 03         [24] 1829 	push	(0+3)
   072F C0 02         [24] 1830 	push	(0+2)
   0731 C0 01         [24] 1831 	push	(0+1)
   0733 C0 00         [24] 1832 	push	(0+0)
   0735 C0 D0         [24] 1833 	push	psw
   0737 75 D0 00      [24] 1834 	mov	psw,#0x00
                           1835 ;	convert_serial.c:413: EXIF &= ~0x10;
   073A AF 91         [24] 1836 	mov	r7,_EXIF
   073C 74 EF         [12] 1837 	mov	a,#0xEF
   073E 5F            [12] 1838 	anl	a,r7
   073F F5 91         [12] 1839 	mov	_EXIF,a
                           1840 ;	convert_serial.c:416: USBIRQ = 0x01;
   0741 90 E6 5D      [24] 1841 	mov	dptr,#_USBIRQ
   0744 74 01         [12] 1842 	mov	a,#0x01
   0746 F0            [24] 1843 	movx	@dptr,a
                           1844 ;	convert_serial.c:418: SetupCommand();
   0747 12 02 84      [24] 1845 	lcall	_SetupCommand
   074A D0 D0         [24] 1846 	pop	psw
   074C D0 00         [24] 1847 	pop	(0+0)
   074E D0 01         [24] 1848 	pop	(0+1)
   0750 D0 02         [24] 1849 	pop	(0+2)
   0752 D0 03         [24] 1850 	pop	(0+3)
   0754 D0 04         [24] 1851 	pop	(0+4)
   0756 D0 05         [24] 1852 	pop	(0+5)
   0758 D0 06         [24] 1853 	pop	(0+6)
   075A D0 07         [24] 1854 	pop	(0+7)
   075C D0 83         [24] 1855 	pop	dph
   075E D0 82         [24] 1856 	pop	dpl
   0760 D0 F0         [24] 1857 	pop	b
   0762 D0 E0         [24] 1858 	pop	acc
   0764 D0 21         [24] 1859 	pop	bits
   0766 32            [24] 1860 	reti
                           1861 ;------------------------------------------------------------
                           1862 ;Allocation info for local variables in function 'Initialize'
                           1863 ;------------------------------------------------------------
                           1864 ;	convert_serial.c:425: static void Initialize(void)
                           1865 ;	-----------------------------------------
                           1866 ;	 function Initialize
                           1867 ;	-----------------------------------------
   0767                    1868 _Initialize:
                           1869 ;	convert_serial.c:433: IFCONFIG=0xc0;  // Internal IFCLK, 48MHz; A,B as normal ports. 
   0767 90 E6 01      [24] 1870 	mov	dptr,#_IFCONFIG
   076A 74 C0         [12] 1871 	mov	a,#0xC0
   076C F0            [24] 1872 	movx	@dptr,a
                           1873 ;	convert_serial.c:434: SYNCDELAY;
   076D 00            [12] 1874 	nop 
                           1875 ;	convert_serial.c:436: REVCTL=0x03;  // See TRM...
   076E 90 E6 0B      [24] 1876 	mov	dptr,#_REVCTL
   0771 74 03         [12] 1877 	mov	a,#0x03
   0773 F0            [24] 1878 	movx	@dptr,a
                           1879 ;	convert_serial.c:437: SYNCDELAY;
   0774 00            [12] 1880 	nop 
                           1881 ;	convert_serial.c:442: EP1OUTCFG=0xa0;
   0775 90 E6 10      [24] 1882 	mov	dptr,#_EP1OUTCFG
   0778 74 A0         [12] 1883 	mov	a,#0xA0
   077A F0            [24] 1884 	movx	@dptr,a
                           1885 ;	convert_serial.c:443: EP1INCFG=0xa0;
   077B 90 E6 11      [24] 1886 	mov	dptr,#_EP1INCFG
   077E 74 A0         [12] 1887 	mov	a,#0xA0
   0780 F0            [24] 1888 	movx	@dptr,a
                           1889 ;	convert_serial.c:444: EP2CFG=0;
   0781 90 E6 12      [24] 1890 	mov	dptr,#_EP2CFG
                           1891 ;	convert_serial.c:445: EP4CFG=0;
                           1892 ;	convert_serial.c:446: EP6CFG=0;
                           1893 ;	convert_serial.c:447: EP8CFG=0;
   0784 E4            [12] 1894 	clr	a
   0785 F0            [24] 1895 	movx	@dptr,a
   0786 90 E6 13      [24] 1896 	mov	dptr,#_EP4CFG
   0789 F0            [24] 1897 	movx	@dptr,a
   078A 90 E6 14      [24] 1898 	mov	dptr,#_EP6CFG
   078D F0            [24] 1899 	movx	@dptr,a
   078E 90 E6 15      [24] 1900 	mov	dptr,#_EP8CFG
   0791 F0            [24] 1901 	movx	@dptr,a
                           1902 ;	convert_serial.c:449: SYNCDELAY;
   0792 00            [12] 1903 	nop 
                           1904 ;	convert_serial.c:450: EP1OUTBC=0xff; // Arm endpoint 1 for OUT (host->device) transfers
   0793 90 E6 8D      [24] 1905 	mov	dptr,#_EP1OUTBC
   0796 74 FF         [12] 1906 	mov	a,#0xFF
   0798 F0            [24] 1907 	movx	@dptr,a
                           1908 ;	convert_serial.c:459: SUDPTRCTL = 1;
   0799 90 E6 B5      [24] 1909 	mov	dptr,#_SUDPTRCTL
   079C 74 01         [12] 1910 	mov	a,#0x01
   079E F0            [24] 1911 	movx	@dptr,a
                           1912 ;	convert_serial.c:462: IE = 0x80;
   079F 75 A8 80      [24] 1913 	mov	_IE,#0x80
                           1914 ;	convert_serial.c:463: EIE = 0x01;
   07A2 75 E8 01      [24] 1915 	mov	_EIE,#0x01
                           1916 ;	convert_serial.c:466: USBIE = 0x01;
   07A5 90 E6 5C      [24] 1917 	mov	dptr,#_USBIE
   07A8 74 01         [12] 1918 	mov	a,#0x01
   07AA F0            [24] 1919 	movx	@dptr,a
   07AB 22            [24] 1920 	ret
                           1921 ;------------------------------------------------------------
                           1922 ;Allocation info for local variables in function 'ProcessXmitData'
                           1923 ;------------------------------------------------------------
                           1924 ;	convert_serial.c:500: static void ProcessXmitData(void)
                           1925 ;	-----------------------------------------
                           1926 ;	 function ProcessXmitData
                           1927 ;	-----------------------------------------
   07AC                    1928 _ProcessXmitData:
                           1929 ;	convert_serial.c:503: TCON &= ~0x30;
   07AC AF 88         [24] 1930 	mov	r7,_TCON
   07AE 74 CF         [12] 1931 	mov	a,#0xCF
   07B0 5F            [12] 1932 	anl	a,r7
   07B1 F5 88         [12] 1933 	mov	_TCON,a
                           1934 ;	convert_serial.c:507: EP1INBUF[0] = FTDI_RS0_CTS | FTDI_RS0_DSR | 1;
   07B3 90 E7 C0      [24] 1935 	mov	dptr,#_EP1INBUF
   07B6 74 31         [12] 1936 	mov	a,#0x31
   07B8 F0            [24] 1937 	movx	@dptr,a
                           1938 ;	convert_serial.c:508: EP1INBUF[1] = FTDI_RS_DR;
   07B9 90 E7 C1      [24] 1939 	mov	dptr,#(_EP1INBUF + 0x0001)
   07BC 74 01         [12] 1940 	mov	a,#0x01
   07BE F0            [24] 1941 	movx	@dptr,a
                           1942 ;	convert_serial.c:511: SYNCDELAY;
   07BF 00            [12] 1943 	nop 
                           1944 ;	convert_serial.c:512: EP1INBC = bytes_waiting_for_xmit + 2;
   07C0 AF 15         [24] 1945 	mov	r7,_bytes_waiting_for_xmit
   07C2 90 E6 8F      [24] 1946 	mov	dptr,#_EP1INBC
   07C5 74 02         [12] 1947 	mov	a,#0x02
   07C7 2F            [12] 1948 	add	a,r7
   07C8 F0            [24] 1949 	movx	@dptr,a
                           1950 ;	convert_serial.c:514: bytes_waiting_for_xmit = 0;
   07C9 E4            [12] 1951 	clr	a
   07CA F5 15         [12] 1952 	mov	_bytes_waiting_for_xmit,a
   07CC F5 16         [12] 1953 	mov	(_bytes_waiting_for_xmit + 1),a
   07CE 22            [24] 1954 	ret
                           1955 ;------------------------------------------------------------
                           1956 ;Allocation info for local variables in function 'putchar'
                           1957 ;------------------------------------------------------------
                           1958 ;c                         Allocated to registers r7 
                           1959 ;dest                      Allocated to registers r5 r6 
                           1960 ;------------------------------------------------------------
                           1961 ;	convert_serial.c:518: static void putchar(char c)
                           1962 ;	-----------------------------------------
                           1963 ;	 function putchar
                           1964 ;	-----------------------------------------
   07CF                    1965 _putchar:
   07CF AF 82         [24] 1966 	mov	r7,dpl
                           1967 ;	convert_serial.c:520: xdata unsigned char *dest=EP1INBUF + bytes_waiting_for_xmit + 2;
   07D1 E5 15         [12] 1968 	mov	a,_bytes_waiting_for_xmit
   07D3 24 C0         [12] 1969 	add	a,#_EP1INBUF
   07D5 FD            [12] 1970 	mov	r5,a
   07D6 E5 16         [12] 1971 	mov	a,(_bytes_waiting_for_xmit + 1)
   07D8 34 E7         [12] 1972 	addc	a,#(_EP1INBUF >> 8)
   07DA FE            [12] 1973 	mov	r6,a
   07DB 74 02         [12] 1974 	mov	a,#0x02
   07DD 2D            [12] 1975 	add	a,r5
   07DE FD            [12] 1976 	mov	r5,a
   07DF E4            [12] 1977 	clr	a
   07E0 3E            [12] 1978 	addc	a,r6
   07E1 FE            [12] 1979 	mov	r6,a
                           1980 ;	convert_serial.c:523: while (EP1INCS & 0x02);
   07E2                    1981 00101$:
   07E2 90 E6 A2      [24] 1982 	mov	dptr,#_EP1INCS
   07E5 E0            [24] 1983 	movx	a,@dptr
   07E6 FC            [12] 1984 	mov	r4,a
   07E7 20 E1 F8      [24] 1985 	jb	acc.1,00101$
                           1986 ;	convert_serial.c:525: *dest = c;
   07EA 8D 82         [24] 1987 	mov	dpl,r5
   07EC 8E 83         [24] 1988 	mov	dph,r6
   07EE EF            [12] 1989 	mov	a,r7
   07EF F0            [24] 1990 	movx	@dptr,a
                           1991 ;	convert_serial.c:527: if (++bytes_waiting_for_xmit >= 62) ProcessXmitData();
   07F0 05 15         [12] 1992 	inc	_bytes_waiting_for_xmit
   07F2 E4            [12] 1993 	clr	a
   07F3 B5 15 02      [24] 1994 	cjne	a,_bytes_waiting_for_xmit,00127$
   07F6 05 16         [12] 1995 	inc	(_bytes_waiting_for_xmit + 1)
   07F8                    1996 00127$:
   07F8 C3            [12] 1997 	clr	c
   07F9 E5 15         [12] 1998 	mov	a,_bytes_waiting_for_xmit
   07FB 94 3E         [12] 1999 	subb	a,#0x3E
   07FD E5 16         [12] 2000 	mov	a,(_bytes_waiting_for_xmit + 1)
   07FF 94 00         [12] 2001 	subb	a,#0x00
   0801 40 03         [24] 2002 	jc	00105$
   0803 12 07 AC      [24] 2003 	lcall	_ProcessXmitData
   0806                    2004 00105$:
                           2005 ;	convert_serial.c:530: if (bytes_waiting_for_xmit && !(TCON & 0x10)) {
   0806 E5 15         [12] 2006 	mov	a,_bytes_waiting_for_xmit
   0808 45 16         [12] 2007 	orl	a,(_bytes_waiting_for_xmit + 1)
   080A 60 19         [24] 2008 	jz	00109$
   080C E5 88         [12] 2009 	mov	a,_TCON
   080E 20 E4 14      [24] 2010 	jb	acc.4,00109$
                           2011 ;	convert_serial.c:531: TH0 = MSB(0xffff - latency_us);
   0811 74 FF         [12] 2012 	mov	a,#0xFF
   0813 C3            [12] 2013 	clr	c
   0814 95 17         [12] 2014 	subb	a,_latency_us
   0816 FE            [12] 2015 	mov	r6,a
   0817 74 FF         [12] 2016 	mov	a,#0xFF
   0819 95 18         [12] 2017 	subb	a,(_latency_us + 1)
   081B FD            [12] 2018 	mov	r5,a
   081C 8D 8C         [24] 2019 	mov	_TH0,r5
                           2020 ;	convert_serial.c:532: TL0 = LSB(0xffff - latency_us);
   081E 7F 00         [12] 2021 	mov	r7,#0x00
   0820 8E 8A         [24] 2022 	mov	_TL0,r6
                           2023 ;	convert_serial.c:533: TCON |= 0x10;
   0822 43 88 10      [24] 2024 	orl	_TCON,#0x10
   0825                    2025 00109$:
   0825 22            [24] 2026 	ret
                           2027 ;------------------------------------------------------------
                           2028 ;Allocation info for local variables in function 'ProcessRecvData'
                           2029 ;------------------------------------------------------------
                           2030 ;src                       Allocated to registers 
                           2031 ;len                       Allocated to registers r6 r7 
                           2032 ;i                         Allocated to registers r2 r3 
                           2033 ;------------------------------------------------------------
                           2034 ;	convert_serial.c:537: static void ProcessRecvData(void)
                           2035 ;	-----------------------------------------
                           2036 ;	 function ProcessRecvData
                           2037 ;	-----------------------------------------
   0826                    2038 _ProcessRecvData:
                           2039 ;	convert_serial.c:539: xdata const unsigned char *src=EP1OUTBUF;
                           2040 ;	convert_serial.c:540: unsigned int len = EP1OUTBC;
   0826 90 E6 8D      [24] 2041 	mov	dptr,#_EP1OUTBC
   0829 E0            [24] 2042 	movx	a,@dptr
   082A FE            [12] 2043 	mov	r6,a
   082B 7F 00         [12] 2044 	mov	r7,#0x00
                           2045 ;	convert_serial.c:545: src++; len--;
   082D 74 01         [12] 2046 	mov	a,#0x01
   082F 24 80         [12] 2047 	add	a,#_EP1OUTBUF
   0831 FC            [12] 2048 	mov	r4,a
   0832 E4            [12] 2049 	clr	a
   0833 34 E7         [12] 2050 	addc	a,#(_EP1OUTBUF >> 8)
   0835 FD            [12] 2051 	mov	r5,a
   0836 1E            [12] 2052 	dec	r6
   0837 BE FF 01      [24] 2053 	cjne	r6,#0xFF,00124$
   083A 1F            [12] 2054 	dec	r7
   083B                    2055 00124$:
                           2056 ;	convert_serial.c:547: for(i=0; i<len; i++,src++)
   083B 7A 00         [12] 2057 	mov	r2,#0x00
   083D 7B 00         [12] 2058 	mov	r3,#0x00
   083F                    2059 00107$:
   083F C3            [12] 2060 	clr	c
   0840 EA            [12] 2061 	mov	a,r2
   0841 9E            [12] 2062 	subb	a,r6
   0842 EB            [12] 2063 	mov	a,r3
   0843 9F            [12] 2064 	subb	a,r7
   0844 50 60         [24] 2065 	jnc	00105$
                           2066 ;	convert_serial.c:549: if(*src>='a' && *src<='z')
   0846 8C 82         [24] 2067 	mov	dpl,r4
   0848 8D 83         [24] 2068 	mov	dph,r5
   084A E0            [24] 2069 	movx	a,@dptr
   084B F9            [12] 2070 	mov	r1,a
   084C B9 61 00      [24] 2071 	cjne	r1,#0x61,00126$
   084F                    2072 00126$:
   084F 40 27         [24] 2073 	jc	00102$
   0851 E9            [12] 2074 	mov	a,r1
   0852 24 85         [12] 2075 	add	a,#0xff - 0x7A
   0854 40 22         [24] 2076 	jc	00102$
                           2077 ;	convert_serial.c:550: {  putchar(*src-'a'+'A');  }
   0856 74 E0         [12] 2078 	mov	a,#0xE0
   0858 29            [12] 2079 	add	a,r1
   0859 F5 82         [12] 2080 	mov	dpl,a
   085B C0 07         [24] 2081 	push	ar7
   085D C0 06         [24] 2082 	push	ar6
   085F C0 05         [24] 2083 	push	ar5
   0861 C0 04         [24] 2084 	push	ar4
   0863 C0 03         [24] 2085 	push	ar3
   0865 C0 02         [24] 2086 	push	ar2
   0867 12 07 CF      [24] 2087 	lcall	_putchar
   086A D0 02         [24] 2088 	pop	ar2
   086C D0 03         [24] 2089 	pop	ar3
   086E D0 04         [24] 2090 	pop	ar4
   0870 D0 05         [24] 2091 	pop	ar5
   0872 D0 06         [24] 2092 	pop	ar6
   0874 D0 07         [24] 2093 	pop	ar7
   0876 80 22         [24] 2094 	sjmp	00108$
   0878                    2095 00102$:
                           2096 ;	convert_serial.c:552: {  putchar(*src);  }
   0878 8C 82         [24] 2097 	mov	dpl,r4
   087A 8D 83         [24] 2098 	mov	dph,r5
   087C E0            [24] 2099 	movx	a,@dptr
   087D F5 82         [12] 2100 	mov	dpl,a
   087F C0 07         [24] 2101 	push	ar7
   0881 C0 06         [24] 2102 	push	ar6
   0883 C0 05         [24] 2103 	push	ar5
   0885 C0 04         [24] 2104 	push	ar4
   0887 C0 03         [24] 2105 	push	ar3
   0889 C0 02         [24] 2106 	push	ar2
   088B 12 07 CF      [24] 2107 	lcall	_putchar
   088E D0 02         [24] 2108 	pop	ar2
   0890 D0 03         [24] 2109 	pop	ar3
   0892 D0 04         [24] 2110 	pop	ar4
   0894 D0 05         [24] 2111 	pop	ar5
   0896 D0 06         [24] 2112 	pop	ar6
   0898 D0 07         [24] 2113 	pop	ar7
   089A                    2114 00108$:
                           2115 ;	convert_serial.c:547: for(i=0; i<len; i++,src++)
   089A 0A            [12] 2116 	inc	r2
   089B BA 00 01      [24] 2117 	cjne	r2,#0x00,00129$
   089E 0B            [12] 2118 	inc	r3
   089F                    2119 00129$:
   089F 0C            [12] 2120 	inc	r4
   08A0 BC 00 9C      [24] 2121 	cjne	r4,#0x00,00107$
   08A3 0D            [12] 2122 	inc	r5
   08A4 80 99         [24] 2123 	sjmp	00107$
   08A6                    2124 00105$:
                           2125 ;	convert_serial.c:555: EP1OUTBC=0xff; // re-arm endpoint 1 for OUT (host->device) transfers
   08A6 90 E6 8D      [24] 2126 	mov	dptr,#_EP1OUTBC
   08A9 74 FF         [12] 2127 	mov	a,#0xFF
   08AB F0            [24] 2128 	movx	@dptr,a
                           2129 ;	convert_serial.c:556: SYNCDELAY;
   08AC 00            [12] 2130 	nop 
   08AD 22            [24] 2131 	ret
                           2132 ;------------------------------------------------------------
                           2133 ;Allocation info for local variables in function 'main'
                           2134 ;------------------------------------------------------------
                           2135 ;	convert_serial.c:560: void main(void)
                           2136 ;	-----------------------------------------
                           2137 ;	 function main
                           2138 ;	-----------------------------------------
   08AE                    2139 _main:
                           2140 ;	convert_serial.c:563: USBCS |= 0x08;
   08AE 90 E6 80      [24] 2141 	mov	dptr,#_USBCS
   08B1 E0            [24] 2142 	movx	a,@dptr
   08B2 44 08         [12] 2143 	orl	a,#0x08
   08B4 F0            [24] 2144 	movx	@dptr,a
                           2145 ;	convert_serial.c:564: Initialize();
   08B5 12 07 67      [24] 2146 	lcall	_Initialize
                           2147 ;	convert_serial.c:565: USBCS |= 0x02;
                           2148 ;	convert_serial.c:566: USBCS &= ~(0x08);
   08B8 90 E6 80      [24] 2149 	mov	dptr,#_USBCS
   08BB E0            [24] 2150 	movx	a,@dptr
   08BC 44 02         [12] 2151 	orl	a,#0x02
   08BE F0            [24] 2152 	movx	@dptr,a
   08BF E0            [24] 2153 	movx	a,@dptr
   08C0 54 F7         [12] 2154 	anl	a,#0xF7
   08C2 F0            [24] 2155 	movx	@dptr,a
                           2156 ;	convert_serial.c:570: CKCO &= ~(0x08);
   08C3 AF 8E         [24] 2157 	mov	r7,_CKCO
   08C5 74 F7         [12] 2158 	mov	a,#0xF7
   08C7 5F            [12] 2159 	anl	a,r7
   08C8 F5 8E         [12] 2160 	mov	_CKCO,a
                           2161 ;	convert_serial.c:571: TMOD = 0x01;
   08CA 75 89 01      [24] 2162 	mov	_TMOD,#0x01
                           2163 ;	convert_serial.c:572: TCON &= ~0x30;
   08CD AF 88         [24] 2164 	mov	r7,_TCON
   08CF 74 CF         [12] 2165 	mov	a,#0xCF
   08D1 5F            [12] 2166 	anl	a,r7
   08D2 F5 88         [12] 2167 	mov	_TCON,a
   08D4                    2168 00106$:
                           2169 ;	convert_serial.c:577: if(!(EP1OUTCS & bmEPBUSY))
   08D4 90 E6 A1      [24] 2170 	mov	dptr,#_EP1OUTCS
   08D7 E0            [24] 2171 	movx	a,@dptr
   08D8 FF            [12] 2172 	mov	r7,a
   08D9 20 E1 03      [24] 2173 	jb	acc.1,00102$
                           2174 ;	convert_serial.c:579: ProcessRecvData();
   08DC 12 08 26      [24] 2175 	lcall	_ProcessRecvData
   08DF                    2176 00102$:
                           2177 ;	convert_serial.c:583: if((TCON & 0x20))
   08DF E5 88         [12] 2178 	mov	a,_TCON
   08E1 30 E5 F0      [24] 2179 	jnb	acc.5,00106$
                           2180 ;	convert_serial.c:585: ProcessXmitData();
   08E4 12 07 AC      [24] 2181 	lcall	_ProcessXmitData
   08E7 80 EB         [24] 2182 	sjmp	00106$
                           2183 	.area CSEG    (CODE)
                           2184 	.area CONST   (CODE)
   0909                    2185 _EPCS_Offset_Lookup_Table:
   0909 00                 2186 	.db #0x00	;  0
   090A 01                 2187 	.db #0x01	;  1
   090B 02                 2188 	.db #0x02	;  2
   090C 02                 2189 	.db #0x02	;  2
   090D 03                 2190 	.db #0x03	;  3
   090E 03                 2191 	.db #0x03	;  3
   090F 04                 2192 	.db #0x04	;  4
   0910 04                 2193 	.db #0x04	;  4
   0911 05                 2194 	.db #0x05	;  5
   0912 05                 2195 	.db #0x05	;  5
   0913                    2196 __str_0:
   0913 45 4E              2197 	.ascii "EN"
   0915 00                 2198 	.db 0x00
   0916                    2199 __str_1:
   0916 66 72 65 65 73 6F  2200 	.ascii "freesoft.org"
        66 74 2E 6F 72 67
   0922 00                 2201 	.db 0x00
   0923                    2202 __str_2:
   0923 46 58 32 20 63 61  2203 	.ascii "FX2 case converter"
        73 65 20 63 6F 6E
        76 65 72 74 65 72
   0935 00                 2204 	.db 0x00
                           2205 	.area XINIT   (CODE)
                           2206 	.area CABS    (ABS,CODE)
