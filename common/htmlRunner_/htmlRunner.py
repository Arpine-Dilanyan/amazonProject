from common.htmlRunner_.sources import htmlTestRunner
import datetime
from pathlib import Path


def get_root_directory():
    projectName = "AmazonProject"
    currentPath = Path(__file__)
    projectRootPath = (str(currentPath).split(projectName))[0] + projectName
    return projectRootPath


class HtmlRunner():
    @property
    def get_report_file_name(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%d-%m-%Y_%H-%M-%S')
        reportFileName = f"html_report_{formatted_datetime}.html"
        return reportFileName

    def get_html_runner(self, title='Test Report'):
        prjRoot = get_root_directory()
        outfile = open(prjRoot + "\_reports_\\" + self.get_report_file_name, "wb")
        runner = htmlTestRunner.HTMLTestRunner(
            stream=outfile,
            title=title,
            description='Random_suite_tests'
        )

        return runner
