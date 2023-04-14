import yaml

# Load the first YAML code
yaml1 = """
---
- regle:
    name: "regle1"
    description: "premiere regle nsx - correction de la description"
    id: 1
    services:
      - name: http
        type: tcp
        ports:
          - 8080
          - 80
          - 8081
"""

# Load the second YAML code
yaml2 = """
---
nsx:
  fqdn: "nsx.estlab.ngq.extra"
  username: "admin"
  password: "password"

- regle:
    name: "regle1"
    description: "premiere regle nsx"
    id: 1
    source:
      groupe: serveurs-client-001
    destination:
      - serveur-bd-client001
      - serveur-web-client001
    services:
      - name: http
        type: tcp
        ports:
          - 8080
          - 80
      - name: https
        type: tcp
        ports:
          - 443
          - 8443

- regle:
    name: "regle2"
    description: "deuxieme regle nsx"
    id: 2
    source:
      groupe: serveurs-client-001
    destination:
      - internet
    services:
      - name: https
        type: tcp
        ports:
          - 443
          - 8443
"""

# Convert the YAML code into Python objects
data1 = yaml.load(yaml1, Loader=yaml.FullLoader)
data2 = yaml.load(yaml2, Loader=yaml.FullLoader)

# Merge the two Python objects
merged_data = data2 + data1

# Convert the merged Python object back to YAML
merged_yaml = yaml.dump(merged_data)

# Print the merged YAML code
print(merged_yaml)