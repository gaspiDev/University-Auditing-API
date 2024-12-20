# University Auditing API
#### This API was developed with intentions of give legitmacy to all public and private universities of Argentina. 
---
### Introduction:
###### Here it's a Mermaid Entities Diagram to get you to know the domain of the API
![GitHub Logo](.\assets\mermaid-erd-ua.png)

---
#### Entities behaviors to be consider:
- **USER:** represents universitie's dean.
 USER are the only one to be authenticated an authorized (there are endpoints unprocted for other client/servers to consume).
 USER can create and delete one UNIVERSITY at a time.
 USER can deleted or update only their related UNIVERSITY.
 USER is the only one to retrieve his data (achieved with JWT).
- **UNIVERSITY:** represents subject to be audited.
UNIVERSITY records are available to all consumers.
UNIVERSITY crud endpoints are protected with USER auth.
UNIVERSITY has all the business logic endpoints to satisfy the API purpose.
- **EXPENSE:** represents each transaction of universities registered by deans.
EXPENSE records are available to all consumers.
EXPENSE crud endpoints are protected with USER auth.
- **BUDGET:** represents the rule that an university must follow.
BUDGET crud endpoints are unporteced.
*next feature:* BUDGET crud endpoints protected with the aut of new entity PARTY (representing the politicalparty taht approved the anual budget)
---
### Posible integration with another API:
> #### Our API would call a public government API periodically to get the most recent anual budgets with better details like which political party approved it, how many negative votes got, and more.
![GitHub Logo](.\assets\mermaid-sd-ua.png)
