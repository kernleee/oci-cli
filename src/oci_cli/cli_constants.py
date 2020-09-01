# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

CLI_RC_FALLBACK_LOCATION = '~/.oci/cli-defaults'
CLI_RC_DEFAULT_LOCATION = '~/.oci/oci_cli_rc'
CLI_RC_CANNED_QUERIES_SECTION_NAME = 'OCI_CLI_CANNED_QUERIES'
CLI_RC_COMMAND_ALIASES_SECTION_NAME = 'OCI_CLI_COMMAND_ALIASES'
CLI_RC_PARAM_ALIASES_SECTION_NAME = 'OCI_CLI_PARAM_ALIASES'
CLI_RC_GENERIC_SETTINGS_SECTION_NAME = 'OCI_CLI_SETTINGS'

OCI_CLI_PROFILE_ENV_VAR = 'OCI_CLI_PROFILE'
CLI_RC_GENERIC_SETTINGS_DEFAULT_PROFILE_KEY = 'default_profile'
CLI_RC_GENERIC_SETTINGS_USE_CLICK_HELP = 'use_click_help'

OCI_CLI_AUTH_ENV_VAR = 'OCI_CLI_AUTH'
OCI_CLI_AUTH_INSTANCE_PRINCIPAL = 'instance_principal'
OCI_CLI_AUTH_RESOURCE_PRINCIPAL = 'resource_principal'
OCI_CLI_AUTH_INSTANCE_OBO_USER = 'instance_obo_user'
OCI_CLI_AUTH_API_KEY = 'api_key'
OCI_CLI_AUTH_SESSION_TOKEN = 'security_token'

OCI_CLI_REGION_ENV_VAR = 'OCI_CLI_REGION'
OCI_CLI_USER_ENV_VAR = 'OCI_CLI_USER'
OCI_CLI_FINGERPRINT_ENV_VAR = 'OCI_CLI_FINGERPRINT'
OCI_CLI_KEY_FILE_ENV_VAR = 'OCI_CLI_KEY_FILE'
OCI_CLI_TENANCY_ENV_VAR = 'OCI_CLI_TENANCY'
OCI_CLI_CONFIG_FILE_ENV_VAR = 'OCI_CLI_CONFIG_FILE'
OCI_CLI_RC_FILE_ENV_VAR = 'OCI_CLI_RC_FILE'
OCI_CLI_CERT_BUNDLE_ENV_VAR = 'OCI_CLI_CERT_BUNDLE'
OCI_CLI_DELEGATION_TOKEN_FILE_ENV_VAR = 'OCI_CLI_DELEGATION_TOKEN_FILE'
OCI_CLI_SECURITY_TOKEN_FILE_ENV_VAR = 'OCI_CLI_SECURITY_TOKEN_FILE'
OCI_CLI_ENDPOINT_ENV_VAR = 'OCI_CLI_ENDPOINT'

OCI_CONFIG_ENV_VARS = {
    OCI_CLI_USER_ENV_VAR: 'user',
    OCI_CLI_FINGERPRINT_ENV_VAR: 'fingerprint',
    OCI_CLI_KEY_FILE_ENV_VAR: 'key_file',
    OCI_CLI_TENANCY_ENV_VAR: 'tenancy',
    OCI_CLI_DELEGATION_TOKEN_FILE_ENV_VAR: 'delegation_token_file',
    OCI_CLI_SECURITY_TOKEN_FILE_ENV_VAR: 'security_token_file'
}

OCI_CLI_PARAM_TO_ENV_MAP = {
    'region': OCI_CLI_REGION_ENV_VAR,
    'endpoint': OCI_CLI_ENDPOINT_ENV_VAR,
    'cert_bundle': OCI_CLI_CERT_BUNDLE_ENV_VAR,
    'config_file': OCI_CLI_CONFIG_FILE_ENV_VAR,
}

MEBIBYTE = 1024 * 1024
CHANGE_LOG_URL = 'https://raw.githubusercontent.com/oracle/oci-cli/master/CHANGELOG.rst'
OCI_CLI_PYPI_URL = 'https://pypi.org/pypi/oci-cli/json'
