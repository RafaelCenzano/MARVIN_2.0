# Imports
import time
import marvin.essentials
from word2number import w2n


##############################
# File containing Timer code #
##############################


class TimerService():
    def __init__(self, time_for, speak_type):
        self.speak_type = speak_type
        self.time_for = time_for
        self.bob = 1
        try:
            if time_for == '':
                raise Exception
        except Exception:
            self.bob = 0

    def timerLogic(self):
        time_for_timer = self.time_for.split(" ")[0]
        if time_for_timer.lower() == 'zero' or time_for_timer == '0':
            self.bob = 0
        if self.bob >= 1:
            time_unit = marvin.essentials.splitJoin(self.time_for, 1)
            if time_unit == '':
                time_unit = 'minutes'
            try:
                bob = float(time_for_timer)
                self.time_for_timer = float(time_for_timer)
            except ValueError:
                self.time_for_timer = float(w2n.word_to_num(str(time_for_timer)))
            if 'min' in time_unit:
                abs_time = abs(float(self.time_for_timer))
                minutes_in_seconds = abs_time * 60
                self.timer(minutes_in_seconds)
            elif 'sec' in time_unit:
                pass
            elif 'hr' in time_unit:
                if self.time_for_timer < 5:
                    pass
                else:
                    marvin.essentials.speak('Timer does not support reminders over 5 hours use a calander reminder for long reminders', speak_type)
            elif 'day' in time_unit:
                marvin.essentials.speak('Timer does not support days use a calander reminder for long reminders', speak_type)
            else:
                marvin.essentials.speak('We couldn\'t find the time unit you wanted to use', speak_type)
        else:
            marvin.essentials.speak('You need to input a number for the timer', speak_type)

    def timer(self, minutes_in_seconds):
        print('Timer Started')
        time.sleep(float(minutes_in_seconds))
        try:
            marvin.essentials.speak('Timer Done!', self.speak_type, 1)
        except AttributeError:
            pass