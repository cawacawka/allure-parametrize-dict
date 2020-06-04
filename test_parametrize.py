import pytest
import allure

test_data = {
    "Story1": {
        "Test1": {"data": 1},
        "Test2": {"data": 2}
    },
    "Story2": {
        "Test3": {"data": 3},
        "Test4": {"data": 4}
    }
}

# just use pytest example https://docs.pytest.org/en/latest/example/parametrize.html#set-marks-or-test-id-for-individual-parametrized-test
# and allure markers https://docs.qameta.io/allure/#_bdd_markers


def pytest_generate_tests(metafunc):
    if "case" in metafunc.fixturenames:
        values = []
        ids = []
        for story, testset in test_data.items():
            values.extend(
                (
                    pytest.param(v, marks=allure.story(story))
                    for v in testset.values()
                )
            )

            ids.extend(testset.keys())
        metafunc.parametrize("case", values, ids=ids)


@allure.feature("Some feature")
def test_some(case):
    assert True
