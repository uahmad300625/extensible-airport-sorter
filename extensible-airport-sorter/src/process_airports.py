from dataclasses import replace

def process_airports(airports, sort_criteria=lambda airport: ()):
  def capitalize_airport_name(airport):
    return replace(airport, name = airport.name.upper())

  return sorted(map(capitalize_airport_name, airports), key=sort_criteria)
