# -*- coding: utf-8 -*- #
# Copyright 2015 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://healthcare.googleapis.com/v1alpha2/'
DOCS_URL = 'https://cloud.google.com/healthcare'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  PROJECTS = (
      'projects',
      'projects/{projectsId}',
      {},
      [u'projectsId'],
      True
  )
  PROJECTS_LOCATIONS = (
      'projects.locations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_DATASETS = (
      'projects.locations.datasets',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/datasets/'
              '{datasetsId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_DATASETS_ANNOTATIONSTORES = (
      'projects.locations.datasets.annotationStores',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/datasets/'
              '{datasetsId}/annotationStores/{annotationStoresId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_DATASETS_DICOMSTORES = (
      'projects.locations.datasets.dicomStores',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/datasets/'
              '{datasetsId}/dicomStores/{dicomStoresId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_DATASETS_FHIRSTORES = (
      'projects.locations.datasets.fhirStores',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/datasets/'
              '{datasetsId}/fhirStores/{fhirStoresId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_DATASETS_HL7V2STORES = (
      'projects.locations.datasets.hl7V2Stores',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/datasets/'
              '{datasetsId}/hl7V2Stores/{hl7V2StoresId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_DATASETS_OPERATIONS = (
      'projects.locations.datasets.operations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/datasets/'
              '{datasetsId}/operations/{operationsId}',
      },
      [u'name'],
      True
  )

  def __init__(self, collection_name, path, flat_paths, params,
               enable_uri_parsing):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
    self.enable_uri_parsing = enable_uri_parsing
