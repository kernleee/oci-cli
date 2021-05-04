# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.operator_access_control.src.oci_cli_operator_access_control.generated import opctl_service_cli


@click.command(cli_util.override('operator_control_assignment.operator_control_assignment_root_group.command_name', 'operator-control-assignment'), cls=CommandGroupWithAlias, help=cli_util.override('operator_control_assignment.operator_control_assignment_root_group.help', """Operator Access Control enables you to control the time duration and the actions an Oracle operator can perform on your Exadata Cloud@Customer infrastructure.
Using logging service, you can view a near real-time audit report of all actions performed by an Oracle operator.

Use the table of contents and search tool to explore the OperatorAccessControl API."""), short_help=cli_util.override('operator_control_assignment.operator_control_assignment_root_group.short_help', """OperatorAccessControl API"""))
@cli_util.help_option_group
def operator_control_assignment_root_group():
    pass


@click.command(cli_util.override('operator_control_assignment.operator_control_assignment_group.command_name', 'operator-control-assignment'), cls=CommandGroupWithAlias, help="""An Operator Control Assignment identifies the target resource that is placed under the governance of an Operator Control. Creating an Operator Control Assignment Assignment with a time duration ensures that human accesses to the target resource will be governed by Operator Control for the duration specified.""")
@cli_util.help_option_group
def operator_control_assignment_group():
    pass


opctl_service_cli.opctl_service_group.add_command(operator_control_assignment_root_group)
operator_control_assignment_root_group.add_command(operator_control_assignment_group)


@operator_control_assignment_group.command(name=cli_util.override('operator_control_assignment.change_operator_control_assignment_compartment.command_name', 'change-compartment'), help=u"""Changes the compartment of the specified Operator Control assignment ID. \n[Command Reference](changeOperatorControlAssignmentCompartment)""")
@cli_util.option('--operator-control-assignment-id', required=True, help=u"""unique OperatorControl identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the new compartment to contain the operator contol assignment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_operator_control_assignment_compartment(ctx, from_json, operator_control_assignment_id, compartment_id, if_match):

    if isinstance(operator_control_assignment_id, six.string_types) and len(operator_control_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-assignment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('operator_access_control', 'operator_control_assignment', ctx)
    result = client.change_operator_control_assignment_compartment(
        operator_control_assignment_id=operator_control_assignment_id,
        change_operator_control_assignment_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operator_control_assignment_group.command(name=cli_util.override('operator_control_assignment.create_operator_control_assignment.command_name', 'create'), help=u"""Creates an Operator Control Assignment resource. In effect, this brings the target resource under the governance of the Operator Control for specified time duration. \n[Command Reference](createOperatorControlAssignment)""")
@cli_util.option('--operator-control-id', required=True, help=u"""The OCID of the operator control that is being assigned to a target resource.""")
@cli_util.option('--resource-id', required=True, help=u"""The OCID of the target resource being brought under the governance of the operator control.""")
@cli_util.option('--resource-name', required=True, help=u"""Name of the target resource.""")
@cli_util.option('--resource-compartment-id', required=True, help=u"""The OCID of the compartment that contains the target resource.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the operator control assignment.""")
@cli_util.option('--resource-type', type=custom_types.CliCaseInsensitiveChoice(["EXACC"]), help=u"""Type of the target resource.""")
@cli_util.option('--time-assignment-from', type=custom_types.CLI_DATETIME, help=u"""The time at which the target resource will be brought under the governance of the operator control in [RFC 3339] timestamp format. Example: '2020-05-22T21:10:29.600Z'""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-assignment-to', type=custom_types.CLI_DATETIME, help=u"""The time at which the target resource will leave the governance of the operator control in [RFC 3339]timestamp format.Example: '2020-05-22T21:10:29.600Z'""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--is-enforced-always', type=click.BOOL, help=u"""If set, then the target resource is always governed by the operator control.""")
@cli_util.option('--comment', help=u"""Comment about the assignment of the operator control to this target resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_operator_control_assignment(ctx, from_json, operator_control_id, resource_id, resource_name, resource_compartment_id, compartment_id, resource_type, time_assignment_from, time_assignment_to, is_enforced_always, comment, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operatorControlId'] = operator_control_id
    _details['resourceId'] = resource_id
    _details['resourceName'] = resource_name
    _details['resourceCompartmentId'] = resource_compartment_id
    _details['compartmentId'] = compartment_id

    if resource_type is not None:
        _details['resourceType'] = resource_type

    if time_assignment_from is not None:
        _details['timeAssignmentFrom'] = time_assignment_from

    if time_assignment_to is not None:
        _details['timeAssignmentTo'] = time_assignment_to

    if is_enforced_always is not None:
        _details['isEnforcedAlways'] = is_enforced_always

    if comment is not None:
        _details['comment'] = comment

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('operator_access_control', 'operator_control_assignment', ctx)
    result = client.create_operator_control_assignment(
        create_operator_control_assignment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operator_control_assignment_group.command(name=cli_util.override('operator_control_assignment.delete_operator_control_assignment.command_name', 'delete'), help=u"""Deletes the specified Operator Control Assignment. This has the effect of unassigning the specific Operator Control from the target resource. \n[Command Reference](deleteOperatorControlAssignment)""")
@cli_util.option('--operator-control-assignment-id', required=True, help=u"""unique OperatorControl identifier""")
@cli_util.option('--description', help=u"""reason for detachment of OperatorAssignment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "APPLIED", "APPLYFAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_operator_control_assignment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operator_control_assignment_id, description, if_match):

    if isinstance(operator_control_assignment_id, six.string_types) and len(operator_control_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-assignment-id cannot be whitespace or empty string')

    kwargs = {}
    if description is not None:
        kwargs['description'] = description
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'operator_control_assignment', ctx)
    result = client.delete_operator_control_assignment(
        operator_control_assignment_id=operator_control_assignment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_operator_control_assignment') and callable(getattr(client, 'get_operator_control_assignment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_operator_control_assignment(operator_control_assignment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@operator_control_assignment_group.command(name=cli_util.override('operator_control_assignment.get_operator_control_assignment.command_name', 'get'), help=u"""Gets the details of an Operator Control Assignment of the specified ID. \n[Command Reference](getOperatorControlAssignment)""")
@cli_util.option('--operator-control-assignment-id', required=True, help=u"""unique OperatorControl identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'OperatorControlAssignment'})
@cli_util.wrap_exceptions
def get_operator_control_assignment(ctx, from_json, operator_control_assignment_id):

    if isinstance(operator_control_assignment_id, six.string_types) and len(operator_control_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-assignment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'operator_control_assignment', ctx)
    result = client.get_operator_control_assignment(
        operator_control_assignment_id=operator_control_assignment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operator_control_assignment_group.command(name=cli_util.override('operator_control_assignment.list_operator_control_assignments.command_name', 'list'), help=u"""Lists all Operator Control Assignments. \n[Command Reference](listOperatorControlAssignments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--operator-control-name', help=u"""A filter to return OperatorControl that match the given operatorControlName.""")
@cli_util.option('--resource-name', help=u"""A filter to return only resources that match the given ResourceName.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "APPLIED", "APPLYFAILED", "DELETED"]), help=u"""A filter to return only resources whose lifecycleState matches the given OperatorControlAssignment lifecycleState.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'OperatorControlAssignmentCollection'})
@cli_util.wrap_exceptions
def list_operator_control_assignments(ctx, from_json, all_pages, page_size, compartment_id, operator_control_name, resource_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if operator_control_name is not None:
        kwargs['operator_control_name'] = operator_control_name
    if resource_name is not None:
        kwargs['resource_name'] = resource_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'operator_control_assignment', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_operator_control_assignments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_operator_control_assignments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_operator_control_assignments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@operator_control_assignment_group.command(name=cli_util.override('operator_control_assignment.update_operator_control_assignment.command_name', 'update'), help=u"""Modifies the existing Operator Control assignment of the specified Operator Control assignment ID. Modifying the assignment does not change the Operator Control assignment ID. \n[Command Reference](updateOperatorControlAssignment)""")
@cli_util.option('--operator-control-assignment-id', required=True, help=u"""unique OperatorControl identifier""")
@cli_util.option('--time-assignment-from', type=custom_types.CLI_DATETIME, help=u"""The time at which the target resource will be brought under the governance of the operator control in [RFC 3339] timestamp format. Example: '2020-05-22T21:10:29.600Z'""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-assignment-to', type=custom_types.CLI_DATETIME, help=u"""The time at which the target resource will leave the governance of the operator control in [RFC 3339]timestamp format.Example: '2020-05-22T21:10:29.600Z'""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--is-enforced-always', type=click.BOOL, help=u"""If true, then the target resource is always governed by the operator control. Otherwise governance is time-based as specified by timeAssignmentTo and timeAssignmentFrom.""")
@cli_util.option('--comment', help=u"""Comment about the modification of the operator control assignment.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "APPLIED", "APPLYFAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'operator_access_control', 'class': 'OperatorControlAssignment'})
@cli_util.wrap_exceptions
def update_operator_control_assignment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, operator_control_assignment_id, time_assignment_from, time_assignment_to, is_enforced_always, comment, freeform_tags, defined_tags, if_match):

    if isinstance(operator_control_assignment_id, six.string_types) and len(operator_control_assignment_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-assignment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_assignment_from is not None:
        _details['timeAssignmentFrom'] = time_assignment_from

    if time_assignment_to is not None:
        _details['timeAssignmentTo'] = time_assignment_to

    if is_enforced_always is not None:
        _details['isEnforcedAlways'] = is_enforced_always

    if comment is not None:
        _details['comment'] = comment

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('operator_access_control', 'operator_control_assignment', ctx)
    result = client.update_operator_control_assignment(
        operator_control_assignment_id=operator_control_assignment_id,
        update_operator_control_assignment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_operator_control_assignment') and callable(getattr(client, 'get_operator_control_assignment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_operator_control_assignment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
