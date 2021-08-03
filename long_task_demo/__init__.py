from otree.api import *

from background.tasks import huey, add

import random


class Constants(BaseConstants):
    name_in_url = 'long_task_demo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    random_number1 = models.IntegerField()
    random_number2 = models.IntegerField()

    task_result = models.IntegerField()
    result_id = models.StringField()


# fill the players with two random numbers as inputs for the long running task
def creating_session(subsession):
    for player in subsession.get_players():
        player.random_number1 = random.randint(1, 10)
        player.random_number2 = random.randint(11, 20)


# PAGES
class MyPage(Page):
    def live_method(player: Player, data):
        if data['message'] == 'start':
            # when the player clicks the start button, we start the long-running task and store its id
            result = add(player.random_number1, player.random_number2)
            player.result_id = result.id

        # the client will ask us for the result over and over again.
        # we check if it is unequal "none". If so, we got a result and can store and return it.
        if data['message'] == 'get_result':
            try:
                result = huey.result(player.result_id)
            except TypeError:
                result = None

            if result:
                # store the result
                player.task_result = result
                return {player.id_in_group: {'message': 'result', 'result': result}}


page_sequence = [MyPage]