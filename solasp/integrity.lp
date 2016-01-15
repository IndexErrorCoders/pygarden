%%%%
% ASP file for solving a combinatorial problem about plants (here, taxons)
%  and their placement in a garden.
% Outputs are limited in order to ensure human readability.
%
% Input:
%  enemy(T,S): T and S are in conflict
%  friend(T,S): T and S are in symbiosis
%  X(T): T is of type X, with X in {fruits, legumes, fleurs, aromates, cereales}
%
% Output:
%  score(S): lower S is better ; S is the sum of relations between taxons
%  taxon(X,Y,T): taxon T is placed in garden at position (X;Y)
%
% Note that the computed score is minimized, not mazimized. This is du to the
%  well-knowed preference of the used tool (Potassco labs' clingo implementation)
%  that optimize more easily a minimization than a maximization.
%%%%

#const score_enemy=10.
#const score_friend=-1.

% universe is 2D, with coordinates specified by coord/1 atom.
coord(1..10).
coords(X,Y):- coord(X) ; coord(Y).

% a taxon is any of the existing taxon
taxon(X):- fruits(X).
taxon(X):- legumes(X).
taxon(X):- fleurs(X).
taxon(X):- aromates(X).
taxon(X):- cereales(X).

% don't consider orientation of enemy and friend atoms
enemy(X,Y):- enemy(Y,X).
friend(X,Y):- friend(Y,X).

% there is one (and only one) taxon at each coords
1 { taxon(X,Y,T): taxon(T) } 1:- coords(X,Y).

% here is some already placed taxons
%taxon(1,1,"ail").
%taxon(1,2,"choux").
%taxon(2,1,"choux").
%taxon(2,2,"thym").

% define the moore neighbors of any place in the universe
neighbors((X,Y),(X+1,Y+1)):- coords(X,Y).
neighbors((X,Y),(X+0,Y+1)):- coords(X,Y).
neighbors((X,Y),(X-1,Y+1)):- coords(X,Y).
neighbors((X,Y),(X+1,Y+0)):- coords(X,Y).
neighbors((X,Y),(X-1,Y+0)):- coords(X,Y).
neighbors((X,Y),(X+1,Y-1)):- coords(X,Y).
neighbors((X,Y),(X+0,Y-1)):- coords(X,Y).
neighbors((X,Y),(X-1,Y-1)):- coords(X,Y).

% score for all neighbors: score_friend for any friend neighbor, score_enemy for any enemy neighbor
neighbor_score((X,Y),(I,J),score_enemy):- neighbors((X,Y),(I,J)) ; taxon(X,Y,T) ; taxon(I,J,N) ; enemy(T,N).
neighbor_score((X,Y),(I,J),score_friend):- neighbors((X,Y),(I,J)) ; taxon(X,Y,T) ; taxon(I,J,N) ; friend(T,N).
neighbor_score((X,Y),(I,J),0):- neighbors((X,Y),(I,J)) ; taxon(X,Y,T) ; taxon(I,J,N) ; not enemy(T,N) ; not friend(T,N).

% total score is the sum of all scores
score(Final):- Final=#sum{S,X,Y,I,J:neighbor_score((X,Y),(I,J),S)}.

% just for user: count relations
counter(enemy, N/2):- N=#count{1,X,Y,I,J:neighbor_score((X,Y),(I,J),score_enemy)}.
counter(friend, N/2):- N=#count{1,X,Y,I,J:neighbor_score((X,Y),(I,J),score_friend)}.

% maximize the total score
#minimize{S:score(S)}.

#show.
#show taxon/3.
#show score/1.
#show counter/2.
%% Debugging shows:
%#show neighbor_score/3.
%#show neighbors/2.
