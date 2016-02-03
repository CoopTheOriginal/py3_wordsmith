import requests as r
import json


class Wordsmith:
    base_url = 'https://wordsmith.automatedinsights.com/api/'

    def __init__(self, version, api_key):
        self.version = version
        self.api_key = api_key

    def _buildBaseURL(self):
        """Builds the base URL for all requests"""
        return self.base_url + 'v' + self.version + '/'

    def _buildRequest(self, url_path, json_body):
        """This method is a build request to the API. Send a json_body
        to run a POST request. Else, it's a GET"""
        url = self._buildBaseURL()
        url += '' if url_path == None else url_path

        if json_body is None:
            headers = {'Authorization' : 'Bearer ' + self.api_key}
            response = r.get(url, headers=headers)
            if response.status_code == 401:
                raise KeyError('Invalid API Key')
            return response
        else:
            headers = {'Authorization' : 'Bearer ' + self.api_key,
                       'Content-Type': 'application/json'}
            return r.post(url, headers=headers, data=json_body)

    def _getProjectsFullData(self):
        """Retrieves the raw list of projects from the API"""
        req = self._buildRequest('projects', None)
        return req.json()['data']

    def _projectExists(self, project_name):
        """check that a project name exists"""
        return any(proj['name'] == project_name for proj in self.getProjects())

    def _getSlugByProjectName(self, project_name):
        """Get a project slug using the project name"""
        projects_full = self._getProjectsFullData()
        for project in projects_full:
            if project['name'] == project_name:
                return project['slug']
        raise ValueError('No project exists with the name "{}"'.format(project_name))

    def _getSlugByTemplateName(self, project_name, template_name):
        """Get a template slug using the template name"""
        project_templates = self.getTemplates(project_name)
        for template in project_templates:
            if template['name'] == template_name:
                return template['slug']
        raise ValueError('No template exists with the name "{}"'.format(template_name))

    def getSkippedNarratives(self):
        """Allow user to get the summary of any skipped narratives in
           the generation process"""
        return self.skipped_narratives

    def getProjects(self):
        """Get list of projects and project slugs from API"""
        projects_full = self._getProjectsFullData()
        project_slugs = [{'name' : project['name'], 'slug' : project['slug']}
                         for project in projects_full]
        return project_slugs

    def getTemplates(self, project_name):
        """Get list of templates and template slugs from the API"""
        projects_full = self._getProjectsFullData()
        for project in projects_full:
            if project['name'] == project_name:
                return project['templates']
        raise ValueError('No project exists with the name "{}"'.format(project_name))

    def getDataSchema(self, project_name):
        """Get the expected data schema for a project from the API"""
        if self._projectExists(project_name):
            req = self._buildRequest('projects/' + self._getSlugByProjectName(project_name), None)
            return req.json()['data']['schema']
        else:
            raise ValueError('No project exists with the name "{}"'.format(project_name))

    def narrativePrep(self, data, schema):
        """Preps data sets for Wordsmith API"""
        missing_cols = []
        for key, value in schema.items():
            try:
                if value in ['Text', 'List']:
                    data[key] = str(data[key])
                elif value == 'Number':
                    data[key] = float(data[key])
            except KeyError:
                missing_cols.append(key)
        if missing_cols:
            return False, {'num_missing_cols' : len(missing_cols),
                           'list_missing_cols' : ', '.join(missing_cols),
                           'raw_data_row' : data}
        else:
            json_data = json.dumps({'data' : data})
            return True, json_data

    def generateNarratives(self, project_name, template_name, data_sets):
        """Generate narratives from a specified project and template. List of dict
        data sets is required as 'data_sets' value"""
        project_slug = self._getSlugByProjectName(project_name)
        template_slug = self._getSlugByTemplateName(project_name, template_name)
        url_path = 'templates/' + project_slug + '/' + template_slug + '/outputs'
        schema = self.getDataSchema(project_name)
        narrative_summary = []
        self.skipped_narratives = []

        for data in data_sets:
            prepped, narrative_prep = self.narrativePrep(data, schema)
            if prepped:
                req = self._buildRequest(url_path, narrative_prep)
                narrative_summary.append({'raw_data' : data,
                                          'narrative' : req.json()['data']})
            else:
                self.skipped_narratives.append(narrative_prep)
        return narrative_summary
