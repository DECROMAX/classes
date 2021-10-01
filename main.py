from datetime import date, timedelta
from datetime import datetime

class Fighter:

    def __init__(self, first_name, last_name, nickname, dob, weight_kg, height, wins, losses, draws, ko, sub):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.dob = datetime.strptime(dob, '%Y-%m-%d')
        self.weight_kg = weight_kg
        self.height = height
        self.wins = wins
        self.losses = losses
        self.total = self.wins + self.losses
        self.draws = draws
        self.ko = ko
        self.sub = sub

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def fight_record(self):
        return f'{self.wins}-{self.draws}-{self.losses}'

    def weight_lb(self):
        return self.weight_kg * 2.20462

    def height_ft(self):
        return self.height * 3.28084

    def win_percentage(self):
        return f'{self.wins / self.total:.2%}'

    def loss_percentage(self):
        return f'{self.losses / self.total:.2%}'

    def sub_percentage(self):
        return f'{self.sub / self.total:.2%}'

    def ko_percenatge(self):
        return f'{self.ko / self.total:.2%}'

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob .month, self.dob .day))


GPierre = Fighter('George', 'St Pierre', 'Rush', '1981-5-19', 77, 1.78, 26, 2, 0, 8, 6)
CMcgregor = Fighter('Connor', 'Mc Gregor', 'Notorious', '1988-7-14', 70, 1.75, 22, 6, 0, 19, 4)
