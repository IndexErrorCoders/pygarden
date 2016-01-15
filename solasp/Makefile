#HEURISTIC=frumpy
#HEURISTIC=auto
#HEURISTIC=frumpy
#HEURISTIC=jumpy
#HEURISTIC=tweety
#HEURISTIC=handy
HEURISTIC=crafty
#HEURISTIC=trendy
#HEURISTIC=many

NB_CPU=4
COST_ENEMY=10
COST_FRIEND=-1
COSTS=-c score_enemy=$(COST_ENEMY) -c score_friend=$(COST_FRIEND)

OPTIONS=-n 0 --configuration=$(HEURISTIC) --parallel-mode=$(NB_CPU),compete $(COSTS)

p:
	./clingo data.lp integrity.lp $(OPTIONS)


g:
	python3 relations2asp.py

