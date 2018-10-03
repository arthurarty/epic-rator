from user import User

class Lfa(User):

    def __init__(self):
        super().__init__()

    def add_score(self, lfa_id, bootcamper_id, score):
        score = {
            "bootcamper_id": bootcamper_id,
            "score": score,
            "lfa_id": lfa_id
        }
        self.scores.append(score)

        return score
    
    def edit_score(self, bootcamper_id, score):
        score = (score for score in self.scores if score['bootcamper_id'] == bootcamper_id)
        self.scores.update({"score": score})
        return score

    def get_scores_lfa_bootcamper(self, lfa_id):
        scores = []
        for score in scores:
            if score['lfa_id'] ==  lfa_id:
                scores.append(score)
        return scores