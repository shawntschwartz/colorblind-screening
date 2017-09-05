"""Code used to quickly test for color blindness.

If participants don't score 100% they may be colorblind and should do the full
test.

To use, simply open and run the code in psychopy.
Alternativly, import and run yourself.

The main function is run_colorscreen.

Pressing 'q' while the program is expecting a key press will quit.

This code was originally written by Albert Chen under the supervision of Colin
Quirk. Small changes in usage and formatting have been made by Colin Quirk.
"""

from __future__ import division

import sys

import psychopy.visual
import psychopy.event
import psychopy.core

win = psychopy.visual.Window(
    units='pix', color=(1, 1, 1), colorSpace='rgb', fullscr=True)

intro_text = psychopy.visual.TextStim(
    win, color=(-1, -1, -1), colorSpace='rgb',
    text="Welcome to the color blindness screening test. " +
    "Press the spacebar to continue.")

instruction_text = psychopy.visual.TextStim(
    win, color=(-1, -1, -1), colorSpace='rgb',
    text="Numbers will be displayed one at a time. See below for an " +
    "example. Each number will last " +
    "for 3 seconds. After the number disappears, enter the " +
    "number you saw. Press the spacebar to submit your answer and use the " +
    "backspace key if needed. Press the spacebar to begin.")

ishihara_16 = psychopy.visual.ImageStim(win, image='p16.jpg', pos=(0, -250))

ishihara_02 = psychopy.visual.ImageStim(win, image='p02.jpg')
ishihara_05 = psychopy.visual.ImageStim(win, image='p05.jpg')
ishihara_06 = psychopy.visual.ImageStim(win, image='p06.jpg')
ishihara_07 = psychopy.visual.ImageStim(win, image='p07.jpg')
ishihara_10 = psychopy.visual.ImageStim(win, image='p10.jpg')
ishihara_29 = psychopy.visual.ImageStim(win, image='p29.jpg')
ishihara_42 = psychopy.visual.ImageStim(win, image='p42.jpg')
ishihara_57 = psychopy.visual.ImageStim(win, image='p57.jpg')

ishihara_dict = {ishihara_02: 2, ishihara_05: 5, ishihara_06: 6,
                 ishihara_07: 7, ishihara_10: 10, ishihara_29: 29,
                 ishihara_42: 42, ishihara_57: 57}

question = psychopy.visual.TextStim(
    win, text="What number was displayed?", color=(-1, -1, -1),
    colorSpace='rgb', pos=(0, 20))


def mean(list_response):
    total = sum(list_response)
    total = float(total)
    average = total / len(list_response)
    return average


def get_response(dict):
    correct = []
    for num in dict:
        num.draw()
        win.flip()
        psychopy.core.wait(3)
        question.draw()
        win.flip()
        string_response = ''
        keyList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'backspace', 'space', 'q']
        while True:
            question.draw()
            keys = psychopy.event.waitKeys(keyList=keyList)

            if 'q' in keys:
                sys.exit(0)

            if len(keys) > 1:
                continue
            elif keys[0] == 'space':
                break
            elif keys[0] == 'backspace':
                string_response = string_response[:-1]
            else:
                string_response += keys[0]

            psychopy.visual.TextStim(
                win, text=string_response, color=(-1, -1, -1),
                colorSpace='rgb', pos=(0, -20)).draw()
            win.flip()

        if string_response == str(ishihara_dict[num]):
            correct.append(1)
        else:
            correct.append(0)
            print 'test: %s response: %s' % (
                str(ishihara_dict[num]), string_response)

    print str(round(mean(correct) * 100, 2)) + '%'


def run_colorscreen():
    intro_text.draw()
    win.flip()
    psychopy.event.waitKeys(
        maxWait='inf', keyList=['space'], modifiers=False, timeStamped=False)
    instruction_text.draw()
    ishihara_16.draw()
    win.flip()
    psychopy.event.waitKeys(
        maxWait='inf', keyList=['space'], modifiers=False, timeStamped=False)
    get_response(ishihara_dict)
    win.close()

if __name__ == "__main__":
    run_colorscreen()
