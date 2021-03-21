
import os
import nltk
import time
import datetime
import pygame
import random
from sets.wiki import *

red = (255,0,0)
blue = (0,0,255)


class Fooliery:
    def __init__(self,file):
        self.file = file


        self.workspace = os.listdir()
        self.running = True
        print(self.workspace)
    def loadItUp(self,file):
        f = open(file, "r")
        lineList = []
        while(True):
            l = f.readline()

            lineList.append(str(l.strip()))

            if not l:
                break
        f.close()
        return lineList


    def Run(self):
        while self.running:
            print('------------------^^^^^^^^^^---------------------')
            userInput = input()
            self.Commands(userInput)
            print('------------------vvvvvvvvvv----------------------')

    def Commands(self,input):

        i = nltk.word_tokenize(input)
        if len(i) > 0:
            if i[0] == 'date':
                print(str(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")))
            #############################################################################

            if i[0] == 'math' and i[1] == ':':
                string = ''
                for e in range(len(i)):
                    if i[e] == 'math' or i[e] == ':':
                        pass
                    else:
                        string += i[e]
                print('OUTPUT = '+str(eval(string)))

            if i[0] == 'window':
                screen = pygame.display.set_mode((200,200))
                now = time.time()
                then = now + 5
                while then >= now:
                    now = time.time()
                    screen.fill(random.choice([red,blue]))
                    pygame.display.flip()
                pygame.quit()

            if i[0] == 'Moon':
                print(ReturnMoonPhase())
            if i[0] == 'search' and i[1] == ':':
                if len(i) > 2:
                    string = ''
                    for e in range(len(i)):
                        if i[e] == 'search' or i[e] == ':':
                            pass
                        else:
                            string += (i[e] + ' ')
                else:
                    string = i[2]
                print('OUTPUT = ' +googlesearch(str(string)))


            ###############################################################################
            if i[0] == 'docs':
                lines = self.loadItUp('docs//Fooliery Docs.txt')
                for i in lines:
                    print(str(i))
        print('COMMANDS--' + str(i))






F = Fooliery(None)
F.Run()
