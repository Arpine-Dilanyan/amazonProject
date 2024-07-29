from common_.suites_.testSuites import TestSuites
from common.htmlRunner_.htmlRunner import HtmlRunner

if __name__ == "__main__":
    testSuites = TestSuites()
    suite = testSuites.get_random_suite()

    htmlRunner = HtmlRunner()
    runner = htmlRunner.get_html_runner("Random Suite")
    runner.run(suite)
