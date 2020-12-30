from mycroft import MycroftSkill, intent_file_handler


class Fintosh(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fintosh.intent')
    def handle_fintosh(self, message):
        self.speak_dialog('fintosh')


def create_skill():
    return Fintosh()

