'''
Metaparser
----------
   
   Metaparser pyats module provides a structure unification among different
   parsing contexts. It provides a unified structure that will be followed
   by different device connections (Ex: 'cli', 'yang', 'xml).

   It addresses the common automation problems such as:
   ----------------------------------------------------

   * Script changes due to CLI command and/or output changes
     (release to release, OS to OS,  Platform/Series to Platform/Series) 
   * Parser reuse limitation due to naming convention 

'''

# Python
import re
import pprint

# Metaparser
from metaparser import MetaParser
# Schema is the user datastructure that every output from the inheriting class
# should comply with.
	# * Any : Marks a section of a schema that matches anything.
	# * Optional : Marks an optional part of the schema.
	# * OR : Defines a schema of OR relationship, eg, the input data must pass
	# the validation of one of the requirements of this Schema.
from metaparser.util.schemaengine import Schema, Any, Optional, Or


class ParserSchema(MetaParser):
    # Schema could be any valid python datastructure/callable.
    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                            	# Optional here means that key is not a mandatory
                            	# key in the parsed output.
                                {Optional('route_map_in'): str,
                            	# OR here means that parsed key could be either
                            	# of type(str) or type(list).
                                 'route_map_out': Or(str, list),
                                }
                            },
                        }
                    },
                }
            },
        }


class Parser(ParserSchema):

    STRING = '''
        Neighbor: 21.0.0.1, Address-Family: ipv4 Unicast (VRF1)
           Locally configured policies:
            route-map RMAP in
            route-map RMAP2 out
        Neighbor: 21.0.0.2, Address-Family: ipv6 Unicast (VRF2)
           Locally configured policies:
            route-map RMAP3 in
            route-map RMAP4 out
        Neighbor: 21.0.0.3, Address-Family: VPNv4 Unicast
           Locally configured policies:
            route-map RMAP5 in
            route-map RMAP6 out
        Neighbor: 21.0.0.4, Address-Family: VPNv6 Unicast (VRF2)
           Locally configured policies:
            route-map RMAP7 in
            route-map RMAP8 out
        '''

    def cli(self):

        # Initialize dictionary
        result = {}

        # split the output into seperate lines
        for line in self.STRING.splitlines():
            # strip the line from any trailing white spaces
            line = line.rstrip()

            # regexp to parse the below different outputs
            # ** Neighbor: 21.0.0.1, Address-Family: ipv4 Unicast
            # ** Neighbor: 21.0.0.2, Address-Family: VPNv4 Unicast (VRF2)
            p1 = re.compile(r'^\s*Neighbor: +(?P<neighbor_name>[0-9\.]+),'
                             ' +Address-Family:'
                             ' +(?P<address_family_name>[a-zA-Z0-9\s]+)'
                             '( +\((?P<vrf_name>[a-zA-Z0-9]+)\))?$')
            # check if the regexp matched with the line
            m = p1.match(line)
            if m:
                # gather the prased keys
                neighbor_name = m.groupdict()['neighbor_name']
                address_family_name = m.groupdict()['address_family_name']
                # check if vrf has been identified in the output, if not default
                # it to 'default'
                if m.groupdict()['vrf_name']:
                    vrf_name = m.groupdict()['vrf_name']
                else:
                    vrf_name = 'default'
                continue

            # regexp to parse the below outputs
            # ** route-map RMAP in
            # ** route-map RMAP out
            p2 = re.compile(r'\s*route-map +(?P<route_map_name>[a-zA-Z0-9]+) '
                '+(?P<direction>[a-z]+)')
            m = p2.match(line)
            # check if the regexp matched with the line
            if m:
                # gather the prased keys
                route_map_name = m.groupdict()['route_map_name']
                direction = m.groupdict()['direction']

                # build the desired structure/hierarchy out of the parsed output
                if 'vrf' not in result:
                    result['vrf'] = {}
                if vrf_name not in result['vrf']:
                    result['vrf'][vrf_name] = {}
                if 'neighbor' not in result['vrf'][vrf_name]:
                    result['vrf'][vrf_name]['neighbor'] = {}
                if neighbor_name not in result['vrf'][vrf_name]\
                    ['neighbor']:
                    result['vrf'][vrf_name]['neighbor'][neighbor_name] = {}
                if 'address_family' not in result['vrf'][vrf_name]\
                    ['neighbor'][neighbor_name]:
                    result['vrf'][vrf_name]['neighbor'][neighbor_name]\
                        ['address_family'] = {}
                if address_family_name not in result['vrf'][vrf_name]\
                    ['neighbor'][neighbor_name]['address_family']:
                    result['vrf'][vrf_name]['neighbor'][neighbor_name]\
                        ['address_family'][address_family_name] = {}

                if direction == 'in':
                    result['vrf'][vrf_name]['neighbor'][neighbor_name]\
                        ['address_family'][address_family_name]\
                            ['route_map_in'] = route_map_name
                else:
                    result['vrf'][vrf_name]['neighbor'][neighbor_name]\
                        ['address_family'][address_family_name]\
                            ['route_map_out'] = route_map_name

                continue

        # print the parsed built structure
        pprint.pprint(result)


# Instantiate the parser class to run it
My_object = Parser(device=None)

# Call the cli function of the class to print the parsed output
My_object.cli()


# Parsed Output
# =============
# result = {
#     'vrf':
#         {'VRF1':
#             {'neighbor':
#                 {'21.0.0.1':
#                     {'address_family':
#                         {'VPNv4 Unicast':
#                             {'route_map_in': 'RMAP',
#                              'route_map_out': 'RMAP2'}
#                         }
#                     }
#                 }
#             },
#         'VRF2':
#             {'neighbor':
#                 {'21.0.0.2':
#                     {'address_family':
#                         {'VPNv6 Unicast':
#                             {'route_map_in': 'RMAP3',
#                              'route_map_out': 'RMAP4'}
#                         }
#                     },
#                 '21.0.0.4':
#                     {'address_family':
#                         {'VPNv6 Unicast':
#                             {'route_map_in': 'RMAP7',
#                              'route_map_out': 'RMAP8'}
#                         }
#                     }
#                 }
#             },
#         'default':
#             {'neighbor':
#                 {'21.0.0.3':
#                     {'address_family':
#                         {'VPNv4 Unicast':
#                             {'route_map_in': 'RMAP5',
#                              'route_map_out': 'RMAP6'}
#                         }
#                     }
#                 }
#             }
#         }
#     }