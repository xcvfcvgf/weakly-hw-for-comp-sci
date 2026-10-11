France = [11,11,12]
Britain_and_N_Ireland= [9,17,19]
China = [38,27,23 ]
Russia = [24,26,32]
South_Korea = [13,8,7]
Australia = [7,16,12]
Germany = [11,19,14] 
United_States = [46,29,29]
Hungary = [8,4,5]
Italy = [8,9,11 ]

countries = [France, Britain_and_N_Ireland, China, Russia, South_Korea, Australia, Germany, United_States, Hungary, Italy]

names = ["France", "Britain_and_N_Ireland", "China", "Russia","South_Korea", "Australia", "Germany", "United_States","Hungary", "Italy"]

# let's srepresent the countries with the amount of gold medals they have

for i in range(0, len(countries)):
    countries[i] = names[i], countries[i][0]

# now let's sort the countries

def sorting_countries_selection_sort (countries):

    n = len(countries)

    for i in range(0,n-1):
        max_value = i
        
        for j in range(i+1, len(countries)):
            if countries[j][1] > countries[max_value][1]:
                max_value = j

        if max_value != i:
            c = countries[i]
            countries[i] = countries[max_value]
            countries[max_value] = c

    return countries






print ("List of countries from best to worst", sorting_countries_selection_sort (countries))
