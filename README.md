# asioncio-event-to-sql
A service which listens to events and writes them asynchronously to a SQL database 



# Story

I did a lot of work as a ETL developer (https://en.wikipedia.org/wiki/Extract,_transform,_load), most of the ETL tools used there are modeling tools (Pentaho, Talend, Informatika), which are in my opinion nice if you want to do one-off jobs. You can use schema detection, generate queries, set different environments (like local - for developing, staging or labs for testing, and probably production). Most likely - if you are working in larger companies (like I used did), you don't even want to give all developers access to live, because of sensitive data, performance risk or similar.

ETL is used for various reasons, basically its a simple (and stupid) way to quickly work down the technical dept and integrate systems; Creating Reports, filling statistics, calculate a few KPI's or even more your data through the pipline. (I later describe one system I designed which typically emerges in big and hypergrowth companies.)

# Proper integration takes time and efford
Companies like startusp are rapidly growing, things are changing fast, people have introduces a new Sales system, a different Email provider, Reports are generated in various places with different custom queries. You need to takle all those problems.

Proper integration takes some time; you have to adapt the workflow of the different systems. That shouldn't be a problem; but often the processes are already fixed, the systems are already up and running. People are manually copying ID's or any kind of references into the next systems. (Oh the list goes on and on).
If it's not a tech-driven company, it's very likely that this has already happened. Honestly: How likely could it be that while new systems were bought, the tech people were consulted. When the sales system was introduces, probably the few developers were doing overtime, just shooting out the first product, adding features rather than caring for the overall "ecosystem", including getting involved in the sales workflow and when to trigger an event/call. (I highly assume, that if you were lucky working in a tech driven company that this sound absurd, but I guarantee, it isn't.)

# Why is ETL used
If I should boil it down - I guess it's: speed through a common demominator.
All the systems might look completly different, different language, maybe they weren't even at all supposed to have a API like a old legacy system, etc. One thing they all have in common: They store data.

# Explain why ETL is incredibly "fast"
- Common denominator SQL (CSV; XML ...)

# Typical workflow
- Get access to the system
- Reverse engineer data model
- Write query
- load data

# Explain the basic first integration problems 
- Data Quality aspects 
- Also political issues
- To less influence as a single developer
- Backend developers just seeing the backend (and frontend) as the system and not the complete eco system


# What to do to make the whole process incrementally?
- optimize DB "layout": Introduce timestamps (if not there), set indexes
- setup "pointer DB" (what have I already transmitted)
- adapt load size (how often do I need to do it? Is the process time critical? How much can I stress the system? Am I working on live or a hot slave? Does it break the replica sync?) 

# Scale the data pipeline
- Avoid source performance problems by loading tables individually
- [Advanced: Referancial integrity?]
# Normalizing model
# BI Part
## Creating analytics optimized model (DWH - Star, Snowflake)
## Targeting audience throug data marts
## Serving audience (list of tools like: Tableau, Gooddata, etc; pros & cons for self serving)


