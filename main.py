import axelrod as axl

# axl.seed(0)
players = (axl.Cooperator(), axl.Random())
match = axl.Match(players, turns=5)
results = match.play()
print("results", results)

scores = match.scores()
print("scores: ", scores)

print("final scores: ", match.final_score())

print("winner: ", match.winner())

players = [axl.Cooperator(), axl.Defector(), axl.Random(), axl.TitForTat(), axl.Grumpy(), axl.Alternator()]
tournament = axl.Tournament(players=players)
print("turns: ", tournament.turns)  # default value of turns

results = tournament.play()
print("results", results)

winners = results.ranked_names
print("winners", winners)

scores = results.scores
print("scores", scores)

for i, player in enumerate(players):
    print(f"{player.name}:", scores[i])
    print("========================================================================")

plot = axl.Plot(results)
p = plot.boxplot()
p.show()
