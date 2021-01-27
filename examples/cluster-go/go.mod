module cluster-go

go 1.14

require (
	// TODO - need a replace to run the test against the local version of the sdk
	github.com/pulumi/pulumi-eks/sdk v0.0.0-20210127043526-2129c31408c8
	github.com/pulumi/pulumi/sdk/v2 v2.18.2
)
