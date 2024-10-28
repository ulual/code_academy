instrument_familes = {
  'Strings': ['Guitar', 'Banjo', 'Sitar'],
  'Percussion': ['Conga', 'Cymbal', 'Cajon'],
  'woodwinds': ['Flute', 'Oboe', 'Clarinet']
}

def print_instrument_families():
  for family in ['Strings', 'Percussion', 'woodwinds']:
    try:
      print('Some instruments in the ' + family + 'family are: ' + ', '.join(instrument_familes[family]))
    except KeyError:
      print("Family not found.")

print_instrument_families()
