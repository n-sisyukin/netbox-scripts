#-------------------------------------------------------------------------------
# Name:        VMware vSphere To NetBox Sync Tool
#
# Author:      Nikolay Sisyukin
# URL:         https://nikolay.sisyukin.ru/
#
# Created:     28.10.2023
# Copyright:   (c) Nikolay Sisyukin 2023
# Licence:     MIT License
#-------------------------------------------------------------------------------

VMWARE_OS_VERSION = {"DOS": "MS-DOS", 
                     "WIN_31": "Windows 3.1", 
                     "WIN_95": "Windows 95", 
                     "WIN_98": "Windows 98", 
                     "WIN_ME": "Windows Millennium Edition", 
                     "WIN_NT": "Windows NT 4", 
                     "WIN_2000_PRO": "Windows 2000 Professional", 
                     "WIN_2000_SERV": "Windows 2000 Server", 
                     "WIN_2000_ADV_SERV": "Windows 2000 Advanced Server", 
                     "WIN_XP_HOME": "Windows XP Home Edition", 
                     "WIN_XP_PRO": "Windows XP Professional", 
                     "WIN_XP_PRO_64": "Windows XP Professional Edition (64 bit)", 
                     "WIN_NET_WEB": "Windows Server 2003, Web Edition", 
                     "WIN_NET_STANDARD": "Windows Server 2003, Standard Edition", 
                     "WIN_NET_ENTERPRISE": "Windows Server 2003, Enterprise Edition", 
                     "WIN_NET_DATACENTER": "Windows Server 2003, Datacenter Edition", 
                     "WIN_NET_BUSINESS": "Windows Small Business Server 2003", 
                     "WIN_NET_STANDARD_64": "Windows Server 2003, Standard Edition (64 bit)", 
                     "WIN_NET_ENTERPRISE_64": "Windows Server 2003, Enterprise Edition (64 bit)", 
                     "WIN_LONGHORN": "Windows Longhorn", 
                     "WIN_LONGHORN_64": "Windows Longhorn (64 bit)", 
                     "WIN_NET_DATACENTER_64": "Windows Server 2003, Datacenter Edition (64 bit)", 
                     "WIN_VISTA": "Windows Vista", 
                     "WIN_VISTA_64": "Windows Vista (64 bit)", 
                     "WINDOWS_7": "Windows 7", 
                     "WINDOWS_7_64": "Windows 7 (64 bit)", 
                     "WINDOWS_7_SERVER_64": "Windows Server 2008 R2 (64 bit)", 
                     "WINDOWS_8": "Windows 8", 
                     "WINDOWS_8_64": "Windows 8 (64 bit)", 
                     "WINDOWS_8_SERVER_64": "Windows 8 Server (64 bit)", 
                     "WINDOWS_9": "Windows 10", 
                     "WINDOWS_9_64": "Windows 10 (64 bit)", 
                     "WINDOWS_9_SERVER_64": "Windows 10 Server (64 bit)", 
                     "WINDOWS_11_64": "Windows 11 (64 bit)", 
                     "WINDOWS_12_64": "Windows 12 (64 bit)", 
                     "WINDOWS_HYPERV": "Windows Hyper-V", 
                     "WINDOWS_SERVER_2019": "Windows Server 2019", 
                     "WINDOWS_SERVER_2021": "Windows Server 2022", 
                     "WINDOWS_SERVER_2025": "Windows Server 2025", 
                     "FREEBSD": "FreeBSD 10 or earlier", 
                     "FREEBSD_64": "FreeBSD 10 x64 or earlier", 
                     "FREEBSD_11": "FreeBSD 11", 
                     "FREEBSD_12": "FreeBSD 12", 
                     "FREEBSD_13": "FreeBSD 13", 
                     "FREEBSD_14": "FreeBSD 14 or later", 
                     "FREEBSD_11_64": "FreeBSD 11 x64", 
                     "FREEBSD_12_64": "FreeBSD 12 x64", 
                     "FREEBSD_13_64": "FreeBSD 13 x64", 
                     "FREEBSD_14_64": "FreeBSD 14 x64 or later", 
                     "REDHAT": "Red Hat Linux 2.1", 
                     "RHEL_2": "Red Hat Enterprise Linux 2", 
                     "RHEL_3": "Red Hat Enterprise Linux 3", 
                     "RHEL_3_64": "Red Hat Enterprise Linux 3 (64 bit)", 
                     "RHEL_4": "Red Hat Enterprise Linux 4", 
                     "RHEL_4_64": "Red Hat Enterprise Linux 4 (64 bit)", 
                     "RHEL_5": "Red Hat Enterprise Linux 5", 
                     "RHEL_5_64": "Red Hat Enterprise Linux 5 (64 bit)", 
                     "RHEL_6": "Red Hat Enterprise Linux 6", 
                     "RHEL_6_64": "Red Hat Enterprise Linux 6 (64 bit)", 
                     "RHEL_7": "Red Hat Enterprise Linux 7", 
                     "RHEL_7_64": "Red Hat Enterprise Linux 7 (64 bit)", 
                     "RHEL_8_64": "Red Hat Enterprise Linux 8 (64 bit)", 
                     "RHEL_9_64": "Red Hat Enterprise Linux 9 (64 bit)", 
                     "CENTOS": "CentOS 4⁄5", 
                     "CENTOS_64": "CentOS 4⁄5 (64-bit)", 
                     "CENTOS_6": "CentOS 6", 
                     "CENTOS_6_64": "CentOS 6 (64-bit)", 
                     "CENTOS_7": "CentOS 7", 
                     "CENTOS_7_64": "CentOS 7 (64-bit)", 
                     "CENTOS_8_64": "CentOS 8 (64-bit)", 
                     "CENTOS_9_64": "CentOS 9 (64-bit)", 
                     "ORACLE_LINUX": "Oracle Linux 4⁄5", 
                     "ORACLE_LINUX_64": "Oracle Linux 4⁄5 (64-bit)", 
                     "ORACLE_LINUX_6": "Oracle Linux 6", 
                     "ORACLE_LINUX_6_64": "Oracle Linux 6 (64-bit)", 
                     "ORACLE_LINUX_7": "Oracle Linux 7", 
                     "ORACLE_LINUX_7_64": "Oracle Linux 7 (64-bit)", 
                     "ORACLE_LINUX_8_64": "Oracle Linux 8 (64-bit)", 
                     "ORACLE_LINUX_9_64": "Oracle Linux 9 (64-bit)", 
                     "SUSE": "Suse Linux", 
                     "SUSE_64": "Suse Linux (64 bit)", 
                     "SLES": "Suse Linux Enterprise Server 9", 
                     "SLES_64": "Suse Linux Enterprise Server 9 (64 bit)", 
                     "SLES_10": "Suse linux Enterprise Server 10", 
                     "SLES_10_64": "Suse Linux Enterprise Server 10 (64 bit)", 
                     "SLES_11": "Suse linux Enterprise Server 11", 
                     "SLES_11_64": "Suse Linux Enterprise Server 11 (64 bit)", 
                     "SLES_12": "Suse linux Enterprise Server 12", 
                     "SLES_12_64": "Suse Linux Enterprise Server 12 (64 bit)", 
                     "SLES_15_64": "Suse Linux Enterprise Server 15 (64 bit)", 
                     "SLES_16_64": "Suse Linux Enterprise Server 16 (64 bit)", 
                     "NLD_9": "Novell Linux Desktop 9", 
                     "OES": "Open Enterprise Server", 
                     "SJDS": "Sun Java Desktop System", 
                     "MANDRAKE": "Mandrake Linux", 
                     "MANDRIVA": "Mandriva Linux", 
                     "MANDRIVA_64": "Mandriva Linux (64 bit)", 
                     "TURBO_LINUX": "Turbolinux", 
                     "TURBO_LINUX_64": "Turbolinux (64 bit)", 
                     "UBUNTU": "Ubuntu Linux", 
                     "UBUNTU_64": "Ubuntu Linux (64 bit)", 
                     "DEBIAN_4": "Debian GNU/Linux 4", 
                     "DEBIAN_4_64": "Debian GNU/Linux 4 (64 bit)", 
                     "DEBIAN_5": "Debian GNU/Linux 5", 
                     "DEBIAN_5_64": "Debian GNU/Linux 5 (64 bit)", 
                     "DEBIAN_6": "Debian GNU/Linux 6", 
                     "DEBIAN_6_64": "Debian GNU/Linux 6 (64 bit)", 
                     "DEBIAN_7": "Debian GNU/Linux 7", 
                     "DEBIAN_7_64": "Debian GNU/Linux 7 (64 bit)", 
                     "DEBIAN_8": "Debian GNU/Linux 8", 
                     "DEBIAN_8_64": "Debian GNU/Linux 8 (64 bit)", 
                     "DEBIAN_9": "Debian GNU/Linux 9", 
                     "DEBIAN_9_64": "Debian GNU/Linux 9 (64 bit)", 
                     "DEBIAN_10": "Debian GNU/Linux 10", 
                     "DEBIAN_10_64": "Debian GNU/Linux 10 (64 bit)", 
                     "DEBIAN_11": "Debian GNU/Linux 11", 
                     "DEBIAN_11_64": "Debian GNU/Linux 11 (64 bit)", 
                     "DEBIAN_12": "Debian GNU/Linux 12", 
                     "DEBIAN_12_64": "Debian GNU/Linux 12 (64 bit)", 
                     "ASIANUX_3": "Asianux Server 3", 
                     "ASIANUX_3_64": "Asianux Server 3 (64 bit)", 
                     "ASIANUX_4": "Asianux Server 4", 
                     "ASIANUX_4_64": "Asianux Server 4 (64 bit)", 
                     "ASIANUX_5_64": "Asianux Server 5 (64 bit)", 
                     "ASIANUX_7_64": "Asianux Server 7 (64 bit)", 
                     "ASIANUX_8_64": "Asianux Server 8 (64 bit)", 
                     "ASIANUX_9_64": "Asianux Server 9 (64 bit)", 
                     "OPENSUSE": "OpenSUSE Linux", 
                     "OPENSUSE_64": "OpenSUSE Linux (64 bit)", 
                     "FEDORA": "Fedora Linux", 
                     "FEDORA_64": "Fedora Linux (64 bit)", 
                     "COREOS_64": "CoreOS Linux (64 bit)", 
                     "VMWARE_PHOTON_64": "VMware Photon (64 bit)", 
                     "OTHER_24X_LINUX": "Linux 2.4x Kernel", 
                     "OTHER_24X_LINUX_64": "Linux 2.4x Kernel (64 bit)", 
                     "OTHER_26X_LINUX": "Linux 2.6x Kernel", 
                     "OTHER_26X_LINUX_64": "Linux 2.6x Kernel (64 bit)", 
                     "OTHER_3X_LINUX": "Linux 3.x Kernel", 
                     "OTHER_3X_LINUX_64": "Linux 3.x Kernel (64 bit)", 
                     "OTHER_4X_LINUX": "Linux 4.x Kernel", 
                     "OTHER_4X_LINUX_64": "Linux 4.x Kernel (64 bit)", 
                     "OTHER_5X_LINUX": "Linux 5.x Kernel", 
                     "OTHER_5X_LINUX_64": "Linux 5.x Kernel (64 bit)", 
                     "OTHER_6X_LINUX": "Linux 6.x Kernel", 
                     "OTHER_6X_LINUX_64": "Linux 6.x Kernel (64 bit)", 
                     "OTHER_LINUX": "Linux 2.2x Kernel", 
                     "GENERIC_LINUX": "Other Linux", 
                     "OTHER_LINUX_64": "Linux (64 bit)", 
                     "SOLARIS_6": "Solaris 6", 
                     "SOLARIS_7": "Solaris 7", 
                     "SOLARIS_8": "Solaris 8", 
                     "SOLARIS_9": "Solaris 9", 
                     "SOLARIS_10": "Solaris 10 (32 bit)", 
                     "SOLARIS_10_64": "Solaris 10 (64 bit)", 
                     "SOLARIS_11_64": "Solaris 11 (64 bit)", 
                     "OS2": "OS/2", 
                     "ECOMSTATION": "eComStation 1.x", 
                     "ECOMSTATION_2": "eComStation 2.0", 
                     "NETWARE_4": "Novell NetWare 4", 
                     "NETWARE_5": "Novell NetWare 5.1", 
                     "NETWARE_6": "Novell NetWare 6.x", 
                     "OPENSERVER_5": "SCO OpenServer 5", 
                     "OPENSERVER_6": "SCO OpenServer 6", 
                     "UNIXWARE_7": "SCO UnixWare 7", 
                     "DARWIN": "Mac OS 10.5", 
                     "DARWIN_64": "Mac OS 10.5 (64 bit)", 
                     "DARWIN_10": "Mac OS 10.6", 
                     "DARWIN_10_64": "Mac OS 10.6 (64 bit)", 
                     "DARWIN_11": "Mac OS 10.7", 
                     "DARWIN_11_64": "Mac OS 10.7 (64 bit)", 
                     "DARWIN_12_64": "Mac OS 10.8 (64 bit)", 
                     "DARWIN_13_64": "Mac OS 10.9 (64 bit)", 
                     "DARWIN_14_64": "Mac OS 10.10 (64 bit)", 
                     "DARWIN_15_64": "Mac OS 10.11 (64 bit)", 
                     "DARWIN_16_64": "Mac OS 10.12 (64 bit)", 
                     "DARWIN_17_64": "Mac OS 10.13 (64 bit)", 
                     "DARWIN_18_64": "Mac OS 10.14 (64 bit)", 
                     "DARWIN_19_64": "Mac OS 10.15 (64 bit)", 
                     "DARWIN_20_64": "Mac OS 11 (64 bit)", 
                     "DARWIN_21_64": "Mac OS 12 (64 bit)", 
                     "DARWIN_22_64": "Mac OS 13 (64 bit)", 
                     "DARWIN_23_64": "Mac OS 14 (64 bit)", 
                     "VMKERNEL": "VMware ESX 4", 
                     "VMKERNEL_5": "VMware ESX 5", 
                     "VMKERNEL_6": "VMware ESX 6", 
                     "VMKERNEL_65": "VMware ESXi 6.5 AND ESXi 6.7.", 
                     "VMKERNEL_7": "VMware ESX 7", 
                     "VMKERNEL_8": "VMware ESX 8", 
                     "AMAZONLINUX2_64": "Amazon Linux 2 (64 bit)", 
                     "AMAZONLINUX3_64": "Amazon Linux 3 (64 bit)", 
                     "CRXPOD_1": "CRX Pod 1", 
                     "ROCKYLINUX_64": "Rocky Linux (64-bit)", 
                     "ALMALINUX_64": "AlmaLinux (64-bit)", 
                     "OTHER": "Other Operating System", 
                     "OTHER_64": "Other Operating System (64 bit)"}

POWER_STATES = {"POWERED_ON": "active",
                "POWERED_OFF": "offline",
                "SUSPENDED": "staged"}

REQUIRED_CUSTOM_FIELDS = {"virtualization_vms_filesystems_capacity",
                          "virtualization_vms_guesstatus",
                          "virtualization_vms_have_direct_attach_luns",
                          "virtualization_vms_iscsi_network_access",
                          "virtualization_vms_guestos",
                          "virtualization_vms_primaryipv4",
                          "virtualization_vms_primaryipv6",
                          "virtualization_vms_type_of_nics",
                          "virtualization_vms_uuid",
                          "virtualization_vms_folder",
                          "virtualization_vms_disks",
                          "virtualization_vms_owners",
                          "virtualization_vms_filesystems",
                          "virtualization_vms_interfaces",
                          "virtualization_vms_notes"}

CLUSTERS_TYPES = {"vmware": {"id": 1, "note": "virtualization (vmware vsphere)"}}

OWNERS_OF_VMS = {}

KB = 2 ** 10  #  1KB in bytes
MB = 2 ** 20  #  1MB in bytes
GB = 2 ** 30  #  1GB in bytes
TB = 2 ** 40  #  1TB in bytes

NAME_OF_ISCSI_NETWORK = 'iSCSI-network-in-VMware'

import requests
import json
import urllib3
import sys
import datetime
import email, smtplib, ssl

import ipaddress
import socket
from netbox_python import NetBoxClient

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import config as conf  #  Config file containing flags, logins, passwords for connecting to NetBox, VMware, Veeam. 


urllib3.disable_warnings()

class ManageNetBox:
    def __init__(self, **arg):
        self.log_flg = arg['log_flg'] if 'log_flg' in arg.keys() else False

        self.mail_flg = arg['mail_flg'] if 'mail_flg' in arg.keys() else False

        self.nb_flg = arg['nb_flg'] if 'nb_flg' in arg.keys() else False
        self.vm_flg = arg['vm_flg'] if 'vm_flg' in arg.keys() else False
        
        if self.log_flg:
            self.errors_log_filename = arg['errors_log_filename']
            self.result_log_filename = arg['result_log_filename']

        if self.mail_flg:
            self.mail_srv = arg['mail_srv']
            self.mail_prt = arg['mail_prt']
            self.mail_sender = arg['mail_sender']
            self.mail_pas = arg['mail_pas']
            self.mail_recipients = arg['mail_recipients']
            
        if self.nb_flg:
            self.nb_url = arg['nb_url']
            self.nb_key = arg['nb_key']
            self.__connectToNetBox()
            self.__loadClustersFromNetBox()  #  To 'self.clusters_from_nb' JSON
            self.__loadIPsFromNetBox()
            self.__loadVMsFromNetBox()       #  To 'self.vms_from_nb' JSON and 'self.vms_lst_from_nb' lst

        if self.vm_flg:
            self.vm_url = arg['vm_url']
            self.vm_log = arg['vm_log']
            self.vm_pas = arg['vm_pas']
            self.__connectToVMware()
            self.__loadClustersFromVMware()  #  To 'self.clusters_from_vw' JSON and 'self.clusters_lst_from_vw' lst
            self.__loadVMsFromVMware()       #  To 'self.vms_from_vw' JSON and 'self.vms_lst_from_vw' lst
        
        if self.nb_flg and self.vm_flg:
            self.__genVMsToNetBox()          #  To 'self.vms_to_netbox' JSON in NetBox format
            self.__genIPsLists()             #  To 'self.list_of_ips_01' JSON and 'self.list_of_ips_02' JSON


    # Write to files methods
    def dumpAllToFiles(self):
        self.__dumpJSN('01.vms_from_vw.json', self.vms_from_vw)
        self.__dumpJSN('02.vms_from_nb.json', self.vms_from_nb)
        self.__dumpTXT('03.clusters_lst_from_vw.txt', self.clusters_lst_from_vw)
        self.__dumpTXT('04.folders_lst_from_vw.txt', self.folders_lst_from_vw)
        self.__dumpTXT('05.vms_lst_from_vw.txt', self.vms_lst_from_vw)
        self.__dumpJSN('06.vms_to_netbox.json', self.vms_to_netbox)
        self.__dumpJSN('07.vms_to_upd_in_nb.json', self.vms_to_upd_in_nb)
        self.__dumpJSN('08.vms_to_crt_in_nb.json', self.vms_to_crt_in_nb)
        self.__dumpJSN('09.vms_to_del_in_nb.json', self.vms_to_del_in_nb)
        self.__dumpJSN('10.list_of_ips_01.json', self.list_of_ips_01)
        self.__dumpTXT('11.list_of_ips_02.txt', self.list_of_ips_02)
        self.__dumpJSN('12.list_white_ips_on_vms.json', self.list_white_ips_on_vms)
        self.__dumpJSN('13.list_vms_with_enabled_ipv6.json', self.list_vms_with_enabled_ipv6)
        self.__dumpJSN('14.raw_ips_from_nb.json', self.raw_ips_from_nb)
        self.__dumpTXT('15.ips_from_nb.txt', self.ips_from_nb)
        self.__dumpTXT('16.list_of_ips_03.txt', self.list_of_ips_03)
    
    def __dumpLOG(self, filename, data):
        if self.log_flg:
            self.__dumpTXT(filename, f'{datetime.datetime.now()}: {data.replace('<b>', '').replace('</b>', '')}', 'a')

    def __dumpTXT(self, filename, data, mode='w'):  #  Change 'mode' from 'w' or 'a'
        with open(filename, mode, encoding="UTF-8") as f:
            if isinstance(data, list):
                print('\n'.join(data), file=f)
            else:
                print(data, file=f)
    
    def __dumpJSN(self, filename, data, mode='w'):  #  Change 'mode' from 'w' or 'a'
        with open(filename, mode, encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # Connect methods
    def __connectToNetBox(self):
        try:
            self.__netbox = NetBoxClient(base_url=self.nb_url, token=self.nb_key)
        except Exception as error:
            self.__dumpLOG(self.errors_log_filename, f'Error connect to NetBox: {type(error).__name__}')
            sys.exit()
    
    def __connectToVMware(self):
        try:
            self.__vmware = requests.Session()
            self.__vmware.post(f'{self.vm_url}/rest/com/vmware/cis/session', auth=(self.vm_log, self.vm_pas), verify=False)
        except Exception as error:
            self.__dumpLOG(self.errors_log_filename, f'Error connect to VMware: {type(error).__name__}')
            sys.exit()


    # Sync data about clusters methods
    def __loadClustersFromNetBox(self):
        self.clusters_from_nb = {}
        self.clusters_ids_from_nb = {}
        for cluster in self.__netbox.virtualization.clusters.list(limit=0).data:
            self.clusters_from_nb[cluster['name']] = cluster['id']
            self.clusters_ids_from_nb[cluster['id']] = cluster['name']
        self.clusters_lst_from_nb = set([cluster for cluster in self.clusters_from_nb.keys()])
    
    def __loadClustersFromVMware(self):
        self.clusters_raw_from_vw = {cluster['cluster']: cluster['name'] 
                                for cluster in 
                                json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/cluster').text)}
        self.clusters_lst_from_vw = set(self.clusters_raw_from_vw.values())
        self.clusters_from_vw = {}
        for cluster_id, cluster_name in self.clusters_raw_from_vw.items():
            for vm in json.loads(self.__vmware.get(f'{self.vm_url}/rest/vcenter/vm', 
                                                   params={'filter.clusters': cluster_id}).text)['value']:
                self.clusters_from_vw[vm['name']] = cluster_name

    def __syncClustersFromVMwareToNetBox(self):
        self.clusters_lst_to_crt_in_nb = sorted(set(self.clusters_lst_from_vw) - set(self.clusters_lst_from_nb))
        self.clusters_lst_to_del_in_nb = sorted(set(self.clusters_lst_from_nb) - set(self.clusters_lst_from_vw))
        
        self.clusters_to_crt_in_nb = []
        for cluster_name in self.clusters_lst_to_crt_in_nb:
            t_cluster = {}
            t_cluster['name'] = cluster_name
            t_cluster['type'] = CLUSTERS_TYPES["vmware"]["id"]
            self.clusters_to_crt_in_nb.append(t_cluster)
        
        self.clusters_to_del_in_nb = []
        for cluster_id, cluster_name in self.clusters_ids_from_nb.items():
            if cluster_name in self.clusters_lst_to_del_in_nb:
                t_cluster = {}
                t_cluster['id'] = cluster_id
                t_cluster['name'] = cluster_name
                self.clusters_to_del_in_nb.append(t_cluster)

        self.__netbox.virtualization.clusters.create(self.clusters_to_crt_in_nb)
        lst_clusters_to_log = ', '.join(self.clusters_lst_to_crt_in_nb)
        message_to_log = f'Created {len(self.clusters_lst_to_crt_in_nb)} clusters: {lst_clusters_to_log}'
        self.__dumpLOG(self.result_log_filename, message_to_log)
        
        # Witout 'try-except' don't work out of errors on 'netbox-python' library
        try:
            self.__netbox.virtualization.clusters.delete(self.clusters_to_del_in_nb)
        except:
            lst_clusters_to_log = ', '.join(self.clusters_lst_to_del_in_nb)
            message_to_log = f'Deleted {len(self.clusters_lst_to_del_in_nb)} clusters: {lst_clusters_to_log}'
            self.__dumpLOG(self.result_log_filename, message_to_log)

    # Sync data about VMs and IPs methods
    def __loadVMsFromNetBox(self):
        self.vms_from_nb = self.__netbox.virtualization.virtual_machines.list(limit=0).data
        self.vms_lst_from_nb = []
        self.vms_ids_from_nb = {}
        for vm in self.vms_from_nb:
            self.vms_lst_from_nb.append(vm['name'])
            self.vms_ids_from_nb[vm['name']] = vm['id']
        self.vms_lst_from_nb.sort()     
    
    def __loadVMsFromVMware(self):
        self.__loadFoldersFromVMware()
        self.__loadNetworksFromVMware()
        self.vms_from_vw = sorted(json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/vm').text), key=lambda vm: vm['name'])
        self.vms_lst_from_vw = sorted([vm['name'] for vm in self.vms_from_vw])
        for vm in self.vms_from_vw:
            vm['data'] = json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/vm/{vm['vm']}').text)
            vm['interfaces'] = json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/vm/{vm['vm']}/guest/networking/interfaces').text)
            vm['routes'] = json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/vm/{vm['vm']}/guest/networking/routes').text)
            vm['filesystems'] = json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/vm/{vm['vm']}/guest/local-filesystem').text)
            vm['guest_status'] = json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/vm/{vm['vm']}/guest/identity').text)
            vm['folder'] = self.folders_from_vw[vm['name']] if vm['name'] in self.folders_from_vw.keys() else None
            vm['cluster'] = self.clusters_from_vw[vm['name']] if vm['name'] in self.clusters_from_vw.keys() else None
    
    def __loadFoldersFromVMware(self):
        folders_raw_from_vw = {folder['folder']: folder['name'] 
                                   for folder in 
                                   json.loads(self.__vmware.get(f'{self.vm_url}/api/vcenter/folder').text) 
                                   if folder['type'] == 'VIRTUAL_MACHINE'}
        self.folders_lst_from_vw = sorted(set(folders_raw_from_vw.values()))
        self.folders_from_vw = {}
        for folder_id, folder_name in folders_raw_from_vw.items():
            for vm in json.loads(self.__vmware.get(f'{self.vm_url}/rest/vcenter/vm', params={'filter.folders': folder_id}).text)['value']:
                self.folders_from_vw[vm['name']] = folder_name
    
    def __loadNetworksFromVMware(self):
        self.networks_from_vw = {network['network']: network['name'] 
                                     for network in 
                                     json.loads(self.__vmware.get(f"{self.vm_url}/api/vcenter/network").text)}
    
    def __genVMsToNetBox(self):
        cstm = 'custom_fields'

        uuid = 'virtualization_vms_uuid'
        gsts_stat = 'virtualization_vms_guesstatus'
        gsts_os = 'virtualization_vms_guestos'
        disks = 'virtualization_vms_disks'
        iscsi = 'virtualization_vms_iscsi_network_access'
        luns = 'virtualization_vms_have_direct_attach_luns'
        fs_capacity = 'virtualization_vms_filesystems_capacity'
        fs_lst = 'virtualization_vms_filesystems'
        interfaces = 'virtualization_vms_interfaces'
        p_ipv4 = 'virtualization_vms_primaryipv4'
        p_ipv6 = 'virtualization_vms_primaryipv6'
        nics_types = 'virtualization_vms_type_of_nics'
        folder = 'virtualization_vms_folder'
        owners = 'virtualization_vms_owners'
        notes = 'virtualization_vms_notes'

        self.vms_to_netbox = []
        for vm in self.vms_from_vw:
            tVM = {}
            if 'cluster' in vm.keys() and vm['cluster'] in self.clusters_from_nb.keys():
                tVM['cluster'] = self.clusters_from_nb[vm['cluster']]
            tVM['name'] = vm['name']
            tVM['slug'] = vm['name'].lower().replace(' ', '-').replace('_', '-').replace('(', '').replace(')','')
            tVM['status'] = POWER_STATES[vm['power_state']]
            tVM['vcpus'] = vm['cpu_count']
            tVM['memory'] = vm['memory_size_MiB']
            tVM['disk'] = 0
            tVM[cstm] = {}
            tVM[cstm][fs_capacity] = 0
            tVM[cstm][iscsi] = 'No'
            tVM[cstm][gsts_stat] = ('VM OFF' if tVM['status'] != 'active' 
                                    else ('Need install' if'error_type' in vm['guest_status'].keys() else 'OK'))
            tVM[cstm][gsts_os] =  VMWARE_OS_VERSION[vm['data']['guest_OS']]
            tVM[cstm][uuid] = vm['data']['identity']['instance_uuid']
            tVM[cstm][fs_lst] = []
            t_free_space_lst = []
            if 'error_type' not in vm['filesystems'].keys():
                for fs_name, fs_data in vm['filesystems'].items():
                    tFS = {}
                    tFS['mountpoint'] = fs_name
                    tFS['filesystem'] = fs_data.setdefault('filesystem', '')
                    tFS['capacity_in_gb'] = fs_data['capacity'] // GB
                    tFS['freespace_in_gb'] = fs_data['free_space'] // GB
                    if fs_data['free_space'] not in t_free_space_lst:
                        tVM[cstm][fs_capacity] += fs_data['capacity'] // GB
                        t_free_space_lst.append(fs_data['free_space'])
                    tVM[cstm][fs_lst].append(tFS)
            tVM[cstm][disks] = []
            if 'error_type' not in vm['data']['disks'].keys():
                for hdd_name, hdd_data in vm['data']['disks'].items():
                    tDRV = {}
                    tDRV['name'] = hdd_name
                    tDRV['label'] = hdd_data['label']
                    tDRV['vmdk'] = hdd_data['backing']['vmdk_file']
                    tDRV['capacity_in_gb'] = hdd_data['capacity'] // GB
                    tVM['disk'] += hdd_data['capacity'] // GB
                    tVM[cstm][disks].append(tDRV)
            tNICsTypes = []
            tVM[cstm][interfaces] = []
            tVM[cstm][p_ipv4] = None
            tVM[cstm][p_ipv6] = None
            primaryIPv4flag = False
            primaryIPv6flag = False
            for nic_name, nic_data in vm['data']['nics'].items():
                tNIC = {}
                tNIC['name'] = nic_name
                tNIC['state'] = nic_data['state']
                tNIC['vswitch'] = self.networks_from_vw[nic_data['backing']['network']]
                if  tNIC['vswitch'] == NAME_OF_ISCSI_NETWORK:
                    tVM[cstm][iscsi] = 'Yes'
                tNIC['mac'] = nic_data['mac_address'].lower()
                tNIC['type'] = nic_data['type']
                tNICsTypes.append(nic_data['type'])
                tNIC['ips'] = []
                if isinstance(vm['interfaces'], list):
                    for interface in vm['interfaces']:
                        if interface['mac_address'].lower() == nic_data['mac_address'].lower() and 'ip' in interface.keys():
                            for ip in interface['ip']['ip_addresses']:
                                tNIC['ips'].append(ip['ip_address'])
                                if not primaryIPv4flag and len(ip['ip_address']) <= 16:
                                    tVM[cstm][p_ipv4] = ip['ip_address']
                                    primaryIPv4flag = True
                                if not primaryIPv6flag and len(ip['ip_address']) > 16:
                                    tVM[cstm][p_ipv6] = ip["ip_address"]
                                    primaryIPv6flag = True
                tVM[cstm][interfaces].append(tNIC)
            tVM[cstm][folder] = None if vm['folder'] == 'vm' else f'{vm['folder']}'
            tVM[cstm][luns] =  'Yes' if tVM[cstm][fs_capacity] > tVM['disk'] else 'No'
            tVM[cstm][owners] = (OWNERS_OF_VMS[tVM['name']]['owner'] if tVM['name'] in OWNERS_OF_VMS.keys() else None)
            tVM[cstm][notes] = (OWNERS_OF_VMS[tVM['name']]['note'] if tVM['name'] in OWNERS_OF_VMS.keys() else None)
            tVM[cstm][nics_types] = ', '.join(sorted(set(tNICsTypes)))
            if vm['name'] in self.vms_ids_from_nb.keys():
                tVM['id'] = self.vms_ids_from_nb[vm['name']]

            self.vms_to_netbox.append(tVM)
                
        self.vms_lst_to_upd_in_nb = sorted(set(self.vms_lst_from_vw) & set(self.vms_lst_from_nb))
        self.vms_lst_to_crt_in_nb = sorted(set(self.vms_lst_from_vw) - set(self.vms_lst_from_nb))
        self.vms_lst_to_del_in_nb = sorted(set(self.vms_lst_from_nb) - set(self.vms_lst_from_vw))
        
        self.vms_to_upd_in_nb = [vm for vm in self.vms_to_netbox if vm['name'] in self.vms_lst_to_upd_in_nb]
        self.vms_to_crt_in_nb = [vm for vm in self.vms_to_netbox if vm['name'] in self.vms_lst_to_crt_in_nb]
        self.vms_to_del_in_nb = [{'id': vm['id'], 'name': vm['name']} 
                                 for vm in self.vms_from_nb if vm['name'] in self.vms_lst_to_del_in_nb]

    def __ip_to_int(self, ip):
            if len(ip) <= 15:
                return int(ipaddress.IPv4Address(ip))
            else:
                return int(ipaddress.IPv6Address(ip))

    def __loadIPsFromNetBox(self):
        self.raw_ips_from_nb = self.__netbox.ipam.ip_addresses.list(limit=0).data
        self.ips_from_nb = sorted(list(set([ip['address'].split('/')[0] 
                                            for ip in self.raw_ips_from_nb])), key=self.__ip_to_int)
    
    def __genIPsLists(self):
        cstm = 'custom_fields'
        interfaces = 'virtualization_vms_interfaces'

        self.list_of_ips_01 = {}
        for vm in self.vms_to_netbox:
            if vm['status'] == 'active':
                for interface in vm[cstm][interfaces]:
                    for ip in interface['ips']:
                        self.list_of_ips_01[ip] = vm['name']
        self.list_of_ips_01 = dict(sorted(self.list_of_ips_01.items(), 
                                          key=lambda item: self.__ip_to_int(item[0])))
        
        self.list_of_ips_02 = sorted(list(self.list_of_ips_01.keys()), key=self.__ip_to_int)
        self.list_of_ips_03 = sorted(list(set(self.list_of_ips_02) - (set(self.list_of_ips_02) & set(self.ips_from_nb))), key=self.__ip_to_int) 

        self.list_white_ips_on_vms = {}
        q_ips = 0
        for ip, vm_name in self.list_of_ips_01.items():
            if ipaddress.ip_address(ip).is_global:
                if vm_name not in self.list_white_ips_on_vms.keys():
                    self.list_white_ips_on_vms[vm_name] = []
                if vm_name in self.list_white_ips_on_vms.keys():
                    self.list_white_ips_on_vms[vm_name].append(ip)
                    q_ips += 1  
        q_vms = len(self.list_white_ips_on_vms.keys())
        self.list_white_ips_on_vms = dict(sorted(self.list_white_ips_on_vms.items()))
        list_vms_to_email = [f"<b>{vm}</b> ({' | '.join(ips)})" 
                             for vm, ips in self.list_white_ips_on_vms.items()]
        self.__sendEmail(f'List of VMs ({q_vms}) with public IPs ({q_ips})', list_vms_to_email)

        self.list_vms_with_enabled_ipv6 = {}
        for ip, vm_name in self.list_of_ips_01.items():
            if len(ip) > 15:
                if vm_name not in self.list_vms_with_enabled_ipv6.keys():
                    self.list_vms_with_enabled_ipv6[vm_name] = []
                if vm_name in self.list_vms_with_enabled_ipv6.keys():
                    self.list_vms_with_enabled_ipv6[vm_name].append(ip)    
        q_vms = len(self.list_vms_with_enabled_ipv6.keys())
        self.list_vms_with_enabled_ipv6 = dict(sorted(self.list_vms_with_enabled_ipv6.items()))
        list_vms_to_email = sorted([f'<b>{vm}</b>' for vm in self.list_vms_with_enabled_ipv6.keys()])
        """
        list_vms_to_email = [f"<b>{vm}:</b> {', '.join(ips)}" 
                             for vm, ips in self.list_vms_with_enabled_ipv6.items()]
        """
        self.__sendEmail(f'List of VMs ({q_vms}) with enabled IPv6', list_vms_to_email)

    def syncVMsFromVMwareToNetBox(self):
        if self.vm_flg and self.nb_flg:
            self.__syncClustersFromVMwareToNetBox()

            list_of_events = []
            self.__netbox.virtualization.virtual_machines.update(self.vms_to_upd_in_nb)
            message_to_log = f'<b>Updated {len(self.vms_lst_to_upd_in_nb)} VMs</b>'
            list_of_events.append( f'{message_to_log}')
            self.__dumpLOG(self.result_log_filename, message_to_log)

            self.__netbox.virtualization.virtual_machines.create(self.vms_to_crt_in_nb)
            lst_vm_to_log = ' | '.join(self.vms_lst_to_crt_in_nb)
            message_to_log = f'<b>Created {len(self.vms_lst_to_crt_in_nb)} VMs:</b> ({lst_vm_to_log})'
            list_of_events.append( f'{message_to_log}')
            self.__dumpLOG(self.result_log_filename, message_to_log)
            
            # Witout 'try-except' don't work out of errors on 'netbox-python' library
            try:
                self.__netbox.virtualization.virtual_machines.delete(self.vms_to_del_in_nb)
            except:
                lst_vm_to_log = ' | '.join(self.vms_lst_to_del_in_nb)
                message_to_log = f'<b>Deleted {len(self.vms_lst_to_del_in_nb)} VMs:</b> ({lst_vm_to_log})'
                list_of_events.append( f'{message_to_log}')
                self.__dumpLOG(self.result_log_filename, message_to_log)

            self.__sendEmail('Report about sync of VMs from VMware to NetBox', list_of_events)
            
    # Send Email methods    
    def __sendEmail (self, subject, list_of_values):
        if self.mail_flg:
            header_html = '<html><body>'
            footer_html = f'<hr><a href="{self.nb_url}">NetBox</a></html>'

            body_html = f'<h3>{subject}:</h3>'
            body_html += '<ul><li>'
            body_html += '</li><li>'.join(list_of_values)
            body_html += '</li></ul>'

            message_html = header_html + body_html + footer_html

            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.mail_sender
            message['To'] = '; '.join(self.mail_recipients)
            
            message.attach(MIMEText(message_html, "html"))

            context = ssl.create_default_context()
            with smtplib.SMTP(self.mail_srv, self.mail_prt) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.mail_sender, self.mail_pas)
                for mail_recipient in self.mail_recipients:
                    server.sendmail(self.mail_sender, mail_recipient, message.as_string())

def main():
    netbox = ManageNetBox(vm_flg=conf.vm_flg, vm_url=conf.vm_url, vm_log=conf.vm_log, vm_pas=conf.vm_pas,
                          nb_flg=conf.nb_flg, nb_url=conf.nb_url, nb_key=conf.nb_key,
                          log_flg=conf.log_flg, 
                          errors_log_filename=conf.errors_log_filename, 
                          result_log_filename=conf.result_log_filename,
                          mail_flg=conf.mail_flg, 
                          mail_srv=conf.mail_srv, mail_prt=conf.mail_prt, 
                          mail_sender=conf.mail_sender, mail_pas=conf.mail_pas,
                          mail_recipients=conf.mail_recipients)
    
    #netbox.dumpAllToFiles()
    netbox.syncVMsFromVMwareToNetBox()  #  Sync of VMs (Source=VMware, Destination=NetBox)

if __name__ == '__main__':
    main()