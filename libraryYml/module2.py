import yaml

# Define the resources to merge
resource1 = """
Cloud_vSphere_Machine_1:
  type: Cloud.vSphere.Machine
  properties:
    image: ubtuntu20.1
    name: "webapp01"
    cpu_count: 4
"""

resource2 = """
Cloud_vSphere_Machine_1:
  type: Cloud.vSphere.Machine
  properties:
    image: template-rhel8.00_v2
    flavor: '$${input.size}'
    name: $${input.hostname}
    constraints:
      - tag: $${input.region}
    networks:
      - network: $${resource.Cloud_NSX_Network_1.id}
    attachedDisks: []
Cloud_NSX_Network_1:
  type: Cloud.NSX.Network
  properties:
    networkType: existing
    constraints:
      - tag: $${input.environnement}
"""

# Load the YAML resources
resource1_dict = yaml.load(resource1, Loader=yaml.FullLoader)
resource2_dict = yaml.load(resource2, Loader=yaml.FullLoader)

# Merge the resources
merged_dict = {**resource1_dict, **resource2_dict}

# Convert the merged resources to YAML
merged_yaml = yaml.dump(merged_dict)

# Print the result
print(merged_yaml)
