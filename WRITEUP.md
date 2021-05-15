# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

I would choose an App Service in this situation because we are working on a lightweight web
application, there are low chances that this application will reach the size limit for App Services.

Additionally, App Services cost less than VMs do and currently we don't have the preoccupation to
scale our application quickly.


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in
the last section.* 

If I were to launch this web app in production, and it had a high adoption by users, then the
situation would change, I might start having concerns about scalability and/or processing power
. These demand changes might require vertical scaling provided by VMs.

Also, if we were very concerned about sensitive information, we might prefer to use dedicated
servers