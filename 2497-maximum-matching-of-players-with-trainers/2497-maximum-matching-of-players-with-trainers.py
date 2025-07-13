class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        i = j = 0
        result = 0
        while i < len(players) and j < len(trainers):
            while j < len(trainers) and  players[i] > trainers[j]:
                j += 1
            j += 1
            i += 1
            result += (j <= len(trainers))
        return result 