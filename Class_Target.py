from Func.Target_func import *


# MOUSEBUTTON -> Gun class -> Target class


class Update:
    @staticmethod
    def enter(target, e):
        pass

    @staticmethod
    def exit(target, e):
        pass

    @staticmethod
    def do(target):
        cal_dis(target)
        update_recoil(target)

    @staticmethod
    def draw(target):
        draw_target(target)


class StateMachineTarget:
    def __init__(self, target):
        self.target = target
        self.cur_state = Update
        self.table = {
            Update: {},
        }

    def start(self):
        self.cur_state.enter(self.target, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.target)

    def handle_event(self, e):  # state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.target, e)
                self.cur_state = next_state
                self.cur_state.enter(self.target, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.target)


class Target:
    def __init__(self, p, gun):
        load_target(self)
        self.p = p
        self.gun = gun
        self.dis, self.recoil = 0, 0
        self.reduce_delay = 0

        self.state_machine = StateMachineTarget(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
