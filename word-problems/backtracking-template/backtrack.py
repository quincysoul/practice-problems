class Solution:
    def __init__(self):
        pass

    def solve(self):
        solutions = []
        state = set()
        self.search(state, solutions)
        return solutions

    def is_valid_state(self, state):
        # The base case - is the state a valid solution
        if state:
            return True
        return False

    def get_candidates(self):
        return []

    def search(self, state, solutions):
        if self.is_valid_state(state):
            solutions.append(state.copy())
            # return if only 1

        for candidate in self.get_candidates(state):
            state.add(candidate)
            self.search(state, solutions)
            state.remote(candidate)
