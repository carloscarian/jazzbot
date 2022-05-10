import pygame
import os
from pygame.locals import *
import random
import time
from threading import Thread

#GLITCH: if you stop, play() is still in sleep, if you play() again before sleep is over it glitches out

def listcycle(lista):

    length = len(lista)
    newlist = lista

    for i in range(1, length):
        newlist [i - 1] = lista[i]

    return newlist

def filepath2chords(filepath):

    if filepath[0:2] == "00":
        min_second = notes[(int(filepath[2:4]) + 2) %12] + "m"
        dominant = notes[(int(filepath[2:4]) + 7) %12] + "7"
        tonic = notes[int(filepath[2:4]) %12]
        chords = [min_second, dominant, tonic]

    return chords

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

def play(seed):

    random.seed(seed)
    typeof251 = random.randrange(0, howmanyallows)
    keyof251 = random.randrange(0, 12)
    bass_name = str(typeof251).zfill(2) + str(keyof251).zfill(2) + str(tempo).zfill(3) + "00.wav"
    bass_file = os.path.join(script_dir,"sounds","full_progs",bass_name)
    bass_sound = pygame.mixer.Sound(bass_file)
    chordsnow = filepath2chords(bass_name)
    chords = ["", chordsnow[0], chordsnow[1], chordsnow[2], ""]

    bass.play(bass_sound)
    seed = random.randrange(0, 16384)
    random.seed(seed)
    typeof251 = random.randrange(0, howmanyallows)
    keyof251 = random.randrange(0, 12)
    bass_name = str(typeof251).zfill(2) + str(keyof251).zfill(2) + str(tempo).zfill(3) + "00.wav"
    chordsnow = filepath2chords(bass_name)
    chords[4] = chordsnow[0]

    while playing:

        bass_file = os.path.join(script_dir,"sounds", "full_progs",bass_name)
        bass_sound = pygame.mixer.Sound(bass_file)
        bass_length = bass_sound.get_length()
        chord_length = bass_length/3
        drawchords(chords)
        time.sleep(chord_length)
        chords = listcycle(chords)
        chords[4] = chordsnow[1]
        drawchords(chords)
        time.sleep(chord_length)
        chords = listcycle(chords)
        chords[4] = chordsnow[2]
        drawchords(chords)
        time.sleep(chord_length)

        if not playing:
            break

        bass.play(bass_sound)
        seed = random.randrange(0, 16384)
        random.seed(seed)
        typeof251 = random.randrange(0, howmanyallows)
        keyof251 = random.randrange(0, 12)
        bass_name = str(typeof251).zfill(2) + str(keyof251).zfill(2) + str(tempo).zfill(3) + "00.wav"
        chordsnow = filepath2chords(bass_name)
        chords = listcycle(chords)
        chords[4] = chordsnow[0]

if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    MID_GREY = (120,120,120)
    RED = (235, 7, 7)

    notes = ["C", "D"+"\u266d", "D", "E"+"\u266d", "E", "F", "G"+"\u266d", "G", "A"+"\u266d", "A", "B"+"\u266d", "B"]

    surface = pygame.display.set_mode((1280,720))

    pygame.display.set_caption("jazzbot alpha")

    #font stuff (and draw initial chords MIGHT SCRAP)
    script_dir = os.path.dirname(__file__)
    font_path = os.path.join(script_dir,"fonts","cadman.ttf")
    main_chord_font = pygame.font.Font(font_path, 160)
    other_chord_font = pygame.font.Font(font_path, 100)
    menu_font = pygame.font.Font(font_path, 40)
    options_text_black = menu_font.render("Options", 1, BLACK)
    quit_text_black = menu_font.render("Quit", 1, BLACK)
    back_text_black = menu_font.render("Back", 1, BLACK)
    options_text_white = menu_font.render("Options", 1, WHITE)
    quit_text_white = menu_font.render("Quit", 1, WHITE)
    back_text_white = menu_font.render("Back", 1, WHITE)
    chord_past = other_chord_font.render("B", 1, BLACK)
    chord_main = main_chord_font.render("D7", 1, RED)
    chord_next = other_chord_font.render("G", 1, BLACK)
    chord_next2 = other_chord_font.render("B"+"\u266d"+"7", 1, BLACK)
    chord_next3 = other_chord_font.render("E"+"\u266d", 1, BLACK)
    surface.blit(chord_past, chord_past.get_rect(center = (140,350)))
    surface.blit(chord_main, chord_main.get_rect(center = (440,350)))
    surface.blit(chord_next, chord_next.get_rect(center = (740,350)))
    surface.blit(chord_next2, chord_next2.get_rect(center = (940,350)))
    surface.blit(chord_next3, chord_next3.get_rect(center = (1140,350)))
    #dumb workaround
    white_rect_small = other_chord_font.render("GGG", 1, BLACK)
    white_rect_big = main_chord_font.render("GGG", 1, RED)

    #mixer stuff
    bass = pygame.mixer.Channel(0)

    #initial setting flags
    fifth_distance = 6
    semitone_distance = 6
    tempo = 100
    starting_key = (0, 0) #first element is what key center (C, Db etc), second element is mode (maj, min)
    #REMEMBER TO SET A OPT MENU CHECK THAT AT LEAST ONE OF THE FOLLOWING IS TRUE
    allow_major = True #Dm G C
    allow_minor = False #Dhd G Cm
    allow_secondary = False #D G Cm
    allow_minsecondaryminor = False #Dm G Cm
    allow_no2major = False #G C
    allow_no2minor = False #G Cm
    darkmode = False
    seed = 0

    #other flags
    howmanyallows = 1

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

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:

                        playing = False
                        bass.stop()

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

                elif event.type == QUIT:

                    running = False

        pygame.display.flip()

    pygame.quit()
