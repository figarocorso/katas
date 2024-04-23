# Plugins kata

We are contributing to the `Meerkat` application, which looks great and widely used, but latelly not many people is contributing to it.

One of the most used scripts is called `Deploy Meerkat` which first deploys the needed infrastructure in the cloud and then deploys `Meerkat` at the recently created infra.

It is really useful, but we would like to customize the infra we rely on in a way communitiy can easily contribute. So we would like to implement a plugin system to help us with that.

## First exercise

* Let's first write our first code. Let's add the needed code to deploy a load balancer (AKA print `Load Balancer deployed`)
* We do not want to deploy always the load balancer, make it conditional somehow
* We are adding some entropy to the code, how do we test that we are actually deploying the load balancer when we want?

## Second exercise

* `Meerkat` is using SQLite by default, which is OK. But we would like to be able to add a Postgres plugin (AKA print `Postgres database deployed`)
* Now we have two plugins, and maybe we could expect community to write plugins for other datastores. Let's make sure commnity life is easier when contributing with a plugins system.
* Keep tests growing.
* Recap all the implementation alternatives pros and cons.

## Third exercise

* `Meerkat` configuration is defined using a YAML file. Plugins should be able to customize some entries of that YAML file.

## Forth exercise: question

It looks like our contribution looks fine and we are starting to own the repo.

* Which testing coverage would you implement and make mandatory to every contribution?
