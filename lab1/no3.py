class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def set(self, h, m, s):
        self.hr, self.min, self.sec = h, m, s
    def get(self):
        return (self.hr, self.min, self.sec)
    def printTime(self):
        time = "{:02d}:{:02d}:{:02d}".format(self.hr, self.min, self.sec)
        print(time)

time1 = Time(9, 30, 0)
time1.printTime()