###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

from Products.ZenRelations.RelSchema import ToManyCont, ToOne

from ZenPacks.zenoss.CloudStack import BaseComponent


class Zone(BaseComponent):
    meta_type = portal_type = "CloudStackZone"

    guest_cidr_address = None
    dhcp_provider = None
    dns1 = None
    dns2 = None
    internal_dns1 = None
    internal_dns2 = None
    network_type = None
    security_groups_enabled = None
    vlan = None
    zone_token = None
    domain = None

    _properties = BaseComponent._properties + (
        {'id': 'guest_cidr_address', 'type': 'string', 'mode': ''},
        {'id': 'dhcp_provider', 'type': 'string', 'mode': ''},
        {'id': 'dns1', 'type': 'string', 'mode': ''},
        {'id': 'dns2', 'type': 'string', 'mode': ''},
        {'id': 'internal_dns1', 'type': 'string', 'mode': ''},
        {'id': 'internal_dns2', 'type': 'string', 'mode': ''},
        {'id': 'network_type', 'type': 'string', 'mode': ''},
        {'id': 'security_groups_enabled', 'type': 'boolean', 'mode': ''},
        {'id': 'vlan', 'type': 'string', 'mode': ''},
        {'id': 'zone_token', 'type': 'string', 'mode': ''},
        {'id': 'domain', 'type': 'string', 'mode': ''},
        )

    _relations = BaseComponent._relations + (
        ('cloud', ToOne(ToManyCont,
            'ZenPacks.zenoss.CloudStack.Cloud.Cloud',
            'zones')
            ),

        ('pods', ToManyCont(ToOne,
            'ZenPacks.zenoss.CloudStack.Pod.Pod',
            'zone')
            ),

        ('vms', ToManyCont(ToOne,
            'ZenPacks.zenoss.CloudStack.VirtualMachine.VirtualMachine',
            'zone')
            ),
        )

    def device(self):
        return self.cloud()
