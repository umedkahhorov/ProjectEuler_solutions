# Open the file in read mode
with open('../data/0022_names.txt', 'r') as file:
    # Read the content and remove leading/trailing whitespace
    names_data = file.read().strip()
# Split the content based on commas and remove surrounding quotes from each name
names_list = [name.strip('"') for name in names_data.split(',')]

def compute():
    ans = sum((i+1)*(ord(c) - ord('A') + 1)
              for (i, name) in enumerate(sorted(names_list))
              for c in name)
    return ans

if __name__ == "__main__":
    print (compute())

