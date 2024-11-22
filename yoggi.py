class Voter:
    def _init_(self, voter_id, name, aadhaar_id):
        self.voter_id = voter_id
        self.name = name
        self.aadhaar_id = aadhaar_id

class Candidate:
    def _init_(self, candidate_id, name, party):
        self.candidate_id = candidate_id
        self.name = name
        self.party = party

class VotingMachine:
    def _init_(self):
        self.voters = []
        self.candidates = []
        self.votes = {}

    def register_voter(self, voter):
        self.voters.append(voter)

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def cast_vote(self, voter_id, candidate_id):
        if voter_id not in self.votes:
            self.votes[voter_id] = candidate_id
            print(f"Vote casted for candidate {candidate_id}")
        else:
            print("Voter has already cast their vote.")

    def tally_votes(self):
        results = {}
        for vote in self.votes.values():
            if vote in results:
                results[vote] += 1
            else:
                results[vote] = 1
        return results
