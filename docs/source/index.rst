.. Sphinx Demo documentation master file, created by
   sphinx-quickstart on Wed Oct 23 11:29:26 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Sphinx demo!
=======================================

.. toctree::
   :maxdepth: 3
   :caption: Infrastructure as Code:

   iac/terraform/terraform.rst
   iac/chef/chef.rst
   iac/ansible/ansible.rst

.. toctree::
   :maxdepth: 3
   :caption: Continious Integration

   cicd/gitlab/gitlab.rst
   cicd/jenkins/jenkins.rst
   cicd/circleci/circleci.rst

.. toctree::
   :maxdepth: 3
   :caption: Cloud Computing:

   cloud/aws/aws.rst
   cloud/azure/azure.rst
   cloud/gcp/gcp.rst

.. toctree::
   :maxdepth: 3
   :caption: Virtualization:

   virtual/docker/docker.rst
   virtual/vagrant/vagrant.rst
   virtual/vmware/vmware.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
