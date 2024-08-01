# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

import os
from .testUtil import authorization_info_version11
from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class TestUpdateCluster(ScenarioTest):
    location = 'eastus2'
    resourceGroup = "hilocli-test"
    clusterPoolName = "hilopool11eus2"

    def test_upgrade_cluster(self):
        self.kwargs.update({
            "rg": self.resourceGroup,
            "loc": self.location,
            "poolName": self.clusterPoolName,
            "clusterName": "cluster2024516144530",
            "clusterType": "Spark",
            # Create a cluster node-profile object.
            "computeNodeProfile": self.cmd('az hdinsight-on-aks cluster node-profile create --count 5 --node-type Worker --vm-size Standard_D16a_v4').get_output_in_json(),
        })

        # If there is no existing cluster to test, use the following code to create the cluster.
        # spark_versions = self.cmd('az hdinsight-on-aks list-available-cluster-version -l {loc} --query "[?clusterType==\'Spark\']"').get_output_in_json()
        # create_command = 'az hdinsight-on-aks cluster create -n {clusterName} --cluster-pool-name {poolName} -g {rg} -l {loc} --cluster-type {clusterType} --spark-storage-url abfs://testspark@hilostorage.dfs.core.windows.net/ --cluster-version ' + spark_versions[0]["clusterVersion"] + ' --oss-version ' + spark_versions[0]["ossVersion"] + ' --nodes ' + '{computeNodeProfile}' +' '+ authorization_info()
        # self.cmd(create_command)

        # Test list a clusterpool's available upgrades.
        self.cmd(
            'az hdinsight-on-aks clusterpool upgrade list --cluster-pool-name {poolName} -g {rg}').get_output_in_json()

        # Test list a cluster's available upgrades.
        upgrades = self.cmd(
            'az hdinsight-on-aks cluster upgrade list --cluster-pool-name {poolName} -g {rg} --cluster-name {clusterName}').get_output_in_json()
        assert upgrades is not None

        # Test upgrade a clusterpool.(There is currently no upgradeable version, but need to test it later)
        # self.cmd('az hdinsight-on-aks clusterpool upgrade run --cluster-pool-name {poolName} -g {rg} --node-os-upgrade ')
        
        # Test list cluster pool upgrade history
        self.cmd('az hdinsight-on-aks clusterpool upgrade history --cluster-pool-name {poolName} -g {rg}')

        # Test upgrade a cluster.
        self.cmd('az hdinsight-on-aks cluster upgrade run --cluster-pool-name {poolName} -g {rg} --cluster-name {clusterName} --hotfix-upgrade component-name=' + upgrades[1]["componentName"] + ' target-build-number='+upgrades[1]["targetBuildNumber"] +' target-cluster-version='+upgrades[1]["targetClusterVersion"] +' target-oss-version='+ upgrades[1]["targetOssVersion"])

        # Test list cluster upgrade history
        histories = self.cmd('az hdinsight-on-aks cluster upgrade history --cluster-pool-name {poolName} -g {rg} --cluster-name {clusterName}').get_output_in_json()

        # Test rollback cluster upgrade. (There is currently no upgradeable version, but need to test it later)
        self.cmd('az hdinsight-on-aks cluster upgrade rollback --cluster-pool-name {poolName} -g {rg} --cluster-name {clusterName} --upgrade-history ' + histories[0]["id"])
