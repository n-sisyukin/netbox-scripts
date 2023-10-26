# netbox-scripts

Little project to load data from VMware vSphere to  [NetBox](https://github.com/netbox-community/netbox).

## requirements

Correct operation of the script requires the presence of the following custom fields in NetBox for VMs:

1. "virtualization_vms_guesstatus" string type
2. "virtualization_vms_guestos" string type
3. "virtualization_vms_uuid" string type
4. "virtualization_vms_filesystems" json type
5. "virtualization_vms_filesystems_capacity" int type
6. "virtualization_vms_interfaces" json type
7. "virtualization_vms_primaryipv4" string type
8. "virtualization_vms_primaryipv6" string type
9. "virtualization_vms_folder" string type
10. "virtualization_vms_have_direct_attach_luns" string type
