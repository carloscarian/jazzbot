import pygame
import os
from pygame.locals import *
import random
import time
from threading import Thread

#MAJOR ISSUES:
#

#ISSUES:
#

#TODO:
#MAKE IT WORK WITH PROGS LONGER THAN 3 CHORDS!! (scalable ideally)
#think of new nomenclature (don't really need the 01 for instrument at the end, so could use it for different versions of the same chord)
#think of how to record better music (chord changes are too abrupt)
    #IDEA: MAKE THE CHORD SOUNDFILES LONGER SO THERE'S MORE OVERLAP
#start working on option menu .-.
#pause button
#record minor tonics and stuff

#IDEAS:
#make logic that chooses a bassline that makes sense with the previous one when changing keys

#PLAN TO MAKE THINGS MORE SCALABLE:
#make a list with all the 251 types
#make the allowed_types list variable size (size should be how many types there are)
#

def randomtruefromboollist(lista, seed, howmanyallows):
    random.seed(seed)
    true_indices = [index for index,element in enumerate(lista) if element]
    result = random.choice(true_indices)
    return result

def bassvolumebutton(location, volume, mouse, instr_font, volume_font):

    l_0 = location[0]
    l_1 = location[1]

    vol_str = str(volume)

    instr_text = instr_font.render("Bass", 1, BLACK)
    vol_text = volume_font.render(vol_str, 1, BLACK)

    pygame.draw.polygon(surface, WHITE, [(l_0, l_1),(l_0, 70 + l_1),(140 + l_0, 70 + l_1),(140 + l_0, l_1)])
    surface.blit(instr_text, instr_text.get_rect(center = (l_0 + 70, l_1 + 35)))
    pygame.draw.polygon(surface, WHITE, [(180 + l_0, l_1),(180 + l_0, 70  + l_1),(240 + l_0, 70 + l_1),(240 + l_0, l_1)])
    surface.blit(vol_text, vol_text.get_rect(center = (l_0 + 210, l_1 + 35)))

    global bassonplus_bool
    global bassonminus_bool
    bassonplus_bool = (250 <= mouse[0] - location[0] <= 270) and (25 <= mouse[1] - location[1] <= 45)
    bassonminus_bool = (150 <= mouse[0] - location[0] <= 170) and (25 <= mouse[1] - location[1] <= 45)
    if bassonplus_bool:
        pygame.draw.polygon(surface, BLACK, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, WHITE, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, BLACK, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)], width=1)
    elif bassonminus_bool:
        pygame.draw.polygon(surface, BLACK, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, WHITE, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, BLACK, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)], width=1)
    else:
        pygame.draw.polygon(surface, BLACK, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, BLACK, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)])

def pianovolumebutton(location, volume, mouse, instr_font, volume_font):

    l_0 = location[0]
    l_1 = location[1]

    vol_str = str(volume)

    instr_text = instr_font.render("Piano", 1, BLACK)
    vol_text = volume_font.render(vol_str, 1, BLACK)

    pygame.draw.polygon(surface, WHITE, [(l_0, l_1),(l_0, 70 + l_1),(140 + l_0, 70 + l_1),(140 + l_0, l_1)])
    surface.blit(instr_text, instr_text.get_rect(center = (l_0 + 70, l_1 + 35)))
    pygame.draw.polygon(surface, WHITE, [(180 + l_0, l_1),(180 + l_0, 70  + l_1),(240 + l_0, 70 + l_1),(240 + l_0, l_1)])
    surface.blit(vol_text, vol_text.get_rect(center = (l_0 + 210, l_1 + 35)))

    global pianoonplus_bool
    global pianoonminus_bool
    pianoonplus_bool = (250 <= mouse[0] - location[0] <= 270) and (25 <= mouse[1] - location[1] <= 45)
    pianoonminus_bool = (150 <= mouse[0] - location[0] <= 170) and (25 <= mouse[1] - location[1] <= 45)
    if pianoonplus_bool:
        pygame.draw.polygon(surface, BLACK, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, WHITE, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, BLACK, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)], width=1)
    elif pianoonminus_bool:
        pygame.draw.polygon(surface, BLACK, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, WHITE, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, BLACK, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)], width=1)
    else:
        pygame.draw.polygon(surface, BLACK, [(150 + l_0, 35 + l_1),(170 + l_0, 25 + l_1),(170 + l_0, 45 + l_1)])
        pygame.draw.polygon(surface, BLACK, [(270 + l_0, 35 + l_1),(250 + l_0, 25 + l_1),(250 + l_0, 45 + l_1)])

def drawchords(chords):

    chord_past = other_chord_font.render(chords[0], 1, BLACK)
    chord_main = main_chord_font.render(chords[1], 1, RED)
    chord_next = other_chord_font.render(chords[2], 1, BLACK)
    chord_next2 = other_chord_font.render(chords[3], 1, BLACK)
    chord_next3 = other_chord_font.render(chords[4], 1, BLACK)

    pygame.draw.rect(surface, WHITE, white_rect_small.get_rect(center = (140,350)))
    pygame.draw.rect(surface, WHITE, white_rect_big.get_rect(center = (440,350)))
    pygame.draw.rect(surface, WHITE, white_rect_small.get_rect(center = (740,350)))
    pygame.draw.rect(surface, WHITE, white_rect_small.get_rect(center = (940,350)))
    pygame.draw.rect(surface, WHITE, white_rect_small.get_rect(center = (1140,350)))

    surface.blit(chord_past, chord_past.get_rect(center = (140,350)))
    surface.blit(chord_main, chord_main.get_rect(center = (440,350)))
    surface.blit(chord_next, chord_next.get_rect(center = (740,350)))
    surface.blit(chord_next2, chord_next2.get_rect(center = (940,350)))
    surface.blit(chord_next3, chord_next3.get_rect(center = (1140,350)))

def listcycle(lista):

    length = len(lista)
    newlist = lista
    newlist[-1] = ""

    for i in range(1, length):
        newlist [i - 1] = lista[i]

    return newlist

def findfirstempty(lista):
    #finds the first empty string in a list of strings and returns its index
    #returns -1 if there is no such element

    for i in lista:
        if i == "":
            return index(i)

    return -1

def keype2namelist(key_251, type_251):
    chordsnow = ["", "", ""]
    indiv_types = types[type_251]
    types_symbols = [type2str[i] for i in indiv_types]
    chordsnow[-1] = notes[key_251] + types_symbols[-1]
    chordsnow[-2] = notes[(key_251 + 7) %12] + types_symbols[-2]
    if len(types_symbols) == 3:
        chordsnow[-3] = notes[(key_251 + 2) %12] + types_symbols[-3]
    return chordsnow

def keype2filenamelist(key_251, type_251, tempo, instrument):
    chordfilesnow = ["", "", ""]
    indiv_types = types[type_251]
    chordfilesnow[-1] = str(indiv_types[-1]).zfill(2) + str(key_251).zfill(2) + str(tempo).zfill(3) + str(instrument).zfill(2)
    chordfilesnow[-2] = str(indiv_types[-2]).zfill(2) + str((key_251 + 7) % 12).zfill(2) + str(tempo).zfill(3) + str(instrument).zfill(2)
    if len(indiv_types) == 3:
        chordfilesnow[-3] = str(indiv_types[-3]).zfill(2) + str((key_251 + 2) % 12).zfill(2) + str(tempo).zfill(3) + str(instrument).zfill(2)
    return chordfilesnow

def play(seed):

    global bass_volume
    global piano_volume

    random.seed(seed)

    true_indices = [index for index,element in enumerate(allowed_types) if element]
    typeof251 = random.choice(true_indices)

    keyof251 = starting_key

    chordnames = ["sup", "", "", "", "", "", "", "", ""]
    basschordfilenames = ["", "", "", "", "", "", "", "", ""]
    pianochordfilenames = ["", "", "", "", "", "", "", "", ""]

    chordnames[1:4] = keype2namelist(keyof251, typeof251)
    basschordfilenames[1:4] = keype2filenamelist(keyof251, typeof251, tempo, 0)
    pianochordfilenames[1:4] = keype2filenamelist(keyof251, typeof251, tempo, 1)


    seed = random.randrange(0, 65535)
    random.seed(seed)
    typeof251 = random.choice(true_indices)

    upfifth = keyof251
    downfifth = keyof251
    fifthfilter = [keyof251]
    if fifth_distance != 0:
        for i in range(fifth_distance - 1):
            upfifth = (upfifth + 7) % 12
            downfifth = (downfifth - 7) % 12
            fifthfilter.append(upfifth)
            fifthfilter.append(downfifth)

    upsemit = keyof251
    downsemit = keyof251
    semitfilter = [keyof251]
    if semitone_distance != 0:
        for i in range(semitone_distance - 1):
            upsemit = (upsemit + 1) % 12
            downsemit = (downsemit - 1) % 12
            semitfilter.append(upsemit)
            semitfilter.append(downsemit)

    possiblekeys = [i for i in fifthfilter if i in semitfilter]
    keyof251 = random.choice(possiblekeys)

    if chordnames[3] == "":
        chordnames[3:6] = keype2namelist(keyof251, typeof251)
        basschordfilenames[3:6] = keype2filenamelist(keyof251, typeof251, tempo, 0)
        pianochordfilenames[3:6] = keype2filenamelist(keyof251, typeof251, tempo, 1)
    else:
        chordnames[4:7] = keype2namelist(keyof251, typeof251)
        basschordfilenames[4:7] = keype2filenamelist(keyof251, typeof251, tempo, 0)
        pianochordfilenames[4:7] = keype2filenamelist(keyof251, typeof251, tempo, 1)


    if chordnames[5] == "":
        seed = random.randrange(0, 65535)
        random.seed(seed)
        typeof251 = random.choice(true_indices)

        upfifth = keyof251
        downfifth = keyof251
        fifthfilter = [keyof251]
        if fifth_distance != 0:
            for i in range(fifth_distance - 1):
                upfifth = (upfifth + 7) % 12
                downfifth = (downfifth - 7) % 12
                fifthfilter.append(upfifth)
                fifthfilter.append(downfifth)

        upsemit = keyof251
        downsemit = keyof251
        semitfilter = [keyof251]
        if semitone_distance != 0:
            for i in range(semitone_distance - 1):
                upsemit = (upsemit + 1) % 12
                downsemit = (downsemit - 1) % 12
                semitfilter.append(upsemit)
                semitfilter.append(downsemit)

        possiblekeys = [i for i in fifthfilter if i in semitfilter]
        keyof251 = random.choice(possiblekeys)

        chordnames[5:8] = keype2namelist(keyof251, typeof251)
        basschordfilenames[5:8] = keype2filenamelist(keyof251, typeof251, tempo, 0)
        pianochordfilenames[5:8] = keype2filenamelist(keyof251, typeof251, tempo, 1)

    #SHOULD ALWAYS HAVE ENOUGH CHORDS AT THIS POINT (i.e. at least five chords are in chordnames)

    while playing:

        endloop = False

        drawchords(chordnames)

        bass_name = basschordfilenames[1] + ".wav"
        bass_file = os.path.join(script_dir,"sounds","single_chords","bass",bass_name)
        bass_sound = pygame.mixer.Sound(bass_file)

        piano_name = pianochordfilenames[1] + ".wav"
        piano_file = os.path.join(script_dir,"sounds","single_chords","piano",piano_name)
        piano_sound = pygame.mixer.Sound(piano_file)

        bass.play(bass_sound)
        bass.set_volume(bass_volume/10)
        piano.play(piano_sound)
        piano.set_volume(piano_volume/10)

        #length in ms
        chord_length = 1000*bass_sound.get_length()

        time_chordstart = pygame.time.get_ticks()
        while True:
            time_now = pygame.time.get_ticks()
            if time_now < time_chordstart + chord_length:
                #print(7)
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        endloop = True
                        break
                elif event.type == MOUSEBUTTONDOWN:
                    if onstop_bool:
                        endloop = True
                        break
            else:
                break

        if endloop == True:
            break

        chordnames = listcycle(chordnames)
        basschordfilenames = listcycle(basschordfilenames)
        pianochordfilenames = listcycle(pianochordfilenames)

        if chordnames[5] == "":

            seed = random.randrange(0, 65535)
            random.seed(seed)
            typeof251 = random.choice(true_indices)

            upfifth = keyof251
            downfifth = keyof251
            fifthfilter = [keyof251]
            if fifth_distance != 0:
                for i in range(fifth_distance - 1):
                    upfifth = (upfifth + 7) % 12
                    downfifth = (downfifth - 7) % 12
                    fifthfilter.append(upfifth)
                    fifthfilter.append(downfifth)

            upsemit = keyof251
            downsemit = keyof251
            semitfilter = [keyof251]
            if semitone_distance != 0:
                for i in range(semitone_distance - 1):
                    upsemit = (upsemit + 1) % 12
                    downsemit = (downsemit - 1) % 12
                    semitfilter.append(upsemit)
                    semitfilter.append(downsemit)

            possiblekeys = [i for i in fifthfilter if i in semitfilter]
            keyof251 = random.choice(possiblekeys)

            chordnames[5:8] = keype2namelist(keyof251, typeof251)
            basschordfilenames[5:8] = keype2filenamelist(keyof251, typeof251, tempo, 0)
            pianochordfilenames[5:8] = keype2filenamelist(keyof251, typeof251, tempo, 1)

if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    MID_GREY = (120,120,120)
    RED = (235, 7, 7)

    notes = ["C", "D"+"\u266d", "D", "E"+"\u266d", "E", "F", "G"+"\u266d", "G", "A"+"\u266d", "A", "B"+"\u266d", "B"]
    types = [[3,2,0], [4,2,1], [2,2,1], [3,2,1], [2,2,1], [2,0], [2,1], [3,2,0,0], [4,2,1,1], [2,2,1,1], [3,2,1,1], [2,2,1,1]]
    type2str = ["", "m", "7", "m7", "\u00f8" + "7"]
    instr = ["Bass", "Piano"]

    surface = pygame.display.set_mode((1280,720))

    pygame.display.set_caption("jazzbot alpha")

    #font stuff (and draw initial chords MIGHT SCRAP)
    script_dir = os.path.dirname(__file__)
    font_path = os.path.join(script_dir,"fonts","cadman.ttf")

    main_chord_font = pygame.font.Font(font_path, 140)
    other_chord_font = pygame.font.Font(font_path, 80)
    menu_font = pygame.font.Font(font_path, 40)
    volume_font = pygame.font.Font(font_path, 35)
    instr_vol_font = pygame.font.Font(font_path, 30)

    options_text_black = menu_font.render("Options", 1, BLACK)
    quit_text_black = menu_font.render("Quit", 1, BLACK)
    back_text_black = menu_font.render("Back", 1, BLACK)
    options_text_white = menu_font.render("Options", 1, WHITE)
    quit_text_white = menu_font.render("Quit", 1, WHITE)
    back_text_white = menu_font.render("Back", 1, WHITE)

    #dumb workaround
    white_rect_small = other_chord_font.render("B"+"\u266d"+"m7", 1, BLACK)
    white_rect_big = main_chord_font.render("B"+"\u266d"+"m7", 1, RED)

    #mixer stuff
    bass = pygame.mixer.Channel(0)
    piano = pygame.mixer.Channel(1)

    #initial setting flags

    fifth_distance = 6
    semitone_distance = 6

    tempo = 100

    starting_key = 0

    random_starting_key_bool = True #true if random, false if not, gray out starting key menu in options if true. this should be a checkbox


    global bass_volume
    global piano_volume
    global drums_volume
    bass_volume = 7 #0 (mute) to 10
    piano_volume = 7
    drums_volume = 7

    #REMEMBER TO SET A OPT MENU CHECK THAT AT LEAST ONE OF THE FOLLOWING IS TRUE
    allowed_types = len(types)*[False]
    allowed_types[0] = True
    howmanyallows = sum(allowed_types)
    #0 Dm G C
    #1 Dhd G Cm
    #2 D G Cm
    #3 Dm G Cm
    #4 D G C
    #5 G C
    #6 G Cm
    #7 Dm G C C
    #8 Dhd G Cm Cm
    #9 D G Cm Cm
    #10 Dm G Cm Cm
    #11 D G C C

    darkmode = False

    seed = 12213

    running = True
    playing = False
    options = False

    while running:

        mouse = pygame.mouse.get_pos()

        if options == False and playing == False:

            surface.fill(WHITE)

            #inactive stop and pause buttons
            #stop
            pygame.draw.circle(surface, WHITE, (840, 580), 80, width=0)
            pygame.draw.circle(surface, MID_GREY, (840, 580), 80, width=1)
            pygame.draw.polygon(surface, MID_GREY, [(800, 620),(880, 620),(880, 540),(800, 540)])
            #pause
            pygame.draw.circle(surface, WHITE, (440, 580), 80, width=0)
            pygame.draw.circle(surface, MID_GREY, (440, 580), 80, width=1)
            pygame.draw.polygon(surface, MID_GREY, [(395, 625),(425, 625),(425, 535),(395, 535)])
            pygame.draw.polygon(surface, MID_GREY, [(455, 625),(485, 625),(485, 535),(455, 535)])

            #play button
            dist2playx = mouse[0] - 640
            dist2playy = mouse[1] - 580
            onplay_bool = dist2playx*dist2playx + dist2playy*dist2playy <= 10000
            if onplay_bool:
                pygame.draw.circle(surface, BLACK, (640, 580), 100, width=0)
                pygame.draw.polygon(surface, WHITE, [(600, 650),(600, 510),(720, 580)], width = 0)
            else:
                pygame.draw.circle(surface, WHITE, (640, 580), 100, width=0)
                pygame.draw.circle(surface, BLACK, (640, 580), 100, width=1)
                pygame.draw.polygon(surface, BLACK, [(600, 650),(600, 510),(720, 580)], width = 0)

            #quit button
            onquit_bool = (980 <= mouse[0] <= 1220) and (590 <= mouse[1] <= 660)
            if onquit_bool:
                pygame.draw.polygon(surface, BLACK, [(980, 660),(1220, 660),(1220, 590),(980, 590)])
                surface.blit(quit_text_white, quit_text_white.get_rect(center = (1100,625)))
            else:
                pygame.draw.polygon(surface, WHITE, [(980, 660),(1220, 660),(1220, 590),(980, 590)])
                pygame.draw.polygon(surface, BLACK, [(980, 660),(1220, 660),(1220, 590),(980, 590)], width=1)
                surface.blit(quit_text_black, quit_text_black.get_rect(center = (1100,625)))

            #options button
            onopt_bool = (980 <= mouse[0] <= 1220) and (500 <= mouse[1] <= 570)
            if onopt_bool:
                pygame.draw.polygon(surface, BLACK, [(980, 570),(1220, 570),(1220, 500),(980, 500)])
                surface.blit(options_text_white, options_text_white.get_rect(center = (1100,535)))
            else:
                pygame.draw.polygon(surface, WHITE, [(980, 570),(1220, 570),(1220, 500),(980, 500)])
                pygame.draw.polygon(surface, BLACK, [(980, 570),(1220, 570),(1220, 500),(980, 500)], width=1)
                surface.blit(options_text_black, options_text_black.get_rect(center = (1100,535)))

            #lines
            pygame.draw.line(surface, MID_GREY, (40,300),(40,416))
            pygame.draw.line(surface, MID_GREY, (240,300),(240,416))
            pygame.draw.line(surface, MID_GREY, (640,300),(640,416))
            pygame.draw.line(surface, MID_GREY, (840,300),(840,416))
            pygame.draw.line(surface, MID_GREY, (1040,300),(1040,416))
            pygame.draw.line(surface, MID_GREY, (1240,300),(1240,416))

            #volume
            bassvolumebutton((40, 480), bass_volume, mouse, instr_vol_font, volume_font)
            pianovolumebutton((40, 530), piano_volume, mouse, instr_vol_font, volume_font)

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:

                        playing = True
                        playthread = Thread(target = play, args = (seed,))
                        playthread.start()

                    if event.key == K_ESCAPE:

                        running = False

                elif event.type == MOUSEBUTTONDOWN:

                    if onquit_bool:

                        running = False

                    elif onopt_bool:

                        options = True
                        surface.fill(WHITE)

                    elif onplay_bool:

                        playing = True
                        playthread = Thread(target = play, args = (seed,))
                        playthread.start()

                    elif bassonplus_bool:

                        bass_volume = min([10, bass_volume + 1])

                    elif bassonminus_bool:

                        bass_volume = max([0, bass_volume - 1])

                    elif pianoonplus_bool:

                        piano_volume = min([10, piano_volume + 1])

                    elif pianoonminus_bool:

                        piano_volume = max([0, piano_volume - 1])

                elif event.type == QUIT:

                    running = False

        elif options == True:

            #quit button
            onquit_bool = (980 <= mouse[0] <= 1220) and (590 <= mouse[1] <= 660)
            if onquit_bool:
                pygame.draw.polygon(surface, BLACK, [(980, 660),(1220, 660),(1220, 590),(980, 590)])
                surface.blit(quit_text_white, quit_text_white.get_rect(center = (1100,625)))
            else:
                pygame.draw.polygon(surface, WHITE, [(980, 660),(1220, 660),(1220, 590),(980, 590)])
                pygame.draw.polygon(surface, BLACK, [(980, 660),(1220, 660),(1220, 590),(980, 590)], width=1)
                surface.blit(quit_text_black, quit_text_black.get_rect(center = (1100,625)))

            #back button
            onopt_bool = (980 <= mouse[0] <= 1220) and (500 <= mouse[1] <= 570)
            if onopt_bool:
                pygame.draw.polygon(surface, BLACK, [(980, 570),(1220, 570),(1220, 500),(980, 500)])
                surface.blit(back_text_white, back_text_white.get_rect(center = (1100,535)))
            else:
                pygame.draw.polygon(surface, WHITE, [(980, 570),(1220, 570),(1220, 500),(980, 500)])
                pygame.draw.polygon(surface, BLACK, [(980, 570),(1220, 570),(1220, 500),(980, 500)], width=1)
                surface.blit(back_text_black, back_text_black.get_rect(center = (1100,535)))

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:

                        running = False

                elif event.type == MOUSEBUTTONDOWN:

                    if onquit_bool:

                        running = False

                    elif onopt_bool:

                        options = False

                        surface.fill(WHITE)

                        #lines
                        pygame.draw.line(surface, MID_GREY, (40,300),(40,416))
                        pygame.draw.line(surface, MID_GREY, (240,300),(240,416))
                        pygame.draw.line(surface, MID_GREY, (640,300),(640,416))
                        pygame.draw.line(surface, MID_GREY, (840,300),(840,416))
                        pygame.draw.line(surface, MID_GREY, (1040,300),(1040,416))
                        pygame.draw.line(surface, MID_GREY, (1240,300),(1240,416))

                        #chords
                        surface.blit(chord_past, chord_past.get_rect(center = (140,350)))
                        surface.blit(chord_main, chord_main.get_rect(center = (440,350)))
                        surface.blit(chord_next, chord_next.get_rect(center = (740,350)))
                        surface.blit(chord_next2, chord_next2.get_rect(center = (940,350)))
                        surface.blit(chord_next3, chord_next3.get_rect(center = (1140,350)))

                elif event.type == QUIT:

                    running = False

        elif playing == True:

            #inactive play button
            pygame.draw.circle(surface, WHITE, (640, 580), 100, width=0)
            pygame.draw.circle(surface, MID_GREY, (640, 580), 100, width=1)
            pygame.draw.polygon(surface, MID_GREY, [(600, 650),(600, 510),(720, 580)], width = 0)

            #pause button
            dist2pausex = mouse[0] - 440
            dist2pausey = mouse[1] - 580
            onpause_bool = dist2pausex*dist2pausex + dist2pausey*dist2pausey <= 6400
            if onpause_bool:
                pygame.draw.circle(surface, BLACK, (440, 580), 80, width=0)
                pygame.draw.polygon(surface, WHITE, [(395, 625),(425, 625),(425, 535),(395, 535)])
                pygame.draw.polygon(surface, WHITE, [(455, 625),(485, 625),(485, 535),(455, 535)])
            else:
                pygame.draw.circle(surface, WHITE, (440, 580), 80, width=0)
                pygame.draw.circle(surface, BLACK, (440, 580), 80, width=1)
                pygame.draw.polygon(surface, BLACK, [(395, 625),(425, 625),(425, 535),(395, 535)])
                pygame.draw.polygon(surface, BLACK, [(455, 625),(485, 625),(485, 535),(455, 535)])

            #stop button
            dist2stopx = mouse[0] - 840
            dist2stopy = mouse[1] - 580
            onstop_bool = dist2stopx*dist2stopx + dist2stopy*dist2stopy <= 6400
            if onstop_bool:
                pygame.draw.circle(surface, BLACK, (840, 580), 80, width=0)
                pygame.draw.polygon(surface, WHITE, [(800, 620),(880, 620),(880, 540),(800, 540)])
            else:
                pygame.draw.circle(surface, WHITE, (840, 580), 80, width=0)
                pygame.draw.circle(surface, BLACK, (840, 580), 80, width=1)
                pygame.draw.polygon(surface, BLACK, [(800, 620),(880, 620),(880, 540),(800, 540)])

            #lines
            pygame.draw.line(surface, MID_GREY, (40,300),(40,416))
            pygame.draw.line(surface, MID_GREY, (240,300),(240,416))
            pygame.draw.line(surface, MID_GREY, (640,300),(640,416))
            pygame.draw.line(surface, MID_GREY, (840,300),(840,416))
            pygame.draw.line(surface, MID_GREY, (1040,300),(1040,416))
            pygame.draw.line(surface, MID_GREY, (1240,300),(1240,416))

            #volume
            bassvolumebutton((40, 480), bass_volume, mouse, instr_vol_font, volume_font)
            pianovolumebutton((40, 530), piano_volume, mouse, instr_vol_font, volume_font)

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:

                        playing = False
                        bass.stop()
                        piano.stop()

                    if event.key == K_ESCAPE:

                        running = False

                elif event.type == MOUSEBUTTONDOWN:

                    if onquit_bool:

                        running = False

                    elif onopt_bool:

                        options = True
                        surface.fill(WHITE)

                    elif onstop_bool:

                        playing = False
                        bass.stop()
                        piano.stop()

                    elif bassonplus_bool:

                        bass_volume = min([10, bass_volume + 1])
                        bass.set_volume(bass_volume/10)

                    elif bassonminus_bool:

                        bass_volume = max([0, bass_volume - 1])
                        bass.set_volume(bass_volume/10)

                    elif pianoonplus_bool:

                        piano_volume = min([10, piano_volume + 1])
                        piano.set_volume(piano_volume/10)

                    elif pianoonminus_bool:

                        piano_volume = max([0, piano_volume - 1])
                        piano.set_volume(piano_volume/10)

                elif event.type == QUIT:

                    running = False

        pygame.display.flip()

    pygame.quit()
