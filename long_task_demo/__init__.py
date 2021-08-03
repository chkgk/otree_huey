from otree.api import *
from huey import SqliteHuey

huey = SqliteHuey()

@huey.task()
def add(player, a, b):
    player.task_result = a + b
    print('task result:', player.task_result)
    return


class Constants(BaseConstants):
    name_in_url = 'long_task_demo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_result = models.IntegerField()


# PAGES
class MyPage(Page):
    def before_next_page(player, timeout_happened):
        result = add(player, 1, 2)


class Result(Page):
    pass

page_sequence = [MyPage, Result]