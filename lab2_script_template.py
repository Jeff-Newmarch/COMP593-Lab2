def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Jeffrey Newmarch',
        'student_Id': '10264299',
        'pizza_toppings': [
            'Pepperoni',
            'Sausage',
            'Bacon'
        ],
        'movies': [
            {
                'title': 'Grown Ups',
                'genre': 'Comedy'
            },
            {    
                'title': 'Die Hard',
                'genre': 'Action'
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    
    about_me['movies'].insert(1, {'title': 'Jurassic Park','genre': 'Sci-fi'})


    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('Ham', 'Onion' ))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(movie_list)
    pass



# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f"My name is {about_me['full_name'].title()}, but you can call me Sir {about_me['full_name']}.")
    print(f"My student ID is {about_me['student_Id']}.")
    
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)

    for i,p in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = p.lower()

    about_me['pizza_toppings'].sort()
    pass
    

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favourite pizza toppings are:')
    for p in about_me['pizza_toppings']:
        print(f'-{p}')
    

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print('\nI like to watch ', end='')
    for i,m in enumerate(about_me['movies']):
        if i < len(about_me['movies']) - 1:
            print(f'{m["genre"]}, ', end= '')
        else:
            print(f'and {m["genre"]} movies.')

    
    

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print(f'\nSome of my favourite movies are ', end='')
    movie_list = []
    for m in movie_list['movies']:
        movie_list.append(m["title"].upper())
    
    
    
if __name__ == '__main__':
    main()