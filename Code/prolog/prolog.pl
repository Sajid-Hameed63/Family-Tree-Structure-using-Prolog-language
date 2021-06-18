%Mianbiwi logic

mianbiwi(choteKhan, chotiRani).
mianbiwi(barreKhan, barriRani).
mianbiwi(salim, kausar).
mianbiwi(nadir, nahid).
mianbiwi(asad, sumra).
mianbiwi(rizwan, sanam).

%Gins Logic
%mard
gins(mard,chotekhan).
gins(mard,barrekhan).
gins(mard,salim).
gins(mard,nadir).
gins(mard,asad).
gins(mard,rizwan).
gins(mard,burhan).
gins(mard,rashid).
gins(mard,akram).

%aurats
gins(aurat,chotirani).
gins(aurat,barrirani).
gins(aurat,kausar).
gins(aurat,nahid).
gins(aurat,sumra).
gins(aurat,sanam).
gins(aurat,salima).
gins(aurat,rabia).



%Parents Logic
parents(chotekhan,kausar).
parents(chotekhan,nadir).
parents(chotekhan,asad).
parents(chotirani,kauser).
parents(chotirani,nadir).
parents(chotirani,asad).
parents(barrekhan,nahid).
parents(barrekhan,sumra).
parents(barrirani,nahid).
parents(barrirani,sumra).
parents(salim,rizwan).
parents(kauser,rizwan).
parents(nadir,burhan).
parents(nadir,rashid).
parents(nadir,akram).
parents(nahid,burhan).
parents(nahid,rashid).
parents(nahid,akram).
parents(asad,salima).
parents(asad,sanam).
parents(sumra,salima).
parents(sumra,sanam).
parents(rizwan,rabia).
parents(sanam,rabia).

%baap rule
baap(X,Y):- parents(X,Y), gins(mard,X).

%maa rule
maa(X,Y) :- parents(X,Y), gins(aurat,X).

%beta rule
beta(X,Y):- parents(Y,X), gins(mard,X).

%beti rule
beti(X,Y):- parents(Y,X), gins(aurat,X).

%dada rule
dada(X,Y):- parents(X,Z), parents(Z,Y),gins(mard,Z),gins(mard,X).

%dadi rule
dadi(X,Y):- parents(X,Z), parents(Z,Y),gins(mard,Z),gins(aurat,X).

%nana rule
nana(X,Y):- parents(X,Z), parents(Z,Y),gins(aurat,Z),gins(mard,X).

%nana rule
nani(X,Y):- parents(X,Z), parents(Z,Y),gins(aurat,Z),gins(aurat,X).

%sala rule
sala(X,Y):- mianbiwi(Y,Z),parents(B,Z),gins(mard,B),beta(X,B),gins(mard,X).

%sali rule
sali(X,Y):- mianbiwi(Y,Z),parents(B,Z),gins(mard,B),beti(X,B),not(mianbiwi(Y,X)),gins(aurat,X).

%bahu rule
bahu(X,Y):- parents(Y,Z),gins(mard,Z),mianbiwi(Z,X).

%damaat rule
damaat(X,Y):- parents(Y,Z), gins(aurat,Z), mianbivi(X,Z).

%pota rule
pota(X,Y):- parents(Y,Z),gins(mard,Z),parents(Z,X),gins(mard,X).

%poti rule
poti(X,Y):- parents(Y,Z),gins(mard,Z),parents(Z,X),gins(aurat,X).

%nawasa rule
nawasa(X,Y):- parents(Y,Z),gins(aurat,Z),parents(Z,X),gins(mard,X).

%nawasi rule
nawasi(X,Y):- parents(Y,Z),gins(aurat,Z),parents(Z,X),gins(aurat,X).

%sussar rule
sassur(X,Y):- mianbiwi(Y,Z),parents(X,Z),gins(mard,X).
sassur(X,Y):- mianbiwi(Z,Y),parents(X,Z),gins(mard,X).

%chachataya rule
chachataya(X,Y):- pota(Y,D),gins(mard,D),beta(X,D),not(baap(X,Y)),gins(mard,X).

%khala rule
khala(X,Y):- nawasa(Y,D),gins(aurat,D),beti(X,D),not(maa(X,Y)),gins(aurat,X).
khala(X,Y):- nawasi(Y,D),gins(aurat,D),beti(X,D),not(maa(X,Y)),gins(aurat,X).

%baapdada rule
baapdada(X,Y) :- parents(X,Y),gins(mard,X).
baapdada(X,Y) :- parents(X,Z),gins(mard,X),baapdada(Z,Y).


%behan
behan(X,Y):- gins(aurat,X),parents(Z,X) ,parents(Z,Y), Y\=X.

%bhai
bhai(X,Y):- gins(mard,X), parents(Z,X), parents(Z,Y), Y\=X.

