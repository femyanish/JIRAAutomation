from TalentHunt.create_JIRA_task import JiraTasks

user_name = "user name"
api_token = "access token"
server = "account url"
jira = JiraTasks(user_name, api_token, server)

# Test Data for Creating Issue
test_data = {
    "project": "proeject name",
    "summary": "Issue summary",
    "description": "Issue description",
    "issuetype": {"name": "issue type"}
}

# Creating Test in Jira
jira.create_issue(test_data)

# Test Data for Updating Issue Fields
updated_test_data = {
    "summary": "test_summary",
    "description": "test_description",
}

# Updating Issue Fields in Jira
jira.update_issue_fields("issue_key", updated_test_data)

# Deleting Issue in Jira
jira.delete_issue("issue_key")