#-------------------------------------------------------------------------------
# Name:        NetBox Sync Tools
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

KB = 2 ** 10  #  1KB in bytes
MB = 2 ** 20  #  1MB in bytes
GB = 2 ** 30  #  1GB in bytes
TB = 2 ** 40  #  1TB in bytes

from xml.etree.ElementInclude import include
from requests.auth import HTTPBasicAuth
import requests
import json
import urllib3
import sys
import smtplib, ssl
from datetime import datetime as dt

import ipaddress
from netbox_python import NetBoxClient
from time import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.utils import formatdate

urllib3.disable_warnings()

RUN_HOUR = int(f'{dt.now():%H}')

def benchmark(func):
    def benchmark_decorator(*args, **kwargs):
        def wrapper():
            start_time = time()
            func()
            end_time = time()
            if len(args) == 0:
                print(f"{(func.__name__ + ':').ljust(33)}{f'{round(end_time - start_time, 2):.2f}'.rjust(8)} с.")
            else:
                print(f"{(args[0] + ':').ljust(33)}{f'{round(end_time - start_time, 2):.2f}'.rjust(8)} с.")
        return wrapper
    return benchmark_decorator

class ManageNetBox:
    def __init__(self, t_conf_filename='config.json'):
        
        self.__readConfigFromFile(t_conf_filename)

        if self.nb_flg:
            self.__connectToNetBox()
        
        if self.vm_flg:
            self.__connectToVMware()

        if self.nb_flg and self.vm_flg:
            pass
    
    def __readConfigFromFile(self, t_conf_filename):
        cf = self.__readJSONFromFile(t_conf_filename)
        self.config_full = cf

        self.log_flg = cf['log_flg'] if 'log_flg' in cf.keys() else False
        self.dump_flg = cf['dump_flg'] if 'dump_flg' in cf.keys() else False

        self.mail_flg = cf['mail_flg'] if 'mail_flg' in cf.keys() else False

        self.nb_flg = cf['nb_flg'] if 'nb_flg' in cf.keys() else False
        self.vm_flg = cf['vm_flg'] if 'vm_flg' in cf.keys() else False

        self.admin_email = cf['admin_email']
        
        if self.log_flg:
            self.errors_log_filename = cf['errors_log_filename']
            self.result_log_filename = cf['result_log_filename']

        if self.mail_flg:
            self.mail_srv = cf['mail_srv']
            self.mail_prt = cf['mail_prt']
            self.mail_sender = cf['mail_sender']
            self.mail_pas = cf['mail_pas']
            
        if self.nb_flg:
            self.nb_url = cf['nb_url']
            self.nb_key = cf['nb_key']

        if self.vm_flg:
            self.vm_url = cf['vm_url']
            self.vm_log = cf['vm_log']
            self.vm_pas = cf['vm_pas']

        self.list_of_vms_prepare_to_backup_job = self.__readListFromFile('list_of_vms_prepare_to_backup_job.txt')
        self.list_of_vms_in_backup_job = self.__readListFromFile('list_of_vms_in_backup_job.txt')

        self.sites = cf['sites']
        
        self.name_of_iscsi_network = cf['name_of_iscsi_network']
        self.min_notification_hour = cf['min_notification_hour']
        self.max_notification_hour = cf['max_notification_hour']
        self.datastores = cf['datastores']
        self.cluster_types = cf['cluster_types']
        
        self.cfs = cf['custom_fields']['cfs']
        self.backup_status = cf[self.cfs]['backup_status']
        self.fs_capacity = cf[self.cfs]['fs_capacity']
        self.guesstatus = cf[self.cfs]['guesstatus']
        self.have_luns = cf[self.cfs]['have_luns']
        self.iscsi_network = cf[self.cfs]['iscsi_network']
        self.guestos = cf[self.cfs]['guestos']
        self.primaryipv4 = cf[self.cfs]['primaryipv4']
        self.primaryipv6 = cf[self.cfs]['primaryipv6']
        self.sans = cf[self.cfs]['sans']
        self.type_of_nics = cf[self.cfs]['type_of_nics']
        self.t_uuid = cf[self.cfs]['t_uuid']
        self.folder = cf[self.cfs]['folder']
        self.disks = cf[self.cfs]['disks']
        self.filesystems = cf[self.cfs]['filesystems']
        self.interfaces = cf[self.cfs]['interfaces']
        self.notes = cf[self.cfs]['notes']
        self.owners = cf[self.cfs]['owners']
        self.purpose = cf[self.cfs]['purpose']
        self.have_public_ips = cf[self.cfs]['have_public_ips']
        self.all_public_ips = cf[self.cfs]['all_public_ips']
        self.all_private_ips = cf[self.cfs]['all_private_ips']
        self.vlans = cf[self.cfs]['vlans']

        self.ignore_to_email = cf[self.cfs]['ignore_to_email']

    # Read and Write files methods
    def dumpAllAboutVMsSyncToFiles(self):
        self.__dumpJSN('dump.vms_from_vw.json', self.vms_from_vw)
        self.__dumpJSN('dump.vms_from_nb.json', self.vms_from_nb)
        
    def __readListFromFile(self, filename):
        with open(filename, 'r', encoding='UTF-8') as f:
            return [line.replace('\n', '') for line in f.readlines()]
        
    def __readJSONFromFile(self, filename):
        with open(filename, 'r', encoding='UTF-8') as f:
            return json.load(f)

    def __dumpLOG(self, filename, data):
        if self.log_flg:
            self.__dumpTXT(filename, f'{dt.now()}: {data.replace('<b>', '').replace('</b>', '')}', 'a')

    def __dumpTXT(self, filename, data, mode='w'):  #  Change 'mode' from 'w' or 'a'
        if data != None and self.dump_flg == True:
            with open(filename, mode, encoding="UTF-8") as f:
                if isinstance(data, list):
                    print('\n'.join(data), file=f)
                else:
                    print(data, file=f)
    
    def __dumpJSN(self, filename, data, mode='w'):  #  Change 'mode' from 'w' or 'a'
        if data != None and self.dump_flg == True:
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
            self.vmware_api_key = self.__vmware.post(f'{self.vm_url}/rest/com/vmware/cis/session', auth=(self.vm_log, self.vm_pas), verify=False).json()['value']
        except Exception as error:
            self.__dumpLOG(self.errors_log_filename, f'Error connect to VMware: {type(error).__name__}')
            sys.exit()

    # Sync data about clusters methods
    def __loadClustersFromNetBox(self):
        self.clusters_from_nb = {}
        self.clusters_ids_from_nb = {}

        for cluster in [cl for cl in self.__netbox.virtualization.clusters.list(limit=0).data
                        if cl['custom_fields']['virtualization_ignore_cl_to_automate'] != True]:
            self.clusters_from_nb[cluster['name']] = [cluster['id'], cluster['site']['id']]
            self.clusters_ids_from_nb[cluster['id']] = cluster['name']
        self.clusters_lst_from_nb = set([cluster for cluster in self.clusters_from_nb.keys()])
    
    def __loadClustersFromVMware(self):
        self.clusters_raw_from_vw = {cluster['cluster']: cluster['name'] for cluster in self.__vmware.get(f'{self.vm_url}/api/vcenter/cluster').json()}
        self.clusters_lst_from_vw = set(self.clusters_raw_from_vw.values())
        self.clusters_from_vw = {}
        for cluster_id, cluster_name in self.clusters_raw_from_vw.items():
            for vm in self.__vmware.get(f'{self.vm_url}/rest/vcenter/vm', params={'filter.clusters': cluster_id}).json()['value']:
                self.clusters_from_vw[vm['name']] = cluster_name

    def __syncClustersFromVMwareToNetBox(self):
        self.clusters_lst_to_crt_in_nb = sorted(set(self.clusters_lst_from_vw) - set(self.clusters_lst_from_nb))
        self.clusters_lst_to_del_in_nb = sorted(set(self.clusters_lst_from_nb) - set(self.clusters_lst_from_vw))
        
        self.clusters_to_crt_in_nb = []
        for cluster_name in self.clusters_lst_to_crt_in_nb:
            t_cluster = {}
            t_cluster['name'] = cluster_name
            t_cluster['type'] = self.cluster_types["vmware"]["id"]
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
    def __loadVMsFromNetBox(self, not_all = True):
        self.vms_from_nb = [vm for vm in self.__netbox.virtualization.virtual_machines.list(limit=0).data 
                            if vm['custom_fields']['virtualization_ignore_to_automate'] != not_all]
        self.vms_lst_from_nb = []
        self.vms_ids_from_nb = {}
        self.vms_uuids_from_nb = {}
        for vm in self.vms_from_nb:
            self.vms_lst_from_nb.append(vm['name'])
            self.vms_ids_from_nb[vm['name']] = vm['id']
            t_uuid_value = {}
            t_uuid_value['name'] = vm['name']
            t_uuid_value['id'] = vm['id']
            self.vms_uuids_from_nb[vm[self.cfs][self.t_uuid]] = t_uuid_value
        self.vms_lst_from_nb.sort()     
    
    def __loadVMsFromVMware(self):
        self.__loadFoldersFromVMware()
        self.__loadNetworksFromVMware()
        self.vms_from_vw = sorted(self.__vmware.get(f'{self.vm_url}/api/vcenter/vm').json(), key=lambda vm: vm['name'])
        self.vms_lst_from_vw = sorted([vm['name'] for vm in self.vms_from_vw])
        for vm in self.vms_from_vw:
            t_url = f'{self.vm_url}/api/vcenter/vm/{vm['vm']}'
            vm['data'] = self.__vmware.get(t_url).json()
            vm['interfaces'] = self.__vmware.get(f'{t_url}/guest/networking/interfaces').json()
            vm['routes'] = self.__vmware.get(f'{t_url}/guest/networking/routes').json()
            vm['filesystems'] = self.__vmware.get(f'{t_url}/guest/local-filesystem').json()
            vm['guest_status'] = self.__vmware.get(f'{t_url}/guest/identity').json()
            vm['folder'] = self.folders_from_vw[vm['name']] if vm['name'] in self.folders_from_vw.keys() else None
            vm['cluster'] = self.clusters_from_vw[vm['name']] if vm['name'] in self.clusters_from_vw.keys() else None
            
        self.vms_uuids_from_vw = {}
        for vm in self.vms_from_vw:
            self.vms_uuids_from_vw[vm['data']['identity']['instance_uuid']] = vm['name']
    
    def __loadFoldersFromVMware(self):
        self.folders_raw_from_vw = {folder['folder']: folder['name'] 
                               for folder in self.__vmware.get(f'{self.vm_url}/api/vcenter/folder').json() 
                               if folder['type'] == 'VIRTUAL_MACHINE'}

        self.folder_path_from_vw = self.__vmware.get(f'{self.vm_url}/rest/vcenter/folder').json() 
        
        self.folders_lst_from_vw = sorted(set(self.folders_raw_from_vw.values()))
        self.folders_from_vw = {}
        for folder_id, folder_name in self.folders_raw_from_vw.items():
            for vm in self.__vmware.get(f'{self.vm_url}/rest/vcenter/vm', params={'filter.folders': folder_id}).json()['value']:
                self.folders_from_vw[vm['name']] = folder_name
    
    def __loadNetworksFromVMware(self):
        self.networks_from_vw = {network['network']: network['name'] for network in self.__vmware.get(f"{self.vm_url}/api/vcenter/network").json()}

    def __loadContactsFromNetBox(self):
        self.contacts_from_netbox = self.__netbox.tenancy.contacts.list(limit=0).data
        self.contacts_from_netbox_shot = {contact['name'].split()[0].lower(): contact['id'] for contact in self.contacts_from_netbox}
        
        try:
            self.contacts_to_netbox = self.__readJSONFromFile('owners_to_netbox99.json')
        except:
            self.contacts_to_netbox = {}

    def __genVMsToNetBox(self):
        self.vms_to_netbox = []
        for vm in self.vms_from_vw:
            tVM = {}
            tVM_all_public_IPs = []
            tVM_all_private_IPs = []
            tVM['name'] = vm['name']
            tVM['slug'] = vm['name'].lower().replace(' ', '-').replace('_', '-').replace('(', '').replace(')','')
            if vm['cluster'] is not None: 
                if vm['cluster'] in self.clusters_from_nb.keys():
                    tVM['cluster'] = self.clusters_from_nb[vm['cluster']][0]
                    tVM['site'] = self.clusters_from_nb[vm['cluster']][1]
            else:
                for prefix, site_id in self.sites.items():
                    if prefix in tVM['name']:
                        tVM['site'] = site_id
            
            tVM['status'] = POWER_STATES[vm['power_state']]
            tVM['vcpus'] = vm['cpu_count']
            tVM['memory'] = vm['memory_size_MiB']
            tVM['disk'] = 0
            tVM[self.cfs] = {}
            if vm['name'] in self.list_of_vms_in_backup_job:
                tVM[self.cfs][self.backup_status] = '_in_backup_job_'
            elif vm['name'] in self.list_of_vms_prepare_to_backup_job:
                tVM[self.cfs][self.backup_status] = '_candidate_'
            else:
                tVM[self.cfs][self.backup_status] = '_none_'
            tVM[self.cfs][self.fs_capacity] = 0
            tVM[self.cfs][self.iscsi_network] = '_none_'
            tVM[self.cfs][self.guesstatus] = ('_vm_off_' if tVM['status'] != 'active' else ('_need_install_' if 'error_type' in vm['guest_status'].keys() else '_ok_'))
            tVM[self.cfs][self.guestos] =  VMWARE_OS_VERSION[vm['data']['guest_OS']]
            tVM[self.cfs][self.t_uuid] = vm['data']['identity']['instance_uuid']
            tVM[self.cfs][self.filesystems] = []
            t_free_space_lst = []
            if 'error_type' not in vm['filesystems'].keys():
                for fs_name, fs_data in vm['filesystems'].items():
                    tFS = {}
                    tFS['mountpoint'] = fs_name
                    tFS['filesystem'] = fs_data.setdefault('filesystem', '')
                    tFS['capacity_in_gb'] = fs_data['capacity'] // GB
                    tFS['freespace_in_gb'] = fs_data['free_space'] // GB
                    if fs_data['free_space'] not in t_free_space_lst:
                        tVM[self.cfs][self.fs_capacity] += fs_data['capacity'] // GB
                        t_free_space_lst.append(fs_data['free_space'])
                    tVM[self.cfs][self.filesystems].append(tFS)
            tVM[self.cfs][self.disks] = []
            tVM[self.cfs][self.sans] = set()
            if 'error_type' not in vm['data']['disks'].keys():
                for hdd_name, hdd_data in vm['data']['disks'].items():
                    tDRV = {}
                    tDRV['name'] = hdd_name
                    tDRV['label'] = hdd_data['label']
                    tDRV['vmdk'] = hdd_data['backing']['vmdk_file']
                    t_str01 = hdd_data['backing']['vmdk_file'].split('[')[1].split(']')[0]
                    if t_str01 in self.datastores.keys():
                        tVM[self.cfs][self.sans].add(self.datastores[t_str01])
                    tDRV['capacity_in_gb'] = hdd_data['capacity'] // GB
                    tVM['disk'] += hdd_data['capacity'] // GB
                    tVM[self.cfs][self.disks].append(tDRV)
            tVM[self.cfs][self.sans] = ', '.join(sorted(list(tVM[self.cfs][self.sans])))
            tNICsTypes = []
            tVM[self.cfs][self.interfaces] = []
            tVM[self.cfs][self.primaryipv4] = None
            tVM[self.cfs][self.primaryipv6] = None
            primaryIPv4flag = False
            primaryIPv6flag = False
            tVM[self.cfs][self.have_public_ips] = '_none_'
            tVLANs = []
            for nic_name, nic_data in vm['data']['nics'].items():
                tNIC = {}
                tNIC['name'] = nic_name
                tNIC['state'] = nic_data['state']
                if 'network' in nic_data['backing'].keys():
                    tNIC['vswitch'] = self.networks_from_vw[nic_data['backing']['network']]
                    tVLANs.append(tNIC['vswitch'])
                else:
                    tNIC['vswitch'] = None
                if  tNIC['vswitch'] in self.name_of_iscsi_network:
                    tVM[self.cfs][self.iscsi_network] = '_yes_'
                tNIC['mac'] = nic_data['mac_address'].lower()
                tNIC['type'] = nic_data['type']
                tNICsTypes.append(nic_data['type'])
                tNIC['ips'] = []
                if isinstance(vm['interfaces'], list):
                    for interface in vm['interfaces']:
                        if (interface['mac_address'].lower() == nic_data['mac_address'].lower() 
                            and 'ip' in interface.keys()):
                            for ip in interface['ip']['ip_addresses']:
                                tNIC['ips'].append(ip['ip_address'])
                                if ipaddress.ip_address(ip['ip_address']).is_global:
                                    tVM[self.cfs][self.have_public_ips] = '_yes_'
                                    tVM_all_public_IPs.append(ip['ip_address'])
                                else:
                                    tVM_all_private_IPs.append(ip['ip_address'])
                                if not primaryIPv4flag and ':' not in ip['ip_address']:
                                    tVM[self.cfs][self.primaryipv4] = ip['ip_address']
                                    primaryIPv4flag = True
                                if not primaryIPv6flag and ':' in ip['ip_address']:
                                    tVM[self.cfs][self.primaryipv6] = ip["ip_address"]
                                    primaryIPv6flag = True
                tVM[self.cfs][self.interfaces].append(tNIC)
            
            tVM[self.cfs][self.vlans] = ', '.join(sorted(tVLANs))

            tVM[self.cfs][self.all_public_ips] = ', '.join(sorted(tVM_all_public_IPs, key=self.__ip_to_int))
            tVM[self.cfs][self.all_private_ips] = ', '.join(sorted(tVM_all_private_IPs, key=self.__ip_to_int))
            
            tVM[self.cfs][self.folder] = None if vm['folder'] == 'vm' else f'{vm['folder']}'
            tVM[self.cfs][self.have_luns] =  '_yes_' if tVM[self.cfs][self.fs_capacity] > tVM['disk'] else '_none_'
            tVM[self.cfs][self.type_of_nics] = ', '.join(sorted(set(tNICsTypes)))
            
            if tVM[self.cfs][self.t_uuid] in self.vms_uuids_from_nb.keys():
                tVM['id'] = self.vms_uuids_from_nb[tVM[self.cfs][self.t_uuid]]['id']
            
            if tVM['name'] in self.contacts_to_netbox.keys():
                tVM[self.cfs][self.owners] = []
                for contact in self.contacts_to_netbox[tVM['name']]:
                    tVM[self.cfs][self.owners].append({"id": self.contacts_from_netbox_shot[contact]})
            
            self.vms_to_netbox.append(tVM)
        
        self.vms_lst_uuids_to_upd_in_nb = sorted(set(self.vms_uuids_from_vw.keys()) & set(self.vms_uuids_from_nb.keys()))
        self.vms_lst_uuids_to_crt_in_nb = sorted(set(self.vms_uuids_from_vw.keys()) - set(self.vms_uuids_from_nb.keys()))
        self.vms_lst_uuids_to_del_in_nb = sorted(set(self.vms_uuids_from_nb.keys()) - set(self.vms_uuids_from_vw.keys()))
        
        self.vms_to_netbox_X = {vm[self.cfs][self.t_uuid]: vm for vm in self.vms_to_netbox}
        self.vms_from_netbox_X = {vm[self.cfs][self.t_uuid]: vm for vm in self.vms_from_nb}

        self.vms_to_upd_in_nb = []

        for vm in self.vms_to_netbox:
            if vm[self.cfs][self.t_uuid] in self.vms_lst_uuids_to_upd_in_nb:
                if self.__VMisChangedByUUID(vm[self.cfs][self.t_uuid]):
                    self.vms_to_upd_in_nb.append(vm)

        self.vms_to_crt_in_nb = [vm for vm in self.vms_to_netbox if vm[self.cfs][self.t_uuid] in self.vms_lst_uuids_to_crt_in_nb]
        self.vms_to_del_in_nb = [{'id': vm['id'], 'name': vm['name']} for vm in self.vms_from_nb if vm[self.cfs][self.t_uuid] in self.vms_lst_uuids_to_del_in_nb]

        self.vms_lst_to_upd_in_nb = sorted(vm['name'] for vm in self.vms_to_upd_in_nb)
        self.vms_lst_to_crt_in_nb = sorted(vm['name'] for vm in self.vms_to_crt_in_nb)
        self.vms_lst_to_del_in_nb = sorted(vm['name'] for vm in self.vms_to_del_in_nb)

    def __VMisChangedByUUID(self, uuid):
        if not('cluster' not in self.vms_to_netbox_X[uuid].keys() and self.vms_from_netbox_X[uuid]['cluster'] is None):
            if self.vms_to_netbox_X[uuid]['cluster'] != self.vms_from_netbox_X[uuid]['cluster']['id']:
                return True
        
        if self.vms_to_netbox_X[uuid]['status'] != self.vms_from_netbox_X[uuid]['status']['value']:
            return True

        for f in ['name', 'vcpus', 'memory', 'disk']:
            if self.vms_to_netbox_X[uuid][f] != self.vms_from_netbox_X[uuid][f]:
                return True
        
        list_of_fields_to_ignore = ['cfs', 'notes', 'owners', 'purpose', 'ignore_to_email']

        for f_key, f_val in self.config_full[self.cfs].items():
            if f_key not in list_of_fields_to_ignore:
                if self.vms_to_netbox_X[uuid][self.cfs][f_val] != self.vms_from_netbox_X[uuid][self.cfs][f_val]:
                    return True
                
        return False

    def __ip_to_int(self, ip):
            if len(ip) <= 15:
                return int(ipaddress.IPv4Address(ip))
            else:
                return int(ipaddress.IPv6Address(ip))

    def __loadIPsFromNetBox(self):
        self.raw_ips_from_nb = self.__netbox.ipam.ip_addresses.list(limit=0).data
        try:
            self.ips_from_nb = sorted(list(set([ip['address'].split('/')[0] 
                                                for ip in self.raw_ips_from_nb])), key=self.__ip_to_int)
        except Exception as error:
            self.__sendEmail(f'Error of parsing of IPs data in IPAM', 
                             [f'Error of parsing of IPs data in IPAM: {type(error).__name__} {error.args}'], self.__readListFromFile('mail_list_to_vms_sync.txt'))
            sys.exit()

    def __genAllPublicIPsListInNetBox(self):
        self.all_public_ips = {}
        self.all_public_ips_by_owner = {}
        for ip in self.raw_ips_from_nb:
            t_ip = ip['address'].split('/')[0]
            if ipaddress.ip_address(t_ip).is_global and ip['status']['value'] == 'active':
                self.all_public_ips[t_ip] = ip['description'] if ip['description'] != '' else 'NO DESCRIPTION'
        self.all_public_ips_by_desc = {}
        for ip, desc in self.all_public_ips.items():
            if desc not in self.all_public_ips_by_desc.keys():
                self.all_public_ips_by_desc[desc] = []
            self.all_public_ips_by_desc[desc].append(ip)
        self.all_public_ips_by_desc = dict(sorted(self.all_public_ips_by_desc.items()))

    def loadAndSendPublicIPsFromNetBoxIPAM(self):
        self.__loadIPsFromNetBox()
        self.__genAllPublicIPsListInNetBox()
        if self.dump_flg:
            self.__dumpJSN("dump.ips_from_nb.json", self.ips_from_nb)            
            self.__dumpJSN("dump.raw_ips_from_nb.json", self.raw_ips_from_nb)
            self.__dumpJSN("dump.all_public_ips.json", self.all_public_ips)
            self.__dumpJSN("dump.all_public_ips_by_desc.json", self.all_public_ips_by_desc)
        self.list_ips_to_email = [f"<b>{ip}</b> ({description if description != 'NO DESCRIPTION' else f'<b style="color:#FF0000">{description}</b>'})" 
                                  for ip, description in self.all_public_ips.items()]
        q_ips = len(self.all_public_ips)
        if self.min_notification_hour <= RUN_HOUR < self.max_notification_hour:
            self.__sendEmail(f'Full List of Public IPs ({q_ips}) in NetBox by IP', 
                             self.list_ips_to_email, self.__readListFromFile('mail_full_list_of_public_ips_in_netbox_ipam.txt'))
        
        self.list_ips_to_email = [f"<b>{description if description != 'NO DESCRIPTION' else f'<span style="color:#FF0000">{description}</span>'}</b> ({' | '.join(ips)})" 
                                  for description, ips in self.all_public_ips_by_desc.items()]
        q_decs = len(self.all_public_ips_by_desc)
        if self.min_notification_hour <= RUN_HOUR < self.max_notification_hour:
            self.__sendEmail(f'Full List of Public IPs ({q_ips}) in NetBox by Description ({q_decs})', 
                             self.list_ips_to_email, self.__readListFromFile('mail_full_list_of_public_ips_in_netbox_ipam.txt'))

    def __genIPsLists(self):
        # List of IPs in NetBox with VM
        self.list_of_ips_00 = {}
        for vm in self.vms_from_nb:
            if vm['status']['value'] == 'active':
                if vm[self.cfs][self.interfaces] != None:
                    for interface in vm[self.cfs][self.interfaces]:
                        for ip in interface['ips']:
                            self.list_of_ips_00[ip] = vm['name']
        self.list_of_ips_00 = dict(sorted(self.list_of_ips_00.items(), key=lambda item: self.__ip_to_int(item[0])))
        
        # List of IPs to NetBox with VM
        self.list_of_ips_01 = {}
        for vm in self.vms_to_netbox:
            if vm['status'] == 'active':
                for interface in vm[self.cfs][self.interfaces]:
                    for ip in interface['ips']:
                        self.list_of_ips_01[ip] = vm['name']
        self.list_of_ips_01 = dict(sorted(self.list_of_ips_01.items(), key=lambda item: self.__ip_to_int(item[0])))
        
        self.list_added_ips = {}
        self.list_removed_ips = {}

        for ip, vm in self.list_of_ips_00.items():
            if ip not in self.list_of_ips_01.keys():
                self.list_removed_ips[ip] = vm

        for ip, vm in self.list_of_ips_01.items():
            if ip not in self.list_of_ips_00.keys():
                self.list_added_ips[ip] = vm

        self.list_ips_to_email = []
        for ip, vm in self.list_added_ips.items():
            self.list_ips_to_email.append(f"Added <b>{ip}</b> ({vm})")
        for ip, vm in self.list_removed_ips.items():
            self.list_ips_to_email.append(f"Removed <b>{ip}</b> ({vm})")
        
        q_ips = len(self.list_ips_to_email)
        if q_ips > 0:
            self.__sendEmail(f'List of changed IPs ({q_ips})', self.list_ips_to_email, self.__readListFromFile('mail_list_to_change_ip.txt'))
        
        self.list_added_white_ips = {}
        self.list_removed_white_ips = {}

        for ip, vm in self.list_of_ips_00.items():
            if len(ip) <= 15 and ipaddress.ip_address(ip).is_global:
                if ip not in self.list_of_ips_01.keys():
                    self.list_removed_white_ips[ip] = vm

        for ip, vm in self.list_of_ips_01.items():
            if len(ip) <= 15 and ipaddress.ip_address(ip).is_global:
                if ip not in self.list_of_ips_00.keys():
                    self.list_added_white_ips[ip] = vm

        self.list_ips_to_email = []
        for ip, vm in self.list_added_white_ips.items():
            self.list_ips_to_email.append(f"Added <b>{ip}</b> ({vm})")
        for ip, vm in self.list_removed_white_ips.items():
            self.list_ips_to_email.append(f"Removed <b>{ip}</b> ({vm})")
        
        q_ips = len(self.list_ips_to_email)
        if q_ips > 0:
            self.__sendEmail(f'List of changed public IPs ({q_ips})', self.list_ips_to_email, self.__readListFromFile('mail_list_to_change_public_ip.txt'))
        
        self.list_of_ips_02 = sorted(list(self.list_of_ips_01.keys()), key=self.__ip_to_int)
        self.list_of_ips_03 = sorted(list(set(self.list_of_ips_02) - (set(self.list_of_ips_02) & set(self.ips_from_nb))), key=self.__ip_to_int) 

        self.ips_to_ipam_nb = {ip: self.list_of_ips_01[ip] for ip in self.list_of_ips_03 if len(ip) <= 16}
        self.list_ips_to_email = [f"<b>{ip}</b> ({vm})" for ip, vm in self.ips_to_ipam_nb.items()]
        q_ips = len(self.list_ips_to_email)
        if self.min_notification_hour <= RUN_HOUR < self.max_notification_hour and q_ips > 0:
            self.__sendEmail(f'List of IPs ({q_ips}) to create in IPAM', self.list_ips_to_email, self.__readListFromFile('mail_list_to_ipam_create.txt'))

        self.list_white_ips_on_vms = {}
        q_ips = 0
        for ip, vm_name in self.list_of_ips_01.items():
            if ipaddress.ip_address(ip).is_global:
                if vm_name not in self.list_white_ips_on_vms.keys():
                    self.list_white_ips_on_vms[vm_name] = []
                self.list_white_ips_on_vms[vm_name].append(ip)
                q_ips += 1  
        
        q_vms = len(self.list_white_ips_on_vms.keys())
        self.list_white_ips_on_vms = dict(sorted(self.list_white_ips_on_vms.items()))
        self.list_vms_to_email = [f"<b>{vm}</b> ({' | '.join(ips)})" for vm, ips in self.list_white_ips_on_vms.items()]
        if self.min_notification_hour <= RUN_HOUR < self.max_notification_hour:
            self.__sendEmail(f'List of VMs ({q_vms}) with public IPs ({q_ips})', self.list_vms_to_email, self.__readListFromFile('mail_list_to_public_ip.txt'))
            
        self.list_vms_with_enabled_ipv6 = {}
        for ip, vm_name in self.list_of_ips_01.items():
            if len(ip) > 15:
                if vm_name not in self.list_vms_with_enabled_ipv6.keys():
                    self.list_vms_with_enabled_ipv6[vm_name] = []
                self.list_vms_with_enabled_ipv6[vm_name].append(ip)
            
        q_vms = len(self.list_vms_with_enabled_ipv6.keys())
        self.list_vms_with_enabled_ipv6 = dict(sorted(self.list_vms_with_enabled_ipv6.items()))
        list_vms_to_email = sorted([f'<b>{vm}</b> ({' | '.join(ips)})' for vm, ips in self.list_vms_with_enabled_ipv6.items()])
        if self.min_notification_hour <= RUN_HOUR < self.max_notification_hour:
            self.__sendEmail(f'List of VMs ({q_vms}) with enabled IPv6 that need to be disabled', list_vms_to_email, self.__readListFromFile('mail_list_to_ipv6_disable.txt'))

    def syncVMsFromVMwareToNetBox(self):
        if self.vm_flg and self.nb_flg:
            self.__loadClustersFromNetBox()  #  To 'self.clusters_from_nb' JSON
            self.__loadIPsFromNetBox()
            self.__loadVMsFromNetBox()       #  To 'self.vms_from_nb' JSON and 'self.vms_lst_from_nb' lst
            self.__loadContactsFromNetBox()  

            self.__loadClustersFromVMware()  #  To 'self.clusters_from_vw' JSON and 'self.clusters_lst_from_vw' lst
            self.__loadVMsFromVMware()       #  To 'self.vms_from_vw' JSON and 'self.vms_lst_from_vw' lst

            self.__genVMsToNetBox()          #  To 'self.vms_to_netbox' JSON in NetBox format
            self.__genIPsLists()             #  To 'self.list_of_ips_01' JSON and 'self.list_of_ips_02' JSON
            
            self.__syncClustersFromVMwareToNetBox()

            list_of_events = []
            
            self.__netbox.virtualization.virtual_machines.update(self.vms_to_upd_in_nb)
            lst_vm_to_log = ' | \n'.join(self.vms_lst_to_upd_in_nb)
            message_to_log = f'<b>Updated {len(self.vms_lst_to_upd_in_nb)} VMs</b> ({lst_vm_to_log})'
            #print(message_to_log)
            list_of_events.append( f'{message_to_log}')
            self.__dumpLOG(self.result_log_filename, message_to_log)
            
            # Witout 'try-except' don't work out of errors on 'netbox-python' library
            try:
                self.__netbox.virtualization.virtual_machines.delete(self.vms_to_del_in_nb)
                lst_vm_to_log = ' | \n'.join(self.vms_lst_to_del_in_nb)
                message_to_log = f'<b>Deleted {len(self.vms_lst_to_del_in_nb)} VMs:</b> ({lst_vm_to_log})'
                #print(message_to_log)
                if len(self.vms_lst_to_del_in_nb) > 0:
                    list_of_events.append( f'{message_to_log}')
                self.__dumpLOG(self.result_log_filename, message_to_log)
            except:
                lst_vm_to_log = ' | \n'.join(self.vms_lst_to_del_in_nb)
                message_to_log = f'<b>Deleted {len(self.vms_lst_to_del_in_nb)} VMs:</b> ({lst_vm_to_log})'
                #print(message_to_log)
                if len(self.vms_lst_to_del_in_nb) > 0:
                    list_of_events.append( f'{message_to_log}')
                self.__dumpLOG(self.result_log_filename, message_to_log)

            self.__netbox.virtualization.virtual_machines.create(self.vms_to_crt_in_nb)
            lst_vm_to_log = ' | \n'.join(self.vms_lst_to_crt_in_nb)
            message_to_log = f'<b>Created {len(self.vms_lst_to_crt_in_nb)} VMs:</b> ({lst_vm_to_log})'
            #print(message_to_log)
            if len(self.vms_lst_to_crt_in_nb) > 0:
                list_of_events.append( f'{message_to_log}')
            self.__dumpLOG(self.result_log_filename, message_to_log)

            t_len = len(self.vms_from_vw)
            self.__sendEmail(f'Report about sync of VMs ({t_len}) from VMware to NetBox', 
                             list_of_events, self.__readListFromFile('mail_list_to_vms_sync.txt'))
            if len(self.vms_to_crt_in_nb) > 0 or len(self.vms_to_del_in_nb) > 0:
                self.__sendEmail(f'Report about sync of VMs ({t_len}) from VMware to NetBox', 
                                 list_of_events, self.__readListFromFile('mail_list_to_changed_vms_sync.txt'))
            
            if self.dump_flg:
                self.dumpAllAboutVMsSyncToFiles() # Dump all data about VMs sync to files
            
    # Send Email methods
    def __sendEmail (self, subject, list_of_values, mail_recipients, title=None):
        if self.mail_flg:
            date = f'{dt.now():%Y-%m-%d %H:%M:%S}'
            
            header_html = '<html>\n<body>'

            vms_url = f'virtualization/virtual-machines'

            footer_html = f"""\
                <hr>\n
                <a href="{self.nb_url}">NetBox</a>\n
                <br><a href="{self.nb_url}/{vms_url}/">NetBox | All VMs</a>\n
                """
            
            body_html = f'<h4>{subject if title == None else title}{(' (' + date + ')') if title == None else ''}</h4>'
            body_html += '<ul>\n<li>'
            body_html += '</li>\n<li>'.join(list_of_values)
            body_html += '</li>\n</ul>\n'

            message_html = header_html + body_html + footer_html

            message_text = f'{subject} ({date})\n\n- '
            message_text += '\n- '.join([string.replace('<b>' , '').replace('</b>', '') for string in list_of_values])

            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.mail_sender
            message['To'] = '; '.join(mail_recipients)
            message['Date'] = formatdate(localtime=True)
            
            message.attach(MIMEText(message_text, "text"))
            message.attach(MIMEText(message_html, "html"))

            context = ssl.create_default_context()
            with smtplib.SMTP(self.mail_srv, self.mail_prt) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.mail_sender, self.mail_pas)
                for mail_recipient in mail_recipients:
                    server.sendmail(self.mail_sender, mail_recipient, str(message).encode('utf-8'))
    
    def sendMessagesToVMsOwners(self):
        self.__loadContactsFromNetBox()  #  self.contacts_from_netbox
        self.__loadVMsFromNetBox(False)  #  self.vms_from_nb

        self.list_of_owners_w_vms = {}
        for contact in self.contacts_from_netbox:
            t_list = {}
            
            t_list['name_short'] = contact['name']
            t_list['name_full'] = contact['title']
            t_list['email'] = contact['email']
            t_list['ignore_email'] = contact[self.cfs][self.ignore_to_email]
            t_list['vms_wo_purpose'] = []

            self.list_of_owners_w_vms[contact['id']] = t_list

        for vm in self.vms_from_nb:
            if vm[self.cfs][self.owners] != None and vm[self.cfs][self.purpose] == None:
                t_vm = {}
                t_vm['name'] = vm['name']
                t_vm['url'] = vm['url'].replace('api/', '')
                for owner in vm[self.cfs][self.owners]:
                    self.list_of_owners_w_vms[owner['id']]['vms_wo_purpose'].append(t_vm)

        email_name = 'Требуется уточнить данные о ВМ, в которых Вы указаны как владелец'
        for onwer_key, owner_val in self.list_of_owners_w_vms.items():
            if owner_val['ignore_email'] == '_yes_':
                continue

            list_of_vms_with_url = []
            for vm in owner_val['vms_wo_purpose']:
                list_of_vms_with_url.append(f'<a href="{vm['url']}">{vm['name']}</a>')
            
            link_to_vms_by_owner = f'{self.nb_url}/virtualization/virtual-machines/?cf_virtualization_vms_owners={onwer_key}'

            email_message = f"""Уважаемый {owner_val['name_short']}!<br><br>\n\
                В ВМ ({len(list_of_vms_with_url)} шт.), указанных ниже списком (кликабельно), Вы указаны как владелец.<br>\n
                Требуется заполнить для указанных в письме ВМ поле "Purpose".<br><br>\n
                <a href="{link_to_vms_by_owner}">Ссылка на все ВМ, в которых Вы указаны как владелец.</a><br>
                """
            
            t_emails_list = []
            t_emails_list.append(owner_val['email'])
            t_emails_list.append(self.admin_email)
            
            if len(list_of_vms_with_url) > 0 and self.min_notification_hour <= RUN_HOUR < self.max_notification_hour:
                self.__sendEmail(email_name, list_of_vms_with_url, t_emails_list, email_message)

def main():
    netbox = ManageNetBox()
    netbox.syncVMsFromVMwareToNetBox()
    netbox.loadAndSendPublicIPsFromNetBoxIPAM()
    netbox.sendMessagesToVMsOwners()
    
if __name__ == '__main__':
    main()