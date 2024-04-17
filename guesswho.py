from pyswip import Prolog
import random

prolog = Prolog()

prolog.consult('guesswho.pl')

def compare_prolog_db(a, b, count = 10000):
    avg = [[],[]]
    g_sum =  [{},{}]
    app_sum = {}

    for char in CHARACTERS:
        g_sum[0][char] = 0
        g_sum[1][char] = 0
        app_sum[char] = 0

    for i in range(count):

        r_char = random.choice(CHARACTERS)
        app_sum[r_char] += 1

        prolog.consult(a)
        char, question_count = find_character(r_char)
        avg[0].append(question_count)

        g_sum[0][char] += question_count

        prolog.consult(b)
        char, question_count = find_character(r_char)
        avg[1].append(question_count)

        g_sum[1][char] += question_count
        print(i)


    a = sum(avg[0]) / count
    b = sum(avg[1]) / count

    print(a)
    print(b)

    print((b) / (a))

    print(g_sum[0])
    print(g_sum[1])

    diff_avg = 0
    diff_wgt_avg = 0

    for name in g_sum[0].keys():
        diff = g_sum[1][name] - g_sum[0][name]
        print(f"{name}: {diff} {(diff) / app_sum[name]}")
        diff_avg += diff
        diff_wgt_avg += (diff) / app_sum[name]

    print(f"avg: {diff_avg / len(CHARACTERS)}")
    print(f"w_avg: {diff_wgt_avg / len(CHARACTERS)}")

def prolog_query(query, id = None):
    values = list(prolog.query(query))

    out = []
    if id is not None:
        for value in values:
            out.append(value[id])
    else:
        return values
    
    return out

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

def main():
    CHOOSEN_CHARACTER = random.choice(CHARACTERS)
    find_character(CHOOSEN_CHARACTER)

def find_character(CHOOSEN_CHARACTER):
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

        current_properties = select_propertie(propertie_distr, properties)

        final_has_prop_or = False

        for current_property in current_properties:
            SEEN_PROPS.append(current_property)    
            # ask if char prop
            has_property = bool(prolog_query(f"character_has_property({CHOOSEN_CHARACTER}, {current_property})"))
            if has_property:
                final_has_prop_or = True

        has_property = final_has_prop_or

           # update props
        properties = update_properties(properties, current_properties, has_property)

        print(f"{current_property}{' not' if not has_property else ''} found on character")
        print()
        
main()