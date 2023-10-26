#-------------------------------------------------------------------------------
# Name:        load_vms_data_from_vmware_to_netbox
#
# Author:      Nikolay Sisyukin
# URL:         https://nikolay.sisyukin.ru/
#
# Created:     04.10.2023
# Copyright:   (c) Nikolay Sisyukin 2023
# Licence:     MIT License
#-------------------------------------------------------------------------------

from netbox_python import NetBoxClient
import requests
import json
import urllib3
import datetime
from vmware_os_versions import vmware_os_versions

GB = 2 ** 30  #  1GB

urllib3.disable_warnings()

class ManageVMs:
    def __init__(self, 
                 vmware_url, vmware_login, vmware_password, 
                 netbox_url, netbox_api_key,
                 raw_data_from_vmware_in_json_filename="raw_data_from_vmware.json", 
                 list_of_names_of_vms_from_vmware_in_txt_filename="list_of_names_of_vms_from_vmware.txt",
                 raw_data_from_netbox_in_json_filename="raw_data_from_netbox.json", 
                 list_of_names_of_vms_from_netbox_in_txt_filename="list_of_names_of_vms_from_netbox.txt",
                 list_of_vms_in_json_filename="list_of_vms.json", 
                 list_of_vms_to_create_in_netbox_in_json_filename="list_of_vms_to_create_in_netbox.json",
                 list_of_vms_to_update_in_netbox_in_json_filename="list_of_vms_to_update_in_netbox.json",
                 list_of_ips_with_vms_filename="list_of_ips_with_vms.json",
                 list_of_vms_with_ips_filename="list_of_vms_with_ips.json",
                 error_log_filename="error.log",
                 result_log_filename="result.log"):
        
        self.error_log_filename = error_log_filename
        self.result_log_filename = result_log_filename
        
        self.raw_data_from_vmware_in_json_filename = raw_data_from_vmware_in_json_filename
        self.raw_data_from_netbox_in_json_filename = raw_data_from_netbox_in_json_filename
        self.list_of_names_of_vms_from_vmware_in_txt_filename = list_of_names_of_vms_from_vmware_in_txt_filename
        self.list_of_names_of_vms_from_netbox_in_txt_filename = list_of_names_of_vms_from_netbox_in_txt_filename
        self.list_of_ips_with_vms_filename = list_of_ips_with_vms_filename
        self.list_of_vms_with_ips_filename = list_of_vms_with_ips_filename
        
        self.list_of_vms_in_json_filename = list_of_vms_in_json_filename
        self.list_of_vms_to_create_in_netbox_in_json_filename = list_of_vms_to_create_in_netbox_in_json_filename
        self.list_of_vms_to_update_in_netbox_in_json_filename = list_of_vms_to_update_in_netbox_in_json_filename
        
        self.dict_of_networks = self.__dataLoadFromVMwareAboutNetworks(vmware_url, vmware_login, vmware_password)
        self.raw_data_from_vmware_in_json = self.__dataLoadFromVMwareAboutVMs(vmware_url, vmware_login, vmware_password)
        self.raw_data_from_netbox_in_json = self.__dataLoadFromNetBoxAboutVMs(netbox_url, netbox_api_key)

        self.dict_of_vms_ids = {temp["name"]: temp["id"] for temp in self.raw_data_from_netbox_in_json}

        self.list_of_names_of_vms_from_vmware = self.__listOfVMs(self.raw_data_from_vmware_in_json)
        self.list_of_names_of_vms_from_netbox = self.__listOfVMs(self.raw_data_from_netbox_in_json)

        self.list_of_names_of_vms_to_create_in_netbox = sorted(set(self.list_of_names_of_vms_from_vmware) - set(self.list_of_names_of_vms_from_netbox))
        self.list_of_names_of_vms_to_delete_in_netbox = sorted(set(self.list_of_names_of_vms_from_netbox) - set(self.list_of_names_of_vms_from_vmware))
        self.list_of_names_of_vms_to_update_in_netbox = sorted(set(self.list_of_names_of_vms_from_netbox) & set(self.list_of_names_of_vms_from_vmware))
        
        self.list_of_vms_in_json = self.__generateActualVMListWithParameteres()
        self.list_of_vms_to_create_in_netbox_in_json = [vm for vm in self.list_of_vms_in_json if vm["name"] in self.list_of_names_of_vms_to_create_in_netbox]
        self.list_of_vms_to_update_in_netbox_in_json = [vm for vm in self.list_of_vms_in_json if vm["name"] in self.list_of_names_of_vms_to_update_in_netbox]
        
        for vm in self.list_of_vms_to_update_in_netbox_in_json:
            vm["id"] = self.dict_of_vms_ids[vm["name"]]

        self.list_of_ips_with_owner, self.list_of_owner_with_ips = self.__generateListOfIPsOfVMs()
        
        return None

    #  Dump logs method
    def __dumpLogsToFile(self, logs_message, output_filename):
        with open(output_filename, 'a', encoding='UTF-8') as f:
            print(f"{datetime.datetime.now()}: {logs_message}", file=f)
        return None

    #  Load VMs data from VMware vSphere to JSON method
    def __dataLoadFromVMwareAboutVMs(self, vmware_url, vmware_login, vmware_password):
        try:
            session = requests.Session()
            session.post(f"{vmware_url}/rest/com/vmware/cis/session", auth=(vmware_login, vmware_password), verify=False)
            vms = json.loads(session.get(f"{vmware_url}/api/vcenter/vm").text)
            vms_list_with_folder = {vm['name']: '' for vm in json.loads(session.get(f"{vmware_url}/api/vcenter/vm").text)}
            folders_of_vms_all = {folder['folder']: folder['name'] for folder in json.loads(session.get(f"{vmware_url}/api/vcenter/folder").text) if folder['type'] == 'VIRTUAL_MACHINE'}
            for folder_id, folder_name in folders_of_vms_all.items():
                vms_list_with_folder.update({vm['name']: folder_name for vm in json.loads(session.get(f"{vmware_url}/rest/vcenter/vm", params={'filter.folders': folder_id}).text)['value']})
        except Exception as error:
            self.__dumpLogsToFile(f"Error connection to VMware: {type(error).__name__}", self.error_log_filename)
            exit()
        for vm in vms:
            vm["data"] = json.loads(session.get(f"{vmware_url}/api/vcenter/vm/{vm["vm"]}").text)
            vm["interfaces"] = json.loads(session.get(f"{vmware_url}/api/vcenter/vm/{vm["vm"]}/guest/networking/interfaces").text)
            vm["routes"] = json.loads(session.get(f"{vmware_url}/api/vcenter/vm/{vm["vm"]}/guest/networking/routes").text)
            vm["filesystems"] = json.loads(session.get(f"{vmware_url}/api/vcenter/vm/{vm["vm"]}/guest/local-filesystem").text)
            vm["guest_status"] = json.loads(session.get(f"{vmware_url}/api/vcenter/vm/{vm["vm"]}/guest/identity").text)
            vm["folder"] = vms_list_with_folder[vm['name']]
        return sorted(vms, key=lambda vm: vm["name"])

    #  Load Networks data from VMware to JSON method
    def __dataLoadFromVMwareAboutNetworks(self, vmware_url, vmware_login, vmware_password):
        try:
            session = requests.Session()
            session.post(f"{vmware_url}/rest/com/vmware/cis/session", auth=(vmware_login, vmware_password), verify=False)
            networks = {network["network"]:network["name"] for network in json.loads(session.get(f"{vmware_url}/api/vcenter/network").text)}
        except Exception as error:
            self.__dumpLogsToFile(f"Error connection to VMware: {type(error).__name__}", self.error_log_filename)
            exit()
        return networks
    
    #  Load VMs data from NetBox to JSON method
    def __dataLoadFromNetBoxAboutVMs(self, netbox_url, netbox_api_key):
        try:
            self.nb = NetBoxClient(base_url=netbox_url, token=netbox_api_key)
        except Exception as error:
            self.__dumpLogsToFile(f"Error connection to NetBox: {type(error).__name__}", self.error_log_filename)
            exit()
        return self.nb.virtualization.virtual_machines.list(limit=9999).data
        
    #  Generate list of VMs names from JSON
    def __listOfVMs(self, list_of_vms_in_json):  
        return sorted([vm["name"] for vm in list_of_vms_in_json])
    
    #  Dump data of VMs in JSON to file
    def __dumpListOfVMsToFileFromJSON(self, filename, data_in_json_format):
        with open(filename, "w", encoding="UTF-8") as f:
            json.dump(data_in_json_format, f, ensure_ascii=False, indent=4)
        return None
    
    #  Dump names of VMs in txt to file
    def __dumpListOfVMsNamesToFile(self, filename, list_of_vms):
        with open(filename, "w", encoding="UTF-8") as f:
            for i, vm_name in enumerate(list_of_vms):
                print(f"{i + 1}. {vm_name}", file=f)
        return None
    
    #  Dump all data about VMs to files 
    def dumpListsOfVMsToFiles(self):
        self.__dumpListOfVMsToFileFromJSON(self.raw_data_from_vmware_in_json_filename, self.raw_data_from_vmware_in_json)
        self.__dumpListOfVMsToFileFromJSON(self.raw_data_from_netbox_in_json_filename, self.raw_data_from_netbox_in_json)
        
        self.__dumpListOfVMsNamesToFile(self.list_of_names_of_vms_from_vmware_in_txt_filename, self.list_of_names_of_vms_from_vmware)
        self.__dumpListOfVMsNamesToFile(self.list_of_names_of_vms_from_netbox_in_txt_filename, self.list_of_names_of_vms_from_netbox)
        
        self.__dumpListOfVMsToFileFromJSON(self.list_of_vms_in_json_filename, self.list_of_vms_in_json)
        self.__dumpListOfVMsToFileFromJSON(self.list_of_vms_to_create_in_netbox_in_json_filename, self.list_of_vms_to_create_in_netbox_in_json)
        self.__dumpListOfVMsToFileFromJSON(self.list_of_vms_to_update_in_netbox_in_json_filename, self.list_of_vms_to_update_in_netbox_in_json)
        
        with open(self.list_of_ips_with_vms_filename, "w", encoding="UTF-8") as f:
            json.dump(self.list_of_ips_with_owner, f, ensure_ascii=False, indent=4)
        with open(self.list_of_vms_with_ips_filename, "w", encoding="UTF-8") as f:
            json.dump(self.list_of_owner_with_ips, f, ensure_ascii=False, indent=4)
        
        return None
    
    #  Generate data about VMs to JSON in NetBox-compatible format
    def __generateActualVMListWithParameteres(self):
        tempActualVMListWithParameteres = []
        for vm in self.raw_data_from_vmware_in_json:
            tempVM = {}
            tempVM["cluster"] = 1
            tempVM["name"] = vm["name"]
            tempVM["slug"] = vm["name"].lower().replace(" ", "-").replace("_", "-").replace("(", "").replace(")","")
            tempVM["status"] = ("offline" if vm["power_state"] == "POWERED_OFF" else ("active" if vm["power_state"] == "POWERED_ON" else "staged"))
            tempVM["vcpus"] = vm["cpu_count"]
            tempVM["memory"] = vm["memory_size_MiB"]
            tempVM["disk"] = 0
            tempVM["custom_fields"] = {}
            tempVM["custom_fields"]["virtualization_vms_filesystems_capacity"] = 0
            if vm["power_state"] != "POWERED_ON":
                tempVM["custom_fields"]["virtualization_vms_guesstatus"] = "VM OFF"
            elif vm["power_state"] == "POWERED_ON" and "error_type" in vm["guest_status"].keys():
                tempVM["custom_fields"]["virtualization_vms_guesstatus"] = "Need install"
            else:
                tempVM["custom_fields"]["virtualization_vms_guesstatus"] = "OK"
            tempVM["custom_fields"]["virtualization_vms_guestos"] = vmware_os_versions[vm["data"]["guest_OS"]]
            tempVM["custom_fields"]["virtualization_vms_uuid"] = vm['data']['identity']['instance_uuid']
            tempVM["custom_fields"]["virtualization_vms_filesystems"] = []
            if "error_type" not in vm["filesystems"].keys():
                for fs_name, fs_data in vm["filesystems"].items():
                    tempFS = {}
                    tempFS["mountpoint"] = fs_name
                    tempFS["filesystem"] = fs_data.setdefault("filesystem", "")
                    tempFS["capacity_in_gb"] = fs_data["capacity"] // GB
                    tempFS["freespace_in_gb"] = fs_data["free_space"] // GB
                    tempVM["custom_fields"]["virtualization_vms_filesystems_capacity"] += fs_data["capacity"] // GB
                    tempVM["custom_fields"]["virtualization_vms_filesystems"].append(tempFS)
            tempVM["custom_fields"]["virtualization_vms_disks"] = []
            if "error_type" not in vm["data"]["disks"].keys():
                for hdd_name, hdd_data in vm["data"]["disks"].items():
                    tempDrive = {}
                    tempDrive["name"] = hdd_name
                    tempDrive["label"] = hdd_data['label']
                    tempDrive["vmdk"] = hdd_data['backing']['vmdk_file']
                    tempDrive["capacity_in_gb"] = hdd_data['capacity'] // GB
                    tempVM["disk"] += hdd_data['capacity'] // GB
                    tempVM["custom_fields"]["virtualization_vms_disks"].append(tempDrive)
            tempVM["custom_fields"]["virtualization_vms_interfaces"] = []
            
            primaryIPv4flag = False
            tempVM["custom_fields"]["virtualization_vms_primaryipv4"] = ""
            primaryIPv6flag = False
            tempVM["custom_fields"]["virtualization_vms_primaryipv6"] = ""
            
            for nic_name, nic_data in vm["data"]["nics"].items():
                tempNIC = {}
                tempNIC["name"] = nic_name
                tempNIC["state"] = nic_data['state']
                tempNIC["vswitch"] = self.dict_of_networks[nic_data['backing']['network']]
                tempNIC["mac"] = nic_data['mac_address'].lower()
                tempNIC["ips"] = []
                if isinstance(vm["interfaces"], list):
                    for interface in vm["interfaces"]:
                        if interface["mac_address"].lower() == nic_data['mac_address'].lower() and "ip" in interface.keys():
                            for ip in interface["ip"]["ip_addresses"]:
                                tempNIC["ips"].append(ip["ip_address"])
                                if not primaryIPv4flag and len(ip["ip_address"]) <= 16:
                                    tempVM["custom_fields"]["virtualization_vms_primaryipv4"] = ip["ip_address"]
                                    primaryIPv4flag = True
                                if not primaryIPv6flag and len(ip["ip_address"]) > 16:
                                    tempVM["custom_fields"]["virtualization_vms_primaryipv6"] = ip["ip_address"]
                                    primaryIPv6flag = True
                tempVM["custom_fields"]["virtualization_vms_interfaces"].append(tempNIC)
            tempVM["custom_fields"]["virtualization_vms_folder"] = f"'{vm['folder']}'"
            tempVM["custom_fields"]['virtualization_vms_have_direct_attach_luns'] = "Yes" if tempVM["custom_fields"]["virtualization_vms_filesystems_capacity"] > tempVM["disk"] else "No"
            tempActualVMListWithParameteres.append(tempVM)
        return tempActualVMListWithParameteres
    
    #  Generate list of IPs of VMs in 2 formats
    def __generateListOfIPsOfVMs(self):
        list_of_ips_with_owner = {}
        list_of_owner_with_ips = {}
        for vm in self.raw_data_from_vmware_in_json:
            list_of_owner_with_ips[vm["name"]] = []
            if isinstance(vm["interfaces"], list):
                for interface in vm["interfaces"]:
                    if "ip" in interface.keys():
                        for ip in interface["ip"]["ip_addresses"]:
                            list_of_ips_with_owner[ip["ip_address"]] = vm["name"]
                            list_of_owner_with_ips[vm["name"]].append(ip["ip_address"])
        return dict(sorted(list_of_ips_with_owner.items())), dict(sorted(list_of_owner_with_ips.items()))

    #  Create new VMs in NetBox
    def createVMsInNetBox(self):
        self.nb.virtualization.virtual_machines.create(self.list_of_vms_to_create_in_netbox_in_json)
        self.__dumpLogsToFile(f"\nIn NetBox created VMs:\n{self.list_of_names_of_vms_to_create_in_netbox}\n", self.result_log_filename)
        return None
    
    #  Delete old VMs in NetBox
    def deleteVMsInNetBox(self):
        listVMsIDsInNetBoxToDelete = [{"id": temp["id"], "name": temp["name"]} 
                                      for temp in self.raw_data_from_netbox_in_json 
                                      if temp["name"] in self.list_of_names_of_vms_to_delete_in_netbox]
        try:
            self.nb.virtualization.virtual_machines.delete(listVMsIDsInNetBoxToDelete)
        except:
            pass
        self.__dumpLogsToFile(f"\nFrom NetBox deleted VMs:\n{self.list_of_names_of_vms_to_delete_in_netbox}\n", self.result_log_filename)
        return None
    
    #  Update data VMs in NetBox
    def updateVMsInNetBox(self):
        self.nb.virtualization.virtual_machines.update(self.list_of_vms_to_update_in_netbox_in_json)
        self.__dumpLogsToFile(f"\nUpdated {len(self.list_of_vms_to_update_in_netbox_in_json)} VMs\n", self.result_log_filename)
        return None


def main():
    vmware_vsphere_url_address = "https://vcsa.example.domain"
    vmware_vsphere_login = "username"
    vmware_vsphere_password = "password"

    netbox_url_address = "https://netbox.example.domain"
    netbox_api_key = "00112233445566778899aabbccddeeffgghhjjqq"
    
    VMs1 = ManageVMs(vmware_vsphere_url_address, vmware_vsphere_login, vmware_vsphere_password, 
                     netbox_url_address, netbox_api_key)
    
    #VMs1.dumpListsOfVMsToFiles()  #  Dump all worked data to files
    
    VMs1.createVMsInNetBox()  #  Create VMs in NetBox
    VMs1.deleteVMsInNetBox()  #  Delete VMs in NetBox
    VMs1.updateVMsInNetBox()  #  Update VMs in NetBox

    return None

if __name__ == "__main__":
	main()