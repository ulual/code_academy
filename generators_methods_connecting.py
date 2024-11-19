def cs_courses():
    yield 'Computer Science'
    yield 'Artificial Intelligence'

def art_courses():
    yield 'Intro to Art'
    yield 'Selecting Mediums'

def all_courses():
    yield from cs_courses()
    yield from art_courses()

combined_generator = all_courses()

print(next(combined_generator))
print(next(combined_generator))
print(next(combined_generator))
print(next(combined_generator))
