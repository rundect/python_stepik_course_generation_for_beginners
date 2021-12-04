def info_kwargs(**kwargs):
    for i in sorted(kwargs):
        print(f'{i}: {kwargs[i]}')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')