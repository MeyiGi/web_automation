import unittest
import pytest
from typing import Generator
from playwright.async_api import Playwright, Page, APIRequestContext, expect

#initialize
GITHUB_API_TOKEN = "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"
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN not set"

GITHUB_USER = "meyigi"
assert GITHUB_USER, "GITHUB_USER is not set"

GITHUB_REPO = "Test_API"


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    header = {
        "Accept" : "application/vnd.github.v3+json",
        "Authorization" : f"token {GITHUB_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=header,
    )
    yield request_context
    request_context.dispose()

    
@pytest.fixture(scope="session", autouse=True)
def create_test_repo(
    api_request_context: APIRequestContext 
) -> Generator[None, None, None]:
    new_repo = api_request_context.post("/user/repos", data={"name" : GITHUB_REPO})
    assert new_repo.ok
    
    yield
    
    # delete_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    # assert delete_repo.ok
    
def test_bug_report(api_request_context: APIRequestContext) -> None:
    data = {
        "title" : "[Bug] report 1",
        "body" : "Bug description",
    }
    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data,
    )
    assert new_issue.ok
    
    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    
    issue_response = issues.json()
    issue = list(filter(lambda issue : issue["title"] == "[Bug] report 1", issue_response))[0]
    assert issue
    assert issue["body"] == "Bug description"
    
    
def test_feature(api_request_context: APIRequestContext) -> None:
    data = {
        "title" : "[Feature] request 1",
        "body" : "Feature description",
    }
    
    new_issue = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data)
    assert new_issue.ok
    
    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok
    
    issues_response = issues.json()
    issue = list(filter(lambda issue: issue["title"] == "[Feature] request 1", issues_response))[0]
    assert issue
    assert issue["body"] == "Feature description"