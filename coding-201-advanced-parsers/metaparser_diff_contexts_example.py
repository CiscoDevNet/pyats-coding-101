'''
Metaparser with different contexts example
------------------------------------------
   The below example will show the importance of having a common unified
   parser structure among different contexts.

   ** Both contexts (cli and xml) should comply with the schema defined in
      the inherited class 'ParserSchema'. 
'''

# Python
import re
import pprint
import xml.etree.ElementTree as ET

# Metaparser
from metaparser import MetaParser
# Schema is the user datastructure that every output from the inheriting class
# should comply with.
    # * Any : Marks a section of a schema that matches anything.
    # * Optional : Marks an optional part of the schema.
    # * OR : Defines a schema of OR relationship, eg, the input data must pass
    # the validation of one of the requirements of this Schema.
from metaparser.util.schemaengine import Schema, Any, Optional, Or

# parser utils
# ** This is needed to compare the cli created from the xml tags is matching
# ** with the cli used in the cli function.
from parser.utils.common import Common


class ParserSchema(MetaParser):

    schema = {
        'vrf': {
            Any(): {
                'rpm_handle_count': int,
                Optional('route_map'): {
                    Any():{
                        Any(): {
                            'action': str,
                            'seq_num': int,
                            'total_accept_count': int,
                            'total_reject_count': int,
                            Optional('command'): {
                                'compare_count': int,
                                'match_count': int,
                                'command': str
                            }
                        },
                    },
                }
            },
        }
    }


class Parser(ParserSchema):

    show_command = 'show bgp vrf all ipv4 unicast policy statistics redistribute'

    cli_input = '''
        Details for VRF default
        Total count for redistribute rpm handles: 1

        C: No. of comparisions, M: No. of matches

        route-map ADD_RT_400_400 permit 10

        Total accept count for policy: 0     
        Total reject count for policy: 0     
        Details for VRF ac
        BGP policy statistics not available
        Details for VRF vpn1
        Total count for redistribute rpm handles: 1

        C: No. of comparisions, M: No. of matches

        route-map PERMIT_ALL_RM permit 20

        Total accept count for policy: 0     
        Total reject count for policy: 0     
        Details for VRF vpn2
        BGP policy statistics not available

    '''

    xml_input = '''<?xml version="1.0" encoding="ISO-8859-1"?>
        <nf:rpc-reply xmlns="http://www.cisco.com/nxos:7.0.3.I7.2.:bgp" xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0">
         <nf:data>
          <show>
           <bgp>
            <vrf>
             <all>
              <ipv4>
               <unicast>
                <policy>
                 <statistics>
                  <redistribute>
                   <__readonly__>
                    <TABLE_vrf>
                     <ROW_vrf>
                      <vrf-name-polstats>default</vrf-name-polstats>
                      <rpm-handle-count>1</rpm-handle-count>
                      <TABLE_rmap>
                       <ROW_rmap>
                        <name>ADD_RT_400_400</name>
                        <action>permit</action>
                        <seqnum>10</seqnum>
                        <totalacceptcount>0</totalacceptcount>
                        <totalrejectcount>0</totalrejectcount>
                       </ROW_rmap>
                      </TABLE_rmap>
                     </ROW_vrf>
                     <ROW_vrf>
                      <vrf-name-polstats>ac</vrf-name-polstats>
                      <rpm-handle-count>0</rpm-handle-count>
                     </ROW_vrf>
                     <ROW_vrf>
                      <vrf-name-polstats>vpn1</vrf-name-polstats>
                      <rpm-handle-count>1</rpm-handle-count>
                      <TABLE_rmap>
                       <ROW_rmap>
                        <name>PERMIT_ALL_RM</name>
                        <action>permit</action>
                        <seqnum>20</seqnum>
                        <totalacceptcount>0</totalacceptcount>
                        <totalrejectcount>0</totalrejectcount>
                       </ROW_rmap>
                      </TABLE_rmap>
                     </ROW_vrf>
                     <ROW_vrf>
                      <vrf-name-polstats>vpn2</vrf-name-polstats>
                      <rpm-handle-count>0</rpm-handle-count>
                     </ROW_vrf>
                    </TABLE_vrf>
                   </__readonly__>
                  </redistribute>
                 </statistics>
                </policy>
               </unicast>
              </ipv4>
             </all>
            </vrf>
           </bgp>
          </show>
         </nf:data>
        </nf:rpc-reply>
        ]]>]]>
    '''

    def cli(self):

        # Init vars
        cli_parsed_output = {}
        index = 1
        vrf = 'default'

        for line in self.cli_input.splitlines():
            line = line.strip()

            # Details for VRF default
            p1 = re.compile(r'^Details +for +VRF +'
                             '(?P<vrf>[\w\-]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                nei_flag = True
                continue

            # No such neighbor
            if re.compile(r'No +such +neighbor$').match(line):
                nei_flag = False

            # regexp to parse the below different outputs
            # ** Total count for redistribute rpm handles: 1
            # ** Total count for neighbor rpm handles: 1
            # ** Total count for dampening rpm handles: 1
            p2 = re.compile(r'^Total +count +for +(?P<type>\w+) +rpm +handles: +'
                             '(?P<handles>\d+)$')
            m = p2.match(line)

            # regexp to parse the below output
            # ** BGP policy statistics not available
            p3 = re.compile(r'^BGP +policy +statistics +not +available$')
            m1 = p3.match(line)

            if m or m1:
                if 'vrf' not in cli_parsed_output:
                    cli_parsed_output['vrf'] = {}

                if vrf not in cli_parsed_output['vrf']:
                    cli_parsed_output['vrf'][vrf] = {}

                cli_parsed_output['vrf'][vrf]['rpm_handle_count'] = \
                    int(m.groupdict()['handles']) if m else 0
                continue

            # regexp to parse the below different outputs
            # ** route-map Filter-pip deny 10
            # ** route-map ADD_RT_400_400 permit 10
            # ** route-map RMAP_DIRECT->BGP_IPV4 permit 10
            p4 = re.compile(r'^route\-map +(?P<name>\S+) +'
                             '(?P<action>\w+) +(?P<seqnum>\d+)$')
            m = p4.match(line)
            if m:
                name = m.groupdict()['name']

                if 'route_map' not in cli_parsed_output['vrf'][vrf]:
                    cli_parsed_output['vrf'][vrf]['route_map'] = {}

                if name not in cli_parsed_output['vrf'][vrf]['route_map']:
                    cli_parsed_output['vrf'][vrf]['route_map'][name] = {}
                    index = 1
                else:
                    index += 1

                if index not in cli_parsed_output['vrf'][vrf]['route_map'][name]:
                    cli_parsed_output['vrf'][vrf]['route_map'][name][index] = {}

                cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                    ['action'] = m.groupdict()['action']

                cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                    ['seq_num'] = int(m.groupdict()['seqnum'])
                continue

            # regexp to parse the below different outputs
            # ** match ip address prefix-list pip-prefix                    C: 0      M: 0 
            # ** match ip address prefix-list DIRECT->BGP_IPV4              C: 16     M: 0 
            p5 = re.compile(r'^(?P<command>[\w\s\-\>]+) +'
                             'C: +(?P<compare_count>\d+) +'
                             'M: +(?P<match_count>\d+)$')
            m = p5.match(line)
            if m:
                command = m.groupdict()['command'].strip()

                if 'command' not in cli_parsed_output['vrf'][vrf]['route_map']\
                    [name][index]:
                    cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                        ['command'] = {}

                cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                    ['command']['compare_count'] = int(m.groupdict()
                        ['compare_count'])

                cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                    ['command']['match_count'] = \
                        int(m.groupdict()['match_count'])

                cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                    ['command']['command'] = command
                continue

            # regexp to parse the below different outputs
            # ** Total accept count for policy: 0
            p6 = re.compile(r'^Total +accept +count +for +policy: +'
                             '(?P<total_accept_count>\d+)$')
            m = p6.match(line)
            if m:
                cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                    ['total_accept_count'] = int(m.groupdict()
                        ['total_accept_count'])
                continue

            # regexp to parse the below different outputs
            # ** Total reject count for policy: 0
            p7 = re.compile(r'^Total +reject +count +for +policy: +'
                             '(?P<total_reject_count>\d+)$')
            m = p7.match(line)
            if m:
                cli_parsed_output['vrf'][vrf]['route_map'][name][index]\
                    ['total_reject_count'] = int(m.groupdict()
                        ['total_reject_count'])
                continue

        pprint.pprint(cli_parsed_output)


    def xml(self):

        xml_parsed_output = {}
        neighbor = None

        # Remove junk characters returned by the device
        out = self.xml_input.replace("]]>]]>", "")
        root = ET.fromstring(out)

        # top table root
        show_root = Common.retrieve_xml_child(root=root, key='show')
        # get xml namespace
        # {http://www.cisco.com/nxos:7.0.3.I7.1.:bgp}
        try:
            m = re.compile(r'(?P<name>\{[\S]+\})').match(show_root.tag)
            namespace = m.groupdict()['name']
        except:
            return xml_parsed_output

        # compare cli command
        Common.compose_compare_command(root=root, namespace=namespace,
                                       expect_command=self.show_command)

        # get neighbor
        nei = Common.retrieve_xml_child(root=root,
                                        key='__XML__PARAM__neighbor-id')

        if hasattr(nei, 'tag'):
            for item in nei.getchildren():
                if '__XML__value' in item.tag:
                    neighbor = item.text
                    continue

                # cover the senario that __readonly__ may be missing when
                # there are values in the output
                if '__readonly__' in item.tag:
                    root = item.getchildren()[0]
                else:
                    root = item
        else:
            # top table rootl
            root = Common.retrieve_xml_child(root=root, key='TABLE_vrf')
        if not root:
            return xml_parsed_output

        # -----   loop vrf  -----
        for vrf_tree in root.findall('{}ROW_vrf'.format(namespace)):
            # vrf
            try:
                vrf = vrf_tree.find('{}vrf-name-polstats'.\
                    format(namespace)).text
            except:
                break

            if 'vrf' not in xml_parsed_output:
                xml_parsed_output['vrf'] = {}
            if vrf not in xml_parsed_output['vrf']:
                xml_parsed_output['vrf'][vrf] = {}

            # <rpm-handle-count>1</rpm-handle-count>
            xml_parsed_output['vrf'][vrf]['rpm_handle_count'] = \
                int(vrf_tree.find('{}rpm-handle-count'.format(namespace)).text)

             # route_map table
            rpm_tree = vrf_tree.find('{}TABLE_rmap'.format(namespace))
            if not rpm_tree:
                continue

            # -----   loop route_map  -----
            for rmp_root in rpm_tree.findall('{}ROW_rmap'.format(namespace)):
                # route map
                try:
                    name = rmp_root.find('{}name'.format(namespace)).text
                    name = name.replace('&gt;', '>')
                except:
                    continue

                if 'route_map' not in xml_parsed_output['vrf'][vrf]:
                    xml_parsed_output['vrf'][vrf]['route_map'] = {}

                if name not in xml_parsed_output['vrf'][vrf]['route_map']:
                    xml_parsed_output['vrf'][vrf]['route_map'][name] = {}
                    # initial index
                    index = 1
                else:
                    index += 1
                    
                if index not in xml_parsed_output['vrf'][vrf]['route_map']\
                    [name]:
                    xml_parsed_output['vrf'][vrf]['route_map'][name][index] = \
                        {}


                # <action>deny</action>
                try:
                    xml_parsed_output['vrf'][vrf]['route_map'][name][index]\
                        ['action'] = rmp_root.\
                            find('{}action'.format(namespace)).text
                except:
                    pass

                # <seqnum>10</seqnum>
                try:
                    xml_parsed_output['vrf'][vrf]['route_map'][name][index]\
                        ['seq_num'] = int(rmp_root.\
                            find('{}seqnum'.format(namespace)).text)
                except:
                    pass

                # <totalacceptcount>0</totalacceptcount>
                try:
                    xml_parsed_output['vrf'][vrf]['route_map'][name][index]\
                        ['total_accept_count'] = int(rmp_root.\
                            find('{}totalacceptcount'.format(namespace)).text)
                except:
                    pass

                # <totalrejectcount>2</totalrejectcount>
                try:
                    xml_parsed_output['vrf'][vrf]['route_map'][name][index]\
                        ['total_reject_count'] = int(rmp_root.\
                            find('{}totalrejectcount'.format(namespace)).text)
                except:
                    pass


                # TABLE_cmd table
                command = rmp_root.find('{}TABLE_cmd'.format(namespace))

                if not command:
                    continue

                # -----   loop command  -----
                for command_root in command.findall('{}ROW_cmd'.\
                    format(namespace)):
                    try:
                        cmd_str = command_root.find('{}command'.\
                            format(namespace)).text.strip()
                        cmd_str = cmd_str.replace('&gt;', '>')
                    except:
                        continue

                    if 'command' not in xml_parsed_output['vrf'][vrf]\
                        ['route_map'][name][index]:
                        xml_parsed_output['vrf'][vrf]['route_map'][name]\
                            [index]['command'] = {}

                    # command
                    xml_parsed_output['vrf'][vrf]['route_map'][name][index]\
                        ['command']['command'] = cmd_str

                    # <comparecount>2</comparecount>
                    try:
                        xml_parsed_output['vrf'][vrf]['route_map'][name][index]\
                            ['command']['compare_count'] = \
                                int(command_root.find('{}comparecount'.\
                                    format(namespace)).text)
                    except:
                        pass
                    
                    # <matchcount>0</matchcount>
                    try:
                        xml_parsed_output['vrf'][vrf]['route_map'][name][index]\
                            ['command']['match_count'] = \
                                int(command_root.find('{}matchcount'.\
                                    format(namespace)).text)
                    except:
                        pass
        pprint.pprint(xml_parsed_output)


# Instantiate the parser class
My_object = Parser(device=None)

# Call the cli function of the class to print the cli parsed output
My_object.cli()

# Call the xml function of the class to print the xml parsed output
My_object.xml()


# Parsed outputs
# ==============

# cli_parsed_output = {
#     "vrf": {
#         "default": {
#            "route_map": {
#                 "ADD_RT_400_400": {
#                     1: {
#                          "seq_num": 10,
#                          "action": "permit",
#                          "total_reject_count": 0,
#                          "total_accept_count": 0
#                     }
#                 }
#            },
#            "rpm_handle_count": 1
#         },
#         "vpn2": {
#            "rpm_handle_count": 0
#         },
#         "vpn1": {
#            "route_map": {
#                 "PERMIT_ALL_RM": {
#                     1: {
#                          "seq_num": 20,
#                          "action": "permit",
#                          "total_reject_count": 0,
#                          "total_accept_count": 0
#                     }
#                 }
#            },
#            "rpm_handle_count": 1
#         },
#         "ac": {
#            "rpm_handle_count": 0
#         }
#     }
# }

# xml_parsed_output = {
#     "vrf": {
#         "default": {
#            "route_map": {
#                 "ADD_RT_400_400": {
#                     1: {
#                         "seq_num": 10,
#                         "action": "permit",
#                         "total_reject_count": 0,
#                         "total_accept_count": 0
#                     }                         
#                 }
#            },
#            "rpm_handle_count": 1
#         },
#         "vpn2": {
#            "rpm_handle_count": 0
#         },
#         "vpn1": {
#            "route_map": {
#                 "PERMIT_ALL_RM": {
#                     1: {
#                          "seq_num": 20,
#                          "action": "permit",
#                          "total_reject_count": 0,
#                          "total_accept_count": 0
#                     }
#                 }
#            },
#            "rpm_handle_count": 1
#         },
#         "ac": {
#            "rpm_handle_count": 0
#         }
#     }
# }