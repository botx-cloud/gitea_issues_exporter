import giteapy
import csv

configuration = giteapy.Configuration()
configuration.host = 'https://<YOUR GITEA URL ORIGIN>/api/v1'
# noinspection SpellCheckingInspection
configuration.api_key['access_token'] = '<YOUR GITEA TOKEN>'  # /user/settings/applications

api_client = giteapy.ApiClient(configuration)
issues_api_instance = giteapy.IssueApi(giteapy.ApiClient(configuration))


def dump_to_csv(filename, array_of_objects):
    converted = list(map(lambda x: {'title': x.title}, array_of_objects))  # could be used vars(x) to convert all
    array_of_dicts = []
    map_info = {}
    for conv in converted:
        if conv['title'] not in map_info:
            array_of_dicts.append(conv)
            map_info[conv['title']] = True

    keys = array_of_dicts[0].keys()

    with open(filename, 'w', newline='') as output_file:
        output_file.seek(0)
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(array_of_dicts)


def fetch_all(**kwargs):
    result = []
    page = 1
    while True:
        fetched = issues_api_instance.issue_list_issues(**kwargs, page=page)
        if len(fetched) == 0:
            break
        result += fetched
        page += 1

    return result


def export_open_closed_issues(organization_name, repository_name):
    open_issues = fetch_all(owner=organization_name, repo=repository_name, state='open')
    # we need to filter issues that are not feature branches merged into main branch
    closed_issues = list(filter(lambda x: x.pull_request is None or (not x.pull_request.merged),
                                fetch_all(owner=organization_name, repo=repository_name, state='closed')))
    print('x', closed_issues)
    dump_to_csv('open_issues.csv', open_issues)
    dump_to_csv('closed_issues.csv', closed_issues)


if __name__ == '__main__':
    print('starting..')
    export_open_closed_issues(organization_name='<GITEA ORGANIZATION NAME>', repository_name='<REPO NAME>')
    print('done.')
