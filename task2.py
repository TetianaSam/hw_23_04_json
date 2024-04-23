import json


class GroupAlbums:

  def __init__(self):
    self.data = {}

  def add_data(self, group, album):
    if group in self.data:
      self.data[group].append(album)
    else:
      self.data[group] = [album]

  def delete_data(self, group, album=None):
    if group in self.data:
      if album:
        if album in self.data[group]:
          self.data[group].remove(album)
        else:
          print(f"{album} not found for {group}.")
      else:
        del self.data[group]
    else:
      print(f"{group} not found.")

  def find_data(self, group):
    if group in self.data:
      return self.data[group]
    else:
      return f"{group} not found."

  def edit_data(self, group, old_album, new_album):
    if group in self.data:
      if old_album in self.data[group]:
        index = self.data[group].index(old_album)
        self.data[group][index] = new_album
      else:
        print(f"{old_album} not found for {group}.")
    else:
      print(f"{group} not found.")

  def save_data(self, filename):
    with open(filename, 'w') as file:
      json.dump(self.data, file)

  def load_data(self, filename):
    with open(filename, 'r') as file:
      self.data = json.load(file)


# Example usage:
ga = GroupAlbums()

# Adding data
ga.add_data("Metallica", "Master of Puppets")
ga.add_data("Metallica", "Ride the Lightning")
ga.add_data("Linkin Park", "Hybrid Theory")
ga.add_data("Linkin Park", "Meteora")

# Deleting data
ga.delete_data("Metallica", "Ride the Lightning")

# Finding data
print(ga.find_data("Linkin Park"))
print(ga.find_data("Nirvana"))

# Editing data
ga.edit_data("Linkin Park", "Hybrid Theory", "Minutes to Midnight")

# Saving data
ga.save_data("groups.json")

# Loading data
ga.load_data("groups.json")
