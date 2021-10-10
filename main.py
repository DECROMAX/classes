from datetime import date, timedelta
from datetime import datetime


class Fighter:

    def __init__(self, first_name, last_name, full_name, nickname, image_url, fighter_url, dob, location,
                 nationality, association, weight_kg, weight_class, height, wins, losses,  win_ko,
                 win_submission, win_decision, loss_ko, loss_submission, loss_decision):

        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.nickname = nickname

        self.image_url = image_url
        self.fighter_url = fighter_url

        self.dob = datetime.strptime(dob, '%Y-%m-%d')
        self.location = location
        self.nationality = nationality
        self.association = association

        self.height = height
        self.weight_kg = weight_kg
        self.weight_class = weight_class

        self.wins = wins
        self.losses = losses

        self.win_ko = win_ko
        self.win_submission = win_submission
        self.win_decision = win_decision

        self.loss_by_ko = loss_ko
        self.loss_submission = loss_submission
        self.loss_decision = loss_decision

        self.total_fights = self.wins + self.losses


    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def fight_record(self):
        return f'W{self.wins}-L{self.losses}'

    def weight_lb(self):
        return self.weight_kg * 2.20462

    def height_ft(self):
        return self.height * 3.28084

    def win_percentage(self):
        return f'{self.wins / self.total:.2%}'

    def loss_percentage(self):
        return f'{self.losses / self.total:.2%}'

    def win_sub_percentage(self):
        return f'{self.win_submission / self.total:.2%}'

    def win_ko_percenatge(self):
        return f'{self.win_ko / self.total:.2%}'

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob .month, self.dob .day))

