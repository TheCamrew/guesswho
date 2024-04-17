character(bill, [ginger_hair, bald, rosy_cheeks, beard]).
character(philip, [black_hair, rosy_cheeks, beard]).
character(david, [blonde_hair, beard]).
character(richard, [moustache, bald, beard]).
character(robert, [blue_eyes, big_nose, rosy_cheeks]).
character(eric, [has_hat, blonde_hair]).
character(george, [has_hat, white_hair]).
character(bernard, [has_hat, big_nose]).
character(paul, [has_glasses, white_hair]).
character(alex, [moustache, black_hair]).
character(max, [moustache, black_hair, big_nose]).
character(charles, [moustache, blonde_hair]).
character(peter, [blue_eyes, white_hair, big_nose]).
character(alfred, [moustache, blue_eyes, ginger_hair]).
character(frans, [ginger_hair]).
character(herman, [ginger_hair, bald, big_nose]).
character(joe, [has_glasses, blonde_hair]).
character(tom, [has_glasses, blue_eyes, bald, black_hair]).
character(sam, [has_glasses, bald, white_hair]).
character(claire, [has_glasses, has_hat, ginger_hair, woman]).
character(maria, [has_hat, woman]).
character(anita, [blue_eyes, woman, blonde_hair, rosy_cheeks]).
character(susan, [woman, white_hair, rosy_cheeks]).
character(anne, [woman, black_hair]).

character_has_property(C, P) :-
    character(C, Props), member(P, Props).