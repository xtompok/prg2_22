from math import hypot
class Monitor(object):
    def __init__(self,uhlopricka=0, rozliseni=[0,0], spotreba=0):
        self.uhlopricka = uhlopricka
        self.rozliseni = rozliseni
        self.spotreba = spotreba
        
    def dpi(self):
        return hypot(*self.rozliseni)/self.uhlopricka

    def __str__(self):
        return f"Monitor ({self.uhlopricka}\", {self.rozliseni[0]}x{self.rozliseni[1]}, {self.spotreba} W)"
        
class PC():
    def __init__(self) -> None:
        self.procesor = None
        self.RAM = 0
        self.spotreba = 0

class Sestava():
    def __init__(self, monitor, pc) -> None:
        self.monitor = monitor
        self.pc = pc
        

muj_monitor = Monitor(uhlopricka=24, rozliseni=[1920,1200], spotreba=20)
ma_sestava = Sestava(muj_monitor, PC())
print(ma_sestava.monitor.dpi())
print(muj_monitor.dpi())
muj_monitor.rozliseni = [1024,768]
print(muj_monitor.dpi())
print(muj_monitor)
muj_druhy_monitor = Monitor()
muj_treti_monitor = Monitor(32,[3200,1800],100)
print(type(muj_monitor))
print(Monitor)
print(type(muj_monitor) == Monitor)
print(isinstance(muj_monitor, Monitor))
print(type(Monitor))
print(muj_druhy_monitor == muj_monitor)