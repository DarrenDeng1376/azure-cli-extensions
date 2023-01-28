# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "mobile-network attached-data-network update",
)
class Update(AAZCommand):
    """Update an attached data network.

    :example: Update attached-data-network tags
        az mobile-network attached-data-network update -n data_network-name -g rg --pccp-name pccp-name --pcdp-name pcdp-name --tags "{tag:test,tag2:test2}"
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.mobilenetwork/packetcorecontrolplanes/{}/packetcoredataplanes/{}/attacheddatanetworks/{}", "2022-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.adn_name = AAZStrArg(
            options=["-n", "--name", "--adn-name"],
            help="The name of the attached data network.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])*(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])*)*$",
                max_length=64,
            ),
        )
        _args_schema.pccp_name = AAZStrArg(
            options=["--pccp-name"],
            help="The name of the packet core control plane.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_-]*$",
                max_length=64,
            ),
        )
        _args_schema.pcdp_name = AAZStrArg(
            options=["--pcdp-name"],
            help="The name of the packet core data plane.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9_-]*$",
                max_length=64,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.dns_addresses = AAZListArg(
            options=["--dns-addresses"],
            arg_group="Properties",
            help="The DNS servers to signal to UEs to use for this attached data network.",
            fmt=AAZListArgFormat(
                unique=True,
            ),
        )
        _args_schema.napt_configuration = AAZObjectArg(
            options=["--napt-configuration"],
            arg_group="Properties",
            help="The network address and port translation (NAPT) configuration. If this is not specified, the attached data network will use a default NAPT configuration with NAPT enabled.",
            nullable=True,
        )
        _args_schema.address_pool = AAZListArg(
            options=["--address-pool"],
            arg_group="Properties",
            help="The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will dynamically assign IP addresses to UEs. The packet core instance assigns an IP address to a UE when the UE sets up a PDU session.  You must define at least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix. If you define both, they must be of the same size.",
            nullable=True,
            fmt=AAZListArgFormat(
                unique=True,
            ),
        )
        _args_schema.static_address_pool = AAZListArg(
            options=["--static-address-pool"],
            arg_group="Properties",
            help="The user equipment (UE) address pool prefixes for the attached data network from which the packet core instance will assign static IP addresses to UEs. The packet core instance assigns an IP address to a UE when the UE sets up a PDU session. The static IP address for a specific UE is set in StaticIPConfiguration on the corresponding SIM resource. At least one of userEquipmentAddressPoolPrefix and userEquipmentStaticAddressPoolPrefix must be defined. If both are defined, they must be of the same size.",
            nullable=True,
            fmt=AAZListArgFormat(
                unique=True,
            ),
        )
        _args_schema.data_interface = AAZObjectArg(
            options=["--data-interface"],
            arg_group="Properties",
            help="The user plane interface on the data network. For 5G networks, this is the N6 interface. For 4G networks, this is the SGi interface.",
        )

        dns_addresses = cls._args_schema.dns_addresses
        dns_addresses.Element = AAZStrArg(
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",
            ),
        )

        napt_configuration = cls._args_schema.napt_configuration
        napt_configuration.enabled = AAZStrArg(
            options=["enabled"],
            help="Whether NAPT is enabled for connections to this attached data network.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        napt_configuration.pinhole_limits = AAZIntArg(
            options=["pinhole-limits"],
            help="Maximum number of UDP and TCP pinholes that can be open simultaneously on the core interface. For 5G networks, this is the N6 interface. For 4G networks, this is the SGi interface.",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=65536,
                minimum=1,
            ),
        )
        napt_configuration.pinhole_timeouts = AAZObjectArg(
            options=["pinhole-timeouts"],
            help="Expiry times of inactive NAPT pinholes, in seconds. All timers must be at least 1 second.",
            nullable=True,
        )
        napt_configuration.port_range = AAZObjectArg(
            options=["port-range"],
            help="Range of port numbers to use as translated ports on each translated address. If not specified and NAPT is enabled, this range defaults to 1,024 - 49,999. (Ports under 1,024 should not be used because these are special purpose ports reserved by IANA. Ports 50,000 and above are reserved for non-NAPT use.)",
            nullable=True,
        )
        napt_configuration.port_reuse_hold_time = AAZObjectArg(
            options=["port-reuse-hold-time"],
            help="The minimum time (in seconds) that will pass before a port that was used by a closed pinhole can be recycled for use by another pinhole. All hold times must be minimum 1 second.",
            nullable=True,
        )

        pinhole_timeouts = cls._args_schema.napt_configuration.pinhole_timeouts
        pinhole_timeouts.icmp = AAZIntArg(
            options=["icmp"],
            help="Pinhole timeout for ICMP pinholes in seconds. Default for ICMP Echo is 60 seconds, as per RFC 5508 section 3.2.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )
        pinhole_timeouts.tcp = AAZIntArg(
            options=["tcp"],
            help="Pinhole timeout for TCP pinholes in seconds. Default for TCP is 2 hours 4 minutes, as per RFC 5382 section 5.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )
        pinhole_timeouts.udp = AAZIntArg(
            options=["udp"],
            help="Pinhole timeout for UDP pinholes in seconds. Default for UDP is 5 minutes, as per RFC 4787 section 4.3.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )

        port_range = cls._args_schema.napt_configuration.port_range
        port_range.max_port = AAZIntArg(
            options=["max-port"],
            help="The maximum port number",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=1024,
            ),
        )
        port_range.min_port = AAZIntArg(
            options=["min-port"],
            help="The minimum port number",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=1024,
            ),
        )

        port_reuse_hold_time = cls._args_schema.napt_configuration.port_reuse_hold_time
        port_reuse_hold_time.tcp = AAZIntArg(
            options=["tcp"],
            help="Minimum time in seconds that will pass before a TCP port that was used by a closed pinhole can be reused. Default for TCP is 2 minutes.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )
        port_reuse_hold_time.udp = AAZIntArg(
            options=["udp"],
            help="Minimum time in seconds that will pass before a UDP port that was used by a closed pinhole can be reused. Default for UDP is 1 minute.",
            nullable=True,
            fmt=AAZIntArgFormat(
                minimum=1,
            ),
        )

        address_pool = cls._args_schema.address_pool
        address_pool.Element = AAZStrArg(
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$",
            ),
        )

        static_address_pool = cls._args_schema.static_address_pool
        static_address_pool.Element = AAZStrArg(
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$",
            ),
        )

        data_interface = cls._args_schema.data_interface
        data_interface.ipv4_address = AAZStrArg(
            options=["ipv4-address"],
            help="The IPv4 address.",
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",
            ),
        )
        data_interface.ipv4_gateway = AAZStrArg(
            options=["ipv4-gateway"],
            help="The default IPv4 gateway (router).",
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",
            ),
        )
        data_interface.ipv4_subnet = AAZStrArg(
            options=["ipv4-subnet"],
            help="The IPv4 subnet.",
            nullable=True,
            fmt=AAZStrArgFormat(
                pattern="^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$",
            ),
        )
        data_interface.name = AAZStrArg(
            options=["name"],
            help="The logical name for this interface. This should match one of the interfaces configured on your Azure Stack Edge device.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AttachedDataNetworksGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AttachedDataNetworksCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AttachedDataNetworksGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}/attachedDataNetworks/{attachedDataNetworkName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "attachedDataNetworkName", self.ctx.args.adn_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packetCoreControlPlaneName", self.ctx.args.pccp_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packetCoreDataPlaneName", self.ctx.args.pcdp_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_attached_data_network_read(cls._schema_on_200)

            return cls._schema_on_200

    class AttachedDataNetworksCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/{packetCoreControlPlaneName}/packetCoreDataPlanes/{packetCoreDataPlaneName}/attachedDataNetworks/{attachedDataNetworkName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "attachedDataNetworkName", self.ctx.args.adn_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packetCoreControlPlaneName", self.ctx.args.pccp_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packetCoreDataPlaneName", self.ctx.args.pcdp_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_attached_data_network_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("dnsAddresses", AAZListType, ".dns_addresses", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("naptConfiguration", AAZObjectType, ".napt_configuration")
                properties.set_prop("userEquipmentAddressPoolPrefix", AAZListType, ".address_pool")
                properties.set_prop("userEquipmentStaticAddressPoolPrefix", AAZListType, ".static_address_pool")
                properties.set_prop("userPlaneDataInterface", AAZObjectType, ".data_interface", typ_kwargs={"flags": {"required": True}})

            dns_addresses = _builder.get(".properties.dnsAddresses")
            if dns_addresses is not None:
                dns_addresses.set_elements(AAZStrType, ".")

            napt_configuration = _builder.get(".properties.naptConfiguration")
            if napt_configuration is not None:
                napt_configuration.set_prop("enabled", AAZStrType, ".enabled")
                napt_configuration.set_prop("pinholeLimits", AAZIntType, ".pinhole_limits")
                napt_configuration.set_prop("pinholeTimeouts", AAZObjectType, ".pinhole_timeouts")
                napt_configuration.set_prop("portRange", AAZObjectType, ".port_range")
                napt_configuration.set_prop("portReuseHoldTime", AAZObjectType, ".port_reuse_hold_time")

            pinhole_timeouts = _builder.get(".properties.naptConfiguration.pinholeTimeouts")
            if pinhole_timeouts is not None:
                pinhole_timeouts.set_prop("icmp", AAZIntType, ".icmp")
                pinhole_timeouts.set_prop("tcp", AAZIntType, ".tcp")
                pinhole_timeouts.set_prop("udp", AAZIntType, ".udp")

            port_range = _builder.get(".properties.naptConfiguration.portRange")
            if port_range is not None:
                port_range.set_prop("maxPort", AAZIntType, ".max_port")
                port_range.set_prop("minPort", AAZIntType, ".min_port")

            port_reuse_hold_time = _builder.get(".properties.naptConfiguration.portReuseHoldTime")
            if port_reuse_hold_time is not None:
                port_reuse_hold_time.set_prop("tcp", AAZIntType, ".tcp")
                port_reuse_hold_time.set_prop("udp", AAZIntType, ".udp")

            user_equipment_address_pool_prefix = _builder.get(".properties.userEquipmentAddressPoolPrefix")
            if user_equipment_address_pool_prefix is not None:
                user_equipment_address_pool_prefix.set_elements(AAZStrType, ".")

            user_equipment_static_address_pool_prefix = _builder.get(".properties.userEquipmentStaticAddressPoolPrefix")
            if user_equipment_static_address_pool_prefix is not None:
                user_equipment_static_address_pool_prefix.set_elements(AAZStrType, ".")

            user_plane_data_interface = _builder.get(".properties.userPlaneDataInterface")
            if user_plane_data_interface is not None:
                user_plane_data_interface.set_prop("ipv4Address", AAZStrType, ".ipv4_address")
                user_plane_data_interface.set_prop("ipv4Gateway", AAZStrType, ".ipv4_gateway")
                user_plane_data_interface.set_prop("ipv4Subnet", AAZStrType, ".ipv4_subnet")
                user_plane_data_interface.set_prop("name", AAZStrType, ".name")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_attached_data_network_read = None

    @classmethod
    def _build_schema_attached_data_network_read(cls, _schema):
        if cls._schema_attached_data_network_read is not None:
            _schema.id = cls._schema_attached_data_network_read.id
            _schema.location = cls._schema_attached_data_network_read.location
            _schema.name = cls._schema_attached_data_network_read.name
            _schema.properties = cls._schema_attached_data_network_read.properties
            _schema.system_data = cls._schema_attached_data_network_read.system_data
            _schema.tags = cls._schema_attached_data_network_read.tags
            _schema.type = cls._schema_attached_data_network_read.type
            return

        cls._schema_attached_data_network_read = _schema_attached_data_network_read = AAZObjectType()

        attached_data_network_read = _schema_attached_data_network_read
        attached_data_network_read.id = AAZStrType(
            flags={"read_only": True},
        )
        attached_data_network_read.location = AAZStrType(
            flags={"required": True},
        )
        attached_data_network_read.name = AAZStrType(
            flags={"read_only": True},
        )
        attached_data_network_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        attached_data_network_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        attached_data_network_read.tags = AAZDictType()
        attached_data_network_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_attached_data_network_read.properties
        properties.dns_addresses = AAZListType(
            serialized_name="dnsAddresses",
            flags={"required": True},
        )
        properties.napt_configuration = AAZObjectType(
            serialized_name="naptConfiguration",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.user_equipment_address_pool_prefix = AAZListType(
            serialized_name="userEquipmentAddressPoolPrefix",
        )
        properties.user_equipment_static_address_pool_prefix = AAZListType(
            serialized_name="userEquipmentStaticAddressPoolPrefix",
        )
        properties.user_plane_data_interface = AAZObjectType(
            serialized_name="userPlaneDataInterface",
            flags={"required": True},
        )

        dns_addresses = _schema_attached_data_network_read.properties.dns_addresses
        dns_addresses.Element = AAZStrType()

        napt_configuration = _schema_attached_data_network_read.properties.napt_configuration
        napt_configuration.enabled = AAZStrType()
        napt_configuration.pinhole_limits = AAZIntType(
            serialized_name="pinholeLimits",
        )
        napt_configuration.pinhole_timeouts = AAZObjectType(
            serialized_name="pinholeTimeouts",
        )
        napt_configuration.port_range = AAZObjectType(
            serialized_name="portRange",
        )
        napt_configuration.port_reuse_hold_time = AAZObjectType(
            serialized_name="portReuseHoldTime",
        )

        pinhole_timeouts = _schema_attached_data_network_read.properties.napt_configuration.pinhole_timeouts
        pinhole_timeouts.icmp = AAZIntType()
        pinhole_timeouts.tcp = AAZIntType()
        pinhole_timeouts.udp = AAZIntType()

        port_range = _schema_attached_data_network_read.properties.napt_configuration.port_range
        port_range.max_port = AAZIntType(
            serialized_name="maxPort",
        )
        port_range.min_port = AAZIntType(
            serialized_name="minPort",
        )

        port_reuse_hold_time = _schema_attached_data_network_read.properties.napt_configuration.port_reuse_hold_time
        port_reuse_hold_time.tcp = AAZIntType()
        port_reuse_hold_time.udp = AAZIntType()

        user_equipment_address_pool_prefix = _schema_attached_data_network_read.properties.user_equipment_address_pool_prefix
        user_equipment_address_pool_prefix.Element = AAZStrType()

        user_equipment_static_address_pool_prefix = _schema_attached_data_network_read.properties.user_equipment_static_address_pool_prefix
        user_equipment_static_address_pool_prefix.Element = AAZStrType()

        user_plane_data_interface = _schema_attached_data_network_read.properties.user_plane_data_interface
        user_plane_data_interface.ipv4_address = AAZStrType(
            serialized_name="ipv4Address",
        )
        user_plane_data_interface.ipv4_gateway = AAZStrType(
            serialized_name="ipv4Gateway",
        )
        user_plane_data_interface.ipv4_subnet = AAZStrType(
            serialized_name="ipv4Subnet",
        )
        user_plane_data_interface.name = AAZStrType()

        system_data = _schema_attached_data_network_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_attached_data_network_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_attached_data_network_read.id
        _schema.location = cls._schema_attached_data_network_read.location
        _schema.name = cls._schema_attached_data_network_read.name
        _schema.properties = cls._schema_attached_data_network_read.properties
        _schema.system_data = cls._schema_attached_data_network_read.system_data
        _schema.tags = cls._schema_attached_data_network_read.tags
        _schema.type = cls._schema_attached_data_network_read.type


__all__ = ["Update"]