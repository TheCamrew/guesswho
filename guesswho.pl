character(bill, [ginger_hair, bald, rosy_cheeks, beard]).
character(philip, [black_hair, rosy_cheeks, beard]).
character(david, [blonde_hair, beard]).
character(richard, [moustache, bald, beard]).
character(robert, [blue_eyes, big_nose, rosy_cheeks]).
character(eric, [hat, blonde_hair]).
character(george, [hat, white_hair]).
character(bernard, [hat, big_nose]).
character(paul, [glasses, white_hair]).
character(alex, [moustache, black_hair]).
character(max, [moustache, black_hair, big_nose]).
character(charles, [moustache, blonde_hair]).
character(peter, [blue_eyes, white_hair, big_nose]).
character(alfred, [moustache, blue_eyes, ginger_hair]).
character(frans, [ginger_hair]).
character(herman, [ginger_hair, bald, big_nose]).
character(joe, [glasses, blonde_hair]).
character(tom, [glasses, blue_eyes, bald, black_hair]).
character(sam, [glasses, bald, white_hair]).
character(claire, [glasses, hat, ginger_hair, woman]).
character(maria, [hat, woman]).
character(anita, [blue_eyes, woman, blonde_hair, rosy_cheeks]).
character(susan, [woman, white_hair, rosy_cheeks]).
character(anne, [woman, black_hair]).

character_property(C, P) :-
    character(C, Props), member(P, Props).