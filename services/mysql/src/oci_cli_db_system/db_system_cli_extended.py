# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from services.mysql.src.oci_cli_db_system.generated import dbsystem_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import click

# rename  oci mysql db-system create-db-system-create-db-system-source-from-backup-details -> oci mysql db-system clone
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_group, dbsystem_cli.create_db_system_create_db_system_source_from_backup_details, "clone")

# rename  oci mysql db-system create-db-system-create-db-system-source-import-from-url-details -> oci mysql db-system import
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_group, dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, "import")

# oci mysql db-system db-system -> oci mysql db-system system
dbsystem_cli.db_system_root_group.commands.pop(dbsystem_cli.db_system_group.name)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system_create_db_system_source_from_backup_details)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.delete_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.get_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.list_db_systems)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.restart_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.start_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.stop_db_system)
dbsystem_cli.db_system_root_group.add_command(dbsystem_cli.update_db_system)


# rename --source-source-url argument
@cli_util.copy_params_from_generated_command(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, params_to_exclude=['source_source_url'])
@cli_util.option('--source-url', required=True, help="""The Pre-Authenticated Request (PAR) URL of the file you want to import from Object Storage.""")
@dbsystem_cli.db_system_root_group.command(name="import", help=dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def rename_create_import_args(ctx, **kwargs):
    if 'source_url' in kwargs:
        kwargs['source_source_url'] = kwargs['source_url']
        kwargs.pop('source_url')

    ctx.invoke(dbsystem_cli.create_db_system_create_db_system_source_import_from_url_details, **kwargs)


# oci mysql db-system heat-wave-cluster -> oci mysql db-system heatwave-cluster
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_root_group, dbsystem_cli.heat_wave_cluster_group, "heatwave-cluster")


# oci mysql db-system heat-wave-cluster-memory-estimate -> oci mysql db-system heatwave-cluster-memory-estimate
cli_util.rename_command(dbsystem_cli, dbsystem_cli.db_system_root_group, dbsystem_cli.heat_wave_cluster_memory_estimate_group, "heatwave-cluster-memory-estimate")


@cli_util.copy_params_from_generated_command(dbsystem_cli.list_db_systems, params_to_exclude=['is_heat_wave_cluster_attached'])
@dbsystem_cli.db_system_root_group.command(name=dbsystem_cli.list_db_systems.name, help=dbsystem_cli.list_db_systems.help)
@cli_util.option('--is-heatwave-cluster-attached', type=click.BOOL, help=u"""If true, return only DB Systems with a HeatWave cluster attached, if false return only DB Systems with no HeatWave cluster attached. If not present, return all DB Systems.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'list[DbSystemSummary]'})
@cli_util.wrap_exceptions
def list_db_systems_extended(ctx, **kwargs):
    if 'is_heatwave_cluster_attached' in kwargs:
        kwargs['is_heat_wave_cluster_attached'] = kwargs['is_heatwave_cluster_attached']
        kwargs.pop('is_heatwave_cluster_attached')

    ctx.invoke(dbsystem_cli.list_db_systems, **kwargs)
