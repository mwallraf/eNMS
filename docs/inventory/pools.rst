============
Pools
============

Pools allow the user to create groups of objects. They can be used to filter the view, but also to target an automation task to a specific subset of devices.
A pool is defined as a combination of values (or regular expressions) for the properties of an object (in the inventory). 

If the properties of an inventory object matches **all** pool properties, the object will belong to the pool.
 
Pools can be created in :guilabel:`inventory/pool_management`.

.. image:: /_static/objects/pools/pool_creation.png
   :alt: test
   :align: center

A first example
---------------

.. image:: /_static/objects/pools/device_filtering.png
   :alt: test
   :align: center

This pool enforces the following conditions:
 * name: ``node.*`` --- this regular expression matches all devices which name starts with ``node``.
 * type: ``Router|Switch`` --- matches routers and switches (devices which type is either ``Router``, or ``Switch``.
 * vendor: ``Cisco`` --- for this property, the regular expression box is not ticked. This means the value must be exactly ``Cisco``.

In summary, all Cisco routers or switches which name starts with ``node`` will match these conditions, and they will be a member of the pool.

.. note:: All properties left with empty fields are simply ignored.

A pool of links
---------------

.. image:: /_static/objects/pools/link_filtering.png
   :alt: test
   :align: center

This pool enforces the following conditions:
 * type: ``Ethernet link`` --- matches all Ethernet links.
 * source: ``bnet6`` --- matches all links whose source is the device ``bnet6``.

In summary, all Ethernet links starting from the device ``bnet6`` will be part of the pool.

Default pools
-------------

Three pools are created by default in eNMS:
  - "All objects": a pool that matches all devices and links.
  - "Devices only": matches all devices, no link.
  - "Links only": matches all links, no device.

Filter the view with a pool
---------------------------

Pools can be used as filters for the geographical and logical views.
You can switch between pools with the drop-down list in the top-right corner of the screen (framed in red below).

.. image:: /_static/objects/pools/view_filter.png
   :alt: Apply a filter to the view
   :align: center

Use a pool as target of an automation task
------------------------------------------

Pools can also be used as targets of an automation. The second step of the scheduling process of a service is to select the targets. You can select multiple devices, as well as multiple pools as targets.

.. image:: /_static/objects/pools/target_pool.png
   :alt: Use a pool as target of a task
   :align: center

Use a pool to restrict all of eNMS to a subset of objects
---------------------------------------------------------

From the :guilabel:`admin/administration` panel, you can select a pool used as a database filtering mechanism.
All mechanisms and all pages in eNMS will be restricted to the objects of that pool.

In a production environment, for scalability purposes, multiples instances of eNMS can be deployed (per region, per type of device) to limit the amount of objects that a single instance must handle.
It is recommended to not have more than 5000 devices per instance of eNMS.