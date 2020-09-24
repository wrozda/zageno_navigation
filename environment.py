import datetime
import logging
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pageObjectsCreator.pageObjectsCreator import PageObjectsCreator
from utilities.logger import Logger

now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

logging.basicConfig(
    filename=f"logs/logs-{now}.txt",
    level=logging.INFO,
    format="[%(levelname)-8s %(asctime)s] %(message)s"
)


def before_all(context):
    context.logger = Logger(context)
    context.logger.logger = logging.getLogger(__name__)
    load_dotenv(".env")
    context.base_e2e_url = os.getenv("E2E_URL")


def before_feature(context, feature):
    context.feature_tags = feature.tags


def before_scenario(context, scenario):
    context.base_screenshots = bool(context.config.userdata.get("base-screenshots"))

    context.logger.current_scenario = scenario.name
    context.logger.info(f"Base E2E URL is: {context.base_e2e_url}")
    context.scenario_tags = scenario.tags
    context.browser = webdriver.Chrome(
        executable_path="./chromedriver",
        desired_capabilities=DesiredCapabilities.CHROME)
    context.browser.set_window_size(
        os.getenv("SCREEN_WIDTH"),
        os.getenv("SCREEN_HEIGHT"))
    context.logger.info("Starting browser")
    context.pages = PageObjectsCreator(context)


def before_step(context, step):
    context.logger.current_step = step.name


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    context.logger.info("Closing browser")
    context.browser.quit()


def after_all(context):
    pass
