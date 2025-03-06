# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-airbyte",
        "name": "Airbyte",
        "description": "`Airbyte <https://airbyte.com/>`__\n",
        "state": "ready",
        "source-date-epoch": 1741121808,
        "versions": [
            "5.0.0",
            "4.0.0",
            "3.9.0",
            "3.8.1",
            "3.8.0",
            "3.7.0",
            "3.6.0",
            "3.5.1",
            "3.5.0",
            "3.4.0",
            "3.3.2",
            "3.3.1",
            "3.3.0",
            "3.2.1",
            "3.2.0",
            "3.1.0",
            "3.0.0",
            "2.1.4",
            "2.1.3",
            "2.1.2",
            "2.1.1",
            "2.1.0",
            "2.0.0",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Airbyte",
                "external-doc-url": "https://airbyte.com/",
                "logo": "/docs/integration-logos/Airbyte.png",
                "how-to-guide": ["/docs/apache-airflow-providers-airbyte/operators/airbyte.rst"],
                "tags": ["service"],
            }
        ],
        "operators": [
            {"integration-name": "Airbyte", "python-modules": ["airflow.providers.airbyte.operators.airbyte"]}
        ],
        "hooks": [
            {"integration-name": "Airbyte", "python-modules": ["airflow.providers.airbyte.hooks.airbyte"]}
        ],
        "sensors": [
            {"integration-name": "Airbyte", "python-modules": ["airflow.providers.airbyte.sensors.airbyte"]}
        ],
        "triggers": [
            {"integration-name": "Airbyte", "python-modules": ["airflow.providers.airbyte.triggers.airbyte"]}
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.airbyte.hooks.airbyte.AirbyteHook",
                "connection-type": "airbyte",
            }
        ],
        "dependencies": ["apache-airflow>=2.9.0", "airbyte-api>=0.52.0"],
        "devel-dependencies": [],
    }
