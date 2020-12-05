# coding=utf-8
# *** WARNING: this file was generated by pulumi-gen-eks. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from .vpc_cni import VpcCni
from . import outputs
from ._inputs import *
import pulumi_aws
import pulumi_kubernetes

__all__ = ['Cluster']


class Cluster(pulumi.ComponentResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_security_group: Optional[pulumi.Input['pulumi_aws.ec2.SecurityGroup']] = None,
                 cluster_security_group_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 cluster_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 create_oidc_provider: Optional[pulumi.Input[bool]] = None,
                 creation_role_provider: Optional[pulumi.Input[pulumi.InputType['CreationRoleProviderArgs']]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 encrypt_root_block_device: Optional[pulumi.Input[bool]] = None,
                 encryption_config_key_arn: Optional[pulumi.Input[str]] = None,
                 endpoint_private_access: Optional[pulumi.Input[bool]] = None,
                 endpoint_public_access: Optional[pulumi.Input[bool]] = None,
                 fargate: Optional[pulumi.Input[Union[bool, pulumi.InputType['FargateProfileArgs']]]] = None,
                 gpu: Optional[pulumi.Input[bool]] = None,
                 instance_profile_name: Optional[pulumi.Input[str]] = None,
                 instance_role: Optional[pulumi.Input['pulumi_aws.iam.Role']] = None,
                 instance_roles: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.iam.Role']]]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 min_size: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_ami_id: Optional[pulumi.Input[str]] = None,
                 node_associate_public_ip_address: Optional[pulumi.Input[bool]] = None,
                 node_group_options: Optional[pulumi.Input[pulumi.InputType['ClusterNodeGroupOptionsArgs']]] = None,
                 node_public_key: Optional[pulumi.Input[str]] = None,
                 node_root_volume_size: Optional[pulumi.Input[int]] = None,
                 node_security_group_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 node_user_data: Optional[pulumi.Input[str]] = None,
                 private_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_credential_opts: Optional[pulumi.Input[pulumi.InputType['KubeconfigOptionsArgs']]] = None,
                 proxy: Optional[pulumi.Input[str]] = None,
                 public_access_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 public_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleMappingArgs']]]]] = None,
                 service_role: Optional[pulumi.Input['pulumi_aws.iam.Role']] = None,
                 skip_default_node_group: Optional[pulumi.Input[bool]] = None,
                 storage_classes: Optional[pulumi.Input[Union[str, pulumi.InputType['StorageClassArgs']]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserMappingArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 vpc_cni_options: Optional[pulumi.Input[pulumi.InputType['VpcCniOptionsArgs']]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Cluster is a component that wraps the AWS and Kubernetes resources necessary to run an EKS cluster, its worker nodes, its optional StorageClasses, and an optional deployment of the Kubernetes Dashboard.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['pulumi_aws.ec2.SecurityGroup'] cluster_security_group: The security group to use for the cluster API endpoint. If not provided, a new security group will be created with full internet egress and ingress from node groups.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] cluster_security_group_tags: The tags to apply to the cluster security group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] cluster_tags: The tags to apply to the EKS cluster.
        :param pulumi.Input[bool] create_oidc_provider: Indicates whether an IAM OIDC Provider is created for the EKS cluster.
               
               The OIDC provider is used in the cluster in combination with k8s Service Account annotations to provide IAM roles at the k8s Pod level.
               
               See for more details:
                - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html
                - https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html
                - https://aws.amazon.com/blogs/opensource/introducing-fine-grained-iam-roles-service-accounts/
                - https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/aws/eks/#enabling-iam-roles-for-service-accounts
        :param pulumi.Input[pulumi.InputType['CreationRoleProviderArgs']] creation_role_provider: The IAM Role Provider used to create & authenticate against the EKS cluster. This role is given `[system:masters]` permission in K8S, See: https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html
        :param pulumi.Input[int] desired_capacity: The number of worker nodes that should be running in the cluster. Defaults to 2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_cluster_log_types: Enable EKS control plane logging. This sends logs to cloudwatch. Possible list of values are: ["api", "audit", "authenticator", "controllerManager", "scheduler"]. By default it is off.
        :param pulumi.Input[bool] encrypt_root_block_device: Encrypt the root block device of the nodes in the node group.
        :param pulumi.Input[str] encryption_config_key_arn: KMS Key ARN to use with the encryption configuration for the cluster.
               
               Only available on Kubernetes 1.13+ clusters created after March 6, 2020.
               See for more details:
               - https://aws.amazon.com/about-aws/whats-new/2020/03/amazon-eks-adds-envelope-encryption-for-secrets-with-aws-kms/
        :param pulumi.Input[bool] endpoint_private_access: Indicates whether or not the Amazon EKS private API server endpoint is enabled. Default is `false`.
        :param pulumi.Input[bool] endpoint_public_access: Indicates whether or not the Amazon EKS public API server endpoint is enabled. Default is `true`.
        :param pulumi.Input[Union[bool, pulumi.InputType['FargateProfileArgs']]] fargate: Add support for launching pods in Fargate. Defaults to launching pods in the `default` namespace.  If specified, the default node group is skipped as though `skipDefaultNodeGroup: true` had been passed.
        :param pulumi.Input[bool] gpu: Use the latest recommended EKS Optimized Linux AMI with GPU support for the worker nodes from the AWS Systems Manager Parameter Store.
               
               Defaults to false.
               
               Note: `gpu` and `nodeAmiId` are mutually exclusive.
               
               See for more details:
               - https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html
               - https://docs.aws.amazon.com/eks/latest/userguide/retrieve-ami-id.html
        :param pulumi.Input[str] instance_profile_name: The default IAM InstanceProfile to use on the Worker NodeGroups, if one is not already set in the NodeGroup.
        :param pulumi.Input['pulumi_aws.iam.Role'] instance_role: This enables the simple case of only registering a *single* IAM instance role with the cluster, that is required to be shared by *all* node groups in their instance profiles.
               
               Note: options `instanceRole` and `instanceRoles` are mutually exclusive.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.iam.Role']]] instance_roles: This enables the advanced case of registering *many* IAM instance roles with the cluster for per node group IAM, instead of the simpler, shared case of `instanceRole`.
               
               Note: options `instanceRole` and `instanceRoles` are mutually exclusive.
        :param pulumi.Input[str] instance_type: The instance type to use for the cluster's nodes. Defaults to "t2.medium".
        :param pulumi.Input[int] max_size: The maximum number of worker nodes running in the cluster. Defaults to 2.
        :param pulumi.Input[int] min_size: The minimum number of worker nodes running in the cluster. Defaults to 1.
        :param pulumi.Input[str] name: The cluster's physical resource name.
               
               If not specified, the default is to use auto-naming for the cluster's name, resulting in a physical name with the format `${name}-eksCluster-0123abcd`.
               
               See for more details: https://www.pulumi.com/docs/intro/concepts/programming-model/#autonaming
        :param pulumi.Input[str] node_ami_id: The AMI ID to use for the worker nodes.
               
               Defaults to the latest recommended EKS Optimized Linux AMI from the AWS Systems Manager Parameter Store.
               
               Note: `nodeAmiId` and `gpu` are mutually exclusive.
               
               See for more details:
               - https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html.
        :param pulumi.Input[bool] node_associate_public_ip_address: Whether or not to auto-assign the EKS worker nodes public IP addresses. If this toggle is set to true, the EKS workers will be auto-assigned public IPs. If false, they will not be auto-assigned public IPs.
        :param pulumi.Input[pulumi.InputType['ClusterNodeGroupOptionsArgs']] node_group_options: The common configuration settings for NodeGroups.
        :param pulumi.Input[str] node_public_key: Public key material for SSH access to worker nodes. See allowed formats at:
               https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
               If not provided, no SSH access is enabled on VMs.
        :param pulumi.Input[int] node_root_volume_size: The size in GiB of a cluster node's root volume. Defaults to 20.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_security_group_tags: The tags to apply to the default `nodeSecurityGroup` created by the cluster.
               
               Note: The `nodeSecurityGroupTags` option and the node group option `nodeSecurityGroup` are mutually exclusive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] node_subnet_ids: The subnets to use for worker nodes. Defaults to the value of subnetIds.
        :param pulumi.Input[str] node_user_data: Extra code to run on node startup. This code will run after the AWS EKS bootstrapping code and before the node signals its readiness to the managing CloudFormation stack. This code must be a typical user data script: critically it must begin with an interpreter directive (i.e. a `#!`).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_subnet_ids: The set of private subnets to use for the worker node groups on the EKS cluster. These subnets are automatically tagged by EKS for Kubernetes purposes.
               
               If `vpcId` is not set, the cluster will use the AWS account's default VPC subnets.
               
               Worker network architecture options:
                - Private-only: Only set `privateSubnetIds`.
                  - Default workers to run in a private subnet. In this setting, Kubernetes cannot create public, internet-facing load balancers for your pods.
                - Public-only: Only set `publicSubnetIds`.
                  - Default workers to run in a public subnet.
                - Mixed (recommended): Set both `privateSubnetIds` and `publicSubnetIds`.
                  - Default all worker nodes to run in private subnets, and use the public subnets for internet-facing load balancers.
               
               See for more details: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html.Note: The use of `subnetIds`, along with `publicSubnetIds` and/or `privateSubnetIds` is mutually exclusive. The use of `publicSubnetIds` and `privateSubnetIds` is encouraged.
               
               Also consider setting `nodeAssociatePublicIpAddress: true` for fully private workers.
        :param pulumi.Input[pulumi.InputType['KubeconfigOptionsArgs']] provider_credential_opts: The AWS provider credential options to scope the cluster's kubeconfig authentication when using a non-default credential chain.
               
               This is required for certain auth scenarios. For example:
               - Creating and using a new AWS provider instance, or
               - Setting the AWS_PROFILE environment variable, or
               - Using a named profile configured on the AWS provider via:
               `pulumi config set aws:profile <profileName>`
               
               See for more details:
               - https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/aws/#Provider
               - https://www.pulumi.com/docs/intro/cloud-providers/aws/setup/
               - https://www.pulumi.com/docs/intro/cloud-providers/aws/#configuration
               - https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html
        :param pulumi.Input[str] proxy: The HTTP(S) proxy to use within a proxied environment.
               
                The proxy is used during cluster creation, and OIDC configuration.
               
               This is an alternative option to setting the proxy environment variables: HTTP(S)_PROXY and/or http(s)_proxy.
               
               This option is required iff the proxy environment variables are not set.
               
               Format:      <protocol>://<host>:<port>
               Auth Format: <protocol>://<username>:<password>@<host>:<port>
               
               Ex:
                 - "http://proxy.example.com:3128"
                 - "https://proxy.example.com"
                 - "http://username:password@proxy.example.com:3128"
        :param pulumi.Input[Sequence[pulumi.Input[str]]] public_access_cidrs: Indicates which CIDR blocks can access the Amazon EKS public API server endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] public_subnet_ids: The set of public subnets to use for the worker node groups on the EKS cluster. These subnets are automatically tagged by EKS for Kubernetes purposes.
               
               If `vpcId` is not set, the cluster will use the AWS account's default VPC subnets.
               
               Worker network architecture options:
                - Private-only: Only set `privateSubnetIds`.
                  - Default workers to run in a private subnet. In this setting, Kubernetes cannot create public, internet-facing load balancers for your pods.
                - Public-only: Only set `publicSubnetIds`.
                  - Default workers to run in a public subnet.
                - Mixed (recommended): Set both `privateSubnetIds` and `publicSubnetIds`.
                  - Default all worker nodes to run in private subnets, and use the public subnets for internet-facing load balancers.
               
               See for more details: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html.Note: The use of `subnetIds`, along with `publicSubnetIds` and/or `privateSubnetIds` is mutually exclusive. The use of `publicSubnetIds` and `privateSubnetIds` is encouraged.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleMappingArgs']]]] role_mappings: Optional mappings from AWS IAM roles to Kubernetes users and groups.
        :param pulumi.Input['pulumi_aws.iam.Role'] service_role: IAM Service Role for EKS to use to manage the cluster.
        :param pulumi.Input[bool] skip_default_node_group: If this toggle is set to true, the EKS cluster will be created without node group attached. Defaults to false, unless `fargate` input is provided.
        :param pulumi.Input[Union[str, pulumi.InputType['StorageClassArgs']]] storage_classes: An optional set of StorageClasses to enable for the cluster. If this is a single volume type rather than a map, a single StorageClass will be created for that volume type.
               
               Note: As of Kubernetes v1.11+ on EKS, a default `gp2` storage class will always be created automatically for the cluster by the EKS service. See https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The set of all subnets, public and private, to use for the worker node groups on the EKS cluster. These subnets are automatically tagged by EKS for Kubernetes purposes.
               
               If `vpcId` is not set, the cluster will use the AWS account's default VPC subnets.
               
               If the list of subnets includes both public and private subnets, the worker nodes will only be attached to the private subnets, and the public subnets will be used for internet-facing load balancers.
               
               See for more details: https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html.
               
               Note: The use of `subnetIds`, along with `publicSubnetIds` and/or `privateSubnetIds` is mutually exclusive. The use of `publicSubnetIds` and `privateSubnetIds` is encouraged.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of tags that are automatically applied to all AWS resources directly under management with this cluster, which support tagging.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserMappingArgs']]]] user_mappings: Optional mappings from AWS IAM users to Kubernetes users and groups.
        :param pulumi.Input[str] version: Desired Kubernetes master / control plane version. If you do not specify a value, the latest available version is used.
        :param pulumi.Input[pulumi.InputType['VpcCniOptionsArgs']] vpc_cni_options: The configuration of the Amazon VPC CNI plugin for this instance. Defaults are described in the documentation for the VpcCniOptions type.
        :param pulumi.Input[str] vpc_id: The VPC in which to create the cluster and its worker nodes. If unset, the cluster will be created in the default VPC.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['cluster_security_group'] = cluster_security_group
            __props__['cluster_security_group_tags'] = cluster_security_group_tags
            __props__['cluster_tags'] = cluster_tags
            __props__['create_oidc_provider'] = create_oidc_provider
            __props__['creation_role_provider'] = creation_role_provider
            __props__['desired_capacity'] = desired_capacity
            __props__['enabled_cluster_log_types'] = enabled_cluster_log_types
            __props__['encrypt_root_block_device'] = encrypt_root_block_device
            __props__['encryption_config_key_arn'] = encryption_config_key_arn
            __props__['endpoint_private_access'] = endpoint_private_access
            __props__['endpoint_public_access'] = endpoint_public_access
            __props__['fargate'] = fargate
            __props__['gpu'] = gpu
            __props__['instance_profile_name'] = instance_profile_name
            __props__['instance_role'] = instance_role
            __props__['instance_roles'] = instance_roles
            __props__['instance_type'] = instance_type
            __props__['max_size'] = max_size
            __props__['min_size'] = min_size
            __props__['name'] = name
            __props__['node_ami_id'] = node_ami_id
            __props__['node_associate_public_ip_address'] = node_associate_public_ip_address
            __props__['node_group_options'] = node_group_options
            __props__['node_public_key'] = node_public_key
            __props__['node_root_volume_size'] = node_root_volume_size
            __props__['node_security_group_tags'] = node_security_group_tags
            __props__['node_subnet_ids'] = node_subnet_ids
            __props__['node_user_data'] = node_user_data
            __props__['private_subnet_ids'] = private_subnet_ids
            __props__['provider_credential_opts'] = provider_credential_opts
            __props__['proxy'] = proxy
            __props__['public_access_cidrs'] = public_access_cidrs
            __props__['public_subnet_ids'] = public_subnet_ids
            __props__['role_mappings'] = role_mappings
            __props__['service_role'] = service_role
            __props__['skip_default_node_group'] = skip_default_node_group
            __props__['storage_classes'] = storage_classes
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['user_mappings'] = user_mappings
            __props__['version'] = version
            __props__['vpc_cni_options'] = vpc_cni_options
            __props__['vpc_id'] = vpc_id
            __props__['aws_provider'] = None
            __props__['core'] = None
            __props__['default_node_group'] = None
            __props__['eks_cluster'] = None
            __props__['eks_cluster_ingress_rule'] = None
            __props__['kubeconfig'] = None
            __props__['node_security_group'] = None
            __props__['provider'] = None
        super(Cluster, __self__).__init__(
            'eks:index:Cluster',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="awsProvider")
    def aws_provider(self) -> pulumi.Output['pulumi_aws.Provider']:
        """
        The AWS resource provider.
        """
        return pulumi.get(self, "aws_provider")

    @property
    @pulumi.getter(name="clusterSecurityGroup")
    def cluster_security_group(self) -> pulumi.Output['pulumi_aws.ec2.SecurityGroup']:
        """
        The security group for the EKS cluster.
        """
        return pulumi.get(self, "cluster_security_group")

    @property
    @pulumi.getter
    def core(self) -> pulumi.Output['outputs.CoreData']:
        """
        The EKS cluster and its dependencies.
        """
        return pulumi.get(self, "core")

    @property
    @pulumi.getter(name="defaultNodeGroup")
    def default_node_group(self) -> pulumi.Output[Optional['outputs.NodeGroupData']]:
        """
        The default Node Group configuration, or undefined if `skipDefaultNodeGroup` was specified.
        """
        return pulumi.get(self, "default_node_group")

    @property
    @pulumi.getter(name="eksCluster")
    def eks_cluster(self) -> pulumi.Output['pulumi_aws.eks.Cluster']:
        """
        The EKS cluster.
        """
        return pulumi.get(self, "eks_cluster")

    @property
    @pulumi.getter(name="eksClusterIngressRule")
    def eks_cluster_ingress_rule(self) -> pulumi.Output['pulumi_aws.ec2.SecurityGroupRule']:
        """
        The ingress rule that gives node group access to cluster API server.
        """
        return pulumi.get(self, "eks_cluster_ingress_rule")

    @property
    @pulumi.getter(name="instanceRoles")
    def instance_roles(self) -> pulumi.Output[Sequence['pulumi_aws.iam.Role']]:
        """
        The service roles used by the EKS cluster.
        """
        return pulumi.get(self, "instance_roles")

    @property
    @pulumi.getter
    def kubeconfig(self) -> pulumi.Output[Any]:
        """
        A kubeconfig that can be used to connect to the EKS cluster.
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter(name="nodeSecurityGroup")
    def node_security_group(self) -> pulumi.Output['pulumi_aws.ec2.SecurityGroup']:
        """
        The security group for the cluster's nodes.
        """
        return pulumi.get(self, "node_security_group")

    @property
    @pulumi.getter
    def provider(self) -> pulumi.Output['pulumi_kubernetes.Provider']:
        """
        A Kubernetes resource provider that can be used to deploy into this cluster.
        """
        return pulumi.get(self, "provider")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

