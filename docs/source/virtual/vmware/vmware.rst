VMware
==========================

Summary 
--------------------------

VMware, Inc. is a publicly traded software company listed 
on the NYSE under stock ticker VMW. Dell Technologies is 
a majority share holder. VMware provides cloud computing 
and virtualization software and services. It was one of 
the first commercially successful companies to virtualize 
the x86 architecture.

Getting Started
--------------------------

Here is an example of some API documentation.

Project list
++++++++++++

.. http:get::  /api/v2/project/

    Retrieve a list of all Read the Docs projects.

    **Example request**:

    .. code:: bash 

       $ curl https://readthedocs.org/api/v2/project/?slug=pip

    **Example response**:

    .. sourcecode:: js

        {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [PROJECTS]
        }

    :>json string next: URI for next set of Projects.
    :>json string previous: URI for previous set of Projects.
    :>json integer count: Total number of Projects.
    :>json array results: Array of ``Project`` objects.

    :query string slug: Narrow the results by matching the exact project slug

Project details
+++++++++++++++

.. http:get::  /api/v2/project/(int:id)/

    Retrieve details of a single project.

    .. sourcecode:: js

        {
            "id": 6,
            "name": "Pip",
            "slug": "pip",
            "programming_language": "py",
            "default_version": "stable",
            "default_branch": "master",
            "repo_type": "git",
            "repo": "https://github.com/pypa/pip",
            "description": "Pip Installs Packages.",
            "language": "en",
            "documentation_type": "sphinx_htmldir",
            "canonical_url": "http://pip.pypa.io/en/stable/",
            "users": [USERS]
        }


    :>json integer id: The ID of the project
    :>json string name: The name of the project.
    :>json string slug: The project slug (used in the URL).
    :>json string programming_language: The programming language of the project (eg. "py", "js")
    :>json string default_version: The default version of the project (eg. "latest", "stable", "v3")
    :>json string default_branch: The default version control branch
    :>json string repo_type: Version control repository of the project
    :>json string repo: The repository URL for the project
    :>json string description: An RST description of the project
    :>json string language: The language code of this project
    :>json string documentation_type: An RST description of the project
    :>json string canonical_url: The canonical URL of the default docs
    :>json array users: Array of ``User`` IDs who are maintainers of the project.

    :statuscode 200: no error
    :statuscode 404: There is no ``Project`` with this ID

Project versions
++++++++++++++++

.. http:get::  /api/v2/project/(int:id)/active_versions/

    Retrieve a list of active versions (eg. "latest", "stable", "v1.x") for a single project.

    .. sourcecode:: js

        {
            "versions": [VERSION, VERSION, ...]
        }

    :>json array versions: Version objects for the given ``Project``

References
--------------------------
