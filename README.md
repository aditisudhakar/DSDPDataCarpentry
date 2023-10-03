# DSDPDataCarpentry
This repo has the code to solve the range problem related to the LIDA 23 DSDP Data Carpentry Workshop


## Scenarios

### Scenario 1 - overlap at a point
- Parameters: [[-3, 0], [-0., 4.5]]
- Result: [0, 0]
### Scenario 2 - no overlap
- Parameters: [[-3, -1], [-0., 4.5]]
- Result: "No overlap"

### Scenario 3 - insufficient parameters
- Parameters: [-3, 2]
- Result: "Enter at least two ranges"

### Scenario 4 - equal ranges
- Parameters: [[-3, 2],[-3, 2]]
- Result: "[-3, 2]"

### Scenario 5 - range example
- Parameters: [[-3, 5],[0, 4.5], [-1, 2]]
- Result: "[0, 2]"
