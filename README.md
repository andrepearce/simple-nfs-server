# simple-nfs-server

This repository contains anisble roles and a playbook that will provision a basic NFS server to localhost, with a firewall in front.

## Pre-requisites

- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Python3](https://www.python.org/downloads/)

## Provisioning

The playbook by default will provision the NFS server on the localhost. The below steps are an example of how you can use this playbook to provision the NFS server:

1. `cd` to the root directory of this repository.
2. Edit `roles/nfs-exports/vars/main.yaml` to export the directories you require.
3. Execute `./provision.yaml -K`.
4. Enter your sudo password.

## Additional Resources

The following is a list of additional resource that I found useful when debugging the NFS server or when attempting to mount a shared folder.

- https://www.tecmint.com/how-to-setup-nfs-server-in-linux/
- https://www.howtoforge.com/nfs-server-and-client-on-centos-7
- https://unix.stackexchange.com/questions/252812/user-permissions-in-nfs-mounted-directory#252815
- https://forums.macrumors.com/threads/nfs-operation-not-permitted.317044/