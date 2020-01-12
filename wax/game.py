from gamestate import GameState


class WaxGame:
    game_states = []

    def __init__(self, meta_data={}):
        self.game_states.append(GameState())
        self.add_meta_data(meta_data)
        
    def add_meta_data(self, meta_data):
        try:
            self.event = meta_data['event']
            self.site = meta_data['site']
            self.white = meta_data['white']
            self.black = meta_data['black']
            self.result = meta_data['result']
            self.utc_date = meta_data['utcdate']
            self.utc_time = meta_data['utctime']
            self.white_elo = meta_data['whiteelo']
            self.black_elo = meta_data['blackelo']
            self.white_rating_diff = meta_data['whiteratingdiff']
            self.black_rating_diff = meta_data['blackratingdiff']
            self.eco = meta_data['eco']
            self.opening = meta_data['opening']
            self.time_control = meta_data['timecontrol']
            self.termination = meta_data['termination']
        except KeyError:
            pass



