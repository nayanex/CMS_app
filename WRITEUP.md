# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

Azure App Service supports Python and I can take advantage of the Continuous deployment model using
GitHub Actions and Deployment Center on Azure portal. I don't need to set up a Docker file, for
example, to install my dependencies and run my project in a remote machine.

Also, we are working on a lightweight web application, there are low chances that this
application will reach the size limit for App Services (maximum of 14GB of memory and 4 vCPU
cores  per instance). Our application currently does not need to manipulate huge quantity of data
, doesn't need to be super fast... We are fine, LOL.

Additionally, App Services cost less than VMs do and currently we don't have the preoccupation to
scale our application quickly.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in
the last section.* 

If I were to launch this web app in production, and it had a high adoption by users, then the
situation would change, I might start having concerns about scalability and/or processing power
. These changes in demand might require vertical scaling provided by VMs.
 
Also, if I need to use something kind of different technology or language not provided by App
 Service, I would need to work on installation of custom images.

Also, if my app starts to require more in terms of hardware, such as a more than 14GB of memory
and 4 vCPU cores persistence, I would need to switch to VMs.

Also, if we were very concerned about sensitive information, we might prefer to use dedicated
servers