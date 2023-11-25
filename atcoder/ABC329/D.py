# def func(N, M, votes):
#     vote_count = [0] * (N + 1)
#     winners = []
    
#     for i in range(M):
#         vote_count[votes[i]] += 1
#         max_votes = max(vote_count)
#         winner = vote_count.index(max_votes)
#         winners.append(winner)

#     return winners

# N, M = map(int, input().split())
# votes = list(map(int, input().split()))

# res = func(N, M, votes)

# for winner in res:
#     print(winner)  


def func(N, M, votes):
    vote_count = [0] * (N + 1)
    current_max_votes = 0
    current_winner = 1  
    
    for vote in votes:
        vote_count[vote] += 1

        if vote_count[vote] > current_max_votes or (vote_count[vote] == current_max_votes and vote < current_winner):
            current_max_votes = vote_count[vote]
            current_winner = vote

        print(current_winner)

N, M = map(int, input().split())
votes = list(map(int, input().split()))

func(N, M, votes)


