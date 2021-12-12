countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
print(*list(map(lambda x: f'{x[1]} is the capital of {x[0]}, population equal {x[2]} people.',
                zip(countries, capitals, population))), sep='\n')