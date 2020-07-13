Functional Roles
========================

Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data, such as text or binary data.

Blob storage is ideal for:


* Serving images or documents directly to a browser
* Storing files for distributed access
* Streaming video and audio
* Storing data for backup and restore, disaster recovery, and archiving
* Storing data for analysis by an on-premises or Azure-hosted service

`Source code <https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/azure/storage/blob>`_ | `Package (PyPI) <https://pypi.org/project/azure-storage-blob/>`_ | `API reference documentation <https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob>`_ | `Product documentation <https://docs.microsoft.com/azure/storage/>`_ | `Samples <https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob/samples>`_

Getting started
---------------

Prerequisites
^^^^^^^^^^^^^


* Python 2.7, or 3.5 or later is required to use this package.
* You must have an `Azure subscription <https://azure.microsoft.com/free/>`_ and an
  `Azure storage account <https://docs.microsoft.com/azure/storage/common/storage-account-overview>`_ to use this package.

Install the package
^^^^^^^^^^^^^^^^^^^

Install the Azure Storage Blobs client library for Python with `pip <https://pypi.org/project/pip/>`_\ :

.. code-block:: bash

   pip install azure-storage-blob --pre

Create a storage account
^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to create a new storage account, you can use the
`Azure Portal <https://docs.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-portal>`_\ ,
`Azure PowerShell <https://docs.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-powershell>`_\ ,
or `Azure CLI <https://docs.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-cli>`_\ :

.. code-block:: bash

   # Create a new resource group to hold the storage account -
   # if using an existing resource group, skip this step
   az group create --name my-resource-group --location westus2

   # Create the storage account
   az storage account create -n my-storage-account-name -g my-resource-group

Create the client
^^^^^^^^^^^^^^^^^

The Azure Storage Blobs client library for Python allows you to interact with three types of resources: the storage
account itself, blob storage containers, and blobs. Interaction with these resources starts with an instance of a
`client <#clients>`_. To create a client object, you will need the storage account's blob service endpoint URL and a
credential that allows you to access the storage account:

.. code-block:: python

   from azure.storage.blob import BlobServiceClient

   service = BlobServiceClient(account_url="https://<my-storage-account-name>.blob.core.windows.net/", credential=credential)

Looking up the endpoint URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Get the blob service endpoint for the storage account
   az storage account show -n my-storage-account-name -g my-resource-group --query "primaryEndpoints.blob"

Types of credentials
~~~~~~~~~~~~~~~~~~~~

The ``credential`` parameter may be provided in a number of different forms, depending on the type of
`authorization <https://docs.microsoft.com/en-us/azure/storage/common/storage-auth>`_ you wish to use:


#. To use a `shared access signature (SAS) token <https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview>`_\ ,
   provide the token as a string. If your account URL includes the SAS token, omit the credential parameter.
#. To use a storage account `shared access key <https://docs.microsoft.com/rest/api/storageservices/authenticate-with-shared-key/>`_\ ,
   provide the key as a string.
#. To use an `Azure Active Directory (AAD) token credential <https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad>`_\ ,
   provide an instance of the desired credential type obtained from the
   `azure-identity <https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#credentials>`_ library.
#. To use `anonymous public read access <https://docs.microsoft.com/en-us/azure/storage/blobs/storage-manage-access-to-resources>`_\ ,
   simply omit the credential parameter.

Creating the client from a connection string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on your use case and authorization method, you may prefer to initialize a client instance with a storage
connection string instead of providing the account URL and credential separately. To do this, pass the storage
connection string to the client's ``from_connection_string`` class method:

.. code-block:: python

   from azure.storage.blob import BlobServiceClient

   service = BlobServiceClient.from_connection_string(conn_str="my_connection_string")

Key concepts
------------

The following components make up the Azure Blob Service:


* The storage account itself
* A container within the storage account
* A blob within a container

The Azure Storage Blobs client library for Python allows you to interact with each of these components through the
use of a dedicated client object.


Examples
--------

The following sections provide several code snippets covering some of the most common Storage Blob tasks, including:


* `Uploading a blob <#uploading-a-blob>`_
* `Downloading a blob <#downloading-a-blob>`_
* `Enumerating blobs <#enumerating-blobs>`_

Uploading a blob
^^^^^^^^^^^^^^^^

Upload a blob to your container

.. code-block:: python

   from azure.storage.blob import BlobClient

   blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

   with open("./SampleSource.txt", "rb") as data:
       blob.upload_blob(data)

Use the async client to upload a blob

.. code-block:: python

   from azure.storage.blob.aio import BlobClient

   blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

   with open("./SampleSource.txt", "rb") as data:
       await blob.upload_blob(data)

Downloading a blob
^^^^^^^^^^^^^^^^^^

Download a blob from your container

.. code-block:: python

   from azure.storage.blob import BlobClient

   blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

   with open("./BlockDestination.txt", "wb") as my_blob:
       blob_data = blob.download_blob()
       my_blob.writelines(blob_data.content_as_bytes())

Download a blob asynchronously

.. code-block:: python

   from azure.storage.blob.aio import BlobClient

   blob = BlobClient.from_connection_string(conn_str="my_connection_string", container_name="my_container", blob_name="my_blob")

   with open("./BlockDestination.txt", "wb") as my_blob:
       stream = await blob.download_blob()
       data = await stream.content_as_bytes()
       my_blob.write(data)

Enumerating blobs
^^^^^^^^^^^^^^^^^

List the blobs in your container

.. code-block:: python

   from azure.storage.blob import ContainerClient

   container = ContainerClient.from_connection_string(conn_str="my_connection_string", container_name="my_container")

   blob_list = container.list_blobs()
   for blob in blob_list:
       print(blob.name + '\n')

List the blobs asynchronously

.. code-block:: python

   from azure.storage.blob.aio import ContainerClient

   container = ContainerClient.from_connection_string(conn_str="my_connection_string", container_name="my_container")

   blob_list = [] 
   async for blob in container.list_blobs():
       blob_list.append(blob)
   print(blob_list)

Troubleshooting
---------------

Storage Blob clients raise exceptions defined in `Azure Core <https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/docs/exceptions.md>`_.
All Blob service operations will throw a ``StorageErrorException`` on failure with helpful `error codes <https://docs.microsoft.com/rest/api/storageservices/blob-service-error-codes>`_.
