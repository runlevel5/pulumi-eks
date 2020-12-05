// *** WARNING: this file was generated by pulumi-gen-eks. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Eks.Inputs
{

    /// <summary>
    /// Defines the core set of data associated with an EKS cluster, including the network in which it runs.
    /// </summary>
    public sealed class CoreDataArgs : Pulumi.ResourceArgs
    {
        [Input("awsProvider")]
        public Input<Pulumi.Aws.Provider>? AwsProvider { get; set; }

        [Input("cluster", required: true)]
        public Input<Pulumi.Aws.Eks.Cluster> Cluster { get; set; } = null!;

        [Input("clusterSecurityGroup", required: true)]
        public Input<Pulumi.Aws.Ec2.SecurityGroup> ClusterSecurityGroup { get; set; } = null!;

        [Input("eksNodeAccess")]
        public Input<Pulumi.Kubernetes.Types.Inputs.Core.V1.ConfigMapArgs>? EksNodeAccess { get; set; }

        [Input("endpoint", required: true)]
        public Input<string> Endpoint { get; set; } = null!;

        [Input("fargateProfile")]
        public Input<Pulumi.Aws.Eks.FargateProfile>? FargateProfile { get; set; }

        [Input("instanceRoles", required: true)]
        private InputList<Pulumi.Aws.Iam.Role>? _instanceRoles;
        public InputList<Pulumi.Aws.Iam.Role> InstanceRoles
        {
            get => _instanceRoles ?? (_instanceRoles = new InputList<Pulumi.Aws.Iam.Role>());
            set => _instanceRoles = value;
        }

        [Input("kubeconfig")]
        public Input<object>? Kubeconfig { get; set; }

        [Input("nodeGroupOptions", required: true)]
        public Input<Inputs.ClusterNodeGroupOptionsArgs> NodeGroupOptions { get; set; } = null!;

        [Input("nodeSecurityGroupTags")]
        private InputMap<string>? _nodeSecurityGroupTags;
        public InputMap<string> NodeSecurityGroupTags
        {
            get => _nodeSecurityGroupTags ?? (_nodeSecurityGroupTags = new InputMap<string>());
            set => _nodeSecurityGroupTags = value;
        }

        [Input("oidcProvider")]
        public Input<Pulumi.Aws.Iam.OpenIdConnectProvider>? OidcProvider { get; set; }

        [Input("privateSubnetIds")]
        private InputList<string>? _privateSubnetIds;
        public InputList<string> PrivateSubnetIds
        {
            get => _privateSubnetIds ?? (_privateSubnetIds = new InputList<string>());
            set => _privateSubnetIds = value;
        }

        [Input("provider", required: true)]
        public Input<Pulumi.Kubernetes.Provider> Provider { get; set; } = null!;

        [Input("publicSubnetIds")]
        private InputList<string>? _publicSubnetIds;
        public InputList<string> PublicSubnetIds
        {
            get => _publicSubnetIds ?? (_publicSubnetIds = new InputList<string>());
            set => _publicSubnetIds = value;
        }

        [Input("storageClasses")]
        private InputMap<Pulumi.Kubernetes.Storage.V1.StorageClass>? _storageClasses;
        public InputMap<Pulumi.Kubernetes.Storage.V1.StorageClass> StorageClasses
        {
            get => _storageClasses ?? (_storageClasses = new InputMap<Pulumi.Kubernetes.Storage.V1.StorageClass>());
            set => _storageClasses = value;
        }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        [Input("vpcCni")]
        public Input<Pulumi.Eks.VpcCni>? VpcCni { get; set; }

        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public CoreDataArgs()
        {
        }
    }
}
