from prolog import prolog_query, prolog
import random

prolog.consult('guesswho.pl')


def update_properties(props, current_properties, has_prop):
    out = []

    if has_prop:
        for prop in props:           
            for current_property in current_properties:       
                if current_property in prop:
                    out.append(prop)
                    break
    else:
        for prop in props: 
            has_any = False   
            for current_property in current_properties:            
                if current_property in prop:
                    has_any = True
                    break 
            if not has_any:
                out.append(prop)
    
    return out

def select_propertie(dist, props):

    curr_sum = 0

    keep_finding = True

    curr_props = []

    max_leng = len(props) // 2

    while keep_finding:
        keys = list(dist.keys())

        random.shuffle(keys)

        dist = dict([(key, dist[key]) for key in keys])

        values = list(dist.values())
        curr_count = max(values)

        if curr_count + curr_sum <= max_leng:
            prop = max(dist, key=dist.get)
            curr_props.append(prop)
            curr_sum += curr_count        
            props = update_properties(props, [prop], False)
            dist = sum_properties(props)
            continue

        diff = max_leng - curr_sum

        found_some = False

        for i in range(diff, -1, -1):
            if i in values:
                found_some = True
                index = values.index(i)
                prop = keys[index]
                curr_props.append(prop)
                curr_sum += i  
                props = update_properties(props, [prop], False)
                dist = sum_properties(props)
                if i == diff:
                    keep_finding = False
                break
        
        if not found_some:
            keep_finding = False

    return curr_props

def select_propertie_old(dist, props):
    keys =  list(dist.keys())
    random.shuffle(keys)

    dist = dict([(key, dist[key]) for key in keys])

    if len(dist) > 3 and len(props) > 2:
        curr_props = [max(dist, key=dist.get), min(dist, key=dist.get)]
    else:
        curr_props = [min(dist, key=dist.get)]

    return curr_props

def sum_properties(properties):
    dict = {}

    properties = [x for xs in properties for x in xs]

    for property in properties:
        if property in dict:
            dict[property] += 1
        else:
            dict[property] = 1
    
    return dict

def get_character(seen_props):   
    return prolog_query(f"character(X, [{','.join(seen_props)}])", "X")[0]

CHARACTERS = prolog_query("character(X, _)", "X")


def find_character(choosen_character, auto_mode = True, select_propertie_func = select_propertie):
    SEEN_PROPS = []

    properties = prolog_query("character(_, X)", "X")
    
    current_properties = None

    has_property = False

    question_count = 0

    while True:
        question_count += 1

        print(f"### Question {question_count}")

        print(f"{len(properties)} possible character{'s' if len(properties) > 1 else ''}")

        # check char
        if len(properties) == 1:
            char = get_character(properties[0])
            print(f"character is {char}")
            print()
            return (char, question_count)

        # select prop
        propertie_distr = sum_properties(properties)

        for seen in SEEN_PROPS:
            if seen in propertie_distr:
                del propertie_distr[seen]  

        if len(propertie_distr) == 0:   
            SEEN_PROPS = []     
            propertie_distr = sum_properties(properties)

        current_properties = select_propertie_func(propertie_distr, properties)

        final_has_prop_or = False

        if auto_mode:

            for current_property in current_properties:
                SEEN_PROPS.append(current_property)    
                # ask if char prop
                has_property = bool(prolog_query(f"character_has_property({choosen_character}, {current_property})"))
                if has_property:
                    final_has_prop_or = True

            has_property = final_has_prop_or
        else:

            in_val = -1
            while in_val != "y" and in_val != "n":
                try:
                    in_val = input(f"your character has: {' or '.join(current_properties)} y/n?: ").lower()
                except:
                    print("Invalid value")
                    
            if(in_val == "y"):
                has_property = True
            elif(in_val == "n"):
                has_property = False
            else:
                raise Exception(">:(")

           # update props
        properties = update_properties(properties, current_properties, has_property)

        print(f"{', '.join(current_properties)}{' not' if not has_property else ''} found on character")
        print()
        

def main():
    in_val = -1

    while in_val < 0 or in_val > 1:
        try:
            in_val = int(input("Choose mode {0}Versus or {1}Auto: "))
        except:
            print("Invalid value")

    choosen_character = ""

    if in_val == 1:
        print(', '.join(CHARACTERS))
        choosen_character = input("Choose a character or Enter to select random: ")
        if choosen_character not in CHARACTERS:
            choosen_character = random.choice(CHARACTERS)
            print(f"Choosen character is {choosen_character}")

    find_character(choosen_character, bool(in_val))

main()